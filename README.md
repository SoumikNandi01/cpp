# Cocktail Party Problem
Humble Approach in solving the cocktail party problem by using machine learning techniques, more precisely ICA and PCA algorithms.
How to use the piece of software : 
1. Clone the repo
2. Under the ./sounds directory run the recordX.py and recordY.py to record two audios (default record time is 10s). This will generate two audios namely sourceX.wav and sourceY.wav
3. Under the same directory run preprocess_sound.py to preprocess the two audio clips such as setting the bitrate and the length of the audio clips.
4. Run mixing_sound.py. This will mix two audios in different proportions to  generate mixedX.wav and mixedY.wav.
5. Next, from the root directory run, sound_FastICA_FOBI.py to generate two separate audio files one, FOBIseparateX.wav and another FOBIseparateY.wav. These are the two source files which are being separated from the mixed audio signals. 
