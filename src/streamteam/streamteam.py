#!/usr/bin/env python
#Copyright (c) James Beedy
import os
from Pubnub import Pubnub


class Streamteam(object):

    def __init__(self, args):
        self.channel = args.channel
        self.pubnub = Pubnub(
                args.publish,
                args.subscribe,
                None,
                False
        )
        
    def publish(self, message):
        self.pubnub.publish({
            'channel'  : self.channel,
            'message' : message
        })
    
    def subscribe(self):
        def receive(message):
           # q = ""
            s = ""
            v = ""
            names = "gyroX gyroY AF3 F7 F3 FC5 T7 P7 O1 O2 P8 T8 FC6 F4 F8 AF4".split(" ")
            os.system('clear')
            for i in names:
               # q += str(message['quality'][i]) + " "
                v += str(message['values'][i]) + "   "

                while len(i) < 7:
                    i += " "
                s += i
            print("Channel : " + s)
           # print("Quality : " + q)
            print("Values  : " + v)
            return True
        
        self.pubnub.subscribe({
            'channel' : self.channel,
            'callback' : receive
        })

