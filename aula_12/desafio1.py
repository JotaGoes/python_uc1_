##
# Criar a classe Carro com as seguintes informações:
# cor  -> info.cor ()
# placa -> emplacar (plc)
# seguro -> seguro.contratar ()
#        -> seguro.cancelar ()
# reboque -> reboque.instal ()
#         -> reboque.desinstal ()

class Carro:
    def __init__(self, marca, modelo, ano, cor):
        self.marca = marca      
        self.modelo = modelo    
        self.ano = ano 
        self.cor = cor
        self.placa = ()
        self._seguro = ()
        self._reboque = ()
        self._ligado = False     
##############################################
    def ligar(self):
        if not self._ligado:
         self._ligado = True
         print(f"{self.marca} {self.modelo} está ligado. ")
        else:
         print(f"{self.marca} {self.modelo} já está ligado.")
##############################################
    def desligar(self):
        if self._ligado:
            self._ligado = False
            print(f"{self.marca} {self.modelo} está desligado. ")
        else:
            print(f"{self.marca} {self.modelo} já está desligado. ")
###############################################
    def exibir_info(self):
        if self._ligado:
            status = "Ligado"
        else:
            status= "Desligado"

        print (f"{self.marca} - {self.modelo} está {status} ")
###############################################
    def info_cor(self):
       print(f"O carro é da cor {self.cor}")
###############################################
    def seguro_contratado(self):
       if self._seguro:
          self._seguro = True
          print(f"{self.marca} {self.modelo} já tem seguro! ")
       else:
          print(f"{self.marca} {self.modelo} está com o seguro contratado")
###############################################
    def seguro_cancelar(self):
       if self._seguro:
          self._seguro = False
          print(f"{self.marca} {self.modelo} já está com o seguro cancelado. ")
       else:
          print(f"{self.marca} {self.modelo} está com o seguro cancelado! ")
###############################################
    def emplacar(self):
       if self.placa:
          self.placa = True
          print(f"{self.marca} {self.modelo} já está emplacado. ")
       else:
          print(f"{self.marca} {self.modelo} está emplacado! ")
###############################################
    def reboque_instal(self):
       if self._reboque:
          self._reboque = True
          print(f"{self.marca} {self.modelo} já está com o reboque instalado na parte traseira.")
       else:
          print(f"{self.marca} {self.modelo}  está com o reboque instalado na parte traseira!")
###############################################
    def reboque_desinstal(self):
       if self._reboque:
          self._reboque = False
          print(f"{self.marca} {self.modelo} já está com o reboque desinstalado. ")
       else:
          print(f"{self.marca} {self.modelo} está com o reboque desinstalado.")

meu_carro = Carro("Chevrolet", "Opala", "1995", "vermelho")

meu_carro.exibir_info()
meu_carro.info_cor()
meu_carro.seguro_contratado()
meu_carro.reboque_instal()
meu_carro.emplacar()
meu_carro.ligar()
meu_carro.reboque_desinstal()
meu_carro.seguro_cancelar()