# Google DevFest Medan 2024 Workshop Gemini API

This project is purposed for [Google DevFest Medan 2024 Workshop](https://gdg.community.dev/events/details/google-gdg-medan-presents-devfest-medan-2024/). This is only a simple [Gemini](https://gemini.google.com/) API usage to show how it works.

### Dependencies

This project requires the following Python library:

* `google-generativeai`


### Usage

Create your `.env` file, I have provide `.env.dist` as template for configurations. Just run `cp .env.dist .env` to create the file. Then adjust these configurations:

1. `GEMINI_API_KEY`
Replace `YOUR_API_KEY` with your actual Gemini API Key.

```bash
GEMINI_API_KEY=YOUR_API_KEY
```

2. `MODEL_NAME`
By default this project use `gemini-1.5-flash` as `model_name`. You can change it with another models like `gemini-1.5-pro` or `gemini-1.5-flash-8b`.

```bash
GEMINI_API_KEY=YOUR_API_KEY
```

3. `SYSTEM_INSTRUCTION`:
Replace `YOUR_INSTRUCTION` with your actual `system_instruction`. The more detail the instructions you give, the more detail result you get.

```bash
SYSTEM_INSTRUCTION=YOUR_INSTRUCTION
```

4.  Run the Script:
I prefer to use `docker`, so make sure you have it.

```bash
docker-compose build chatbot
docker-compose run --rm chatbot
```

This will start interactive chat. Make sure the `SYSTEM_INSTRUCTION` you defined in `.env` is related with the chat. And just type `exit` if you want to stop the interactive chat.


### Code Structure

The code consists of a single Python script (`main.py`) that performs the following:
 - Imports `google-generativeai` library and loads the Gemini API Key from the .env file.
 - Configures the GenerativeModel with modle name, safety settings, generation configurations, and system instructions.
 - Creates a chat history list.
 - Starts a loop that continuously prompts the user for input and sends it to the model.
 - Receives the model's response and prints it to the console.
 - Updates the chat history with both user input and model responses.


### Authors

- [Dolly Aswin Harahap](https://medium.com/@dollyaswin)
