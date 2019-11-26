import threading as _
import _thread

class Conta(object):                    #Criando a classe

    def __init__(self, nome=" ", saldo=0):    #Definindo os métodos
        self.saldo = saldo                 #Método do saldo
        self.nome = nome                   #Método do nome

    def get_saldo(self):               #Consulta o saldo
        return self.saldo

    def get_nome(self):             #Consulta o nome
        return self.nome

    def transferencia(self, conta, transferencia, a):   #Função que realiza a transferência de uma conta p/ outra
        a.acquire()   #Libera a entrdada de uma thread

        try:              #Tentativa de ralização

            if self.saldo >= transferencia:
                conta.saldo += transferencia
                self.saldo -= transferencia
                print(self.get_nome(), self.get_saldo(),'R$\n')
                print(conta.get_nome(),  conta.get_saldo(),'R$')

        finally:         #Código sempre será executado

            a.release()     #Liberação da thread

if __name__ == '__main__':                 #Função principal
    p1 = Conta('Jeferson', 100)      #Obejto 1
    p2 = Conta('Filipe', 0)          #Objeto 2

    block = _.Lock()     #Impede que as duas Thread execute ao mesmo tempo

    for processo in range(100):   #Qunatidade de Prcessos

        processo1 = _.Thread(target=p1.transferencia, args=(p2, 10, block))   #Cria o primeiro processo
        processo1.start()   #Inicia o primeiro processo

        processo2 = _.Thread(target=p2.transferencia, args=(p1, 10, block))   #Cria o segundo Processo
        processo2.start()   #Inicia o segundo processo
