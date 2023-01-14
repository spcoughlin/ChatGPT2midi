
# ChatGPT2midi 🎶    
A Python program that generates chord progressions with ChatGPT using [acheong08's ChatGPT API](https://github.com/acheong08/ChatGPT)

Tell ChatGPT what kind of chord progression you want, and you will have a midi file in seconds. I find it fun to just mess around, getting it to generate some pretty wacky chord progressions, and trying to play over them.

  
# Installation  
Run the following commands:

`git clone https://github.com/spcoughlin/ChatGPT2midi.git`

`cd ChatGPT2midi`

`pip install -r requirements.txt`

Follow the steps in [https://github.com/acheong08/ChatGPT/wiki/Setup](https://github.com/acheong08/ChatGPT/wiki/Setup) to replace "`YOUR-TOKEN`" with your token where the chatbot is initialized, near the top of `main.py`, or you can use another login method entirely if needed.

  
# Usage  
To run the program, just run `main.py`.

Once the browser window appears, the program will ask for what progression you want to make. I have added all the formatting stuff already, so you really just have to tell it what you want. Good examples include:

 - "Write a chord progression in Bb Blues"
 - "Write a chord progression that I can play an Ebm7 scale over"
 - "Write a chord progression in F using some 6/9 chords"
