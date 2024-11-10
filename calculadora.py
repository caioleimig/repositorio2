import os
os.system('cls')
 
def pergunta ():
    a = int(input('Digite um numero: '))
    b = int(input('Digite outro numero: '))
    return a, b
def soma(a, b):
    return a + b
def sub(a, b):
    return a - b
def multi(a, b):
    return a * b
def div(a, b):
    if a > 0 and b > 0:
        if a > b:
            return a / b
        elif a < b:
            return b / a
    else: print('Erro, divirsão por zero. ')

while True: 
    print('Calculadora')
    print('\nDigite 1 para soma, 2 para subtração, 3 para multiplicação e 4 para divisão. Digite 0 caso queira sair. ')
    op = int(input('Digite a o numero da sua opção: '))

    if op == 0: 
        print('Saindo...')
    elif op == 1:
        a, b = pergunta()
        print(f'Resultado: {soma(a, b)}')
    elif op == 2:
        a, b = pergunta()
        print(f'Resultado: {sub(a, b)}')
    elif op == 3:
        a, b = pergunta()
        print(f'Resultado: {multi(a, b)}')
    elif op == 4: 
        a, b = pergunta()
        print(f'Resultado: {div(a, b)}')
    else: print('Opção invalida. ')