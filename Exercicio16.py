print ("{:^40}".format(' Lojas Marques '))
preco = float (input('Preco das compras: R$'))
print('''FORMAS DE PAGAMENTOS
[ 1 ] À VISTA DINHEIRO / CHEQUE
[ 2 ] À VISTA CARTÂO
[ 3 ] 2X NO CARTÂO
[ 4 ] 3X OU MAIS NO CARTÃO''')
opcao = int (input ('Qual é a opção de compra? '))
if opcao == 1:
    total = preco - (preco * 10 / 100)
elif opcao == 2:
    total = preco - (preco * 5 / 100)
elif opcao == 3:
    total = preco
    parcela = total / 2
    print('Sua compra será parcelada em 2x de R${:.2f}'.format(parcela))
elif opcao == 4:
    total = preco + (preco * 20 / 100)
    totparc = int (input('Quantas parcelas? '))
    parcela = total / totparc
    print ('Sua compra será parcelada em {}x de R${:.2f} COM JUROS'.format(totparc, parcela))
else:
    total = 0
    print ('Opçâo Invalida de pagamento. Tente novamente ')
print ('Sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(preco, total))