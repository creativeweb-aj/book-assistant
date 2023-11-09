import os
from dotenv import load_dotenv
import streamlit as st
from langchain.llms import OpenAI
from langchain.chat_models import ChatOpenAI

load_dotenv(os.path.join(os.path.dirname(__file__), '.env'))

# Initialize OpenAI with your API key
openai_api_key = os.environ.get('OPENAI_API_KEY', '')  # Replace with your actual OpenAI API key
openai_llm = OpenAI(model_kwargs={'api_key': openai_api_key})

# Initialize ChatOpenAI
chat_model = ChatOpenAI()

# Create Streamlit interface for input
st.title("Book Name Assistant")
user_interest = st.text_input("Enter your interests coma separated to get book recommendations:")
# Process user input and display response
if user_interest:
    try:
        # Generate custom prompt using the user's interests
        text = (f"I am looking for book recommendations based on my interest in {user_interest}. "
                f"Can you suggest some titles?")
        # Get the response from ChatOpenAI
        response = chat_model.predict(text)
        # Display the book names
        st.write("Based on your interest, here are some book recommendations:")
        st.write(response)
    except Exception as e:
        print(f"Exception --> {e}")
        # Display the book names
        st.write("Error in APP: ")
        st.write(str(e))
