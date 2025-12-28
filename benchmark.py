import time
import csv
from greedy.iterative import greedy_iterative
from greedy.recursive import greedy_recursive

COINS = [1000, 500, 200, 100]

with open("runtime_greedy.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["N", "Iteratif", "Rekursif"])

    for N in range(100, 1100, 100):
        start = time.perf_counter()
        greedy_iterative(N, COINS)
        t_iter = time.perf_counter() - start

        start = time.perf_counter()
        greedy_recursive(N, COINS)
        t_rek = time.perf_counter() - start

        writer.writerow([N, t_iter, t_rek])
