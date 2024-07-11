# O método difference retorna tudo o que eu tenho no conjunto_a e não tenho no conjunto_b.
conjunto_a = {1, 2, 3}
conjunto_b = {3, 4, 5}

conjunto_a.difference(conjunto_b) # {1, 2}
conjunto_b.difference(conjunto_a) # {4, 5}

# O método difference também pode ser utilizado através do operador de subtração (-).
conjunto_a - conjunto_b # {1, 2}
conjunto_b - conjunto_a # {4, 5}

