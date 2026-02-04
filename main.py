import os

# "Banco de dados" em memória
biblioteca = []


def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')


def adicionar_livro():
    titulo = input("Título do Livro: ")
    autor = input("Autor: ")
    id_livro = len(biblioteca) + 1
    livro = {"id": id_livro, "titulo": titulo, "autor": autor, "status": "Disponível"}
    biblioteca.append(livro)
    print(f"\n✅ Livro '{titulo}' cadastrado com sucesso!")


def listar_livros():
    if not biblioteca:
        print("\nA biblioteca está vazia.")
    else:
        print("\n--- Catálogo de Livros ---")
        for livro in biblioteca:
            print(f"ID: {livro['id']} | {livro['titulo']} ({livro['autor']}) - [{livro['status']}]")


def emprestar_livro():
    id_procurado = int(input("Informe o ID do livro para empréstimo: "))
    for livro in biblioteca:
        if livro['id'] == id_procurado:
            if livro['status'] == "Disponível":
                livro['status'] = "Emprestado"
                print(f"\n📖 Empréstimo do livro '{livro['titulo']}' realizado!")
            else:
                print("\n❌ Este livro já está emprestado.")
            return
    print("\n⚠️ Livro não encontrado.")


while True:
    print("\n--- SISTEMA DE GESTÃO DE BIBLIOTECA v1.0 ---")
    print("1. Cadastrar Novo Livro")
    print("2. Listar Livros")
    print("3. Registrar Empréstimo")
    print("4. Sair")

    opcao = input("\nEscolha uma opção: ")

    if opcao == '1':
        adicionar_livro()
    elif opcao == '2':
        listar_livros()
    elif opcao == '3':
        emprestar_livro()
    elif opcao == '4':
        break
    else:
        print("Opção inválida.")


def print_hi(name):
    print(f'Hi, {name}')  


if __name__ == '__main__':
    print_hi('PyCharm')


