from string import Template
 
nomes = ['Anna', 'Paulo', 'Maria', 'Rafael', 'Patricia']
 
email = """Olá $name,
 
Seja muito bem vindo(a) ao curso Python!!!

Abraço, Fernando Feltrin"""
 
template = Template(email)
 
for i in nomes:
    print(template.substitute(name = i))
    print('-' * 42)
