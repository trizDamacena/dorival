class ContaBancaria:
    def __init__(self, titular, saldo: int):
        self.titular = titular #Atributo público
        self.__saldo = saldo

    @property
    def saldo(self):
        return self.__saldo

    @saldo.setter
    def saldo(self,valor):
        if valor < 0:
            print("Saldo não pode ser negativo")
        else:
            self.__saldo = valor
    #def get_saldo(self):
    #    return  self.__saldo
    #def set_saldo(self, valor):
    #    if valor < 0:
    #        raise   ValueError("Saldo nao pode ser negativo")

minhaConta = ContaBancaria("Beatriz", 700)
minhaConta.saldo = 500 #modificando o valor da conta bancária
print(minhaConta.saldo)