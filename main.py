from datetime import date

# ---------------------------------------------------------------
# SUPERCLASSE: concentra o que é comum a Membro e Autor
# ---------------------------------------------------------------
class Pessoa:
    def __init__(self, nome):
        self.__nome = ""
        self.set_nome(nome)

    def get_nome(self):
        return self.__nome

    def set_nome(self, nome):
        if len(nome) >= 3:
            self.__nome = nome
        else:
            print("Erro (Pessoa - João Turano): O nome deve ter 3 ou mais caracteres.")

    def apresentar(self):
        return f"Olá, meu nome é {self.__nome}."


# ---------------------------------------------------------------
# SUBCLASSE 1: Membro (antes "Leitor")
# ---------------------------------------------------------------
class Membro(Pessoa):
    def __init__(self, id, nome, email):
        super().__init__(nome)
        self.__id = id
        self.__email = email
        self.__emprestimos = []  # Membro 1 -> 0..* Emprestimo

    def get_id(self):
        return self.__id

    def get_email(self):
        return self.__email

    def pegar_emprestado(self, livro, data):
        if livro.emprestar():
            emprestimo = Emprestimo(livro, data)
            self.__emprestimos.append(emprestimo)
            return emprestimo
        return None

    def listar_emprestimos(self):
        return list(self.__emprestimos)


# ---------------------------------------------------------------
# SUBCLASSE 2: Autor
# ---------------------------------------------------------------
class Autor(Pessoa):
    def __init__(self, nome, nacionalidade):
        super().__init__(nome)
        self.__nacionalidade = nacionalidade
        self.__obras = []  # Autor 1..* <-> 1..* Livro

    def get_nacionalidade(self):
        return self.__nacionalidade

    def adicionar_obra(self, livro):
        if livro not in self.__obras:
            self.__obras.append(livro)

    def listar_obras(self):
        return list(self.__obras)


# ---------------------------------------------------------------
# Livro
# ---------------------------------------------------------------
class Livro:
    def __init__(self, isbn, titulo, ano_publicacao=None):
        self.__isbn = isbn
        self.__titulo = ""
        self.__ano_publicacao = None
        self.__disponivel = True
        self.__autores = []  # Livro 1..* <-> 1..* Autor

        self.set_titulo(titulo)
        if ano_publicacao is not None:
            self.set_ano_publicacao(ano_publicacao)

    def get_isbn(self):
        return self.__isbn

    def get_titulo(self):
        return self.__titulo

    def get_ano_publicacao(self):
        return self.__ano_publicacao

    def set_titulo(self, titulo):
        if len(titulo) >= 2:
            self.__titulo = titulo
        else:
            print("Erro (Livro - João App): O título deve ter pelo menos 2 caracteres.")

    def set_ano_publicacao(self, ano):
        if 1000 < ano <= 2026:
            self.__ano_publicacao = ano
        else:
            print("Erro (Livro - João App): Ano de publicação inválido.")

    def adicionar_autor(self, autor):
        if autor not in self.__autores:
            self.__autores.append(autor)
            autor.adicionar_obra(self)

    def get_autores(self):
        return list(self.__autores)

    def esta_disponivel(self):
        return self.__disponivel

    def emprestar(self):
        if self.__disponivel:
            self.__disponivel = False
            return True
        print(f"Erro (Livro): '{self.__titulo}' já está emprestado.")
        return False

    def devolver(self):
        self.__disponivel = True


# ---------------------------------------------------------------
# Emprestimo
# ---------------------------------------------------------------
class Emprestimo:
    PRAZO_DIAS = 7
    MULTA_POR_DIA = 1.00

    def __init__(self, livro, data_emprestimo):
        self.__livro = livro  # Emprestimo * -> 1 Livro
        self.__data_emprestimo = data_emprestimo
        self.__data_devolucao = None

    def get_livro(self):
        return self.__livro

    def get_data_emprestimo(self):
        return self.__data_emprestimo

    def get_data_devolucao(self):
        return self.__data_devolucao

    def calcular_multa(self):
        if self.__data_devolucao is None:
            return 0.0
        dias_usados = (self.__data_devolucao - self.__data_emprestimo).days
        atraso = max(0, dias_usados - self.PRAZO_DIAS)
        return atraso * self.MULTA_POR_DIA

    def finalizar(self, data_devolucao):
        self.__data_devolucao = data_devolucao
        self.__livro.devolver()


