import os
import google.generativeai as genai

try:
    from dotenv import load_dotenv
    load_dotenv()
except Exception as e:
    print(f"Warning: Could not load .env file: {e}")
    print("Please set GEMINI_API_KEY environment variable manually")

class LLMWrapper:
    def __init__(self):
        api_key = os.getenv("GEMINI_API_KEY")
        if api_key:
            genai.configure(api_key=api_key)
            self.model = genai.GenerativeModel("gemini-1.5-flash")
        else:
            raise ValueError("GEMINI_API_KEY not found in environment variables. Please set it in your .env file or as an environment variable.")
    
    def generate_response(self, prompt: str) -> str:
        try:
            response = self.model.generate_content(prompt)
            if response.text:
                return response.text.strip()
            else:
                return "Sorry, I didn't understand that. Could you rephrase or try again?"
        except Exception as e:
            error_msg = str(e).lower()
            if "quota" in error_msg or "limit" in error_msg:
                return "Sorry, I'm experiencing high traffic. Please try again in a moment."
            elif "invalid" in error_msg or "malformed" in error_msg:
                return "Sorry, I didn't understand that. Could you rephrase or try again?"
            else:
                return "Sorry, I encountered an error. Please try again."
    
    def analyze_response(self, question, response, context=""):
        try:
            prompt = f"""
            Analyze this candidate response:
            
            Question: {question}
            Response: {response}
            Context: {context}
            
            Provide:
            1. A score from 1-10
            2. Brief feedback
            3. Key strengths and areas for improvement
            """
            return self.generate_response(prompt)
        except Exception as e:
            return f"Unable to analyze response: {str(e)}" 