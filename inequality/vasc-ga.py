# https://math.stackexchange.com/a/4692188

import pygad


def check(n):

    def fitness_func(ga_instance, solution, solution_idx):
        X = [abs(x) for x in solution]
        S = 0
        for i in range(n):
            if X[(i - 1)] + X[i] == 0:
                return -1
            S += (X[i] - X[(i + 1) % n]) / (X[(i - 1) % n] + X[i])

        return S

    fitness_function = fitness_func

    num_generations = 100
    num_parents_mating = 4

    sol_per_pop = 50
    num_genes = n

    init_range_low = 0
    init_range_high = 1

    parent_selection_type = "sss"
    keep_parents = 1

    crossover_type = "single_point"

    mutation_type = "random"
    mutation_percent_genes = "default"
    mutation_num_genes = 1

    for attempt in range(200):
        gene_type = [float] * n

        ga_instance = pygad.GA(num_generations=num_generations,
                               num_parents_mating=num_parents_mating,
                               fitness_func=fitness_function,
                               sol_per_pop=sol_per_pop,
                               num_genes=num_genes,
                               init_range_low=init_range_low,
                               init_range_high=init_range_high,
                               parent_selection_type=parent_selection_type,
                               keep_parents=keep_parents,
                               crossover_type=crossover_type,
                               mutation_type=mutation_type,
                               mutation_percent_genes=mutation_percent_genes,
                               mutation_num_genes=mutation_num_genes,
                               gene_type=gene_type)

        ga_instance.run()

        solution, solution_fitness, solution_idx = ga_instance.best_solution()

        if solution_fitness > 0:
            return [abs(x) for x in solution], solution_fitness

    return None, None


for n in range(3, 20):
    sol, fitness = check(n)
    if sol is None:
        print(f"{n}: counterexample not found")
    else:
        print(f"{n}: counterexample found: {sol}, {fitness}")