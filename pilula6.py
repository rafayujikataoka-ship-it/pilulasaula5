def ehPrimo():
    if n <2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

#main
n = (input('Digite um número: '))
if ehPrimo():
    print(f'{n} é primo')
else:
    print(f'{n} não é primo')
    