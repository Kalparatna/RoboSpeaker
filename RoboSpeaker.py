# Import necessary modules
import win32com.client
from flask import Flask, render_template, request

# Create a Flask app
app = Flask(__name__)

# Create a SAPI.SpVoice object
speaker = win32com.client.Dispatch("SAPI.SpVoice")

# Define a route to render the HTML form
@app.route('/')
def index():
    return render_template('index.html')

# Define a route to handle the form submission
@app.route('/speak', methods=['POST'])
def speak():
    text = request.form['text']
    if text == "0":
        speaker.speak("Ok bye, See you again")
    else:
        speaker.Speak(text)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
