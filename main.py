from datetime import date
import math

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
        if not isinstance(nome, str) or len(nome.strip()) < 3:
            raise ValueError("O nome deve ter pelo menos 3 caracteres.")
        self.__nome = nome.strip()

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
        if not isinstance(livro, Livro) or type(data) is not date:
            raise ValueError("Os dados do empréstimo são inválidos.")
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
        if not isinstance(isbn, str) or not isbn.strip():
            raise ValueError("O ISBN não pode ficar vazio.")
        self.__isbn = isbn.strip()
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
        if not isinstance(titulo, str) or len(titulo.strip()) < 2:
            raise ValueError("O título deve ter pelo menos 2 caracteres.")
        self.__titulo = titulo.strip()

    def set_ano_publicacao(self, ano):
        if type(ano) is not int or not 1000 < ano <= date.today().year:
            raise ValueError(
                f"O ano deve estar entre 1001 e {date.today().year}."
            )
        self.__ano_publicacao = ano

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
        if self.__disponivel:
            raise ValueError("Este livro já está disponível para empréstimo.")
        self.__disponivel = True


# ---------------------------------------------------------------
# Emprestimo
# ---------------------------------------------------------------
class Emprestimo:
    PRAZO_DIAS = 7
    MULTA_POR_DIA = 1.00

    def __init__(self, livro, data_emprestimo):
        if not isinstance(livro, Livro) or type(data_emprestimo) is not date:
            raise ValueError("Os dados do empréstimo são inválidos.")
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
        if self.__data_devolucao is not None:
            raise ValueError("Este empréstimo já foi finalizado.")
        if (
            type(data_devolucao) is not date
            or data_devolucao < self.__data_emprestimo
        ):
            raise ValueError("A data de devolução não pode ser anterior ao empréstimo.")
        self.__livro.devolver()
        self.__data_devolucao = data_devolucao


# ---------------------------------------------------------------
# Biblioteca
# ---------------------------------------------------------------
class Biblioteca:
    def __init__(self, nome, endereco):
        self.nome = nome
        self.__endereco = endereco
        self.__livros = []  # Biblioteca 1 -> 0..* Livro (composição)
        self.__membros = []  # Biblioteca 1 -> 0..* Membro (agregação)

    def cadastrar_livro(self, isbn, titulo, ano_publicacao=None):
        livro = Livro(isbn, titulo, ano_publicacao)
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
        if cargo not in cargos_permitidos:
            raise ValueError(
                "Cargo inválido. Use Bibliotecario, Atendente ou Gerente."
            )
        self.__cargo = cargo

    def set_salario(self, salario):
        if (
            not isinstance(salario, (int, float))
            or not math.isfinite(salario)
            or salario < 1412.00
        ):
            raise ValueError("O salário mínimo permitido é R$ 1.412,00.")
        self.__salario = salario


def ler_inteiro(prompt, minimo, maximo=None):
    while True:
        try:
            valor = int(input(prompt))
        except ValueError:
            print("Entrada inválida. Digite um número inteiro.")
            continue
        if valor < minimo:
            print(f"Entrada inválida. Digite um valor a partir de {minimo}.")
            continue
        if maximo is not None and valor > maximo:
            print(f"Entrada inválida. Digite um valor até {maximo}.")
            continue
        return valor


def ler_texto(prompt, campo, minimo=1):
    while True:
        valor = input(prompt).strip()
        if len(valor) < minimo:
            print(f"Entrada inválida: {campo} deve ter pelo menos {minimo} caracteres.")
            continue
        return valor


def ler_salario():
    while True:
        try:
            salario = float(input("Salário: R$ "))
        except ValueError:
            print("Entrada inválida. Digite um valor numérico para o salário.")
            continue
        if not math.isfinite(salario) or salario < 1412.00:
            print("Entrada inválida. O salário mínimo permitido é R$ 1.412,00.")
            continue
        return salario


def selecionar_indice(itens, prompt):
    if not itens:
        raise ValueError("Não há itens cadastrados para esta operação.")
    return ler_inteiro(prompt, 1, len(itens)) - 1


