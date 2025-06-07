import google.generativeai as genai
import os
from dotenv import load_dotenv
load_dotenv()

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=GOOGLE_API_KEY)


class GoogleGemini:
    def __init__(self, model_name="gemini-1.5-flash-latest"):
        self.model = genai.GenerativeModel(model_name)

    def ask(self, context, question):
        prompt = f"""Answer the question based on the context below:

        {context}

        Question: {question}

        Make sure the answer is concise and relevant only, no extra text.
        """
        response = self.model.generate_content(prompt)
        return response.text
