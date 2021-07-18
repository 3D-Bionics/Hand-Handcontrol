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
        if(self.parentApp.demomode is True):
            self.name = "3D-Bionics Hand Control Software DEMO"
        else:
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

    def __init__(self, comframe: Comframe,hand: hand,demomode = None):
        self.comframe = comframe
        self.hand = hand
        self.demomode = demomode
        super(hand_controll,self).__init__()

    def onStart(self):
        self.addForm("MAIN", MainForm)


if __name__ == "__main__":
    import argparse
    from demo import Demo
    import threading

    # Define Parser for arguments frim commandline
    def CLIParser():
        parser = argparse.ArgumentParser(description="The 3D-Bionics Hand Controll software,")
        parser.add_argument('-v','--version', action='version',version='%(prog)s 1.0')
        parser.add_argument('-p','--port', help="Specify the serial-port of the 3D-Bionics Hand" )
        parser.add_argument('--getAvailablePorts', help="Displays a list of all available ports", action='version',version= "\n".join(getOpenPorts()))
        parser.add_argument('-d','--demo', help="For demonstration purposes. Plays a sequenze of animations defindend in demo.py", action="store_true")
        return parser.parse_args()

    args = CLIParser()

    # Intizialize Handobject and Communication-Framework
    hand_object = hand()

    try:
        comframe = Comframe(hand_object, args.port)
    except:
        if args.port:
            print("Connection Error: Could not open connection in specified port")
        else:
            print("Connection Error: No valid serial port detected!")

        print("Make sure the arduino is connected and that the application has access right to the serial-port")
        quit()
    
    # Start thread with demo-script. See demo.py to see how it works
    if args.demo:
        threading.Thread(target=Demo,args=(comframe,), daemon=True).start()

    # Start App
    App = hand_controll(comframe,hand_object,args.demo)
    App.run()
