from mega_sena_engine import *
from random import shuffle

def random(historic, guesses_number):
	todos = np.arange(60)+1
	np.random.shuffle(todos)
	return todos[:6]

def most_frequent(historic, guesses_number):
    freq = [[i, 0] for i in range(1, MAX_UNIT_NUMBER + 1)]
    for lottery_draw in historic:
        for number in lottery_draw.numeros:
            for counter in freq:
                if counter[0] == number:
                    counter[1] += 1

    sorted_by_freq = sorted(freq, key=lambda tup: tup[1], reverse=True)
    return np.array([sorted_by_freq[i][0] for i in range(0, guesses_number)])

def less_frequent(historic, guesses_number):
    freq = [[i, 0] for i in range(1, MAX_UNIT_NUMBER + 1)]
    for lottery_draw in historic:
        for number in lottery_draw.numeros:
            for counter in freq:
                if counter[0] == number:
                    counter[1] += 1

    sorted_by_freq = sorted(freq, key=lambda tup: tup[1])
    return np.array([sorted_by_freq[i][0] for i in range(0, guesses_number)])

def most_and_less_frequent(historic, guesses_number):
    freq = [[i, 0] for i in range(1, MAX_UNIT_NUMBER + 1)]
    for lottery_draw in historic:
        for number in lottery_draw.numeros:
            for counter in freq:
                if counter[0] == number:
                    counter[1] += 1

    guess_list = sorted(freq, key=lambda tup: tup[1], reverse=True)
    guess_list = guess_list[0:guesses_number] + guess_list[-guesses_number:]
    shuffle(guess_list)

    return np.array([guess_list[i][0] for i in range(0, guesses_number)])

sorteios = carregar_sorteios('sena_parsed.csv')
algorithm_list = [random, most_frequent, less_frequent, most_and_less_frequent]

for f in algorithm_list:
    print "Algorithm: %s" % f.__name__
    simulate(sorteios, f)
    print ""