def executar_menu():
    biblioteca = Biblioteca("Biblioteca UNASP", "Engenheiro Coelho - SP")
    funcionarios = []

    while True:
        print("\n=== SISTEMA DE BIBLIOTECA ===")
        print("1 - Cadastrar livro")
        print("2 - Cadastrar membro")
        print("3 - Registrar empréstimo")
        print("4 - Finalizar empréstimo")
        print("5 - Cadastrar funcionário")
        print("6 - Listar livros")
        print("0 - Sair")

        try:
            opcao = int(input("Escolha uma opção: "))
        except ValueError:
            print("Opção inválida. Digite um dos números do menu.")
            continue

        if opcao == 0:
            print("Sistema encerrado.")
            return

        try:
            if opcao == 1:
                isbn = ler_texto("ISBN: ", "O ISBN")
                titulo = ler_texto("Título do livro: ", "O título", 2)
                ano = ler_inteiro("Ano de publicação: ", 1001, date.today().year)
                livro = biblioteca.cadastrar_livro(isbn, titulo, ano)
                print(f"Livro cadastrado: {livro.get_titulo()}")
            elif opcao == 2:
                membro_id = ler_inteiro("ID do membro: ", 1)
                nome = ler_texto("Nome do membro: ", "O nome", 3)
                email = ler_texto("E-mail do membro: ", "O e-mail")
                membro = Membro(membro_id, nome, email)
                biblioteca.cadastrar_membro(membro)
                print(f"Membro cadastrado: {membro.get_nome()}")
            elif opcao == 3:
                livros = biblioteca.get_livros()
                membros = biblioteca.get_membros()
                for indice, livro in enumerate(livros, start=1):
                    estado = "disponível" if livro.esta_disponivel() else "emprestado"
                    print(f"{indice} - {livro.get_titulo()} ({estado})")
                livro = livros[selecionar_indice(livros, "Número do livro: ")]
                for indice, membro in enumerate(membros, start=1):
                    print(f"{indice} - {membro.get_nome()}")
                membro = membros[selecionar_indice(membros, "Número do membro: ")]
                emprestimo = membro.pegar_emprestado(livro, date.today())
                if emprestimo is None:
                    print("Este livro já está emprestado.")
                else:
                    print("Empréstimo registrado.")
            elif opcao == 4:
                emprestimos = [
                    emprestimo
                    for membro in biblioteca.get_membros()
                    for emprestimo in membro.listar_emprestimos()
                    if emprestimo.get_data_devolucao() is None
                ]
                for indice, emprestimo in enumerate(emprestimos, start=1):
                    print(f"{indice} - {emprestimo.get_livro().get_titulo()}")
                emprestimo = emprestimos[
                    selecionar_indice(emprestimos, "Número do empréstimo: ")
                ]
                emprestimo.finalizar(date.today())
                print(f"Devolução registrada. Multa: R$ {emprestimo.calcular_multa():.2f}")
            elif opcao == 5:
                cargo = ler_texto("Cargo (Bibliotecario, Atendente ou Gerente): ", "O cargo")
                salario = ler_salario()
                funcionario = Funcionario(cargo, salario)
                funcionarios.append(funcionario)
                print(f"Funcionário cadastrado: {funcionario.get_cargo()}")
            elif opcao == 6:
                livros = biblioteca.get_livros()
                if not livros:
                    print("Ainda não há livros cadastrados.")
                for livro in livros:
                    print(f"{livro.get_titulo()} - {livro.get_ano_publicacao()}")
            else:
                print("Opção inexistente. Escolha uma opção de 0 a 6.")
        except (IndexError, ValueError) as erro:
            print(f"Não foi possível concluir a operação: {erro}")


def executar_testes():
    print("=== TESTANDO O SISTEMA DE BIBLIOTECA ===")
    print("\n--- Herança: Pessoa -> Membro e Autor ---")
    tolkien = Autor("J. R. R. Tolkien", "Britânica")
    maria = Membro(1, "Maria Silva", "maria@email.com")
    print(isinstance(tolkien, Pessoa), isinstance(maria, Pessoa))
    print(tolkien.apresentar())
    print(maria.apresentar())
    try:
        Membro(2, "Jo", "jo@email.com")
    except ValueError as erro:
        print(f"Entrada inválida tratada: {erro}")

    print("\n--- Biblioteca, Livro e Autor ---")
    biblioteca = Biblioteca("Biblioteca UNASP", "Engenheiro Coelho - SP")
    biblioteca.cadastrar_membro(maria)
    livro = biblioteca.cadastrar_livro("978-85-333-0227-3", "O Senhor dos Anéis")
    livro.set_ano_publicacao(1954)
    livro.adicionar_autor(tolkien)
    print(f"Livro: {livro.get_titulo()} ({livro.get_ano_publicacao()})")
    print("Autores:", [a.get_nome() for a in livro.get_autores()])
    print("Obras de Tolkien:", [l.get_titulo() for l in tolkien.listar_obras()])
    try:
        biblioteca.cadastrar_livro("0", "A")
    except ValueError as erro:
        print(f"Entrada inválida tratada: {erro}")

    print("\n--- Empréstimo (com multa) ---")
    emprestimo = maria.pegar_emprestado(livro, date(2026, 10, 1))
    print("Disponível após emprestar?", livro.esta_disponivel())
    maria.pegar_emprestado(livro, date(2026, 10, 2))
    emprestimo.finalizar(date(2026, 10, 12))  # 11 dias -> 4 de atraso
    print(f"Multa: R$ {emprestimo.calcular_multa():.2f}")
    print("Disponível após devolver?", livro.esta_disponivel())
    print("Empréstimos da Maria:", len(maria.listar_emprestimos()))

    print("\n--- Funcionario ---")
    func = Funcionario("Atendente", 2500.00)
    print(f"Funcionário: {func.get_cargo()} - R$ {func.get_salario():.2f}")
    try:
        Funcionario("Diretor", 1000.00)
    except ValueError as erro:
        print(f"Entrada inválida tratada: {erro}")


if __name__ == "__main__":
    executar_menu()
