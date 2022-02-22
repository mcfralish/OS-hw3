import random
import numpy as np

def generate(k):
    tuples = []
    PID_counter = 1000

    def gen_PID():
        PID = PID_counter
        PID_counter += 1
        return PID

    def gen_cycles():
        nparr = np.random.normal(loc = .5, size = 1)
        return abs(Integer(nparr[0] * 10000 + 1000))

    def gen_mem():
        nparr = np.random.normal(loc = .2, size = 1)
        return Integer(nparr[0] * )



    for i in range(k):
        new_tuple = (gen_PID(), gen_cycles(), gen_mem())
        tuples.append(new_tuple)

    return tuples

print(generate(100))