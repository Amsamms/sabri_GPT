import streamlit as st
import openai
import base64

# Custom CSS for styling
st.markdown("""
    <style>
    .title {
        font-size: 48px;
        color: #4CAF50;
        text-align: center;
    }
    .sidebar .sidebar-content {
        background-color: #f9f9f9;
        padding: 20px;
    }
    .user-message {
        background-color: #e1f5fe;
        border-radius: 10px;
        padding: 10px;
        margin: 5px 0;
    }
    .footer {
        position: fixed;
        left: 0;
        bottom: 0;
        width: 100%;
        text-align: center;
        padding: 10px 0;
    }
    </style>
""", unsafe_allow_html=True)

# Set up available models
available_models = [
    "gpt-4o",
    "gpt-3.5-turbo-0125",
    "asst_sK9jEcNrczzrlb3gnbtgjWCr"
]

# Initialize session state variables
if 'messages' not in st.session_state:
    st.session_state.messages = [{"role": "system", "content": "You are a helpful assistant."}]
if 'api_key' not in st.session_state:
    st.session_state.api_key = ""
if 'instructions' not in st.session_state:
    st.session_state.instructions = "You are a helpful assistant."

# Function to clear chat history
def clear_chat():
    st.session_state.messages = [{"role": "system", "content": st.session_state.instructions}]

# Function to encode image to base64
def encode_image(image):
    return base64.b64encode(image.read()).decode('utf-8')

# Streamlit UI
st.title("Chat with OpenAI")

# OpenAI API key input in sidebar
st.sidebar.title("Settings")
st.session_state.api_key = st.sidebar.text_input("Enter your OpenAI API key:", type="password")

# Only proceed if API key is provided
if st.session_state.api_key:
    openai.api_key = st.session_state.api_key

    # Instruction input in sidebar
    instructions = st.sidebar.text_area("Instructions for the assistant:", st.session_state.instructions)
    if instructions != st.session_state.instructions:
        st.session_state.instructions = instructions
        clear_chat()

    # Model selection in sidebar
    model = st.sidebar.selectbox("Choose a model", available_models)

    # Token control in sidebar
    max_tokens = st.sidebar.slider("Max tokens for response:", min_value=1, max_value=4096, value=4096)

    # Image uploader in sidebar
    uploaded_file = st.sidebar.file_uploader("Upload an image", type=["png", "jpg", "jpeg"])

    # Clear chat history button in sidebar
    if st.sidebar.button("Clear History"):
        clear_chat()

    for message in st.session_state.messages:
        role = message["role"]
        content = message["content"]
        if role == "user":
            st.markdown(f'<div class="user-message"><strong>You:</strong> {content}</div>', unsafe_allow_html=True)
        elif role == "assistant":
            st.markdown(f'<div class="assistant-message"><strong>Model:</strong> {content}</div>', unsafe_allow_html=True)
        else:
            st.markdown(f'<div class="system-message"><strong>System (Instructions):</strong> {content}</div>', unsafe_allow_html=True)

    # User input at the bottom with a "Send" button
    user_input = st.text_area("You:", key="user_input", height=100)
    if st.button("Send"):
        if user_input or uploaded_file:
            st.session_state.messages.append({"role": "user", "content": user_input})
            
            # If there is an uploaded image, encode it to base64
            if uploaded_file:
                base64_image = encode_image(uploaded_file)
                image_message = {
                    "role": "user",
                    "content": [
                        {"type": "text", "text": user_input},
                        {
                            "type": "image_url",
                            "image_url": {
                                "url": f"data:image/jpeg;base64,{base64_image}"
                            }
                        }
                    ]
                }
                st.session_state.messages.append(image_message)

            try:
                # Generate a response using OpenAI's API with error handling
                response = openai.ChatCompletion.create(
                    model=model,
                    messages=st.session_state.messages,
                    max_tokens=max_tokens
                )
                bot_reply = response['choices'][0]['message']['content']
                st.session_state.messages.append({"role": "assistant", "content": bot_reply})
                st.experimental_rerun()
            except openai.error.RateLimitError:
                st.error("You exceeded your current quota. Please check your OpenAI plan and billing details.")
else:
    st.sidebar.write("Please enter your OpenAI API key to start the conversation.")
    
# Footer
st.markdown('<div class="footer">Created by Ahmed Sabri, amsamms</div>', unsafe_allow_html=True)
