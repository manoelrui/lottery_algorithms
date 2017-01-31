import csv
import numpy as np


class Sorteio(object):
	def __init__(self,id,premio,n1,n2,n3,n4,n5,n6):
		self.id = id
		self.premio = premio
		self.numeros = np.array([n1,n2,n3,n4,n5,n6])

	def comparar(self,aposta):
		iguais = 0
		for n in aposta:
			if n in self.numeros:
				iguais += 1
		return iguais
		
def carregar_sorteios(file):
	with open(file, 'r') as csvfile:
		reader = csv.reader(csvfile,quotechar="'")
		sorteios = [Sorteio(int(row[0]),float(row[8].replace('.','').replace(',','.')),*[int(row[i]) for i in range(2,8)]) for row in reader]
		return sorteios
		
def gerar_data_sets(sorteios):
	for i in range(1,len(sorteios)):
		yield sorteios[:i],sorteios[i]

def jogar(sorteios, funcao_jogo):
	sorteios_ganhos_6 = 0
	sorteios_ganhos_5 = 0
	sorteios_ganhos_4 = 0
	for historico,atual in gerar_data_sets(sorteios):
		if atual.comparar(funcao_jogo(historico)) == 6:
			sorteios_ganhos_6 +=1
		elif atual.comparar(funcao_jogo(historico)) == 5:
			sorteios_ganhos_5 +=1
		elif atual.comparar(funcao_jogo(historico)) == 4:
			sorteios_ganhos_4 +=1
	print 'Sorteios ganhos 4: %s' % sorteios_ganhos_4
	print 'Sorteios ganhos 5: %s' % sorteios_ganhos_5
	print 'Sorteios ganhos 6: %s' % sorteios_ganhos_6
