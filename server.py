from flask import Flask, request, redirect
from espeak import espeak
import twilio.twiml
import urllib, pycurl, os
import collections
import re
import subprocess

class ESpeak:
    def __init__(self, amplitude=100, word_gap=10, capitals=1, line_length=1,
                 pitch=50, speed=50, voice='en', spell_punctuation=[],
                 split=''):
        """
        The base ESpeak class. You can set espeak's arguments from the
        named parameters or change them after creation using the properties
        """

        args = [('amplitude',         ['-a', amplitude, int]),
                ('word_gap',          ['-g', word_gap, int]),
                ('capitals',          ['-k', capitals, int]),
                ('line_length',       ['-l', line_length, int]),
                ('pitch',             ['-p', pitch, int]),
                ('speed',             ['-s', speed, int]),
                ('voice',             ['-v', voice, str]),
                ('spell_punctuation', ['--punct=', ''.join(spell_punctuation),
                                       str]),
                ('split',             ['--split=', split, str])]
        self.args = collections.OrderedDict(args)

def getPhrase(phrase):
	textPhrase = ""
	parameters = {"": phrase}
	data = urllib.urlencode(parameters)
	textPhrase = "%s%s" % (textPhrase,data)
	return textPhrase

def speakSpeechFromText(phrase):
	phrase = getPhrase(phrase)
	espeak.synth(phrase) -s100
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
