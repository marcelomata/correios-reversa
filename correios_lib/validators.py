from voluptuous import Invalid
from brazilnum.util import clean_id
from brazilnum.cnpj import validate_cnpj
from brazilnum.cpf import validate_cpf
from brazilnum.cep import format_cep
import datetime
import re


def CNPJ(value):
    if not validate_cnpj(value):
        raise Invalid("Invalid CNPJ")
    return clean_id(value)


def CPF(value):
    if not validate_cpf(value):
        raise Invalid("Invalid CPF")
    return clean_id(value)


def CEP(value):
    try:
        format_cep(value)
    except ValueError as e:
        raise Invalid(e)

    return clean_id(value)


def Email(value):
    if not re.match("[^@]+@[^@]+\.[^@]+", value):
        raise Invalid("This email is invalid.")
    return value


def Date(value):
    fmt = '%d/%m/%Y'
    try:
        if isinstance(value, int):
            value = datetime.date.today() + datetime.timedelta(value)

        return value.strftime(fmt)
    except Exception:
        raise Invalid("Should be an instance of datetime.datetime")
