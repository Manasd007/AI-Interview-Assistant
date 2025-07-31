import streamlit as st
from utils import validate_email, validate_phone, generate_anonymous_session_id, format_timestamp, save_candidate_data, anonymize_candidate_info
from question_generator import QuestionGenerator

st.set_page_config(
    page_title="TalentScout AI",
    page_icon="🤖",
    layout="centered",
    initial_sidebar_state="collapsed"
)

if "stage" not in st.session_state:
    st.session_state.stage = "greeting"

if "candidate_info" not in st.session_state:
    st.session_state.candidate_info = {}

if "tech_questions" not in st.session_state:
    st.session_state.tech_questions = []

if "behavioral_questions" not in st.session_state:
    st.session_state.behavioral_questions = []

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

if "session_id" not in st.session_state:
    st.session_state.session_id = None

EXIT_KEYWORDS = ["exit", "quit", "bye", "stop", "end", "finish"]

def add_to_chat_history(role, message):
    st.session_state.chat_history.append((role, message))

def check_exit_keywords(user_input):
    if user_input and any(keyword in user_input.lower() for keyword in EXIT_KEYWORDS):
        return True
    return False

st.markdown("""
# 🤖 TalentScout AI – Your AI Hiring Assistant

*Intelligent candidate screening powered by Google Gemini*
""")

if st.session_state.chat_history:
    st.markdown("### 💬 Conversation History")
    for role, message in st.session_state.chat_history:
        if role == "assistant":
            st.chat_message("assistant").write(message)
        else:
            st.chat_message("user").write(message)
    st.divider()

if st.session_state.stage == "greeting":
    st.markdown("### 👋 Welcome to TalentScout!")
    st.markdown("I'm your AI-powered hiring assistant. I'll help you screen candidates by collecting their information and generating tailored interview questions.")
    
    greeting_message = "Hello! I'm your AI Hiring Assistant. Let's get started with a few basic questions to understand the candidate's profile."
    st.chat_message("assistant").write(greeting_message)
    add_to_chat_history("assistant", greeting_message)
    
    col1, col2 = st.columns([1, 2])
    with col1:
        if st.button("🚀 Start Interview", type="primary"):
            st.session_state.session_id = generate_anonymous_session_id()
            add_to_chat_history("user", "Start Interview")
            st.session_state.stage = "collect_info"
            st.rerun()

elif st.session_state.stage == "collect_info":
    st.markdown("### 📝 Candidate Information")
    st.markdown("Please provide the candidate's basic information:")
    
    user_input = st.text_input("💡 Tip: Type 'exit' to quit at any time", key="exit_check")
    if check_exit_keywords(user_input):
        st.session_state.stage = "end"
        st.rerun()

    with st.container():
        col1, col2 = st.columns(2)
        with col1:
            full_name = st.text_input("👤 Full Name", placeholder="John Doe")
            email = st.text_input("📧 Email Address", placeholder="john.doe@email.com")
            phone = st.text_input("📞 Phone Number", placeholder="+1 (555) 123-4567")
        with col2:
            experience = st.number_input("⏰ Years of Experience", min_value=0, max_value=50, step=1)
            position = st.text_input("💼 Desired Position(s)", placeholder="Software Engineer")
            location = st.text_input("📍 Current Location", placeholder="San Francisco, CA")

    col1, col2 = st.columns(2)
    with col1:
        if st.button("➡️ Next", type="primary"):
            if not validate_email(email):
                st.error("❌ Please enter a valid email address.")
            elif not validate_phone(phone):
                st.error("❌ Please enter a valid phone number.")
            else:
                candidate_data = {
                    "name": full_name,
                    "email": email,
                    "phone": phone,
                    "experience": experience,
                    "position": position,
                    "location": location,
                }
                st.session_state.candidate_info = candidate_data
                add_to_chat_history("user", f"Provided candidate info: {full_name}, {position}, {experience} years experience")
                st.session_state.stage = "tech_stack"
                st.rerun()
    
    with col2:
        if st.button("⬅️ Back"):
            st.session_state.stage = "greeting"
            st.rerun()

