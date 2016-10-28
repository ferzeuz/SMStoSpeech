from flask import Flask, request, redirect
from espeak import espeak
import twilio.twiml
import urllib, pycurl, os

def getPhrase(phrase):
	textPhrase = ""
	parameters = {"": phrase}
	data = str.encode(parameters)
	textPhrase = "%s%s" % (textPhrase,data)
	return textPhrase

def speakSpeechFromText(phrase):
	phrase = getPhrase(phrase)
	espeak.synth(phrase)
	print("Espeak on")
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
