import npyscreen

from hand_object import hand,hand_positions

class Slider(npyscreen.SliderPercent):
    def __init__(self,screen,block_color='CAUTIONHL',*args,**keywords):
        super(Slider,self).__init__(screen,out_of=100, step=2, block_color=block_color ,*args,**keywords)

    def when_value_edited(self):
        self.parent.sendPos()


class TSlider(npyscreen.TitleText):
    _entry_type=Slider

class SelectOne(npyscreen.SelectOne):
    def __init__(self,screen,*args,**keywords):
        super(SelectOne,self).__init__(screen,values=list(hand_positions.keys()),*args,**keywords)

    def when_value_edited(self):
        options = self.get_selected_objects()
        for option in options:
            self.parent.parentApp.Comframe.sendPosList(hand_positions.get(option))


class BoxSelectOne(npyscreen.BoxTitle):
    _contained_widget = SelectOne

    