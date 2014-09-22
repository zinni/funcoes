#coding:utf-8
from unittest import TestCase
from funcoes import Funcoes

class FuncoesTest(TestCase):

    def test_funcao_tamanho(self):
        obj=Funcoes('hello world')
        esperado = 11
        resposta = obj.tamanho()
        self.assertEqual(resposta, esperado)
        
    def test_funcao_remove_espacos_em_branco(self):
        obj=Funcoes('hello world')
        esperado = 'helloworld'
        resposta = obj.remove_whitespaces()
        self.assertEqual(resposta, esperado)
    
    def test_funcao_centro_menor(self):
        obj=Funcoes('hello')
        esperado = ('hello')
        resposta = obj.centro(5)
        self.assertEqual(resposta, esperado)

    def test_funcao_centro_maior_par(self):
        obj=Funcoes('hello')
        esperado = ('  hello   ')
        resposta = obj.centro(10)
        self.assertEqual(resposta, esperado)

    def test_funcao_centro_maior_impar(self):
        obj=Funcoes('hello')
        esperado = ('  hello  ')
        resposta = obj.centro(9)
        self.assertEqual(resposta, esperado)

    def test_funcao_achar_uma_variavel(self):
        obj=Funcoes('hello world')
        esperado = 6
        resposta = obj.achar('w')
        self.assertEqual(resposta, esperado)

    def test_funcao_achar_tres_variaveis(self):
        obj=Funcoes('welcome to jamaica have a nice day')
        esperado = 15
        resposta = obj.achar('ica')
        self.assertEqual(resposta,esperado)

    def test_funcao_terminacom_verdadeira(self):
        obj=Funcoes('welcome to jamaica have a niec day')
        esperado = True
        resposta = obj.terminacom('day')
        self.assertEqual(resposta, esperado)

    def test_funcao_terminacom_falsa(self):
        obj=Funcoes('Hellow World')
        esperado = False
        resposta = obj.terminacom('day')
        self.assertEqual(resposta, esperado)

    def test_funcao_comecacom_verdadeira(self):
        obj=Funcoes('hello world')
        esperado = True
        resposta = obj.comecacom('hell')
        self.assertEqual(resposta, esperado)

    def test_funcao_comecacom(self):
        obj=Funcoes('hello world')
        esperado = False
        resposta = obj.comecacom('nada')
        self.assertEqual(resposta, esperado)

    def test_funcao_maiusculo(self):
        obj=Funcoes('hello world @#$%')
        esperado = 'HELLO WORLD @#$%'
        resposta = obj.maiusculo()
        self.assertEqual(resposta, esperado)

    def test_funcao_maiusculo_alternado(self):
        obj=Funcoes('heLLo WorlD @#$%')
        esperado = 'HELLO WORLD @#$%'
        resposta = obj.maiusculo()
        self.assertEqual(resposta, esperado)

    def test_indice(self):
        obj=Funcoes('hello world')
        esperado = 6
        resposta = obj.indice('w')
        self.assertEqual(resposta, esperado)

    def test_indice_falho(self):
        obj=Funcoes('hello world')
        esperado = -1
        resposta = obj.indice('a')
        self.assertEqual(resposta, esperado)

    def test_minusculo_simples(self):
        obj=Funcoes('HELLO WORLD AAA')
        esperado = 'hello world aaa'
        resposta = obj.minusculo()
        self.assertEqual(resposta, esperado)

    def test_minusculo_alternado(self):
        obj=Funcoes('AleLUia WOrlD @#$%')
        esperado = 'aleluia world @#$%'
        resposta = obj.minusculo()
        self.assertEqual(resposta, esperado)

    def test_juntar_simples(self):
        obj=Funcoes(['hello','world','aaa'])
        esperado = 'hello world aaa'
        resposta = obj.juntar(' ')
        self.assertEqual(resposta, esperado)

    def test_juntar_composto(self):
        obj=Funcoes(['hello','world','aaa'])
        esperado = 'hellomaxworldmaxaaa'
        resposta = obj.juntar('max')
        self.assertEqual(resposta, esperado)

    def test_juntar_vazio(self):
        obj=Funcoes()
        esperado = ''
        resposta = obj.juntar()
        self.assertEqual(esperado, resposta)

    def test_contar_simples(self):
        obj=Funcoes('hello world')
        esperado = 3
        resposta = obj.contar('l')
        self.assertEqual(resposta, esperado)

    def test_contar_string(self):
        obj=Funcoes('hello hello hello world')
        esperado = 3
        resposta = obj.contar('ll')
        self.assertEqual(resposta, esperado)

    def test_contar_string_maior(self):
        obj=Funcoes('aaaa max max aamaxaa maxmaaamax')
        esperado = 5
        resposta = obj.contar('max')
        self.assertEqual(resposta, esperado)
