#!/usr/bin/python3

# create a ros node with a string subscriber
import rospy
import std_msgs.msg

import thi_moving_head.msg


import random



import requests
from requests.structures import CaseInsensitiveDict

# url of the moving head ola server
url = "http://192.168.188.58:9090/set_dmx"

headers                 = CaseInsensitiveDict()
headers["Content-Type"] = "application/x-www-form-urlencoded"


class MovingHeadInterface:
    def __init__(self):
        self.sub = rospy.Subscriber('/moving_head/cmd', thi_moving_head.msg.Moving_Head, self.callback)

    def callback(self, data):
        pan     = data.pan
        tilt    = data.tilt
        color   = data.color
        dimmer  = data.dimmer # full brightness


        shutter = 5     # open
        globo   = 0     # open

        data = "u=1&d=" + str(pan) + "," + str(tilt) + ",0,0,0," + str(color) + "," + str(shutter) + "," + str(dimmer) + "," + str(globo) + ",255"
        resp = requests.post(url, headers=headers, data=data)



# create ros main function
if __name__ == '__main__':
    rospy.init_node('moving_head_interface')
    mh = MovingHeadInterface()
    rospy.spin()

