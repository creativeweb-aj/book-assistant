import os
from dotenv import load_dotenv
import streamlit as st
from langchain.llms import OpenAI
from langchain.chat_models import ChatOpenAI
from langchain.prompts import SystemMessagePromptTemplate, HumanMessagePromptTemplate, ChatPromptTemplate

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
        # System generate message prompt
        systemTemplate = ("I am looking for book recommendations based on my interest in {interest}. "
                          "Can you suggest some titles?")
        systemMessagePromptTemplate = SystemMessagePromptTemplate.from_template(systemTemplate)

        # Human input message prompts
        humanTemplate = "{user_interest}"
        humanMessagePromptTemplate = HumanMessagePromptTemplate.from_template(humanTemplate)

        # Create chat prompt by passing user input and convert into message string
        chatPrompt = ChatPromptTemplate.from_messages([systemMessagePromptTemplate, humanMessagePromptTemplate])
        inputs = chatPrompt.input_variables
        chatPrompt = chatPrompt.format_prompt(user_interest=user_interest, interest=user_interest).to_messages()

        # Get the response from ChatOpenAI
        response = chat_model(chatPrompt)
        # Display the book names
        st.write("Based on your interest, here are some book recommendations:")
        st.write(response.content)
    except Exception as e:
        print(f"Exception --> {e}")
        # Display the book names
        st.write("Error in APP: ")
        st.write(str(e))
