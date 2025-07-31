class PromptManager:
    def __init__(self):
        self.system_prompt = """You are an AI hiring assistant designed to conduct initial screening interviews. 
        Your role is to ask relevant questions based on the candidate's profile and evaluate their responses."""
    
    def get_technical_prompt(self, tech: str) -> str:
        return f"""
You are an expert technical interviewer. Generate exactly 3 real-world technical interview questions for {tech}.

Requirements:
- Focus on applied understanding and practical scenarios, not theoretical definitions
- Each question should test problem-solving skills and hands-on experience
- Include varying difficulty levels (junior to mid-level)
- Questions should be answerable in 3–5 minutes each
- Avoid yes/no or rote questions

Format:
**Technical Questions for {tech}:**
1. ...
2. ...
3. ...
"""
    
    def get_behavioral_prompt(self, role: str) -> str:
        return f"""
You are an experienced HR interviewer. Generate exactly 3 behavioral interview questions tailored for a {role} position.

Requirements:
- Assess communication, leadership, teamwork, and role-specific soft skills
- Encourage STAR (Situation, Task, Action, Result) responses
- Avoid generic or overused questions
- Each question should explore different aspects of the candidate's work style

Format:
**Behavioral Questions for {role}:**
1. ...
2. ...
3. ...
"""
    
    def get_follow_up_prompt(self, answer: str) -> str:
        return f"""
You are an experienced interviewer. Based on the candidate's response below, generate 1 thoughtful follow-up question to probe deeper.

Candidate's Answer:
"{answer}"

Requirements:
- Test depth of understanding or uncover gaps
- Ask about "why", "how", or edge cases
- Be conversational and non-confrontational

Format:
**Follow-up Question:**
...
"""
    
    def get_multi_tech_stack_prompt(self, tech_list: list[str]) -> str:
        tech_string = ", ".join(tech_list)
        
        format_sections = []
        for tech in tech_list:
            format_sections.append(f"\n**{tech}:**\n1.\n2.\n3.\n")
        
        format_string = "".join(format_sections)
        
        return f"""
You are a technical interview expert. Generate exactly 3 technical questions per technology in this list: {tech_string}.

Requirements:
- Scenario-based, real-world questions
- Vary difficulty from basic to advanced
- Highlight integration where applicable

Format:
**Tech Stack Interview Questions:**{format_string}
"""
    
    def get_personalized_prompt(self, role: str, level: str, tech_list: list[str]) -> str:
        tech_string = ", ".join(tech_list)
        return f"""
You are an expert technical recruiter. Generate personalized interview questions for a {role} role.

Job Role: {role}
Experience Level: {level}
Key Technologies: {tech_string}

Generate:
- 2 technical questions based on daily job responsibilities
- 2 behavioral questions tied to role-specific soft skills

Adjust question complexity to match experience level.

Format:
**Personalized Questions for {role} ({level}):**

**Technical Questions:**
1. ...
2. ...

**Behavioral Questions:**
1. ...
2. ...
"""
    
    def get_system_prompt(self) -> str:
        return "You are an intelligent AI Hiring Assistant chatbot. Ask technical questions and guide candidates."
    
    def get_question_prompt(self, tech: str) -> str:
        return self.get_technical_prompt(tech)
    
    def generate_question_prompt(self, candidate_info):
        return f"""
        Based on the following candidate information, generate an appropriate technical or behavioral question:
        
        Candidate Info: {candidate_info}
        
        Generate a relevant question that would help assess their suitability for the role.
        """
    
    def evaluate_response_prompt(self, question, response, candidate_info):
        return f"""
        Evaluate the following candidate response:
        
        Question: {question}
        Response: {response}
        Candidate Info: {candidate_info}
        
        Provide a score from 1-10 and brief feedback on their response.
        """ 