from livro import Livro

livro_monica = Livro('Turma da monica', 'Mauricio Araújo de Sousa', '1970')
livro_monica.muda_disponivel()

def main():
    Livro.exibir_livros()

if __name__ == '__main__':
    main()