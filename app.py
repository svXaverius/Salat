from flask import Flask, render_template, request, jsonify, make_response
import json
from datetime import datetime
import answergen
from datetime import datetime



app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/send_message', methods=['POST'])
def send_message():
    user_message = request.json.get('message')
    chat_history = request.cookies.get('chat_history')
    
    if chat_history:
        chat_history = json.loads(chat_history)
    else:
        chat_history = []

    # Add user's message to chat history with datetime
    user_message_data = {
        'sender': 'user',
        'message': user_message,
        'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M")
    }
    chat_history.append(user_message_data)

    # Generate a response
    response_message = answergen.generate_response(user_message, chat_history, "Praha 5", datetime.now().strftime("%d.%m.%Y %H:%M:%S"))

    response_message_data = {
        'sender': 'bot',
        'message': response_message,
        'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M")
    }
    chat_history.append(response_message_data)

    # Update the cookie
    resp = make_response(jsonify({'response': response_message_data}))
    resp.set_cookie('chat_history', json.dumps(chat_history))

    return resp

@app.route('/get_chat_history', methods=['GET'])
def get_chat_history():
    chat_history = request.cookies.get('chat_history')
    if chat_history:
        chat_history = json.loads(chat_history)
    else:
        chat_history = []
    return jsonify(chat_history)

@app.route('/delete_history', methods=['POST'])
def delete_history():
    response = make_response(jsonify({"message": "History deleted"}))
    response.set_cookie('chat_history', '', expires=0)
    return response

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=80)