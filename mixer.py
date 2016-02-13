import os, math
from pydub import AudioSegment
from random import randint

if os.name == "nt":
	AudioSegment.converter = r"C:\\ffmpeg\\bin\\ffmpeg.exe"

import os, math, sys
from pydub import AudioSegment
from random import randint

print("Exporting to MP3 track takes 20-40 seconds. Exporting to WAV much faster.")

format_selected = ""

user_input = input("Please select export format. 1 - MP3, 2 - WAV: ")

while (user_input != "1") and (user_input != "2"):
	print("You typed '" + user_input + "'. But you should type 1 or 2.")
	user_input = input("Please select export format. 1 - MP3, 2 - WAV: ")

if user_input == "1":
	format_selected = "mp3"
elif user_input == "2":
	format_selected = "wav"

def export(format_selected):
		output.export("Result/{}".format(filename + " + " + os.path.splitext(background)[0] + 
						"." + format_selected), format=format_selected, bitrate="320k")
		print("Ready: {}".format(filename + " + " + os.path.splitext(background)[0] + "." + format_selected))


for voice in os.listdir("Voice"):
	for background in os.listdir("Background"):
		if voice.endswith(".mp3") or voice.endswith(".wav"):
			if background.endswith(".mp3") or background.endswith(".wav"):

				sound1 = AudioSegment.from_file("Voice/{}".format(voice))
				sound2 = AudioSegment.from_file("Background/{}".format(background))
				sound1 = AudioSegment.high_pass_filter(sound1, 2000)
				sound1 = AudioSegment.low_pass_filter(sound1, 2000)
				sound1 = AudioSegment.normalize(sound1, headroom=-1.0)

				while len(sound2) < 600000:
					sound2 = sound2 * 2

				while len(sound1) < len(sound2):
					random_silence = AudioSegment.silent(duration=(randint(2,7)*1000))
					sound1 = sound1 + random_silence + sound1

				output = sound2.overlay(sound1, position=2000)
				filename = os.path.splitext(voice)[0]

				if not os.path.exists("Result"):
					os.makedirs("Result")

				export(format_selected)
		



