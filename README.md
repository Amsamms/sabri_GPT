
# Chat with OpenAI

This is a Streamlit application that allows users to chat with OpenAI's language models (GPT-4 and GPT-3.5-turbo-0125). The application provides a simple user interface to interact with the models by sending and receiving messages in a conversational format.

## Features

- Choose between available OpenAI models.
- Send messages and receive responses from the selected model.
- Clear chat history to start fresh conversations.
- Provide specific instructions to guide the assistant's behavior.
- Input OpenAI API key securely.

## Requirements

- Python 3.7+
- Streamlit
- OpenAI Python client library

## Usage

1. Run the Streamlit application.

2. Enter your OpenAI API key in the sidebar.

3. Choose a model from the dropdown menu in the sidebar.

4. Provide any specific instructions for the assistant in the sidebar.

5. Start chatting with the model by typing your messages and pressing the "Send" button.

## File Structure

- `Sabri_gpt.py`: The main Python script containing the Streamlit application.

## Code Overview

The script initializes a Streamlit application with the following main components:

- **Session State Initialization**: Initializes session state variables for messages, API key, and instructions.
- **Clear Chat Function**: A function to clear the chat history.
- **Streamlit UI**: Defines the layout of the application, including the title, sidebar inputs (API key, instructions, model selection, and clear history button), and the main chat interface.
- **User Input Handling**: Captures user input and sends it to the OpenAI API to generate a response. Handles potential rate limit errors.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.

## Acknowledgements

- [Streamlit](https://streamlit.io/)
- [OpenAI](https://openai.com/)
