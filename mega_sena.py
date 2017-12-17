from mega_sena_engine import *


def random(historico):
	todos = np.arange(60)+1
	np.random.shuffle(todos)
	return todos[:6]

def fixo(historico):
	return np.array([39,9,37,49,43,41])


def most_frequent(historic):
    freq = [[i, 0] for i in range(1, MAX_UNIT_NUMBER + 1)]
    for lottery_draw in historic:
        for number in lottery_draw.numeros:
            for counter in freq:
                if counter[0] == number:
                    counter[1] += 1

    sorted_by_freq = sorted(freq, key=lambda tup: tup[1], reverse=True)
    return np.array([sorted_by_freq[i][0] for i in range(0, MAX_GUESS_NUMBERS)])



sorteios = carregar_sorteios('sena_parsed.csv')
jogar(sorteios,most_frequent)