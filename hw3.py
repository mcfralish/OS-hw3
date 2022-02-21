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
        nparr = np.random.normal()
        return

    def gen_mem():
        return



    for i in range(k):
        new_tuple = (gen_PID(), gen_cycles(), gen_mem())
        tuples.append(new_tuple)

    return tuples