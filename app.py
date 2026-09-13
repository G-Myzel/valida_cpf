def valida_cpf(cpf):
    cpf = ''.join(c for c in cpf if c.isdigit())
    if len(cpf) != 11 or cpf == cpf[0] * 11:
        return False

    for i in (9, 10): 
        soma = sum(int(cpf[n]) * (i + 1 - n) for n in range (i))
        digito = (11 - soma % 11) % 11
        if digito > 9:
            digito = 0
        if digito != int(cpf[i]):
            return False
    return True

print(valida_cpf('07368589544'))