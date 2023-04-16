from flask import Flask, render_template, request, redirect, jsonify

#from chatterbot import ChatBot
#from chatterbot.trainers import ChatterBotCorpusTrainer


#chatbot = ChatBot('VBot')
#trainer = ChatterBotCorpusTrainer(chatbot)
#trainer.train("chatterbot.corpus.english")

app = Flask(__name__)

@app.route("/", methods=["GET","POST"])
def index():
  return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    ip_data = request.get_json().get("message")
    #reply = str(chatbot.get_response(ip_data))
    reply = "how are you"
    message = {"answer":reply}
    return jsonify(message)
  
if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)