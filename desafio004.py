#Dissecar string
value = input('Digite um número algo e de enter: ')

print('O tipo do valor digitado é:' ,type(value))
print('O valor digitado é alfabético?', value.isalpha())
print('O valor digitado é um numero?', value.isnumeric())
print('O valor digitado é um alfanumérico?', value.isalnum())
print('O valor digitado é maiúsculo?', value.isupper())
print('O valor digitado é minúsculo?', value.islower())
print('O valor digitado está com inicial maiúscula?', value.istitle())
print('O valor digitado só tem espaços?', value.isspace())


