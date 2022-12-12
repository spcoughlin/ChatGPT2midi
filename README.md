# ChatGPT2midi  
A Python script that converts a ChatGPT-generated chord progression into a .midi file

# Installation
To install the required dependencies, simply run:

    $ pip install -r requirements.txt  

in your preferred environment.

# Usage
Copy + paste your chord progression from ChatGPT into the input.txt file, making sure it is the only thing in the file.
![firefox_08eHhXz5d1](https://user-images.githubusercontent.com/99555305/206937987-3674954f-e5d6-46ad-8d4c-4aea0e81aa23.png)
This is what the input format should look like. If you get a different format, you can add on "in 4 lines with 4 chords per lines, and dashes separate the chords" to your query to force this format.
Run the file, and a timestamped .midi file will be placed in the same directory as everything else.

# Supported Chords
Right now, the program supports major, minor, dim, maj7, m7, 7, sus2, sus4, aug, 6/9, 7sus, 7susadd3, add9, 7alt chords. More can be added. To add a chord, call the "build chord" function where all the others are called. The first parameter is the symbol of the chord as it appears on ChatGPT, and the rest are the numbers of semitones you go up to build the chord.

