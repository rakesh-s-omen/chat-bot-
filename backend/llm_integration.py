"""
Local LLM Integration using Ollama
Lightweight and efficient - uses Phi-3 Mini (3.8B parameters)
"""

import ollama
import json
from typing import Dict, List, Optional

class LocalLLM:
    def __init__(self, model_name: str = "phi3"):
        """
        Initialize local LLM
        
        Models (in order of size/speed):
        - phi3: 3.8B params, very fast, excellent for this use case (RECOMMENDED)
        - llama3.2: 3B params, also very fast
        - gemma2:2b: 2B params, fastest but less capable
        """
        self.model_name = model_name
        self.available = self._check_availability()
        
    def _check_availability(self) -> bool:
        """Check if Ollama is installed and model is available"""
        try:
            # Try to list models
            models_response = ollama.list()
            
            # Handle object response (new version) or dict response (old version)
            if hasattr(models_response, 'models'):
                model_names = [m.model for m in models_response.models]
            else:
                model_names = [m['name'] for m in models_response.get('models', [])]
            
            # Check if our model is available
            if any(self.model_name in name for name in model_names):
                print(f"\n✨ SUCCESS: Local LLM '{self.model_name}' is connected and ready! ✨\n")
                return True
            else:
                print(f"⚠️ Model '{self.model_name}' not found. Please run: ollama pull {self.model_name}")
                return False
        except Exception as e:
            print(f"⚠️ Ollama not available: {e}")
            print("Please install Ollama from: https://ollama.ai")
            return False
    
    def generate_response(
        self, 
        user_query: str, 
        user_data: Optional[Dict] = None,
        context_docs: Optional[List[str]] = None,
        role: str = "student",
        conversation_history: Optional[List[Dict]] = None
    ) -> str:
        """
        Generate response using local LLM
        
        Args:
            user_query: User's question
            user_data: User's personal data from database
            context_docs: Relevant documents from vector search
            role: User's role (student/employee/admin)
            conversation_history: Previous messages for context
        """
        
        if not self.available:
            return self._fallback_response(user_query, user_data, role)
        
        try:
            # Build context-aware prompt
            system_prompt = self._build_system_prompt(role, user_data, context_docs)
            
            # Build conversation history
            messages = [{"role": "system", "content": system_prompt}]
            
            if conversation_history:
                messages.extend(conversation_history[-3:])  # Last 3 messages for context
            
            messages.append({"role": "user", "content": user_query})
            
            # Generate response
            response = ollama.chat(
                model=self.model_name,
                messages=messages,
                options={
                    "temperature": 0.7,  # Balanced creativity
                    "top_p": 0.9,
                    "num_predict": 256,  # Max tokens (keep responses concise)
                }
            )
            
            return response['message']['content'].strip()
            
        except Exception as e:
            print(f"LLM Error: {e}")
            return self._fallback_response(user_query, user_data, role)
    
    def _build_system_prompt(
        self, 
        role: str, 
        user_data: Optional[Dict], 
        context_docs: Optional[List[str]]
    ) -> str:
        """Build system prompt with context"""
        
        prompt = """You are a helpful AI assistant for HICAS (Hindustan Institute of Computer Applications and Sciences).

Your role: Provide accurate, friendly, and concise responses to students, faculty, and staff.

Guidelines:
- Be professional but friendly
- Keep responses concise (2-3 sentences for simple queries)
- Use emojis sparingly for visual appeal
- If you don't know something, say so honestly
- For personal data queries, use the provided user information
- For general queries, use the knowledge base documents provided

"""
        
        # Add user-specific context
        if user_data and role == "student":
            prompt += f"\nCurrent Student Information:\n"
            prompt += f"- Name: {user_data.get('name', 'N/A')}\n"
            prompt += f"- Department: {user_data.get('department', 'N/A')}\n"
            prompt += f"- Year: {user_data.get('year', 'N/A')}\n"
            prompt += f"- Attendance: {user_data.get('attendance', 'N/A')}%\n"
            prompt += f"- CGPA: {user_data.get('gpa', 'N/A')}\n"
            prompt += f"- Fees Due: ₹{user_data.get('fees_due', 0)}\n"
            # Dynamic Schedule Info
            prompt += f"- Next Class: {user_data.get('next_class', 'N/A')}\n"
            prompt += f"- Next Activity (Now): {user_data.get('next_hour_activity', 'N/A')}\n"
            prompt += f"- Upcoming Exam: {user_data.get('next_exam', 'N/A')} on {user_data.get('exam_date', 'N/A')}\n"
            prompt += f"- Next Holiday: {user_data.get('next_holiday', 'N/A')}\n"
        
        elif user_data and role == "employee":
            prompt += f"\nCurrent Employee Information:\n"
            prompt += f"- Name: {user_data.get('name', 'N/A')}\n"
            prompt += f"- Designation: {user_data.get('designation', 'N/A')}\n"
            prompt += f"- Department: {user_data.get('department', 'N/A')}\n"
            prompt += f"- Leave Balance: {user_data.get('leave_balance', 'N/A')} days\n"
            prompt += f"- Salary: ₹{user_data.get('salary', 0):,.2f}\n"
            # Dynamic Schedule Info
            prompt += f"- Next Class to Teach: {user_data.get('next_class_to_teach', 'N/A')}\n"
            prompt += f"- Next Activity (Now): {user_data.get('next_hour_activity', 'N/A')}\n"
            prompt += f"- Upcoming Task: {user_data.get('next_task', 'N/A')}\n"
            prompt += f"- Deadlines: {user_data.get('submission_deadline', 'N/A')}\n"
            prompt += f"- Next Holiday: {user_data.get('next_holiday', 'N/A')}\n"
        
        # Add knowledge base context
        if context_docs:
            prompt += "\nRelevant Knowledge Base:\n"
            for i, doc in enumerate(context_docs[:3], 1):
                prompt += f"{i}. {doc}\n"
        
        prompt += "\nRespond naturally and helpfully based on the above information."
        
        return prompt
    
    def _fallback_response(self, query: str, user_data: Optional[Dict], role: str) -> str:
        """Fallback response when LLM is not available"""
        
        query_lower = query.lower()
        
        # Quick pattern matching for common queries
        if "attendance" in query_lower and user_data and role == "student":
            att = user_data.get('attendance', 'N/A')
            return f"Your current attendance is {att}%. The minimum requirement is 75%."
        
        if "cgpa" in query_lower or "gpa" in query_lower and user_data and role == "student":
            gpa = user_data.get('gpa', 'N/A')
            grade = user_data.get('grades', 'N/A')
            return f"Your CGPA is {gpa} with a grade of {grade}."
        
        if "fees" in query_lower and user_data and role == "student":
            fees = user_data.get('fees_due', 0)
            if fees == 0:
                return "You have no pending fees. Your account is clear!"
            return f"You have ₹{fees:,.2f} in pending fees."
        
        if "leave" in query_lower and user_data and role == "employee":
            leave = user_data.get('leave_balance', 'N/A')
            return f"You have {leave} days of leave remaining."
        
        if "salary" in query_lower and user_data and role == "employee":
            salary = user_data.get('salary', 0)
            return f"Your annual salary is ₹{salary:,.2f}."
        
        return "I'm here to help! Could you please rephrase your question or ask about your attendance, grades, fees, or other university information?"
    
    def stream_response(
        self, 
        user_query: str, 
        user_data: Optional[Dict] = None,
        context_docs: Optional[List[str]] = None,
        role: str = "student"
    ):
        """
        Stream response for real-time display (future enhancement)
        """
        if not self.available:
            yield self._fallback_response(user_query, user_data, role)
            return
        
        try:
            system_prompt = self._build_system_prompt(role, user_data, context_docs)
            
            messages = [
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_query}
            ]
            
            stream = ollama.chat(
                model=self.model_name,
                messages=messages,
                stream=True,
                options={
                    "temperature": 0.7,
                    "num_predict": 256,
                }
            )
            
            for chunk in stream:
                if 'message' in chunk and 'content' in chunk['message']:
                    yield chunk['message']['content']
                    
        except Exception as e:
            print(f"Streaming error: {e}")
            yield self._fallback_response(user_query, user_data, role)


# Singleton instance
_llm_instance = None

def get_llm() -> LocalLLM:
    """Get or create LLM instance"""
    global _llm_instance
    if _llm_instance is None:
        _llm_instance = LocalLLM(model_name="phi3")
    return _llm_instance
