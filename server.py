from flask import Flask, request, redirect
from espeak import espeak
from .espeak import ESpeak
import twilio.twiml
import urllib, pycurl, os
import collections
import re
import subprocess

class ESpeak:
	 def __init__(self, amplitude=80, word_gap=5, capitals=1, line_length=1,
                 pitch=50, speed=30, voice='en', spell_punctuation=[],
                 split=''):
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
	data = str.encode(parameters)
	textPhrase = "%s%s" % (textPhrase,data)
	return textPhrase

def speakSpeechFromText(phrase):
	phrase = getPhrase(phrase)
	espeak.synth(phrase)
	
@property
def amplitude(self):
        return self.args['amplitude']

@amplitude.setter
def amplitude(self, v):
        self.args['amplitude'][1] = v

@property
def word_gap(self):
        return self.args['word_gap']

@word_gap.setter
def word_gap(self, v):
        self.args['word_gap'][1] = v

@property
def capitals(self):
        return self.args['capitals']

@capitals.setter
def capitals(self, v):
        self.args['capitals'][1] = v

@property
def line_length(self):
        return self.args['line_length']

@line_length.setter
def line_length(self, v):
        self.args['line_lenght'][1] = v

@property
def pitch(self):
        return self.args['pitch']

@pitch.setter
def pitch(self, v):
        self.args['pitch'][1] = v

@property
def speed(self):
        return self.args['speed']

@speed.setter
def speed(self, v):
        self.args['speed'][1] = v

@property
def voice(self):
        return self.args['voice']

@voice.setter
def voice(self, v):
        self.args['voice'][1] = v

@property
def spell_punctuation(self):
        return self.args['spell_punctuation']

@spell_punctuation.setter
def spell_punctuation(self, v):
        self.args['spell_punctuation'][1] = v

@property
def split(self):
        return self.args['split']

@split.setter
def split(self, v):
        self.args['split'][1] = v

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
