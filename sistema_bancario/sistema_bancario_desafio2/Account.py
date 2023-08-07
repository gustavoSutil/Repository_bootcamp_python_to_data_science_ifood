import DateController

class Account:
    def __init__(self,id: int,*,draft_value_limit : float,draft_qtd_limit : int, initial_value_account : float):
        try:
            self.__id = id
            self.__draft_value_limit = draft_value_limit #float(500)
            self.__draft_qtd_limit =  draft_qtd_limit#int(3)
            self.__account_value = initial_value_account #float('0')
            self.__draft_qtd_done_day = 0
            self.__draft_value_done_day = 0
            self.__extract = f'''Conta criada em {DateController.now()[0:-7]}\n'''
        except:
            print("Erro ao criar conta repita novamente")

    def moviment(self,value: float) -> int:
        operation = "Saque" if value < 0 else "Depósito" 
        if operation=="Saque":
            self.__draft(value)
        elif operation=="Depósito":
            self.__deposit(value)
    
    def __deposit(self,value):
        #Tratamento de caso , para evitar erros
        valor = float(str(input("Qual o valor?\nR$")).replace(",","."))
        if valor <= 0:
            print("Valor inválido")
        else:
            SALDO+=float(valor)
            print(f'Valor depositado {valor},\nSaldo atual R$ {SALDO}')
            MOVIMENTACAO +=f'Valor depositado {valor},\nSaldo atual R$ {SALDO}\n\n'
    
    def __draft(self,value):
        if  self.__draft_qtd_done_day >= self.__draft_qtd_limit:
            print(f'Valor o limite de saques, LIMITE_SAQUE são {self.__draft_qtd_limit:.2f}')
        else:
            if value <= 0:
                print("Valor inválido")
                return 0
            elif (self.__account_value<value):
                print('Saldo insuficiente!')
                return 0
            elif ((value+self.__draft_value_done_day)>self.__draft_value_limit):
                print(f'Valor acima do limite de saque R$ {self.__draft_value_limit:.2f}')
                return 0
            else:
                return 1
                # make transaction
                # SALDO-=valor
                # print(f'Valor sacado {valor},\nSaldo atual R$ {SALDO}')
                # saques_no_dia+=1
                # valor_sacado_no_dia+=valor
                # MOVIMENTACAO += f'Valor sacado {valor},\nSaldo atual R$ {SALDO}\n\n'