import phonenumbers

# msg para consultar
nmr = input('Digite o número a ser consultado, adicionando o +55, e sem espaços ou acentos: ')

# ajuste do telefone
telefone = "nmr"
telefone_ajustado = phonenumbers.parse(nmr)
print(telefone_ajustado)

# descobrir a loc do tel
from phonenumbers import geocoder
local = geocoder.description_for_number(telefone_ajustado, 'pt-br')
print("Este número é do(a): " + local)

# descobrir operadora
from phonenumbers import carrier
operadora = carrier.name_for_number(telefone_ajustado, "pt-br")
print("Utilizando a operadora: " + operadora)
