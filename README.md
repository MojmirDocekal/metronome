# metronome.py

This is a fork of the original Python 2 metronome application, updated and adapted by Mojmír Dočekal to run on Python 3 in 2026, especially on Linux machines.

A light program that uses python, python-mingus and fluidsynth to reproduce a tone at any regular rate

## Installation

You will need `python3`, `python-mingus` and `fluidsynth` to use this script. `python-mingus` is a wonderful python module dedicated to music; if it isn't in your distribution's repo you can install it with:
  ```
pip install mingus
  ```

Download and run the script. You will also need `getch.py`, `switch.py` and a soundfont file, called `african.sf2`, living in the same directory as the script. Soundfont courtesy of Thomas Hammer at hammersound: http://hammersound.net/hs_soundfonts.html. Note: while his website mentions a copyright at the bottom, I was unable to locate any license involved in this copyright. The site just mentions that one can download and use the soundfonts. TBC...

## Usage

The syntax is:

  `python3 metronome.py [tempo]`

where tempo is an optional integer expressed in beats per minute (bpm). If it is omitted, the tempo will default to 80. The script will run forever; to quit press `q`; to interrupt press any other key. Press a key again to resume.

Note: For audio to work, ensure fluidsynth and an audio driver (ALSA, PulseAudio, or JACK) are properly installed on your Linux system.
