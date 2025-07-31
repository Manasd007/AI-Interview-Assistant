# TalentScout AI – Hiring Assistant Chatbot 🤖

A Streamlit-based AI-powered chatbot that screens technical candidates by collecting profile data and generating tailored technical and behavioral questions using Google's Gemini AI.

## 🚀 Features

- **Smart Candidate Profiling**: Collects comprehensive candidate information (name, email, experience, role, location)
- **Tech Stack Analysis**: Generates personalized technical questions based on candidate's technology stack
- **Behavioral Assessment**: Creates role-specific behavioral questions for soft skills evaluation
- **Conversational Interface**: Chat-like experience with conversation history and context awareness
- **Data Privacy**: Secure, anonymized data handling with GDPR compliance
- **Session Management**: Complete interview flow with navigation and restart capabilities
- **Error Handling**: Robust error management and graceful fallbacks

## 🛠️ Tech Stack

- **Frontend**: Streamlit (Python web framework)
- **AI/LLM**: Google Gemini Pro (via `google-generativeai`)
- **Data Storage**: Local JSON with anonymized session IDs
- **Environment**: Python 3.10+, dotenv for configuration
- **Privacy**: UUID-based anonymization, no raw PII storage

## 📦 Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/talentscout-ai.git
cd talentscout-ai
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Configure Environment Variables
Create a `.env` file in the project root:
```env
GEMINI_API_KEY=your_google_ai_key_here
```

### 4. Run the Application
```bash
streamlit run app.py
```

The app will be available at `http://localhost:8501`

## 📂 Project Structure

```
talentscout-ai/
├── app.py                      # Main Streamlit application
├── prompts.py                  # AI prompt templates and logic
├── question_generator.py       # Question generation engine
├── llm_utils.py               # Gemini API wrapper
├── utils.py                    # Helper functions and data handling
├── requirements.txt            # Python dependencies
├── .env                        # Environment variables (API keys)
├── .gitignore                  # Git ignore rules
├── README.md                   # Project documentation
├── data/                       # Data storage (candidates.json)
└── assets/                     # Static assets (if any)
```

## 🎯 Prompt Design

The application uses sophisticated, instruction-rich prompts designed for:

- **Technical Questions**: Real-world scenarios, varying difficulty levels, practical applications
- **Behavioral Questions**: STAR method encouragement, role-specific soft skills assessment
- **Follow-up Questions**: Depth testing, gap identification, conversational tone
- **Multi-tech Stack**: Integration-focused questions across technologies
- **Personalized Assessment**: Role + experience + tech stack combination

## 🔐 Data Handling & Privacy

### Privacy Features
- ✅ **Anonymized Session IDs**: UUID-based tracking without PII
- ✅ **No Raw PII Storage**: Names and phone numbers not stored
- ✅ **Email Hashing**: Email addresses hashed for reference only
- ✅ **Local Storage**: Data stored locally in `data/candidates.json`
- ✅ **Version Control Protection**: Sensitive files excluded via `.gitignore`

### Data Structure
```json
{
  "user_abc12345": {
    "timestamp": "2024-01-15 14:30:25",
    "session_id": "user_abc12345",
    "candidate_info": {
      "experience_years": 5,
      "position": "Software Engineer",
      "location": "San Francisco",
      "email_hash": 123456789
    },
    "tech_questions": [...],
    "behavioral_questions": [...],
    "chat_history": [...]
  }
}
```

## 🎨 User Experience

### Interview Flow
1. **Greeting**: Welcome and introduction
2. **Candidate Info**: Collect basic profile information
3. **Tech Stack**: Input technologies and tools
4. **Question Generation**: AI-powered technical and behavioral questions
5. **Completion**: Secure data storage and session summary

### Features
- **Conversational Interface**: Chat-like experience with message history
- **Navigation**: Forward/backward movement through stages
- **Error Recovery**: Graceful handling of API failures
- **Exit Options**: Multiple ways to end the conversation
- **Restart Capability**: Start fresh interviews easily

## 🚀 Deployment Options

### Local Development (Default)
```bash
streamlit run app.py
```

### Cloud Deployment

#### Streamlit Cloud (Recommended)
1. Push code to GitHub
2. Connect repository to [Streamlit Cloud](https://streamlit.io/cloud)
3. Add `GEMINI_API_KEY` as a secret in Streamlit Cloud settings
4. Deploy automatically

#### Alternative Platforms
- **Render**: Deploy as a web service
- **Replit**: Cloud IDE deployment
- **GCP/AWS**: Advanced cloud hosting options

## 📊 Usage Example

1. **Start Interview**: Click "Start Interview" button
2. **Enter Candidate Info**: Fill in name, email, experience, role, location
3. **Provide Tech Stack**: List technologies (Python, React, PostgreSQL, etc.)
4. **Generate Questions**: AI creates personalized technical and behavioral questions
5. **Complete Interview**: Data is securely saved with session ID

## 🔧 Configuration

### Customizing Prompts
Edit `prompts.py` to modify question generation:
- Technical question requirements
- Behavioral assessment criteria
- Follow-up question logic

### API Configuration
Update `llm_utils.py` for different LLM providers:
- Model selection
- Temperature settings
- Error handling

### Data Storage
Modify `utils.py` for different storage options:
- Database integration
- Cloud storage
- Enhanced anonymization

## 📝 License

This project is for educational and demonstration purposes.

## 🤝 Contributing

Feel free to submit issues and enhancement requests!

## 📬 Contact

Created for the AI/ML Internship Assignment – TalentScout Simulation

---

**Built with ❤️ using Streamlit and Google Gemini AI** 