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
            return 1
        elif operation=="Depósito":
            self.__deposit(value)
            return 1
        return 0
    
    def __deposit(self,value):
        #Tratamento de caso , para evitar erros
        status = self.moveMoney(self,value)
        if status:
            print(f'Valor depositado {value:.2f},\nSaldo atual R$ {self.__account_value:.2f}')
            self.__extract += f'Valor depositado {value:.2f},\nSaldo atual R$ {self.__account_value:.2f}\n\n'
            return 1
        else:
            return 0

    def __draft(self,value):
        if  self.__draft_qtd_done_day >= self.__draft_qtd_limit:
            print(f'Valor o limite de saques, LIMITE_SAQUE são {self.__draft_qtd_limit:.2f}')
        else:
            if (self.__account_value<value):
                print('Saldo insuficiente!')
                return 0
            elif ((value+self.__draft_value_done_day)>self.__draft_value_limit):
                print(f'Valor acima do limite de saque R$ {self.__draft_value_limit:.2f}')
                return 0
            else:
                status = self.moveMoney(self,value)
                if status:
                    print(f'Valor sacado {value:.2f},\nSaldo atual R$ {self.__account_value:.2f}')
                    self.__draft_qtd_done_day +=1
                    self.__draft_value_done_day+=value
                    self.__extract += f'Valor sacado {value:.2f},\nSaldo atual R$ {self.__account_value:.2f}\n\n'
                    return 1
                
    def __moveMoney(self,value) -> int:
        try:
            self.__account_value += value
            return 1
        except:
            return 0