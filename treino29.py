vogal: str
letra: str

letra = str(input('Digite uma letra: '))

vogal = ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'I', 'O', 'U')


if letra in vogal:
  print('É volgal')
else :
  print('É consoante')

# PARA NÃO PRECISAR DIGITAR OS CARACTERES MAIUSCULOS E MINUSCULOS BASTA CONVERTER JÁ NA ENTRADA EM MAIUSCULO: .upper() OU EM MINUSCULO: .lower()
# SE FOR DIGITADO QUALQUER CARACTERE QUE NÃO SEJA LETRA, USAR A FUNÇÃO: .isalpha() para verificar


letra = str(input('Digite uma letra: ')).lower()

vogal = ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'I', 'O', 'U')


if letra.isalpha() and letra in 'AaEeIiOoUu':
  print('É volgal')
else:
  print('É consoante')
