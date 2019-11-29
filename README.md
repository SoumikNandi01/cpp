# Cocktail Party Problem
Humble Approach in solving the cocktail party problem by using machine learning techniques, more precisely ICA and PCA algorithms. 
Cocktail party problem also known as the blind source separation is a classical problem in the signal processing domain.
The motivation for this problem is, imagine yourself in a party with a lot of people.  
There will be a sort of cacaphony because of all the people talking at the same time.  
Now you can shut out the voices in the background to hear some specific conversation or some specific human voice.  
We also want to do the same by using machine learning tools
How to use the piece of software : 
1. Clone the repo
2. Under the ./sounds directory run the recordX.py and recordY.py to record two audios (default record time is 10s). This will generate two audios namely sourceX.wav and sourceY.wav
3. Under the same directory run preprocess_sound.py to preprocess the two audio clips such as setting the bitrate and the length of the audio clips.
4. Run mixing_sound.py. This will mix two audios in different proportions to  generate mixedX.wav and mixedY.wav.
5. Next, from the root directory run, sound_FastICA_FOBI.py to generate two separate audio files one, FOBIseparateX.wav and another FOBIseparateY.wav. These are the two source files which are being separated from the mixed audio signals. 
