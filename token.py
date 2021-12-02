from tokentype import *
#la clase token guarda el tipo de token y el texto original
class Token:
    def __init__(self,tokenText,tokenKind):
        self.text=tokenText
        self.kind=tokenKind
        
    @staticmethod
    def checkIfKeyword(tokenText):
        for kind in TokenType:
            if kind.name==tokenText and kind.value >= 100 and kind.value < 600:
                return kind
        return None 
