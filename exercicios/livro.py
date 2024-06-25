class Livro:
    livros = []

    def __init__(self, titulo, autor, ano):
        self._titulo = titulo
        self._autor = autor
        self._ano = ano
        self._disponivel = True
        Livro.livros.append(self)

    def __str__(self):
        return f'{self._titulo} | {self._autor} | {self._ano}'
    
    def emprestar(self):
        self._disponivel = not self._disponivel

    @property
    def muda_disponivel(self):
        return '☑' if self._disponivel else '☐'
    
    @classmethod
    def exibir_livros(cls):
        print(f'{'Titulo'.center(20)} | {'Autor'.center(30)} | {'Ano'.center(20)} | {'Disponibilidade'.center(20)}')
        for livro in cls.livros:
            print(f'{livro._titulo.ljust(20)} | {livro._autor.ljust(30)} | {livro._ano.ljust(20)} | {livro.muda_disponivel}')