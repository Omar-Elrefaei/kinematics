import argparse
from math import sqrt
import matplotlib.pyplot as plt

parser = argparse.ArgumentParser()

parser.add_argument('-a'        , help='Acceleration is required'       ,type=float   ,required=True)
parser.add_argument('-x'        , help='Displacement is optional'       ,type=float)
parser.add_argument('-iv'       , help='Initial velocity is optional'   ,type=float)
parser.add_argument('-v'        , help='Velocity is optional'           ,type=float)
parser.add_argument('-t'        , help='Time is optional'               ,type=float)
parser.add_argument('--plot' 
    , help='Plot the Graphs of the Displacement & Velocity against time', action="store_true")

args = parser.parse_args()

a = args.a
x = args.x
t = args.t
v = args.v
iv = args.iv

def eq1():
    v = iv + a * t
    return v


def eq2():
    x = iv * t + 0.5 * a * t**2
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


if (iv or v) != None :
    t = eq3()
    x = eq2()
elif (iv or t) != None :
    v = eq1()
    x = eq2()
elif (iv or x) != None :
    v = eq4()
    t = eq3()
elif (x or t) != None :
    iv = eq5()
    v = eq1()
elif (v or x) != None :
    iv = eq6()
    t = eq3()
elif (v or t) != None :
    iv = eq7()
    x = eq2()
else:
    print("User input is not satisfying")
    exit()

if args.plot == True :
    timeValues = []
    dispValues = []
    veloValues = []

    for i in range(40):
        timeValues.append(i * 5)
        t = timeValues[i]
        v = eq1()
        x = eq2()
        veloValues.append(v)
        dispValues.append(x)

    plt.figure('Displacement vs Time')
    plt.plot(timeValues, dispValues)
    plt.ylabel('Displacement')
    plt.xlabel('Time')
    
    plt.figure('Velocity vs Time')
    plt.plot(timeValues, veloValues, 'r')
    plt.ylabel('Velocity')
    plt.xlabel('Time')

    plt.figure('Displacement vs Time')
    plt.show(block=False)
    plt.figure('Velocity vs Time')
    plt.show()

else:
    t = round(t, 3)
    x = round(x, 3)
    v = round(v, 3)
    a = round(a, 3)
    iv = round(iv, 3)

    print ("\nAcceleration = ", a,
           "\nInitial Velocity = ", iv,
           "\nFinal Velocity = ", v,
           "\nDisplacement = ", x,
           "\nTime = ", t, "\n")
