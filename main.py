from pychord import Chord
import pretty_midi
import time
from revChatGPT.ChatGPT import Chatbot

global chatbot
chatbot = Chatbot({
    "session_token": "YOUR-TOKEN" # place your token here
}, conversation_id=None, parent_id=None)


def create_midi(chords):
    """
    This function is adapted from https://github.com/yuma-m/pychord/blob/main/examples/pychord-midi.py
    """
    midi_data = pretty_midi.PrettyMIDI()
    piano_program = pretty_midi.instrument_name_to_program('Acoustic Grand Piano')
    piano = pretty_midi.Instrument(program=piano_program)
    length = 1
    for n, chord in enumerate(chords):
        for note_name in chord.components_with_pitch(root_pitch=4):
            note_number = pretty_midi.note_name_to_number(note_name)
            note = pretty_midi.Note(velocity=100, pitch=note_number, start=n * length, end=(n + 1) * length)
            piano.notes.append(note)
    midi_data.instruments.append(piano)
    timestr = time.strftime("%Y%m%d-%H%M%S")
    midi_data.write(f'progression-{timestr}.mid')


def main():
    user_input = input("Enter what kind of chord progression you would like to generate: ")

    response = chatbot.ask(f"{user_input} in the format of this chord progression: Bb7 - Bb7 - Bb7 - Bb7\nEb7 - Eb7 - "
                           f"Bb7 - Bb7\nAb7 - Ab7 - Bb7 - Bb7\nEb7 - Bb7 - Ab7 - Eb7\nDo not write anything other than the chord progression itself.",
                           conversation_id=None,
                           parent_id=None)

    print(response["message"])
    lines = response["message"].split("\n")

    letters = ["A", "B", "C", "D", "E", "F", "G"]

    # removing the lines breaks
    lines_nobreak = []
    for i in lines:
        if i[0] in letters:
            lines_nobreak.append(i)

    # making it a list of just the chord symbols
    chords_str = []
    for i in lines_nobreak:
        for j in i.split(" - "):
            if j.__contains__("\n"):
                chords_str.append(j[0:-1])
            else:
                chords_str.append(j)

    chords = [Chord(c) for c in chords_str]
    create_midi(chords)

    print("File created!")
    end_input = input("Would you like to generate another midi file? (Y/N) ")
    if end_input == "Y" or end_input == "y":
        main()
    else:
        input("Press enter to close the program")


if __name__ == '__main__':
    main()
