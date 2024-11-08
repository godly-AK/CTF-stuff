# m00nwalk

**Flag:** `picoCTF{beep_boop_im_in_space}`

How you approached the challenge:

- step 1

since this a message from moon we need to decode the signal
 this .wav file is a slow scan television signals(SSTV)
 we can use QSSTV to decode this 
 so we need to install qsstv first 
```
sudo apt-get install pkg-config g++ libfftw3-dev qtbase5-dev qtchooser qt5-qmake qtbase5-dev-tools libhamlib++-dev libasound2-dev libpulse-dev libopenjp2-7 libopenjp2-7-dev libv4l-dev build-essential
cd ~/Downloads
wget https://github.com/ON4QZ/QSSTV/archive/refs/heads/main.zip
unzip main.zip
cd QSSTV-main
mkdir src/build
cd src/build
qmake ..
make -j2
sudo make install
```


- step 2

now we need to install pulsesound in order to input audio in qsstv
```
sudo apt update
sudo apt install pulseaudio
pulseaudio --start
```
- step 3
 now we can select inout in qsstv by going to config in options
 then under sound select default and pulsesound

- step 4
play  the audio to get the image which has the flag

What you learned through solving this challenge:

1.getting image from SSTV recordings



References

- copilot
- internet
