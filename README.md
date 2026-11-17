# Sistema de Biblioteca em Python

## Descrição do Projeto

Este projeto foi desenvolvido como atividade de Programação Orientada a Objetos (POO) para simular o funcionamento de uma biblioteca acadêmica. O sistema permite cadastrar livros, membros, autores, funcionários e controlar empréstimos e devoluções de obras.

A aplicação foi organizada em classes, com uso de conceitos como:

- Herança
- Encapsulamento
- Composição e agregação
- Validação de dados
- Tratamento de exceções
- Menu interativo em terminal

## Integrantes da Dupla/Grupo

- João Turano Firagi
- Pedro Henrique Anjos Barbosa
- João Pedro Apolinário de Souza

## Estrutura do Projeto

```text
hhhhhhhh/
├── README.md
├── alt.py
├── projeto-final-poo-JTJpPh/
│   └── main.py
└── .git/
```

## Arquivos Principais

- `alt.py`: versão alternativa do sistema, com foco em validações e classes relacionadas ao gerenciamento da biblioteca.
- `projeto-final-poo-JTJpPh/main.py`: arquivo principal do sistema, onde o menu e a execução do programa são integrados.

## Classes do Sistema

- `Pessoa`: classe base para `Membro` e `Autor`
- `Membro`: representa o usuário da biblioteca
- `Autor`: representa o autor do livro
- `Livro`: controla ISBN, título, publicação e disponibilidade
- `Emprestimo`: registra a data do empréstimo, devolução e multa por atraso
- `Biblioteca`: centraliza cadastro de livros e membros
- `Funcionario`: armazena cargo e salário

## Funcionalidades

- Cadastro de livros
- Cadastro de membros
- Cadastro de autores
- Empréstimo de livros
- Devolução de livros
- Cálculo de multa por atraso
- Validação de entradas e regras de negócio
- Menu principal para interação com o usuário

## Como Executar

### Executar a versão principal

```bash
python projeto-final-poo-JTJpPh/main.py
```

### Executar a versão alternativa

```bash
python alt.py
```

## Menu Principal e Integração do Sistema

O programa usa um laço `while True` para manter o sistema em execução até que o usuário escolha sair. O menu principal apresenta opções numeradas para os principais módulos do sistema, como:

- cadastrar livro
- cadastrar membro
- registrar empréstimo
- finalizar empréstimo
- cadastrar funcionário
- listar livros
- encerrar sistema

Assim, o usuário navega entre as funcionalidades do sistema sem sair do programa, e cada opção chama o trecho correspondente da lógica do projeto.

## Testes e Depuração

Durante a fase de testes, o grupo identificou alguns erros lógicos e de validação. Abaixo estão exemplos de falhas comuns corrigidas:

| # | Descrição do erro / bug | Causa raiz identificada | Solução aplicada |
|---|------------------------|-------------------------|------------------|
| 1 | Livro com título inválido era aceito | Falta de validação no campo de título | Foi adicionada validação para garantir tamanho mínimo e entrada correta |
| 2 | Empréstimo de livro indisponível era permitido | Verificação de disponibilidade não era tratada corretamente | A lógica de `emprestar()` passou a impedir novos empréstimos quando o livro já estava alugado |
| 3 | Data de devolução anterior ao empréstimo aceitava valor inválido | Falta de validação da ordem das datas | Foi adicionada checagem para impedir devoluções anteriores à data do empréstimo |

Esses ajustes foram realizados no VS Code durante a depuração e testes do sistema.

## Publicação no GitHub

### Link do Repositório

```text
https://github.com/Turanoxz/projeto-final-poo-JTJpPh.git
```

### Checklist de Publicação

- [ ] O repositório contém um arquivo `README.md` descritivo explicando o tema do projeto, os integrantes e como executar o código.
- [ ] O código-fonte está organizado em módulos/arquivos limpos, comentados e sem arquivos temporários desnecessários.
- [ ] O histórico de commits demonstra a participação colaborativa dos integrantes ao longo do desenvolvimento.

## Observações

Este projeto tem finalidade acadêmica e foi desenvolvido para demonstrar a aplicação prática de conceitos de programação orientada a objetos em Python.

## Licença

Projeto para fins educacionais e de entrega acadêmica.
