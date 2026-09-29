import pygad
import numpy as np


def function(x, y):
    return 0.5 + (np.sin(x ** 2 - y ** 2) ** 2 - 0.5) / (1 + 0.001 * (x ** 2 + y ** 2)) ** 2

def fitness_func(ga_instance, solution, solution_idx):
    x, y = solution
    return - function(x , y)

selections = ["sss", "sss"]
mutations = ["random", "random"] #,
crossovers = ["two_points", "uniform"]
for selection, mutation, crossover in zip(selections, mutations, crossovers):
    print("=====================================", selection, mutation, crossover)
    for sol_per_pop in [10, 50, 100, 250]:
        print("++++++++++++++++++++++++++Нач популяция ", sol_per_pop)
        for coef in [1, 0.8, 0.6, 0.4, 0.2, 0]:
            print("mutation", coef, "cross", 1 - coef)
            ga_instance = pygad.GA(fitness_func = fitness_func,
                           num_generations=1000,
                           sol_per_pop = sol_per_pop,
                           num_genes = 2,
                           num_parents_mating = int(0.4 * sol_per_pop),
                           parent_selection_type = selection,
                           mutation_type = mutation,
                           crossover_type = crossover,
                           mutation_probability = coef,
                           crossover_probability = 1 - coef,
                           keep_parents = int(0.2 * sol_per_pop),
                           gene_space = [{'low': -50, 'high': 50}, {'low': -50, 'high': 50}],
                           stop_criteria="reach_0.05")

            ga_instance.run()

            solution, solution_fitness, solution_idx = ga_instance.best_solution()
            x_opt, y_opt = solution
            z_opt = function(x_opt , y_opt)

            print(f"Найденный минимум:")
            print(f"x = {x_opt:.6f}")
            print(f"y = {y_opt:.6f}")
            print(f"f(x,y) = {z_opt:.6f}")

    # Дополнительная информация
            print(f"It: {ga_instance.best_solution_generation}\n")

# # График сходимости
            ga_instance.plot_fitness(title="Сходимость генетического алгоритма")
