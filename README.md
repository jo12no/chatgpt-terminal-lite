# chatgpt-terminal-lite
A lightweight Python CLI application that opens an interactive chat session with OpenAI language models using the provided API. 
<img width="554" alt="example" src="https://github.com/jo12no/chatgpt-terminal-lite/assets/19522573/509a8589-eca1-40f3-8832-486df4b89c92">
## Getting Started
* Add your OpenAI API key to either the config.py file or as an enviroment variable:
_export OPEN_API_KEY="KEY"_
* Adjust other configuration options in the config.py as needed (eg. changing models) - uses "gpt4" by default. 
* Using a shell alias, you can conveniently create a session using your own keyword. For example, adding the below to .bash_profile:
_alias chat='python path_to_script.py'_

## Considerations
* It's a significant productivity boost for me to be able to quickly ask throwaway questions while in the middle of doing work with a terminal open. 
* Privacy and security centric because it is a simple wrapper around the OpenAI API, without introducing another 3rd party. 
* Uses the latest conversional API endpoints. 
