# A Custom dict class that automatically calls a function if accessed 
class CallableDict(dict):
     def __getitem__(self, key):
        val = super().__getitem__(key)
        if callable(val):
            return val()
        return val