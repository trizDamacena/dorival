class ItemBiblioteca:
    def __init__(self, titulo: str, ano_publicacao: int, disponivel: bool):
        self.titulo = titulo
        self.ano_publicacao = ano_publicacao
        self.disponivel = disponivel

    def emprestar(self):
        if not self.disponivel:
            print("Este livro não está dísponivel")
        else:
            self.disponivel = False
            print(f"Livro: {self.titulo} emprestado com sucesso!\n")

    def devolver(self):
        self.disponivel = True
        print(f"Livro {self.titulo} devolvido com sucesso!\n")
    
    def obter_info(self):

        if self.disponivel == True:
            print( f"Livro: {self.titulo}\nAno de publicação: {self.ano_publicacao}\nDisponivel: Sim\n")
        else:
            print( f"Livro: {self.titulo}\nAno de publicação: {self.ano_publicacao}\nDisponivel: Não\n")
    

livro1 = ItemBiblioteca("Percy Jackson", 2006, True)

livro1.obter_info()

livro1.emprestar()

livro1.obter_info()

livro1.devolver()

livro1.obter_info()


class ColecaoLivro(ItemBiblioteca):
    def __init__(self, titulo, ano_publicacao, disponivel, lista_livros):
        super().__init__(titulo, ano_publicacao, disponivel)
        lista_livros = []

    def adicionar_livro(self, livro:ItemBiblioteca):
        self.lista_livros.append(livro)
    
    def verificar_disponibilidade_colecao(self):
        for livro in self.lista_livros:
            if not livro.disponivel:
                print("A coleção não está disponivel")
            else:
                print("Coleção disponivel")

colecao_PJ = ColecaoLivro(ItemBiblioteca)