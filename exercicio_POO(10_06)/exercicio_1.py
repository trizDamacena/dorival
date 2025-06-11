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
    

pj_1 = ItemBiblioteca("Percy Jackson", 2006, True)

#pj_1.obter_info()

#pj_1.emprestar()

#pj_1.obter_info()

#pj_1.devolver()

#pj_1.obter_info()


class ColecaoLivro(ItemBiblioteca):
    def __init__(self, titulo, ano_publicacao, disponivel):
        super().__init__(titulo, ano_publicacao, disponivel)
        self.lista_livros = []

    def adicionar_livro(self, livro:ItemBiblioteca):
        self.lista_livros.append(livro)
    
    def verificar_disponibilidade_colecao(self):

        for livro in self.lista_livros:
            if not livro.disponivel:
                print(f"A coleção não está disponível")
                return False
        print("A coleção está disponivel")
        return True
    
    def obter_info(self):
        for livro in self.lista_livros:
            if not livro.disponivel:
                print(f"\nNome: {self.titulo}\nAno: {self.ano_publicacao}\nDisponivel: Não")
            else:
                print(f"\nNome: {self.titulo}\nAno: {self.ano_publicacao}\nDisponivel: Sim")
        

pj_2 = ItemBiblioteca("Percy Jackson e o Mar de Monstro", 2006, True)
pj_3 = ItemBiblioteca("Percy Jakcson e a Maldição do Titãn",2007, False )

Percy_Jackson = ColecaoLivro("Percy Jackson e os Olimpianos", 2009, True)

Percy_Jackson.adicionar_livro(pj_1)
Percy_Jackson.adicionar_livro(pj_2)
Percy_Jackson.adicionar_livro(pj_3)
Percy_Jackson.verificar_disponibilidade_colecao()

Percy_Jackson.obter_info()
