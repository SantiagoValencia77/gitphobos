import gradio as gr
import requests
import json

# Format the text to look cleaner
def format_text(output_text):
    # Check if it's a list
    if isinstance(output_text, list):
        # Join elements together
        formatted_output = ''.join(output_text)
    else:
        # Remove square bracketes and extra spaces
        formatted_output = output_text
    return formatted_output

first_interaction = True

# Create function to grab input text, pass to LLM API, retreive text from API and return that response
def generate_text(input_data, interface):
    """
    Fetch the LLM API, with the user's input text, pass the text
    to the LLM, retrieve the LLM response via API and return that response
    to the interface for the user.
    """
    global first_interaction
    if first_interaction:
        first_interaction = False
        return f'Hi, Please click down below under the examples: "gen phobos" = General Questions outside of medicine. "phobos" = Questions specifically medical. Before you ask me the questions :)'
    
    else:
        # Create a dictionary with the key "input" and the value as the input_data string
        data = {"input": input_data}
        api_url = 'http://localhost:8000/generate' # Url of FLASH API
        response = requests.post(api_url, json=data)
        output_text = response.json()['output']
        formatted_text = format_text(output_text=output_text)
        return formatted_text

# let's pass the response into the interface
iface = gr.ChatInterface(fn=generate_text,
                         #chatbot=gr.Chatbot(height=300),
                         textbox=gr.Textbox(placeholder="Ask me your questions.", label="Phobos Mode"),
                         title="Phobos 🪐",
                         theme='soft',
                         description="I'm your medical assistant.",
                         examples=["gen phobos",
                                    "phobos",
                                    "reset memory"]
                        )
iface.launch(port=5000) #C:/Users/santi/Deep-Learning/rag/medical-rag/venv/Scripts/python.exe gpt-llm.py