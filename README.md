# mixer
Mixer of audios.
This script can mix together all files from folder "Voice" and from folder "Background".
Any voice becomes with "telephone" effect.
Final thack appears in folder "Result". Length 10-20 min randomly.

How to use:

Just create "Voice" and "Background" folders near the mixer.py file. Then add any MP3's or WAV's to these folders and start mixer.py.
"Result" folder will be created automatically.

Installation:

1. You need Python 3
2. pip install pydub
3. Install ffmpeg for Mac: brew install ffmpeg --with-libvorbis --with-ffplay --with-theora   for Linux(aptitude): apt-get install ffmpeg libavcodec-extra-53   for Windows you should install ffmpeg package to the folder "C:\ffmpeg"
