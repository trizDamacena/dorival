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
#
Percy_Jackson = ColecaoLivro("Percy Jackson e os Olimpianos", 2009, True)
#
Percy_Jackson.adicionar_livro(pj_1)
Percy_Jackson.adicionar_livro(pj_2)
Percy_Jackson.adicionar_livro(pj_3)
#Percy_Jackson.verificar_disponibilidade_colecao()
#
#Percy_Jackson.obter_info()


class Revista(ItemBiblioteca):
    def __init__(self, titulo, ano_publicacao, disponivel, edicao):
        super().__init__(titulo, ano_publicacao, disponivel)
        self.edicao = edicao

    def atualizar_edicao(self, nova_edicao):
        self.nova_edicao = nova_edicao

        if nova_edicao <= 0:
            raise  ValueError("O número da nova edição não pode ser inferior ou igual a 0")
        else:
            self.edicao = nova_edicao

    def restringir_emprestimo(self, dias_max):
        self.dias_max = dias_max

        if self.ano_publicacao < 2000 and self.dias_max <= 7 or self.ano_publicacao >=2000 and self.dias_max <= 14:
            print("Emprestimo pode ser realizado")
        else:
            print("Não é possível realizar empréstimo.")

    def obter_info(self):
        if self.disponivel == True:
            print( f"Livro: {self.titulo}\nAno de publicação: {self.ano_publicacao}\nEdição: {self.edicao}\nDisponivel: Sim\n")
        else:
            print( f"Livro: {self.titulo}\nAno de publicação: {self.ano_publicacao}\nEdição: {self.edicao}\nDisponivel: Não\n")

revista1 = Revista("Capricho", 2014, False, 0)


#revista1.atualizar_edicao(7)
#
#revista1.restringir_emprestimo(13)
#
#revista1.obter_info()



class Biblioteca():
    def __init__(self, nome):
        self.nome = nome
        self.itens = {}
    
    def adicionar_itens(self, livro):
        if livro.titulo in self.itens.keys():
            raise ValueError("Não pode acrescentar algo que já exista.")
        else:
            self.itens[livro.titulo] = livro.ano_publicacao, livro.disponivel
            print(self.itens)
            
    def remover_itens(self, livro):

        if livro.titulo in self.itens.keys():
            del self.itens[livro.titulo]
        else:
            raise ValueError ("Não pode ser removido algo que não existe")
    
    def listar_itens_disponiveis(self):
        for titulo, (ano, disponivel) in self.itens.items():
            if disponivel:
                print(f"\nTítulo: {titulo}\nAno publicação: {ano}\nDisponivel: Sim")

    def contar_itens_emprestados(self):
        contador = 0 
        for titulo, (ano, disponivel) in self.itens.items():
            if not disponivel:
                contador += 1
                print(f"Total de itens emprestados: {contador}")


acervo = Biblioteca("Acervo")
acervo.adicionar_itens(Percy_Jackson)
acervo.adicionar_itens(revista1)
acervo.listar_itens_disponiveis()
acervo.contar_itens_emprestados()

