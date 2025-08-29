##
# Classificar carro por meio da placa
##
colecao = {}

class Carros:
    def __init__(self, marca, modelo, ano, cor, placa):
        self.marca = marca      
        self.modelo = modelo    
        self.ano = ano 
        self.cor = cor
        self.placa = placa
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

        print (f"{self.marca} - {self.modelo} - {self.cor} - {self.placa} está {status} ")
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
          print(f"{self.marca} {self.modelo} já está emplacado com {self.placa}. ")
       else:
          print(f"{self.marca} {self.modelo} está emplacado com {self.placa}! ")
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

meu_carro = Carros("Chevrolet", "Opala", "1995", "vermelho", "KFC123")
meu_carro2 = Carros("Volkswagen", "Beetle", "1970", "azul", "MDB456")
meu_carro3 = Carros("Jeep", "Renegade", "2015", "verde", "MDC789")

colecao["KFC123"] = [meu_carro]
colecao["MDB456"] = [meu_carro2]
colecao["MDC789"] = [meu_carro3]