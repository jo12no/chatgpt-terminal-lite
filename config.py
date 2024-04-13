"""Configuration for chatgpt-terminal-lite.py

If you have an API key, you can enter it directly here.
However, for better security practices, it is recommended to set it as an 
environment variable.

To use an environment variable, set the API_KEY environment variable in your 
operating system.
If you're unsure how to do this, refer to the documentation specific to your 
operating system or deployment environment.

If you prefer to enter the API key directly (not recommended for production), replace 
'API_KEY' with your actual API key.
Otherwise, the code will attempt to read the key from the environment variable.
"""

OPENAI_API_KEY = ""

# Constants
MODEL_PARAMS = {
    "model": "gpt-4-turbo-2024-04-09",
    "n": 1,  # of samples
    "temperature": 1.0,
    "max_tokens": 4090,
}

# Enable this for an initial prompt, eg: 'You are creative and helpful'.
SESSION_PROMPT = ""
