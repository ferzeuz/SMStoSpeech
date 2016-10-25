from flask import Flask, request, redirect
from espeak import espeak
import twilio.twiml
import urllib, pycurl, os

def speakSpeechFromText(phrase):
	phrase = sms
	espeak.synth(phrase)
	print ("Espeak on")


app = Flask(__name__)
@app.route("/", methods=['GET', 'POST'])
def hello_monkey():
        """Respond to incoming calls with a simple text message."""
        sms = request.args.get('Body')
	
        if not sms == "":
                speakSpeechFromText(sms)
        resp = twilio.twiml.Response()
        return str(resp)

if __name__ == "__main__":
	print ("Hello twilio")
	app.run( host='0.0.0.0', debug=True, port = 80)
