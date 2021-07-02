import npyscreen
import curses.ascii
from curses import endwin
from hand_object import hand
from communication_framework import Comframe, getOpenPorts
from ui_widgets import TSlider, TimeSlider, BoxSelectOne, BoxOptions, PortBox

class MainForm(npyscreen.FormBaseNew):
    DEFAULT_LINES = 26

    def create(self):
        # Init Form and Objects
        self.name = "3D-Bionics Hand Control Software"

        self.comframe = self.parentApp.comframe
        self.hand = self.parentApp.hand

        y, x = self.useable_space()

        left = round(x*2/3)
        
        # Create UI
        self.nextrely = 3
        self.klein = self.add(TSlider, max_width=left,name = "Klein")
        self.nextrely +=1
        self.ring = self.add(TSlider, max_width=left, name = "Ring")
        self.nextrely +=1
        self.mittel = self.add(TSlider, max_width=left,  name = "Mittel")
        self.nextrely +=1
        self.zeige = self.add(TSlider, max_width=left, name = "Zeige")
        self.nextrely +=1
        self.daumen = self.add(TSlider, max_width=left, name = "Daumen")

        self.nextrely += 3
        self.timeslider = self.add(TimeSlider, max_width=round(left/1.5), value=0.3, name = "Delay", hidden = True)

        self.nextrely = y-3
        self.ports = self.add(PortBox,max_width=left)

        self.nextrelx = left + 10
        self.nextrely = 2
        self.quickPos = self.add(BoxSelectOne, max_height= round((y-2)/2), name = "Quick Positions")
        self.nextrely += 1
        self.reloadPos = self.add(npyscreen.ButtonPress, name="Nochmal!", relx=self.nextrelx+15, when_pressed_function = lambda : self.quickPos.entry_widget.setPosition() )
        self.nextrely += 1
        self.options = self.add(BoxOptions)

        # init handlers

        handlers = {
            '^Q': self.exit_func,
            curses.ascii.ESC: self.exit_func
        }

        self.add_handlers(handlers)

        # Additional Config

        self.keypress_timeout=1

    def afterEditing(self):
        self.parentApp.setNextForm(None)

    def while_waiting(self):
        self.updatePos()


    def sendPos(self):
        
        new_pos = [[
            int(self.klein.value),
            int(self.ring.value),
            int(self.mittel.value),
            int(self.zeige.value),
            int(self.daumen.value)
            ]]

        self.comframe.queue_clear()
        self.comframe.queue_position(new_pos)
        

    def reloadQuickPos(self):
        self.quickPos.entry_widget.setPosition()

    def updatePos(self):
        self.klein.set_value(self.hand.getKlein())
        self.mittel.set_value(self.hand.getMittel())
        self.ring.set_value(self.hand.getRing())
        self.zeige.set_value(self.hand.getZeige())
        self.daumen.set_value(self.hand.getDaumen())
        self.display()
    
    # Various functions
    def exit_func(self, _input):
        self.editing = False


class hand_controll(npyscreen.NPSAppManaged):

    def __init__(self, comframe: Comframe,hand: hand):
        self.comframe = comframe
        self.hand = hand
        super(hand_controll,self).__init__()

    def onStart(self):
        self.addForm("MAIN", MainForm)

    
if __name__ == "__main__":

    hand_object = hand()
    try:
        comframe = Comframe(hand_object)
    except:
        print("Connection Error: No valid serial port detected!")
        print("Make sure the arduino is connected and that the application has access right to the serial-port")
        quit()
    
    App = hand_controll(comframe,hand_object)
    App.run()
