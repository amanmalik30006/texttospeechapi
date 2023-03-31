from flask import Flask, request, send_file
from gtts import gTTS
import io

app = Flask(__name__)

def text_to_speech(text, lang='en', slow=False):
    """
    Converts text to speech and returns the speech as an mp3 file.

    Parameters:
    text (str): The text to be converted to speech.
    lang (str): The language to use for the speech. Default is 'en' (English).
    slow (bool): Whether to speak slowly or not. Default is False.

    Returns:
    io.BytesIO: A file-like object containing the mp3 audio data.
    """
    # Create a gTTS object with the specified parameters
    tts = gTTS(text=text, lang=lang, slow=slow)

    # Save the speech as an mp3 file in memory
    mp3_file = io.BytesIO()
    tts.write_to_fp(mp3_file)
    mp3_file.seek(0)

    return mp3_file

@app.route('/tts', methods=['POST'])
def tts():
    """
    Converts text to speech and returns the speech as an mp3 file.

    Parameters:
    text (str): The text to be converted to speech.
    lang (str): The language to use for the speech. Default is 'en' (English).
    slow (bool): Whether to speak slowly or not. Default is False.

    Returns:
    str: A string containing the mp3 audio data.
    """
    # Get the text, language, and speed from the request
    text = request.json.get('text')
    lang = request.json.get('lang', 'en')
    slow = request.json.get('slow', False)

    # Convert the text to speech
    mp3_file = text_to_speech(text, lang, slow)

    # Return the mp3 audio data as a response
    return send_file(mp3_file, mimetype='audio/mpeg')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
