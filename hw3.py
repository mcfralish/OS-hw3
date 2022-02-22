"""Simulates k number of processes and generates a PID number, a random # of cycles <1000> - <11000> with a mean of 6000
as well as a random amount of memory <1KB> - <100KB> with a mean of 20KB. Numpy library used to facilitate renormalization of mean.
Writes to tuples.csv in same directory."""

import numpy as np
import csv


def generate(k):
    tuples = []
    PID_counter = 1000

    def gen_cycles():
        cycles = int(np.random.gamma(5, 2.0) * 500) + 1000

        # Truncates by wrapping
        if cycles < 1000:
            cycles = 11000 - cycles
        if cycles > 11000:
            cycles = cycles % 10000
            cycles += 1000

        return cycles

    def gen_mem():
        mem = int(np.random.gamma(2, 2.0) * 5)

        # Truncates by wrapping
        if mem < 1:
            mem = 100 - abs(mem)
        if mem > 100:
            mem = mem % 99
            mem += 1

        return mem

    for i in range(k):
        new_tuple = (PID_counter, gen_cycles(), gen_mem())
        tuples.append(new_tuple)
        PID_counter += 1

    return tuples


tuples = generate(100)
csum = 0
msum = 0
for tuple in tuples:
    csum += tuple[1]
    msum += tuple[2]

cmean = csum / len(tuples)
mmean = msum / len(tuples)

print(cmean, mmean)

f = open("./tuples.csv", "w")
w = csv.writer(f)

header = ["PID", "Cycles", "Memory in KB"]
w.writerow(header)
for i in range(len(tuples)):
    w.writerow(tuples[i])

f.close()
