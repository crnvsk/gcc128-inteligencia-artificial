import random

# Parâmetros variáveis
POP_SIZE = 4 # ~30
MUTATION_RATE = 0.01
CROSSOVER_RATE = 0.7
NUM_GENERATIONS = 5 # ~20
BIT_LENGTH = 5 # [-10, 10]

# Função para decodificar o vetor binário para inteiro no intervalo [-10, 10]
def decode(individual):
    value = int("".join(str(bit) for bit in individual), 2)

    mapped = value - 10
    return max(-10, min(10, mapped))

# Função de fitness
def fitness(x):
    return x**2 - 3*x + 4

# Gerar indivíduo aleatório
def random_individual():
    return [random.randint(0, 1) for _ in range(BIT_LENGTH)]

# Seleção por torneio
def tournament_selection(population, fitnesses):
    i1, i2 = random.sample(range(len(population)), 2)
    return population[i1] if fitnesses[i1] > fitnesses[i2] else population[i2]

# Crossover de um ponto
def crossover(parent1, parent2):
    if random.random() < CROSSOVER_RATE:
        point = random.randint(1, BIT_LENGTH - 1)
        return parent1[:point] + parent2[point:], parent2[:point] + parent1[point:]
    return parent1[:], parent2[:]

# Mutação
def mutate(individual):
    return [bit if random.random() > MUTATION_RATE else 1 - bit for bit in individual]

# Algoritmo Genético Principal
def genetic_algorithm():

    population = [random_individual() for _ in range(POP_SIZE)]

    for generation in range(NUM_GENERATIONS):

        decoded = [decode(ind) for ind in population]
        fitnesses = [fitness(x) for x in decoded]

        new_population = []
        while len(new_population) < POP_SIZE:

            parent1 = tournament_selection(population, fitnesses)
            parent2 = tournament_selection(population, fitnesses)

            offspring1, offspring2 = crossover(parent1, parent2)

            offspring1 = mutate(offspring1)
            offspring2 = mutate(offspring2)
            new_population.extend([offspring1, offspring2])

        population = new_population[:POP_SIZE]

        best_idx = fitnesses.index(max(fitnesses))
        print(f"Geração {generation+1}: Melhor x = {decoded[best_idx]}, Fitness = {fitnesses[best_idx]}")

    decoded = [decode(ind) for ind in population]
    fitnesses = [fitness(x) for x in decoded]
    best_idx = fitnesses.index(max(fitnesses))
    print(f"\nMelhor solução encontrada: x = {decoded[best_idx]}, Fitness = {fitnesses[best_idx]}")

if __name__ == "__main__":
    genetic_algorithm()