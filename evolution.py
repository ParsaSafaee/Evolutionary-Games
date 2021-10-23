import copy
import random

from player import Player
import numpy as np
from config import CONFIG


class Evolution:

    def __init__(self, mode):
        self.mode = mode

    # calculate fitness of players
    def calculate_fitness(self, players, delta_xs):
        for i, p in enumerate(players):
            p.fitness = delta_xs[i]

    def mutate(self, child):
        rp = 0.5
        probability1 = random.random()
        probability2 = random.random()
        probability3 = random.random()
        probability4 = random.random()
        if probability1 <= rp:
            child.nn.W_L1 += np.random.normal(loc=0, scale=0.5, size=child.nn.W_L1.shape)
        if probability2 <= rp:
            child.nn.B_L1 += np.random.normal(loc=0, scale=0.5, size=child.nn.B_L1.shape)
        if probability3 <= rp:
            child.nn.W_L2 += np.random.normal(loc=0, scale=0.5, size=child.nn.W_L2.shape)
        if probability4 <= rp:
            child.nn.B_L2 += np.random.normal(loc=0, scale=0.5, size=child.nn.B_L2.shape)

    def generate_new_population(self, num_players, prev_players=None):

        # in first generation, we create random players
        if prev_players is None:
            return [Player(self.mode) for _ in range(num_players)]

        else:

            # TODO
            # num_players example: 150
            # prev_players: an array of `Player` objects
            # TODO (additional): a selection method other than `fitness proportionate`
            # TODO (additional): implementing crossover
            prev_players.sort(key=lambda x: x.fitness, reverse=True)
            # print(len(prev_players), "p")
            new_players = []
            for i in range(0, 10):
                for j in range(15):
                    child = copy.deepcopy(prev_players[i])
                    self.mutate(child)
                    new_players.append(child)
            '''for i in range(int(150 / 2)):
                for j in range(2):
                    new_player = copy.deepcopy(prev_players[i])
                    new_player.nn.W1 = (prev_players[i].nn.W1 + prev_players[i + j + 1].nn.W1) / 2
                    new_player.nn.W2 = (prev_players[i].nn.W2 + prev_players[i + j + 1].nn.W2) / 2
                    new_player.nn.B1 = (prev_players[i].nn.B1 + prev_players[i + j + 1].nn.B1) / 2
                    new_player.nn.B2 = (prev_players[i].nn.B2 + prev_players[i + j + 1].nn.B2) / 2
                    self.mutate(new_player)
                    new_players.append(new_player)
            '''
            # print(len(new_players), "n")
            return new_players

    def next_population_selection(self, players, num_players):
        l = len(players)
        players.sort(key=lambda x: x.fitness, reverse=True)
        sum = 0
        for item in players:
            sum += item.fitness
        avg = sum / len(players)
        max = players[0].fitness
        min = players[-1].fitness
        next_generation = [copy.deepcopy(players[0])]
        for i in range(num_players - 1):
            rand_param = random.random()
            index = int(((4 * l * (l + 1) * rand_param + 1) ** 0.5 - 1) / 2)
            next_generation.append(copy.deepcopy(players[num_players - index - 1]))

        return next_generation