elif st.session_state.stage == "tech_stack":
    st.markdown("### 🛠️ Tech Stack Declaration")
    st.markdown("Please list the technologies the candidate is proficient in:")
    
    user_input = st.text_input("💡 Tip: Type 'exit' to quit at any time", key="exit_check_tech")
    if check_exit_keywords(user_input):
        st.session_state.stage = "end"
        st.rerun()
    
    tech_stack_input = st.text_area(
        "🔧 Programming Languages, Frameworks, Databases, and Tools",
        placeholder="Python, React, PostgreSQL, Docker, AWS (comma-separated)",
        height=100
    )

    col1, col2 = st.columns(2)
    with col1:
        if st.button("🎯 Generate Questions", type="primary"):
            if not tech_stack_input.strip():
                st.error("❌ Please enter the candidate's tech stack.")
            else:
                tech_list = [t.strip() for t in tech_stack_input.split(",") if t.strip()]
                qg = QuestionGenerator()
                questions = []
                
                with st.spinner("🤖 Generating personalized questions..."):
                    try:
                        for tech in tech_list:
                            tech_questions = qg.generate_technical_question(tech, st.session_state.candidate_info.get("experience", 0))
                            questions.extend(tech_questions)
                        
                        st.session_state.tech_questions = questions
                        add_to_chat_history("user", f"Tech stack provided: {', '.join(tech_list)}")
                        add_to_chat_history("assistant", f"✅ Generated {len(questions)} technical questions based on the tech stack.")
                        st.session_state.stage = "show_questions"
                        st.rerun()
                    except Exception as e:
                        st.error(f"❌ Error generating questions: {str(e)}")
                        add_to_chat_history("assistant", "Sorry, I encountered an error generating questions. Please try again.")
    
    with col2:
        if st.button("⬅️ Back"):
            st.session_state.stage = "collect_info"
            st.rerun()

elif st.session_state.stage == "show_questions":
    st.markdown("### 🧪 Technical Questions")
    st.markdown("Here are the personalized technical questions for the candidate:")
    
    if not st.session_state.tech_questions:
        st.warning("⚠️ No questions generated. Please go back and try again.")
        if st.button("⬅️ Back to Tech Stack"):
            st.session_state.stage = "tech_stack"
            st.rerun()
    else:
        for i, q in enumerate(st.session_state.tech_questions, 1):
            st.markdown(f"**Q{i}.** {q}")
            st.divider()

        if not st.session_state.behavioral_questions:
            st.markdown("### 🧠 Behavioral Questions")
            st.markdown("Generating behavioral questions based on the role...")
            qg = QuestionGenerator()
            
            with st.spinner("🤖 Generating behavioral questions..."):
                try:
                    role = st.session_state.candidate_info.get("position", "Software Engineer")
                    behavioral_qs = qg.generate_behavioral_question(role)
                    st.session_state.behavioral_questions = behavioral_qs
                    add_to_chat_history("assistant", f"✅ Generated {len(behavioral_qs)} behavioral questions for {role} role.")
                except Exception as e:
                    st.error(f"❌ Error generating behavioral questions: {str(e)}")
                    st.session_state.behavioral_questions = []
        else:
            st.markdown("### 🧠 Behavioral Questions")
            st.markdown("Here are the behavioral questions for the candidate:")
        
        if st.session_state.behavioral_questions:
            for i, q in enumerate(st.session_state.behavioral_questions, 1):
                st.markdown(f"**BQ{i}.** {q}")
                st.divider()

        col1, col2 = st.columns(2)
        with col1:
            if st.button("✅ Finish Interview", type="primary"):
                add_to_chat_history("user", "Completed interview")
                st.session_state.stage = "end"
                st.rerun()
        
        with col2:
            if st.button("⬅️ Back to Tech Stack"):
                st.session_state.stage = "tech_stack"
                st.rerun()

elif st.session_state.stage == "end":
    st.markdown("### 🎉 Interview Complete!")
    
    end_message = "Thank you! The candidate's information and generated questions have been recorded. Our team will review the responses and get back to you shortly."
    st.chat_message("assistant").write(end_message)
    add_to_chat_history("assistant", end_message)
    
    if st.session_state.session_id and st.session_state.candidate_info:
        try:
            anonymized_info = anonymize_candidate_info(st.session_state.candidate_info)
            
            candidate_data = {
                "timestamp": format_timestamp(),
                "session_id": st.session_state.session_id,
                "candidate_info": anonymized_info,
                "tech_questions": st.session_state.tech_questions,
                "behavioral_questions": st.session_state.behavioral_questions,
                "chat_history": st.session_state.chat_history,
            }
            
            save_candidate_data(st.session_state.session_id, candidate_data)
            st.success(f"📊 Interview data saved securely with session ID: `{st.session_state.session_id}`")
            
        except Exception as e:
            st.warning("⚠️ Unable to save interview data. Your responses are still recorded in this session.")
    
    st.markdown("---")
    col1, col2 = st.columns(2)
    with col1:
        if st.button("🔄 Start New Interview", type="primary"):
            st.session_state.clear()
            st.rerun()
    
    with col2:
        st.markdown("""
        ### 📋 Summary
        - **Technical Questions:** Generated based on tech stack
        - **Behavioral Questions:** Tailored to the role
        - **Data Security:** Anonymized and stored locally
        - **Session ID:** Available for reference
        """) 