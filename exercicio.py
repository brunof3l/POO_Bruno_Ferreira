class livro:
    def __init__(self, ISBN: str, titulo: str, autor: str, disponivel: bool):
        self.ISBN = ISBN
        self.titulo = titulo
        self.autor = autor
        self.disponivel = disponivel

class limite_emprestismos_excedido:
    pass

class livro_indisponivel:
    pass

class usuario:
    def __init__(self,matricula: str, nome: str, limite: int):
        self.matricula = matricula
        self.nome = nome
        self.limite = limite
        self.livros_emprestados = []


    