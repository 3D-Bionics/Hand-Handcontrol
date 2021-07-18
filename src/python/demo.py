from communication_framework import Comframe
from hand_object import hand
from positions import hand_positions
import time

def Demo(com: Comframe):
    ''' Send a sequenze of animations to the hand via the communication-framework'''
    default = 0.3

    animation: tuple[str,float,bool,float]
    sequenz: list[ animation ]

    sequenz = [
        ('F You',default,False,5),
        ('Metal',default,False,5),
        ('Rainbow',0.2,True,10),
        ('Schere Stein Papier',1,False,10),
        ('Schere Stein Papier',1,False,10),
        ('Schere Stein Papier',1,False,10),
    ]

    while True:
        for (key, delay, loop, wait) in sequenz:
            com.queue_clear()
            com.delay = delay
            com.loop = loop
            # print("Play Animation '{}' with delay {} for {}s".format(key,delay,wait))
            com.queue_position(hand_positions[key])
            time.sleep(wait)


if __name__ == '__main__':

    demo_hand = hand()
    com = Comframe(demo_hand)
    print(com.port)

    Demo(com)