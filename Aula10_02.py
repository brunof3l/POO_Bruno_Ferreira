# class cpf:
#     def __init__(self,nome,numero):
#         self.nome = nome
#         self.numero = numero

#     def status(self):
#         return f"O CPF de {self.nome} é {self.numero}"

# pessoa1 = cpf("Bruno",12345678900)
# pessoa2 = cpf("Ruan",12345678901)

# print(pessoa1.status())
# print(pessoa2.status())

# class gato:
#     def __init__(self,nome,pelagem):
#         self.nome = nome
#         self.pelagem = pelagem

#     def falar(self):
#         return f"Miau"

#     def comer(self):
#         return f"Come Ração"
    
#     def dormir(self):
#         return f"Dorme"
    
# meu_gato = gato("Bixano","Malhado")

# print(f"Meu gato se chama {meu_gato.nome} e sua pelagem é {meu_gato.pelagem} e quando ele esta com fome ele faz {meu_gato.falar()} e depois que ele {meu_gato.comer()} ele {meu_gato.dormir()} ")

# class veiculo:
#     def __init__(self,modelo,cor,ano):
#         self.modelo = modelo
#         self.cor = cor
#         self.ano = ano
    
# veiculo1 = veiculo("Fusca","Prata",1990)
# veiculo2 = veiculo("Argo","Preto",2020)
# veiculo3 = veiculo("Civic","Branco",2010)

# print(f"""VEICULO 1:
# Modelo: {veiculo1.modelo} 
# Cor: {veiculo1.cor} 
# Ano: {veiculo1.ano}
# """)

# print(f"""VEICULO 2:
# Modelo: {veiculo2.modelo} 
# Cor: {veiculo2.cor} 
# Ano: {veiculo2.ano}
# """)

# print(f"""VEICULO 3:
# Modelo: {veiculo3.modelo} 
# Cor: {veiculo3.cor} 
# Ano: {veiculo3.ano}
# """)

#Exercicio:

class Círculo:
    def __init__(self,raio):
        self.raio = raio    
    
    def area(self):
        return 3.14 * self.raio ** 2
    
    def perimetro(self):
        return 2 * 3.14 * self.raio

raio = 20
círculo1 = Círculo(raio)

print(f"""
O raio do círculo é {círculo1.raio}
A área do círculo é {círculo1.area()}
O perímetro do círculo é {círculo1.perimetro()}
""")