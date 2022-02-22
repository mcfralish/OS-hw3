# pyright: reportMissingImports=false,
import numpy as np
import csv


def generate(k):
    tuples = []
    PID_counter = 1000

    def gen_cycles():
        cycles = int(np.random.gamma(5, 2.0) * 500) + 1000

        # Hard truncates at min/max
        if cycles < 1000:
            cycles = 1000
        if cycles > 11000:
            cycles = 11000

        return cycles
        

    def gen_mem():
        mem = int(np.random.gamma(2, 2.0) * 5)
        
        # Hard truncates at min/max
        if mem < 0:
            mem = 0
        if mem > 100:
            mem = 100

        return mem


    for i in range(k):
        new_tuple = (PID_counter, gen_cycles(), gen_mem())
        tuples.append(new_tuple)
        PID_counter += 1

    return tuples

tuples = generate(100)

f = open('./tuples.csv', 'w')
w = csv.writer(f)

header = ['PID', 'Cycles', 'Memory in KB']
w.writerow(header)
for i in range(len(tuples)):
    w.writerow(tuples[i])

f.close()
