from flask import Flask, render_template, request, redirect, jsonify
import requests, json, os

#from chatterbot import ChatBot
#from chatterbot.trainers import ChatterBotCorpusTrainer

#chatbot = ChatBot('VBot')
#trainer = ChatterBotCorpusTrainer(chatbot)
#trainer.train("chatterbot.corpus.english")

app = Flask(__name__)

url = os.environ['API_URL']
key = os.environ['API_KEY']

payload = {
    "enable_google_results": "true",
    "enable_memory": False
}

headers = {
    "accept": "application/json",
    "content-type": "application/json",
    "X-API-KEY": key
}

@app.route("/", methods=["GET","POST"])
def index():
  return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    ip_data = request.get_json().get("message")

    payload["input_text"] = ip_data

    #reply = str(chatbot.get_response(ip_data))
    #reply = "how are you"

    response = requests.post(url, json=payload, headers=headers)
    if response.ok:
      reply = json.loads(response.text)['message']
    else:
      reply = 'You’ve reached your usage limit.'

    print(reply)  
    message = {"answer":reply}
    return jsonify(message)
  
if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
