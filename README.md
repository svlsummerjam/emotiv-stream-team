# emotiv-stream-team 


#### This is a WIP realtime streaming cli for emotiv eeg using pubnub. 
#### A big thanks to the guys at openyou [openyou/emokit](https://github.com/openyou/emokit "openyou/emokit") for reverse engineering the device and creating the emokit python package.


`emotiv-stream-team` is a tool to help facilitate the process of realtime data manipulation. Currently `emotiv-stream-team` only supports publish and subscribe functionality. More to come soon!  

### Installation

To install `emotiv-stream-team`, cd into the `emotiv-stream-team` directory and run: 

	$ ./configure
	$ sudo make
	$ sudo make install

### Usage

       usage: emotiv-stream-team [-h] [-p [PUB] | -s [SUB]] [-v] channel publish subscribe

       pubnub publisher

       positional arguments:
         channel               channel
         publish               publish
         subscribe             subscribe

       optional arguments:
         -h, --help            show this help message and exit
         -p [PUB], --pub [PUB]
                               Value must be yes
         -s [SUB], --sub [SUB]
                               Value must be yes
         -v, --version         show program's version number and exit
       

'emotiv-tream-team' under GPLv3

See the COPYING file for the full license text.

TODO: Add data channel selectors. 
TODO: Add graphics/plotting capibility.
TODO: Add requirements
