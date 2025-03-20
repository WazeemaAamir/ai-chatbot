import random
import streamlit as st
import json

# Load custom responses from file
def load_custom_responses():
    try:
        with open("custom_responses.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

# Save custom responses to file
def save_custom_responses():
    with open("custom_responses.json", "w") as file:
        json.dump(st.session_state.custom_responses, file)

# Predefined responses with keyword matching
responses = {
    "hello": ["Hi there! How can I help you?", "Hello! What can I do for you?"],
    "name": ["I'm a simple chatbot created by you! 🤖"],
    "joke": [
        "Why don’t scientists trust atoms? Because they make up everything! 😂",
        "Why did the scarecrow win an award? Because he was outstanding in his field! 🌾"
    ],
    "goodbye": ["Bye! Have a great day! 😊", "Goodbye! See you soon!"],
}

# Initialize session state
if "custom_responses" not in st.session_state:
    st.session_state.custom_responses = load_custom_responses()
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Find best matching response
def get_response(user_input):
    for key, replies in responses.items():
        if key in user_input:
            return random.choice(replies)
    return None

# Streamlit UI
def chatbot():
    st.set_page_config(page_title="AI Chatbot", layout="centered")
    st.title("🤖 AI Chatbot")
    st.markdown("Chat with me! Type 'exit' or 'goodbye' to end the chat.")
    
    # Display chat history with chat bubbles
    for i, msg in enumerate(st.session_state.chat_history):
        if i % 2 == 0:
            st.chat_message("user").write(msg)
        else:
            st.chat_message("assistant").write(msg)
    
    user_input = st.text_input("You:", "").strip().lower()
    
    if user_input:
        response = ""
        
        if user_input in ["exit", "goodbye"]:
            response = "Goodbye! 👋"
        else:
            response = get_response(user_input) or st.session_state.custom_responses.get(user_input, "I don’t understand. Can you teach me how to respond?")
            
            if response == "I don’t understand. Can you teach me how to respond?":
                new_response = st.text_input("Type the response or 'skip' to ignore:")
                if new_response and new_response.lower() != "skip":
                    st.session_state.custom_responses[user_input] = new_response
                    save_custom_responses()
                    response = "Got it! I'll remember this."
        
        st.session_state.chat_history.append(f"You: {user_input}")
        st.session_state.chat_history.append(f"Bot: {response}")
        st.rerun()

# Run the chatbot
if __name__ == "__main__":
    chatbot()
