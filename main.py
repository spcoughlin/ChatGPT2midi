import datetime
from pymusicxml import *
import music21
import os
from revChatGPT.revChatGPT import Chatbot

with open("input.txt", "r") as f:
    lines = f.readlines()

letters = ["A", "B", "C", "D", "E", "F", "G"]

# removing the lines breaks
lines_nobreak = []
for i in lines:
    if i[0] in letters:
        lines_nobreak.append(i)

# making it a list of just the chord symbols
chords = []
j = 0
plus = 0
for i in lines_nobreak:
    for j in i.split(" - "):
        if j.__contains__("\n"):
            chords.append(j[0:-1])
        else:
            chords.append(j)

# building the chords in terms of {ChatGPT format: pymusicxml format (notes)}

notes = ["c4", "db4", "d4", "eb4", "e4", "f4", "gb4", "g4", "ab4", "a4", "bb4", "b4", "c5", "db5", "d5",
         "eb5",
         "e5", "f5", "gb5", "g5", "ab5", "a5", "bb5", "b5", "c6", "db6", "d6", "eb6", "e6", "f6", "gb6",
         "g6",
         "ab6", "a6", "bb6", "b6"]

built_chords = {}


def build_chord(name: str, *args):
    for i in notes[0:13]:
        if i.__contains__("b"):
            key = i[0].upper() + i[1]
        else:
            key = i[0].upper()
        built_chords[f"{key + name}"] = [notes[idx + notes.index(i)] for idx in args]


build_chord("", 0, 4, 7)
build_chord("m", 0, 3, 7)
build_chord("dim", 0, 3, 6)
build_chord("maj7", 0, 4, 7, 11)
build_chord("m7", 0, 3, 7, 10)
build_chord("7", 0, 4, 7, 10)
build_chord("sus2", 0, 2, 7)
build_chord("sus4", 0, 5, 7)
build_chord("aug", 0, 4, 8)
build_chord("6/9", 0, 4, 7, 9, 14)
build_chord("7sus", 0, 5, 7, 10)
build_chord("7sus2", 0, 2, 7, 10)
build_chord("7sus4", 0, 5, 7, 10)
build_chord("7susadd3", 0, 5, 7, 10, 16)
build_chord("add9", 0, 4, 7, 14)
build_chord("7alt", 0, 3, 6, 10)

# working with pymusicxml

gen_time = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
score = Score(title=gen_time, composer="ChatGPT2midi")
part = Part("Piano")
score.append(part)

measures = []

for i in range(len(chords)):
    m = Measure(time_signature=(4, 4) if i == 0 else None)
    m.append(Chord(built_chords[chords[i]], 4.0))
    measures.append(m)

part.extend(measures)
score.export_to_file(f"{gen_time}.musicxml")

# music21: converting the musicxml to midi

convert = music21.converter.parse(f"{gen_time}.musicxml")
convert.write("midi", fp=f"{gen_time}.midi")
os.remove(f"{gen_time}.musicxml")


input("Press enter to close the program")