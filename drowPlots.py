import matplotlib.pyplot as plt, sys
import matplotlib
matplotlib.use('TkAgg')

def plotting(steps, results, algName):
    x = [i for i in range(1, steps+1)]
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    ax.plot(x, results, '-o', color="blue", label=f"{algName}: average execution time (ns)")
    ax.legend()
    return fig

if __name__== "__main__":
   plotting(int(sys.argv[1]), int(sys.argv[2]), int(sys.argv(3)))