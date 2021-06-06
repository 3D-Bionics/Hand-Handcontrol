import npyscreen

from hand_object import hand,hand_positions

# Sliders for displaying current position of hand
class Slider(npyscreen.SliderPercent):
    def __init__(self,screen,block_color='CAUTIONHL',*args,**keywords):
        super(Slider,self).__init__(screen,out_of=100, step=2, editable= False, block_color=block_color ,*args,**keywords)

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

    