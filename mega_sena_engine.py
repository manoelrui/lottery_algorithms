import csv
import numpy as np

MAX_GUESS_NUMBERS = 6

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
    guesses_counter_list = [0 for i in range(0, MAX_GUESS_NUMBERS + 1)]

    for historico, atual in gerar_data_sets(sorteios):
        guesses_counter_list[atual.comparar(funcao_jogo(historico))] += 1

    for i in reversed(range(1, MAX_GUESS_NUMBERS + 1)):
        print 'Wins with %d guesses: %d/%d | Probability: %.2f%%' % (i,
                                                                guesses_counter_list[i],
                                                                len(sorteios) - 1,
                                                                100.0 * float(guesses_counter_list[i]) / float(len(sorteios) - 1)
                                                                )
