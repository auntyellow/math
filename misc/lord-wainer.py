from numpy import random
from matplotlib import pyplot

def main():
    # The Book of Why, Figure 6.9
    wiAB, wfAB, cAB, wiA, wfA, wiB, wfB = [], [], [], [], [], [], []
    for i in range(1000):
        wi = random.normal(50, 10)
        wf = wi + random.normal(0, 5)
        wiAB.append(wi)
        wfAB.append(wf)
        if wi + wf + random.normal(0, 5) > 100: # A/B causes W_F
        # if wi + random.normal(0, 5) > 50: # A/B doesn't cause W_F
            cAB.append('red')
            wiA.append(wi)
            wfA.append(wf)
        else:
            cAB.append('blue')
            wiB.append(wi)
            wfB.append(wf)
    pyplot.xlim(20, 80)
    pyplot.ylim(20, 80)
    pyplot.scatter(wiAB, wfAB, c = cAB, s = 0.5, marker = '.')
    pyplot.show()
    pyplot.xlim(20, 80)
    pyplot.ylim(20, 80)
    pyplot.scatter(wiA, wfA, c = 'red', s = 0.5, marker = '.')
    pyplot.show()
    pyplot.xlim(20, 80)
    pyplot.ylim(20, 80)
    pyplot.scatter(wiB, wfB, c = 'blue', s = 0.5, marker = '.')
    pyplot.show()

if __name__ == '__main__':
    main()