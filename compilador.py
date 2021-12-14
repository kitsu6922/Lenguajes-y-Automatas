from lex import *
from tokentype import *
import sintaxys
from PyQt5 import QtWidgets
from window import *

class MainWindow(QtWidgets.QMainWindow,Ui_MainWindow):
    def __init__(self,editor,*args,**kwargs):
        QtWidgets.QMainWindow.__init__(self,*args,**kwargs)
        self.setupUi(self,editor)
        self.editor=editor
        self.btnRun.clicked.connect(self.compilar)
    def compilar(self):
        lexer=Lexer(self.editor.toPlainText())
        token = lexer.getToken()
        cont = 0
        todo=""
        while token.kind != TokenType.EOF:
            todo+="Token Type: {} , Content: {} \n".format(token.kind, token.text)
            token = lexer.getToken()
            cont+=1
        todo+="\nNumber tokens found: {} ".format(cont)
        self.txtConsola.setPlainText(todo)

if __name__ == '__main__':
    app=QtWidgets.QApplication([])
    editor=QtWidgets.QPlainTextEdit()
    editor.setStyleSheet("""QPlainTextEdit{
        color:#ccc;
        background-color:#2b2b2b;
        font-family:'consolas';
    }""")
    file=open("./code.pvm","r")
    editor.setPlainText(file.read())
    pintar=sintaxys.PythonHighlighter(editor.document())
    window=MainWindow(editor)
    window.show()
    app.exec_()

def main():
    file = open("./code.pvm","r")
    input = file.read()
    lexer = Lexer(input)
    token = lexer.getToken()
    cont = 0
    while token.kind != TokenType.EOF:
        print("Token Type: {} , Content: {}".format(token.kind, token.text))
        token = lexer.getToken()
        cont+=1
    print("Number tokens found: {} ".format(cont))
#main()