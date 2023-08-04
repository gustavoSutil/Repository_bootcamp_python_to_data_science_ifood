import DateController

class Account():

    def __init__(self,id,*draft_value_limit,draft_qtd_limit):
        self.__id = id
        self.__draft_value_limit = draft_value_limit
        self.__draft_qtd_limit = float(500)
        LIMITE_DE_SAQUES = int(3)
        MOVIMENTACAO = str('')
        SALDO = float('0')
        __saques_no_dia = 0
        valor_sacado_no_dia = 0
        self.__extract = f'''Conta criada em {DateController.now[0:-7]}\n'''