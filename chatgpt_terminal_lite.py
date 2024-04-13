"""This script initiates an interactive chat session between the user and OpenAI's 
language model using the newer API version. 

Since it is designed for quick 1 or 2 response questions, the recommendation is to add 
this file as an alias in your shell so you can access easily via the terminal to quickly 
start a session. 
"""
import os
from openai import OpenAI
import config

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", config.OPENAI_API_KEY)
SESSION_PROMPT = config.SESSION_PROMPT
MODEL_PARAMS = config.MODEL_PARAMS


def create_client():
    """Creates an OpenAI client with the specified API key."""
    if not OPENAI_API_KEY:
        raise ValueError("API key must be set in config file or environment variable.")
    return OpenAI(api_key=OPENAI_API_KEY)


def start_chat(client):
    """Initiates an interactive chat session between the user and OpenAI's language
    model.

    This function handles the user input, sends it to the OpenAI API, and prints out the
    model's response. It continues this in a loop until the user types 'quit' or 'q',
    at which point the chat session is terminated. If SESSION_PROMPT is defined, it
    starts the session with that prompt.

    Args:
        client (OpenAI): An instance of the OpenAI client with the necessary API key
    configured.

    The function expects MODEL_PARAMS to be a globally accessible variable that contains
    parameters for the OpenAI API request.

    General exceptions are caught and printed to the console without interrupting the 
    program flow. 
    """
    messages = [{"role": "system", "content": SESSION_PROMPT}] if SESSION_PROMPT else []
    print(f"model: {MODEL_PARAMS['model']}")
    print(f"'q' or 'quit' to exit.\n{'=' * 10}")
    while True:
        user_input = input("You: ").strip()
        if user_input.lower() in ["quit", "q"]:
            print("Exiting chat...")
            break

        messages.append({"role": "user", "content": user_input})

        try:
            response = client.chat.completions.create(**MODEL_PARAMS, messages=messages)
            answer = response.choices[0].message.content
            print(f"AI Response:\n{answer}")
            messages.append({"role": "assistant", "content": answer})
        except Exception as e:
            print(f"An error occurred: {e}")


if __name__ == "__main__":
    chat_client = create_client()
    start_chat(chat_client)
