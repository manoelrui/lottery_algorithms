from mega_sena_engine import *

def random(historico):
	todos = np.arange(60)+1
	np.random.shuffle(todos)
	return todos[:6]

def fixo(historico):
	return np.array([39,9,37,49,43,41])

sorteios = carregar_sorteios('sena_parsed.csv')
jogar(sorteios,fixo)