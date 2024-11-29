import os, sys
import google.generativeai as genai


# suppress logging warnings
os.environ["GRPC_VERBOSITY"]   = "ERROR"
os.environ["GLOG_minloglevel"] = "2"

# Create the model. Ref https://ai.google.dev/api/python/google/generativeai/GenerativeModel
generation_config = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 64,
  "max_output_tokens": 8192,
  "response_mime_type": "text/plain",
}

safety_settings = [
  {
    "category": "HARM_CATEGORY_HARASSMENT",
    "threshold": "BLOCK_NONE",
  },
  {
    "category": "HARM_CATEGORY_HATE_SPEECH",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE",
  },
  {
    "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE",
  },
  {
    "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE",
  },
]

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel(
  model_name=os.getenv("MODEL_NAME"),
  generation_config=generation_config,
  safety_settings=safety_settings,
  system_instruction=os.getenv("SYSTEM_INSTRUCTION")
)
chat_session = model.start_chat(
    history=[]
)

print("Bot: Halo, bingung mau kuliah S1 jurusan apa?")
print()

while True:
    user_input = input("You: ")

    # exit from app
    if user_input.lower() == 'exit':
        sys.exit(0)

    response = chat_session.send_message(user_input)
    model_response = response.text

    print()
    print(f'Bot: {model_response}')
    print()
    chat_session.history.append({"role": "user",  "parts": [user_input]})
    chat_session.history.append({"role": "model", "parts": [model_response]})
