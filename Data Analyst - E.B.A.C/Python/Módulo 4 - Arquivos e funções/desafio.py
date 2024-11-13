'''Faça um programa que calcule o valor total investido por um colecionador em sua coleção de CDs e o valor médio gasto em cada um deles. O usuário deverá informar a quantidade de CDs e o valor para cada um.

Lembre-se de que você já tem a habilidade de desenvolver variáveis, estruturar dados, criar condições, repetições e funções. '''


cont = sum_qtd = 0
list_info = list()
list_total_value = list()

while True:
    cont += 1
    cd = dict() 
    
    cd['name_cd'] = input('Nome do {}º CD: '.format(cont)).upper()
    cd['qtd_cd'] = int(input('Quantidade do {}º CD: '.format(cont)))
    cd['preco_cd'] = float(input('Preço do {}º CD: '.format(cont)))

    option = input('Deseja continuar [S/N]? ').upper().strip()

    list_info.append(cd)
    sum_qtd += cd['qtd_cd']

    if option == 'S':
        print()
        continue
    elif option == 'N':   
        break
    else:
        print('Digite uma das opções, por favor!')


print('\n{:<10} {:<15} {:<15} {:<15}'.format('ÍNDICE', 'NOME_CD', 'QUANTIDADE', 'PREÇO'))
print('-=' * 25)

for i, k in enumerate(list_info):
    print('{:<10} {:<15} {:<15} {:<16}'.format(i + 1, k['name_cd'], k['qtd_cd'], k['preco_cd']))

    qtd_preco = k['preco_cd'] * k['qtd_cd']
    list_total_value.append(qtd_preco)

total_value = sum(list_total_value)

average_value = total_value / sum_qtd

print('-=' * 25)

print('O valor total é: R${:.2f}.'.format(total_value))
print("A quantidade total é de {} CD's.".format(sum_qtd))
print('O valor médio gasto é: R${:.2f}.'.format(average_value))

