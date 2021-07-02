from pySerialTransfer import pySerialTransfer as transfer
from hand_object import hand
import time

class Comframe:
    
    def __init__(self, hand: hand, port = None):

        self._hand = hand

        self._queue = []
        self._queue_iter = iter(self._queue)
        self.loop = False
        self.pause = False

        self._connect(port)

    # Function for connecting to an arduino. Trys to detect possible ports manually
    def _connect(self,port = None):
        if type(port) == list:
            available_ports = port
        elif type(port) == int:
            available_ports = [port]
        else:
            available_ports = getOpenPorts()

        if not available_ports:
            raise Exception("No available Serial Ports")

        while True:
            try:
                # Create Link
                port = available_ports.pop()
                self._link = transfer.SerialTransfer(port)

                # Set Callbacks for automatic receiving and processing of packages
                self._callbacklist = [self._receivePos, self._receiveDebug]
                self._link.set_callbacks(self._callbacklist)

                # Open Link
                if self._link.open():
                    self.port = port
                    return

            except KeyboardInterrupt:
                try:
                    self._link.close()
                except:
                    quit()

            except:
                pass
            
        raise Exception("No Connection")
    
    # Reconnects to an arduino at runtime either with old port or a new given port
    def reconnect(self,port = None):
        self._link.close()
        self._connect(port or self.port)
        
    
    def __del__(self):
        try:
            self._link.close()
        except:
            pass

    # Method for extending support for optional handtracker on seperate serial Port
    def attachHandTracker(self, port):
        pass

    
    # Callback for receiving position update packages (package id 0)
    def _receivePos(self):
        buffer = self._link.rx_obj(obj_type=list,obj_byte_size=20,list_format='i')

        self._hand.setPos(buffer)

    # Callback for debug purposes (package id 1) [NOT YET IMPLEMENTED]
    def _receiveDebug(self):
        pass

    # Send specific position to the arduino
    def sendPosList(self, positions: list[int]):
        if hand.checkPos(positions):
            self._link.send(self._link.tx_obj(positions))

    # Send position of hand to arduino
    def sendPos(self):
        self._link.send(self._link.tx_obj(self._hand.getPos()))

    # process all incoming packages
    def processAll(self):
        while(self.processOne()):
            pass

    # process one incoming package
    def processOne(self):
        self._link.tick()
        
    # process the incoming package + position queue

    def processQueue(self):
        self.processOne()

        if(self.pause is True):
            return

        def nextpos():
            nextpos = next(self._queue_iter)
            self.sendPosList(nextpos)
        
        try:
            nextpos()
        except:
            if(self.loop is True):
                self._queue_iter = iter(self._queue)
                nextpos()
                
                
    # queus a list of positions into the internal queue
    def queue_position(self,position_array: list[list[int]]):
        for pos in position_array:
            self._queue.append(pos)

    # clears the internal queue
    def queue_clear(self):
        self._queue.clear()
        self._queue_iter = iter(self._queue)


# Gets all available Ports for serial communication
def getOpenPorts() -> list:
    return transfer.open_ports()