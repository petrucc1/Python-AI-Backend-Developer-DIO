# O método issubset retorna True se o conjunto for um subconjunto de outro conjunto, ou False caso contrário.
conjunto_a = {1, 2, 3}
conjunto_b = {4, 1, 2, 5, 6, 3}

conjunto_a.issubset(conjunto_b) # True
conjunto_b.issubset(conjunto_a) # False