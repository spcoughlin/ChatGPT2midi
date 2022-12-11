# ChatGPT2midi  
A Python script that converts a ChatGPT-generated chord progression into a .midi file

# Installation
To install the required dependencies, simply run:

    $ pip install -r requirements.txt  

in your preferred environment.

# Usage
Copy + paste your chord progression from ChatGPT into the input.txt file, making sure it is the only thing in the file.
Run the file, and a timestamped .midi file will be placed in the same directory as everything else.

# Supported Chords
Right now, the program only supports Major, Minor, Diminished, maj7, -7, 7, sus2, sus4, and + chords. Even with these,
I am not sure how ChatGPT writes the chord symbol, so they may not work. At the time of writing this, ChatGPT has been 
at capacity for hours, so I will add more chords/correct them when I get the chance.