import re


def valida_cpf(cpf):
    """Retorna True quando o CPF informado tem dígitos verificadores válidos."""
    if not isinstance(cpf, str):
        return False

    valor = cpf.strip()
    if not re.fullmatch(r"[0-9.\-\s]+", valor):
        return False

    digitos = re.sub(r"[^0-9]", "", valor)
    if len(digitos) != 11 or digitos == digitos[0] * 11:
        return False

    for posicao in (9, 10):
        soma = sum(
            int(digitos[indice]) * (posicao + 1 - indice)
            for indice in range(posicao)
        )
        digito = (soma * 10) % 11
        if digito == 10:
            digito = 0
        if digito != int(digitos[posicao]):
            return False
    return True


def main():
    cpf = input("Digite o CPF: ").strip()
    if not cpf:
        print("Nenhum CPF informado.")
        return
    resultado = "válido" if valida_cpf(cpf) else "inválido"
    print(f"CPF {resultado}.")


if __name__ == "__main__":
    main()
