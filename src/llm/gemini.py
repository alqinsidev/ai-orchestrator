import dspy
import google.generativeai as genai
from config import GEMINI_API_KEY, GEMINI_MODEL_NAME


class GeminiModule(dspy.Module):
    def __init__(self, model: str = GEMINI_MODEL_NAME):
        super().__init__()
        genai.configure(api_key=GEMINI_API_KEY)
        self.model = genai.GenerativeModel(model)

    def generate(self, prompt: str) -> str:
        """generate gemini response"""
        response = self.model.generate_content(prompt)
        return response.text if response else "No response"

    def stream_generate(self, prompt: str):
        """Streaming call: Yields response chunks in real-time."""
        response = self.model.generate_content(prompt, stream=True)
        for chunk in response:
            if chunk.text:
                yield chunk.text
