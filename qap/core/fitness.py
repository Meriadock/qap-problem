import numpy as np

def getFitness(distance_matrix,flow_matrix,solution):
    problem_size = len(solution)
    normalized_solution = list(map(lambda x: x-1, solution))
    fitness_value = .0
    for i in range(problem_size):
        for j in range(problem_size):
            fitness_value += distance_matrix[i][j] * flow_matrix[normalized_solution[i]][normalized_solution[j]]
    return fitness_value


print("hello")