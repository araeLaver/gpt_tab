import streamlit as st
import openai
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Set OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")


st.title("GPT-4o")
st.write("GPT-4o ChatBot!")

# Initialize the session state if not already done
if "messages" not in st.session_state:
    st.session_state.messages = []

system_prompt = "나의 프롬프트 엔지니어링 코치가 되어줘."

# Function to get chatbot response
def get_chatbot_response(user_input):
    client = openai.OpenAI()
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            # {"role": "system", "content": "나의 프롬프트 엔지니어링 코치가 되어줘."},
            # {"role": "user", "content": "어떻게 하면 프롬프트 엔지니어링을 잘 할수 있을까?"}
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_input}
        ]
    )

    print(response.choices[0].message)
    return response.choices[0].message.content
    # return response.choices[0].message["content"]

# Input field for the user
user_input = st.text_input("메시지를 입력하세요")

# Handle user input and get chatbot response
if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})
    response = get_chatbot_response(user_input)
    st.session_state.messages.append({"role": "assistant", "content": response})

# Display messages
for msg in st.session_state.messages:
    with st.container():
        st.markdown(f"**{msg['role']}**: {msg['content']}")
