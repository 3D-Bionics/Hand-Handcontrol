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
