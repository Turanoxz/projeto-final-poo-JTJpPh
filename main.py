# ============================================================================== 
# CLASSE 1: LIVRO (Para João App)
# ==============================================================================
class Livro:
    def __init__(self, titulo, ano_publicacao):
        self.__titulo = ""
        self.__ano_publicacao = 0

        self.set_titulo(titulo)
        self.set_ano_publicacao(ano_publicacao)

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
        if ano > 1000 and ano <= 2026:
            self.__ano_publicacao = ano
        else:
            print("Erro (Livro - João App): Ano de publicação inválido.")


# ============================================================================== 
# CLASSE 2: LEITOR (Para João Turano)
# ==============================================================================
class Leitor:
    def __init__(self, nome, idade):
        self.__nome = ""
        self.__idade = 0

        self.set_nome(nome)
        self.set_idade(idade)

    def get_nome(self):
        return self.__nome

    def get_idade(self):
        return self.__idade

    def set_nome(self, nome):
        if len(nome) >= 3:
            self.__nome = nome
        else:
            print("Erro (Leitor - João Turano): O nome deve ter 3 ou mais caracteres.")

    def set_idade(self, idade):
        if idade >= 12:
            self.__idade = idade
        else:
            print("Erro (Leitor - João Turano): O leitor deve ter no mínimo 12 anos.")


# ============================================================================== 
# CLASSE 3: FUNCIONARIO (Para Pedro)
# ==============================================================================
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


# ==============================================================================
# TESTES DE VALIDAÇÃO DO PROJETO FINAL (Trio: João App, João Turano e Pedro)
# ==============================================================================
if __name__ == "__main__":
    print("=== TESTANDO AS CLASSES DO SISTEMA DE BIBLIOTECA ===")

    print("\n--- TESTES DO JOÃO APP (LIVRO) ---")
    livro_valido = Livro("O Senhor dos Anéis", 1954)
    print(f"Livro Criado: {livro_valido.get_titulo()} - Ano: {livro_valido.get_ano_publicacao()}")
    livro_invalido = Livro("A", 3000)

    print("\n--- TESTES DO JOÃO TURANO (LEITOR) ---")
    leitor_valido = Leitor("Maria Silva", 25)
    print(f"Leitor Criado: {leitor_valido.get_nome()} - Idade: {leitor_valido.get_idade()}")
    leitor_valido.set_idade(8)

    print("\n--- TESTES DO PEDRO (FUNCIONARIO) ---")
    func_valido = Funcionario("Atendente", 2500.00)
    print(f"Funcionário Criado: {func_valido.get_cargo()} - Salário: R$ {func_valido.get_salario():.2f}")
    func_invalido = Funcionario("Diretor", 1000.00)
