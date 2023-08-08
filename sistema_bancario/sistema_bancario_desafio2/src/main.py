#use cases:
#1 - só deve ser possivel fazer depósitos positivos ( em uma só variavel )
#2 - max 3 saques diarios de no max 500 reais - mensagens de erro
#3 - ter um menu: d / s / e / q  adicional: ajuda
#4 - cadastro de usuario
#5 - cadastro de conta bancária



def main():
    inp = 'Ajuda'
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
                #Tratamento de caso , para evitar erros
                valor = float(str(input("Qual o valor?\nR$")).replace(",","."))
                if valor <= 0:
                    print("Valor inválido")
                else:
                    SALDO+=float(valor)
                    print(f'Valor depositado {valor},\nSaldo atual R$ {SALDO}')
                    MOVIMENTACAO +=f'Valor depositado {valor},\nSaldo atual R$ {SALDO}\n\n'
            case '3' | 'saque':
                valor = float(str(input("Qual o valor?\nR$")).replace(",","."))
                if valor >= 0:
                    print("Valor inválido")


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