# ---------------------------------------------------------------
# Biblioteca
# ---------------------------------------------------------------
class Biblioteca:
    def __init__(self, nome, endereco):
        self.nome = nome
        self.__endereco = endereco
        self.__livros = []  # Biblioteca 1 -> 0..* Livro (composição)
        self.__membros = []  # Biblioteca 1 -> 0..* Membro (agregação)

    def cadastrar_livro(self, isbn, titulo):
        livro = Livro(isbn, titulo)
        self.__livros.append(livro)
        return livro

    def cadastrar_membro(self, membro):
        self.__membros.append(membro)

    def get_livros(self):
        return list(self.__livros)

    def get_membros(self):
        return list(self.__membros)


# ---------------------------------------------------------------
# Funcionario (classe original do grupo, mantida sem alterações)
# ---------------------------------------------------------------
class Funcionario:
    def __init__(self, cargo, salario):
        self.__cargo = ""
        self.__salario = 0.0
        self.set_cargo(cargo)
        self.set_salario(salario)

    def get_cargo(self):
        return self.__cargo

    def get_salario(self):
        return self.__salario

    def set_cargo(self, cargo):
        cargos_permitidos = ["Bibliotecario", "Atendente", "Gerente"]
        if cargo in cargos_permitidos:
            self.__cargo = cargo
        else:
            print("Erro (Funcionario - Pedro): Cargo inválido. Use Bibliotecario, Atendente ou Gerente.")

    def set_salario(self, salario):
        if salario >= 1412.00:
            self.__salario = salario
        else:
            print("Erro (Funcionario - Pedro): O salário não pode ser menor que R$ 1412,00.")


# ---------------------------------------------------------------
# TESTES
# ---------------------------------------------------------------
if __name__ == "__main__":
    print("=== TESTANDO O SISTEMA DE BIBLIOTECA ===")
    print("\n--- Herança: Pessoa -> Membro e Autor ---")
    tolkien = Autor("J. R. R. Tolkien", "Britânica")
    maria = Membro(1, "Maria Silva", "maria@email.com")
    print(isinstance(tolkien, Pessoa), isinstance(maria, Pessoa))
    print(tolkien.apresentar())
    print(maria.apresentar())
    Membro(2, "Jo", "jo@email.com")  # nome inválido (validação herdada de Pessoa)

    print("\n--- Biblioteca, Livro e Autor ---")
    biblioteca = Biblioteca("Biblioteca UNASP", "Engenheiro Coelho - SP")
    biblioteca.cadastrar_membro(maria)
    livro = biblioteca.cadastrar_livro("978-85-333-0227-3", "O Senhor dos Anéis")
    livro.set_ano_publicacao(1954)
    livro.adicionar_autor(tolkien)
    print(f"Livro: {livro.get_titulo()} ({livro.get_ano_publicacao()})")
    print("Autores:", [a.get_nome() for a in livro.get_autores()])
    print("Obras de Tolkien:", [l.get_titulo() for l in tolkien.listar_obras()])
    biblioteca.cadastrar_livro("0", "A")  # título inválido

    print("\n--- Empréstimo (com multa) ---")
    emprestimo = maria.pegar_emprestado(livro, date(2026, 10, 1))
    print("Disponível após emprestar?", livro.esta_disponivel())
    maria.pegar_emprestado(livro, date(2026, 10, 2))  # já emprestado
    emprestimo.finalizar(date(2026, 10, 12))  # 11 dias -> 4 de atraso
    print(f"Multa: R$ {emprestimo.calcular_multa():.2f}")
    print("Disponível após devolver?", livro.esta_disponivel())
    print("Empréstimos da Maria:", len(maria.listar_emprestimos()))

    print("\n--- Funcionario ---")
    func = Funcionario("Atendente", 2500.00)
    print(f"Funcionário: {func.get_cargo()} - R$ {func.get_salario():.2f}")
    Funcionario("Diretor", 1000.00)
