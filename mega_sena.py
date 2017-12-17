from mega_sena_engine import *
from random import shuffle
import abc


class PredictiveModel(object):
    def __init__(self):
        self.histogram = [[i, 0] for i in range(1, MAX_UNIT_NUMBER + 1)]

    def updateHistogram(self, lottery_draw):
        for number in lottery_draw.numeros:
            self.histogram[number - 1][1] += 1

    @abc.abstractmethod
    def run(self, historic, guesses_number):
        return np.array([i for i in range(1, MIN_GUESS_NUMBERS + 1)])


class RandomPred(PredictiveModel):
    def run(self, historic, guesses_number):
        all_numbers = np.arange(MAX_UNIT_NUMBER) + 1
        np.random.shuffle(all_numbers)
        return np.array(all_numbers[:MIN_GUESS_NUMBERS])


class MostFrequentPred(PredictiveModel):
    def run(self, historic, guesses_number):
        self.updateHistogram(historic[-1])
        sorted_by_freq = sorted(self.histogram, key=lambda tup: tup[1], reverse=True)
        return np.array([sorted_by_freq[i][0] for i in range(0, guesses_number)])


class LessFrequentPred(PredictiveModel):
    def run(self, historic, guesses_number):
        self.updateHistogram(historic[-1])
        sorted_by_freq = sorted(self.histogram, key=lambda tup: tup[1])
        return np.array([sorted_by_freq[i][0] for i in range(0, guesses_number)])


class MostAndLessFrequentPred(PredictiveModel):
    def run(self, historic, guesses_number):
        self.updateHistogram(historic[-1])
        guess_list = sorted(self.histogram, key=lambda tup: tup[1], reverse=True)
        guess_list = guess_list[0:guesses_number] + guess_list[-guesses_number:]
        shuffle(guess_list)

        return np.array([guess_list[i][0] for i in range(0, guesses_number)])


sorteios = carregar_sorteios('sena_parsed.csv')
algorithm_list = [RandomPred(), MostFrequentPred(), LessFrequentPred(), MostAndLessFrequentPred()]

for prediction in algorithm_list:
    print "Algorithm: %s" % prediction.__class__.__name__
    simulate(sorteios, prediction)
    print ""