# Sound Equalizer


### Run
    $ python real_time_audio.py <value> <pauseDuration> <pauseValue> 

Print time of 
- <b>disturbances</b> that are greater than <i>value</i> 
- <b>pauses</b> for more than <i>pauseDuration</i> seconds with values lower than <i>pauseValue</i>
    All parameters all optional.

 
### Installing dependencies

    $ brew install portaudio

<b>PyAudio-0.2.9</b>  
Configuration 
https://gist.github.com/jiaaro/9767512210a1d80a8a0d

    $ sudo chown -R `whoami` /usr/local 
    $ sudo chown -R `whoami` /usr/local/Cellar/


<b>PyQt4</b>
http://www.noktec.be/python/how-to-install-pyqt4-on-osx

    $ sudo port install qt4-mac 
    $ sudo port install py-pyqt 
    $ brew install homebrew/python/numpy
    
    
