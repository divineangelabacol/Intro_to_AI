import random

# Initial population
population = [random.randint(1, 10) for _ in range(6)]

def fitness(x):
    return x * x

for generation in range(5):

    # Sort population based on fitness
    population = sorted(population, key=fitness, reverse=True)

    print("Generation", generation, ":", population)

    # Select best parents
    parent1 = population[0]
    parent2 = population[1]

    # Crossover
    child = (parent1 + parent2) // 2

    # Mutation
    if random.random() < 0.3:
        child = child + random.randint(-1,1)

    population[-1] = child