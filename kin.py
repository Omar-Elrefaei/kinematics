from math import sqrt

import argparse
import numpy as np
import matplotlib.pyplot as plt

parser = argparse.ArgumentParser()

parser.add_argument("-a",
                    help="Acceleration is required",
                    type=float,
                    required=True)
parser.add_argument("-x", help="Displacement is optional", type=float)
parser.add_argument("-vi", help="Initial velocity is optional", type=float)
parser.add_argument("-vf", help="Velocity is optional", type=float)
parser.add_argument("-t", help="Time is optional", type=float)
parser.add_argument(
    "--plot",
    help="Plot the Graphs of the Displacement & Velocity against time",
    action="store_true")

args = parser.parse_args()

a = args.a
x = args.x
t = args.t
v = args.vf
iv = args.vi


def eq1():
    v = iv + a * t
    return v


def eq2():
    x = (iv * t) + (0.5 * a * t**2)
    return x


def eq3():
    t = (v - iv) / a
    return t


def eq4():
    v = sqrt(iv**2 + 2 * a * x)
    return v


def eq5():
    iv = (x - 0.5 * a * t**2) / t
    return iv


def eq6():
    iv = sqrt(v**2 - 2 * a * x)
    return iv


def eq7():
    iv = v - a * t
    return iv


if iv and v:
    t = eq3()
    x = eq2()
elif iv and t:
    v = eq1()
    x = eq2()
elif iv and x:
    v = eq4()
    t = eq3()
elif x and t:
    iv = eq5()
    v = eq1()
elif v and x:
    iv = eq6()
    t = eq3()
elif v and t:
    iv = eq7()
    x = eq2()
else:
    print("User input is not satisfactory")
    exit()

# Plotting
if args.plot is True:
    dispValues = []
    veloValues = []
    timeValues = np.linspace(0, t, 10)

    for i in timeValues:
        t = i
        v = eq1()
        x = eq2()
        veloValues.append(v)
        dispValues.append(x)

    plt.figure("Displacement vs Time")
    plt.plot(timeValues, dispValues)
    plt.ylabel("Displacement")
    plt.xlabel("Time")
    plt.grid(True)

    plt.figure("Velocity vs Time")
    plt.plot(timeValues, veloValues, "r")
    plt.ylabel("Velocity")
    plt.xlabel("Time")
    plt.grid(True)

    plt.figure("Displacement vs Time")
    plt.show(block=False)
    plt.figure("Velocity vs Time")
    plt.show()

else:
    t = round(t, 3)
    x = round(x, 3)
    v = round(v, 3)
    a = round(a, 3)
    iv = round(iv, 3)

    # Printing
    string = ""
    spacing = 18
    vars = [a, iv, v, x, t]
    names = ["Acceleration", "Initial Velocity",
             "Final Velocity", "Displacement", "Time"]

    def myprint(name, var):
        return("\n" + name + "\t=\t" + str(var))

    print(''.join(list(map(myprint, names, vars))).expandtabs(spacing))
