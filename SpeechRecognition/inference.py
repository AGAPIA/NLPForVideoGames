# NOTE: this requires PyAudio because it uses the Microphone class
import speech_recognition as sr

from flask import Flask, request, jsonify
import string
import requests
app = Flask(__name__)


r = sr.Recognizer()


@app.route("/listenfrommic", methods=['GET'])
def inference():
    audioToText = None
    with sr.Microphone() as source:
        print("Listening from mic something...")
        audio = r.listen(source)
        print("finished listening from mic...")

        # Try to recognize the audio
        succeeded = False
        # recognize speech using Google Speech Recognition
        try:
            # for testing purposes, we're just using the default API key
            # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
            # instead of `r.recognize_google(audio)`
            audioToText = r.recognize_google(audio)
            print("Google Speech Recognition thinks you said " + audioToText)
            succeeded = True
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")
        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))

        if succeeded is False:
            try:
                audioToText = r.recognize_sphinx(audio)
                print("Sphinx thinks you said " + audioToText)
                succeeded = True
            except sr.UnknownValueError:
                print("Sphinx could not understand audio")
            except sr.RequestError as e:
                print("Sphinx error; {0}".format(e))

    if audioToText is None:
        audioToText = "Didn't catch That"

    response = dict()
    response['textRecognized'] = audioToText
    response = jsonify(response)

    return response

if __name__ == "__main__":
    # Run the server
    app.run(debug=True, port=5002)
