n = input('Digite qualquer coisa: ')

print(f'''O tipo primitivo do valor digitado é:{type(n)}
Só tem espaços ?{n.isspace()}
É um número ?{n.isnumeric()}
É alfábético ?{n.isalnum()}
Está em minúsculo ?{n.isupper()}
Está em maiúscula ?{n.islower()}
Está capitalizado ?{n.istitle()}''')