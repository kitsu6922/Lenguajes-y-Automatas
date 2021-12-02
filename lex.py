import sys
from token import Token
from tokentype import *

class Lexer:

    #constructor this
    def __init__(self, input):
        self.source=input
        self.curChar=''
        self.curPos=-1
        self.nextChar()

    #procesa del caracter actual
    def nextChar(self):
        self.curPos+=1
        if self.curPos >= len(self.source):
            self.curChar='\0' #EOF
        else:
            self.curChar=self.source[self.curPos]
    

    #anticipa el caracter que sigue
    def peek(self):
        if self.curPos + 1>= len(self.source):
            return '\0'
        return self.source[self.curPos+1]

    #muestra el error por si hay tokens invalidos
    def abort(self, message):
        sys.exit("Error de lexico "+message)

    #saltearse los espacios en blanco
    def skipWhitespace(self):
        while self.curChar==' ' or self.curChar=='\t' or self.curChar=='\r':
            self.nextChar()
    
    #skip comentarios
    def skipComment(self):
        if self.curChar=='#':
            self.nextChar()

    #obtiene el token siguiente
    def getToken(self):
        self.skipWhitespace()
        self.skipComment()
        token= None
        #verificando los textos multilinea y las anotaciones
        if self.curChar=='\"':
            self.nextChar()
            starPos = self.curPos
            while self.curChar != '\"':
                if self.curChar=='\r' or self.curChar=='\n' or self.curChar=='\t' or self.curChar=='\\' or self.curChar=='%':
                    self.abort("caracter no valido en el string")
                self.nextChar()

            tokenText=self.source[starPos:self.curPos]
            token = Token(tokenText,TokenType.STRING)
        #capturar numeros
        elif self.curChar.isdigit():
            starPos = self.curPos
            while self.peek().isdigit():
                self.nextChar()
            if self.peek()=='.':
                self.nextChar()
                if not self.peek().isdigit():
                    self.abort("caracter no valido en el numero")
                while self.peel().isdigit():
                    self.nextChar()
            tokenText=self.source[starPos:self.curPos+1]
            token = Token (tokenText,TokenType.NUMBER)
        elif self.curChar.isalpha():
            starPos=self.curPos
            while self.peek().isalnum():
                self.nextChar()
            tokenText=self.source[starPos:self.curPos+1]
            keyword = Token.checkIfKeyword(tokenText)
            if keyword == None:
                #identificador
                self.abort("Token desconocido"+self.curChar)
            else:
                token = Token(tokenText,keyword)
        elif self.curChar=='\n':
            token = Token(self.curChar,TokenType.NL)
        elif self.curChar=='\0':
            token = Token(self.curChar,TokenType.EOF)
        else:
            self.abort("Token desconocido"+self.curChar)
        self.nextChar()
        return token

