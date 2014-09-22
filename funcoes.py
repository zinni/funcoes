class Funcoes(object):


    def __init__(self, conjunto = ''):
        self.upper = 'ABCDEFGHIJKLMNOPQRSTUVXYWZ'
        self.lower = 'abcdefghijklmnopqrstuvxywz'
        self.conjunto = conjunto

    def tamanho(self):
        contador = 0
        for x in self.conjunto:
            contador += 1
        return contador

    def remove_whitespaces(self):
        saida = ''
        for x in self.conjunto:
            if x != ' ':
                saida = saida+x
        return saida

    def centro(self, quantidade):
        espaco_total = quantidade - self.tamanho()
        espaco_frente = espaco_total / 2
        espaco_atras = 0
        saida = ''
        if espaco_total <= 0:
            espaco_atras = 0
            espaco_frente = 0
        elif espaco_total % 2 != 0:
            espaco_atras = espaco_frente + 1
        else:
            espaco_atras = espaco_frente
        saida =  ' '*espaco_frente+self.conjunto+' '*espaco_atras
        return saida

    def achar(self, parametro):
        for x in self.conjunto:
            contador = 0
            while x != parametro[:1]:
                contador += 1
                if parametro == self.conjunto[contador:(contador+len(parametro))]:
                    break
            return contador
        
    def terminacom(self, parametro):
        a = len(self.conjunto)
        b = len(parametro)
        if self.conjunto[a-b:] == parametro:
            return True
        else:
            return False

    def comecacom(self, parametro):
        b = len(parametro)
        if self.conjunto[:b] == parametro:
            return True
        else:
            return False

    def maiusculo(self):
        saida = ''
        for x in self.conjunto:
            if x in self.lower: 
                contador = 0
                for y in self.lower:
                    contador += 1
                    if x == y:
                        saida = saida + self.upper[contador - 1]
            else:
                saida+=x
        return saida

    def indice(self, parametro, conjunto = None):
        conjunto = conjunto or self.conjunto
        contador = 0
        for x in conjunto:
            if x == parametro:
                return contador
            contador += 1
        return -1

    def minusculo(self):
        saida=''
        for x in self.conjunto:
            indice_de_x = self.indice(x, conjunto=self.upper)
            if indice_de_x == -1:
                saida += x
            else:
                saida += self.lower[indice_de_x]

        return saida

    def juntar(self, string=''):
        saida = ''
        for x in self.conjunto:
            saida = saida+x+string    
        return saida[:-(len(string))]

    def contar(self, string):
        contador=0
        localizador=0
        for x in self.conjunto:
            if x != string[:1]:
                localizador += 1
            if string == self.conjunto[localizador:(localizador+len(string))]:
                contador += 1
                localizador += 1
        return contador
