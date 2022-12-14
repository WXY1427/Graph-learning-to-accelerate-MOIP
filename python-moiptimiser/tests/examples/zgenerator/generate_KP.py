#!/usr/bin/env python3
import sys
import random


def KP_rand(mean, stdev):
    #return random.randint(mean - 2*stdev, mean + 2*stdev)
    return random.randint(1, 101)

if len(sys.argv) != 4:
    print("Usage: %s <lp-file> <num-vars> <num-objectives>" % (sys.argv[0]))
    sys.exit(-1)

n = int(sys.argv[2])
nObjectives = int(sys.argv[3])
with open(sys.argv[1], "w") as lpfile:
    #lpfile.write("Maximize 0\ns.t.\n")
    lpfile.write("Maximize multi-objectives\n")

    for k in range(nObjectives):
        first = True
        lpfile.write("OBJ%d: Priority=%d Weight=1 AbsTol=0 RelTol=0\n" % (k+1, nObjectives-k))
        for j in range(n):
            if not first:
                lpfile.write(" + ")
            lpfile.write("%5d X%d\n" % (KP_rand(80, 10), j+1))
            first = False
        #lpfile.write("> %d\n" % (k+1))

    lpfile.write("\ns.t.\n")

    total_weight = KP_rand(80, 10)
    lpfile.write("%5d X%d\n" % (total_weight, 1))
    for k in range(n-1):
        next_weight = KP_rand(80, 10)
        total_weight += next_weight
        lpfile.write(" + %5d X%d\n" % (next_weight, k+2))
    lpfile.write("< %f\n" % (round(total_weight/2, 1)))


    lpfile.write("BINARY\n")
    for k in range(n):
        lpfile.write("X%d\n" % (k+1))
    lpfile.write("END\n")
