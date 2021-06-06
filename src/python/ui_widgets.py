import npyscreen

from hand_object import hand,hand_positions

# Sliders for displaying current position of hand
class Slider(npyscreen.SliderPercent):
    def __init__(self,screen,block_color='CAUTIONHL',*args,**keywords):
        super(Slider,self).__init__(screen,out_of=100, step=2, editable= True, block_color=block_color ,*args,**keywords)

    def when_value_edited(self):
        self.parent.sendPos()

class TSlider(npyscreen.TitleText):
    _entry_type=Slider


# Widget for selecting pre-programmed hand positions
# Positions are located in a dict hand_positions in hand_object
class SelectOne(npyscreen.SelectOne):
    def __init__(self,screen,*args,**keywords):
        super(SelectOne,self).__init__(screen,values=list(hand_positions.keys()),*args,**keywords)

    def when_value_edited(self):
        options = self.get_selected_objects()
        self.find_parent_app().Comframe.queue_clear()
        for option in options:
            self.find_parent_app().Comframe.queue_position(hand_positions.get(option))

class BoxSelectOne(npyscreen.BoxTitle):
    _contained_widget = SelectOne


# Widget for selecting various options
class Options(npyscreen.MultiSelect):

    def __init__(self,screen,*args,**keywords):
        super(Options,self).__init__(screen,values=['Loop'],*args,**keywords)

    def when_value_edited(self):
        options = self.get_selected_objects() or []
        Comframe = self.find_parent_app().Comframe

        if 'Loop' in options:
            Comframe.loop = True
        else:
            Comframe.loop = False

class BoxOptions(npyscreen.BoxTitle):
    _contained_widget = Options
    name = 'Options'

from npyscreen import fmPopup, wgmultiline 
from communication_framework import getOpenPorts

class _PortBox(npyscreen.ComboBox):

    def h_change_value(self, input):
        self.values = getOpenPorts()
        self.find_parent_app().Comframe.reconnect()
        "Pop up a window in which to select the values for the field"
        F = fmPopup.Popup(name = self.name)
        l = F.add(wgmultiline.MultiLine, 
            values = [self.display_value(x) for x in self.values],
            return_exit=True, select_exit=True,
            value=self.value)
        F.display()
        l.edit()
        self.value = l.value

    def when_value_edited(self):
        Comframe = self.find_parent_app().Comframe        
        try:
            Comframe.reconnect(self.values[self.value])
        except:
            Comframe.reconnect()


class PortBox(npyscreen.TitleCombo):
    _entry_type=_PortBox

    def __init__(self,screen,*args,**keywords):
        super(PortBox,self).__init__(screen,name = "Serial Port:", use_two_lines=False, *args,**keywords)

        currentPort = self.find_parent_app().Comframe.port
        self.values.append(currentPort)
        self.value = self.values.index(currentPort)
