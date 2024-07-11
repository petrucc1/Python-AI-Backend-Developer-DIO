# O método issuperset retorna True se o conjunto for um superconjunto de outro conjunto, ou False caso contrário.
conjunto_a = {1, 2, 3}
conjunto_b = {4, 1, 2, 5, 6, 3}

conjunto_a.issuperset(conjunto_b) # False
conjunto_b.issuperset(conjunto_a) # True
