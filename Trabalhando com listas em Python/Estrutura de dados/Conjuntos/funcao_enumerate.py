# Para saber o índice de um valor em um conjunto, você pode utilizar a função enumerate.

carros = {'Fusca', 'Gol', 'Celta', 'Palio'}

for indice, carro in enumerate(carros):
    print(f'{indice} - {carro}') # 0 - Gol, 1 - Palio, 2 - Celta, 3 - Fusca
