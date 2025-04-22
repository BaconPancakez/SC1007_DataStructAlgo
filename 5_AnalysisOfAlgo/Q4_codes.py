import time
import itertools
import matplotlib.pyplot as plt


def calculate_total_distance(route, distance_matrix):
    total_distance = 0
    for i in range(len(route) - 1):
        total_distance += distance_matrix[route[i]][route[i + 1]]
    total_distance += distance_matrix[route[-1]][route[0]]  # Return to starting point
    return total_distance


def brute_force_tsp(distance_matrix):
    n = len(distance_matrix)
    locations = list(range(n))
    min_distance = float('inf')
    best_route = None

    for perm in itertools.permutations(locations[1:]):  # Fix warehouse (index 0) as the start
        route = [0] + list(perm)
        total_distance = calculate_total_distance(route, distance_matrix)
        if total_distance < min_distance:
            min_distance = total_distance
            best_route = route

    return min_distance, best_route


def measure_time(func, distance_matrix):
    start_time = time.time()
    min_distance, best_route = func(distance_matrix)
    exec_time = time.time() - start_time
    return exec_time, min_distance, best_route


def read_input(filename):
    with open(filename, 'r') as f:
        lines = [line.strip() for line in f.readlines() if line.strip()]

    scenarios = []
    i = 0
    while i < len(lines):
        n = int(lines[i])  # Number of locations
        i += 1
        matrix = []
        for _ in range(n):
            matrix.append(list(map(int, lines[i].split())))
            i += 1
        scenarios.append(matrix)

    return scenarios


# Read input from file
input_file = "q4input.txt"
distance_matrices = read_input(input_file)

execution_times = []
n_values = []

for i, distance_matrix in enumerate(distance_matrices):
    n = len(distance_matrix)
    exec_time, min_distance, best_route = measure_time(brute_force_tsp, distance_matrix)
    execution_times.append(exec_time)
    n_values.append(n)
    print(f"Scenario {i + 1} with {n} locations:")
    print(f"  Shortest Distance: {min_distance}")
    print(f"  Best Route: {best_route}")
    print(f"  Execution Time: {exec_time:.5f} sec\n")

plt.plot(n_values, execution_times, marker='o', label='Brute Force TSP')
plt.xlabel('Number of Locations')
plt.ylabel('Execution Time (seconds)')
plt.title('Execution Time of Brute Force TSP')
plt.legend()
plt.grid()
plt.show()
