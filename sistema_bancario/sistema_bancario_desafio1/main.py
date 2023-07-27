#use cases:
#1 - só deve ser possivel fazer depósitos positivos ( em uma só variavel )
#2 - max 3 saques diarios de no max 500 reais - mensagens de erro
#3 - ter um menu: d / s / e / q  adicional: ajuda
# fazer como um inicante para progredir com o curso..

#constantes para no caso de alteração de regras de negócio seja facil de manipular
global LIMITE_SAQUE
global LIMITE_DE_SAQUES
global MOVIMENTACAO #relatório
global SALDO

def main():

    LIMITE_SAQUE = float(500)
    LIMITE_DE_SAQUES = int(3)
    MOVIMENTACAO = str('')
    SALDO = float('0')



    inp = 'Ajuda'
    saques_no_dia = 0
    valor_sacado_no_dia = 0
    print('Bem vindo!')
    while(1):
        match inp:
            case '1' | 'Ajuda':
                print(
                ''' 
Menu:
1 - Ajuda   
2 - Depósito
3 - Saque
4 - Extrato
5 - Sair
                '''
            )
            case '2' | 'Depósito':
                #Tratamento de caso , pra .
                valor = float(str(input("Qual o valor?\nR$")).replace(",","."))
                if valor <= 0:
                    print("Valor inválido")
                else:
                    SALDO+=float(valor)
                    print(f'Valor depositado {valor},\nSaldo atual R$ {SALDO}')
                    MOVIMENTACAO +=f'Valor depositado {valor},\nSaldo atual R$ {SALDO}\n\n'
            case '3' | 'saque':
                if saques_no_dia > 3:
                    #constantes para no caso de alteração de regras de negócio seja facil de manipular
                    print(f'Valor o limite de saques, LIMITE_SAQUE são {LIMITE_DE_SAQUES}')
                else:
                    valor = float(str(input("Qual o valor?\nR$")).replace(",","."))
                    if valor <= 0:
                        print("Valor inválido")
                    elif (SALDO<valor):
                        print('Saldo insuficiente!')
                    elif ((valor+valor_sacado_no_dia)>LIMITE_SAQUE):
                        print(f'Valor acima do limite de saque R$ {LIMITE_SAQUE:.2f}')
                    else:
                        SALDO-=valor
                        print(f'Valor sacado {valor},\nSaldo atual R$ {SALDO}')
                        saques_no_dia+=1
                        valor_sacado_no_dia+=valor
                        MOVIMENTACAO += f'Valor sacado {valor},\nSaldo atual R$ {SALDO}\n\n'
            
            case '4' | 'extrato':
                print(f'\n\n\n\n\n\nMovimentação da conta:\n{MOVIMENTACAO}\n\nSaldo atual: {SALDO:.2f}\n\nLimite: {LIMITE_SAQUE:.2f}\n\n')
                print(f'Valor sacado {valor},\nSaldo atual R$ {SALDO-valor}')
            case '5' | 'sair':
                exit("Tenha um bom dia!")
            case _:
                print("Desculpe não entendi\nVocê pode usar a palavra sem letra maiúscula ou o número!")
        inp = str(input("O que você deseja hoje? "))


if __name__ == "__main__":
    main()