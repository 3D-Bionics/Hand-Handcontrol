import argparse
from handcontrol.src.ui_App import hand_controll
from handcontrol.src.communication_framework import Comframe, hand, getOpenPorts  

# Define Parser for arguments frim commandline
def CLIParser():
    parser = argparse.ArgumentParser(description="The 3D-Bionics Hand Controll software,")
    parser.add_argument('-v','--version', action='version',version='3D-Bionics Hand-Control 1.0')
    parser.add_argument('-p','--port', help="Specify the serial-port of the 3D-Bionics Hand" )
    parser.add_argument('--getAvailablePorts', help="Displays a list of all available ports", action='version',version= "\n".join(getOpenPorts()))
    parser.add_argument('-d','--demo', help="For demonstration purposes. Plays a sequenze of animations defindend in demo.py", action="store_true")
    return parser.parse_args()

def main():
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
        from handcontrol.src.demo import Demo
        from threading import Thread
        Thread(target=Demo,args=(comframe,), daemon=True).start()

    # Start App
    App = hand_controll(comframe,hand_object,args.demo)
    App.run()

if __name__ == "__main__":
   main()