from prompts import PromptManager
from llm_utils import LLMWrapper

class QuestionGenerator:
    def __init__(self):
        self.prompt_manager = PromptManager()
        self.llm = LLMWrapper()
    
    def generate_technical_question(self, tech: str, experience_level=0):
        prompt = self.prompt_manager.get_technical_prompt(tech)
        response = self.llm.generate_response(prompt)
        
        questions = []
        for line in response.split('\n'):
            line = line.strip()
            if line.startswith('Q:') or line.startswith('Q.'):
                question = line[2:].strip()
                if question:
                    questions.append(question)
            elif line and not line.startswith('Q:'):
                questions.append(line)
        
        return questions if questions else [response]
    
    def generate_behavioral_question(self, role: str):
        prompt = self.prompt_manager.get_behavioral_prompt(role)
        response = self.llm.generate_response(prompt)
        
        questions = []
        for line in response.split('\n'):
            line = line.strip()
            if line.startswith('Q:') or line.startswith('Q.'):
                question = line[2:].strip()
                if question:
                    questions.append(question)
            elif line and not line.startswith('Q:'):
                questions.append(line)
        
        return questions if questions else [response]
    
    def generate_follow_up_question(self, answer: str):
        prompt = self.prompt_manager.get_follow_up_prompt(answer)
        response = self.llm.generate_response(prompt)
        return response.strip()
    
    def generate_behavioral_question_legacy(self, role, experience_years):
        candidate_info = f"Role: {role}, Experience Years: {experience_years}"
        prompt = f"""
        Generate a behavioral interview question for a {role} position with {experience_years} years of experience.
        Focus on leadership, problem-solving, or teamwork scenarios.
        """
        
        return self.llm.generate_response(prompt)
    
    def generate_follow_up_question_legacy(self, previous_question, previous_response):
        prompt = f"""
        Based on this previous question and response, generate a relevant follow-up question:
        
        Previous Question: {previous_question}
        Previous Response: {previous_response}
        
        Generate a follow-up that digs deeper into their response or explores a related topic.
        """
        
        return self.llm.generate_response(prompt) 