
# RoboSpeaker Project

This is a simple Flask web application that uses the Windows Speech API (SAPI) to speak text entered by the user.

## Installation

Before running the application, make sure you have the required modules installed:

```bash
pip install pywin32 Flask
```

## Usage

1. Clone this repository.
2. Run the Flask app using the following command:

    ```bash
    python app.py
    ```

3. Visit [http://localhost:5000](http://localhost:5000) in your web browser.
4. Enter the text you want the computer to speak and click the "Speak" button.
5. The computer will speak the entered text.

## Code

The main code for this project is located in `app.py`. Here's an overview of the key components:

```python
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
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
```

This Markdown version should render properly in Markdown viewers and on platforms that support Markdown formatting.
