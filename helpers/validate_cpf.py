import re


def validate_tax_id(tax_id):
    try:
        # Remover pontos e traços do CPF
        tax_id = re.sub('[.-]', '', tax_id)

        # Verificar se o CPF tem 11 dígitos
        if len(tax_id) != 11:
            raise ValueError("CPF deve conter 11 dígitos")

        # Verificar se todos os dígitos são iguais (CPF inválido)
        if tax_id == tax_id[0] * 11:
            raise ValueError("CPF inválido")

        # Verificar a validação dos dígitos verificadores
        soma = 0
        peso = 10
        for i in range(9):
            soma += int(tax_id[i]) * peso
            peso -= 1

        digito_verificador1 = 11 - (soma % 11)
        if digito_verificador1 > 9:
            digito_verificador1 = 0

        if int(tax_id[9]) != digito_verificador1:
            raise ValueError("CPF inválido")

        soma = 0
        peso = 11
        for i in range(10):
            soma += int(tax_id[i]) * peso
            peso -= 1

        digito_verificador2 = 11 - (soma % 11)
        if digito_verificador2 > 9:
            digito_verificador2 = 0

        if int(tax_id[10]) != digito_verificador2:
            raise ValueError("CPF inválido")

        return True

    except ValueError as error:
        print(f"Erro de validação do CPF: {error}")
        return False
