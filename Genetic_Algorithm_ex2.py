import random
import string

target = "AI"

def fitness(word):
    score = 0
    for i in range(len(word)):
        if word[i] == target[i]:
            score += 1
    return score

# initial population
population = [''.join(random.choice(string.ascii_uppercase) for _ in range(2)) for _ in range(6)]

for generation in range(10):

    population = sorted(population, key=fitness, reverse=True)

    print("Generation", generation, ":", population)

    if population[0] == target:
        print("Target found!")
        break

    parent1 = population[0]
    parent2 = population[1]

    # crossover
    child = parent1[0] + parent2[1]

    # mutation
    if random.random() < 0.2:
        child = random.choice(string.ascii_uppercase) + child[1]

    population[-1] = child