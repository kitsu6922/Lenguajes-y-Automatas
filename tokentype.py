import enum
class TokenType(enum.Enum):
    EOF=-1
    NL=0
    #PAYMANTS
    CA=101
    TB=102
    QR=103
    AZ=104
    #COMMANDS
    MM=201
    SS=202
    FV=203
    TL=204
    CSP=205
    BA=206
    VD=207
    CP=208
    PS=209
    PR=210
    DEN=211
    #SUPERVISOR
    EDC=301
    SUSPENDER=302
    RECUPERAR=303
    REIMPRIMIR=304
    CT=305
    #SERVICES
    PAYCASH=401
    CB=402
    CFE=403
    SKY=404
    MEGACABLE=405
    INFONAVIT=406
    #WITHDRAWALS
    MP=501
    CREDIMEX=502
    TSV=503
    TCV=504
    BONOMATIC=505
    EFECTIVO=506
    VALES=507
    #OTHERS
    STRING=601
    POINT=602
    NUMBER=603