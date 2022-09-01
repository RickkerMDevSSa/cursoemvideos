listanum = []
mai = 0
men = 0
for c in range(0, 5):
    listanum.append(int(input('Digite um valor para posicao {c}: ')))
    if c == 0:
        mai = men = listanum[c]
    else:
        if listanum[c] > mai:
            mai = listanum[c]
        if listanum[c] < men:
            men = listanum[c]
print('=-' *30)
print (f'Voce digitou os valores {listanum}')
print (f'O maior valor digitado foi {mai}')
print (f'O menor valor digitado foi {men}')