from random import randint

# Object for storing hand positions

class hand:
    def __init__(self, positions: list = [0,0,0,0,0]):
        
        if hand.checkPos(positions):
            self._positions = positions
        else:
            raise "Wrong positional args in hand-object"

        
    def getPos(self)-> list: return self._positions


    def getKlein(self) -> int: return self._positions[0]
    
    def getRing(self) -> int: return self._positions[1]
    
    def getMittel(self) -> int: return self._positions[2]

    def getZeige(self) -> int: return self._positions[3]

    def getDaumen(self) -> int: return self._positions[4]


    def setPos(self, positions : list) -> bool:

        if not hand.checkPos(positions) :
            return False

        self._positions = positions
        return True

    def setKlein(self, pos: int):
        if not hand.checkPosInt(pos):
            return False
        
        self._positions[0] = pos
        return True
    
    def setRing(self, pos: int):
        if not hand.checkPosInt(pos):
            return False
        
        self._positions[1] = pos
        return True

    def setMittel(self, pos: int):
        if not hand.checkPosInt(pos):
            return False
        
        self._positions[2] = pos
        return True

    def setZeige(self, pos: int):
        if not hand.checkPosInt(pos):
            return False
        
        self._positions[3] = pos
        return True

    def setDaumen(self, pos: int):
        if not hand.checkPosInt(pos):
            return False
        
        self._positions[4] = pos
        return True

    
    @staticmethod
    def checkPos(positions: list) -> bool:
        if len(positions) != 5:
            return False

        for pos in positions:
            if not(0<=pos and pos <=100):
                return False
        
        return True

    @staticmethod
    def checkPosInt(pos: int) -> bool:
        if not(0<=pos and pos <=100):
                return False
        
        return True

# A Custom dict that if the value is a function automatically calls it
class CallableDict(dict):
     def __getitem__(self, key):
        val = super().__getitem__(key)
        if callable(val):
            return val()
        return val

def schereSteinPapier() -> list:
    ssp_animation=[
        [100,100,0,0,100],
        [100,100,0,0,100],
        [100,100,0,0,100],
        [100,100,100,100,100],
        [100,100,100,100,100],
        [100,100,100,100,100],
        [0,0,0,0,0],
        [0,0,0,0,0],
        [0,0,0,0,0]
    ]

    ssp_options=[
        [100,100,0,0,100],
        [100,100,100,100,100],
        [0,0,0,0,0]
    ]

    ssp_animation.append(ssp_options[randint(0,2)])

    return ssp_animation

# A list of possible Hand Positions
hand_positions = CallableDict(
    {
    'Open': [[0,0,0,0,0]],
    'Fist': [[100,100,100,100,100]],
    'F You': [[100,100,0,100,100]],
    'Metal': [[0,100,100,0,100]],
    'Three Finger Salute': [[100,0,0,0,100]],
    'Rainbow': [
        [60, 50, 40, 30, 20],
        [70, 60, 50, 40, 30],
        [80, 70, 60, 50, 40],
        [90, 80, 70, 60, 50],
        [100, 90, 80, 70, 60],
        [90, 100, 90, 80, 70],
        [80, 90, 100, 90, 80],
        [70, 80, 90, 100, 90],
        [60, 70, 80, 90, 100],
        [50, 60, 70, 80, 90],
        [40, 50, 60, 70, 80],
        [30, 40, 50, 60, 70],
        [20, 30, 40, 50, 60],
        [10, 20, 30, 40, 50],
        [0, 10, 20, 30, 40],
        [10, 0, 10, 20, 30],
        [20, 10, 0, 10, 20],
        [30, 20, 10, 0, 10],
        [40, 30, 20, 10, 0],
        [50, 40, 30, 20, 10]
    ],
    'Schere Stein Papier': schereSteinPapier
}
)