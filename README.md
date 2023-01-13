# ChatGPT2midi  
A Python script that converts a ChatGPT-generated chord progression into a .midi file

# Installation
To install the required dependencies, simply run:

    $ pip install -r requirements.txt  

in your preferred environment.

# Usage
Copy + paste your chord progression from ChatGPT into the input.txt file, making sure it is the only thing in the file.

![spicychords](https://user-images.githubusercontent.com/99555305/206938153-0839d3cf-73a4-44b3-a4fc-fc66cfb95140.png)

This is what the input format should look like, and the highlighted text shows what you should put into input.txt. If you get a different format, you can add on "in 4 lines with 4 chords per lines, and dashes separate the chords" to your query to force this format.

Run the file, and a timestamped .midi file will be placed in the same directory as everything else.