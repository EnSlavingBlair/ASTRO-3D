import matplotlib.pyplot as plt
import matplotlib.animation as animation
import time

def animate(i):
    # Code modified from internet
    # Set up the histgram parameters for the data from "histData.txt"
    pullData = open("histData.txt","r").read()
    dataArray = pullData.split('\n')
    numData = len(dataArray)
    xar = []
    for eachLine in dataArray:
        if eachLine != '':
            print(eachLine)
            x = float(eachLine)
            print(type(x))
            xar.append(x)
    ax1.clear()
    ax1.hist(xar, bins=[0,4,8,12,16,20,24,28,32,36,40,44,48,52,56,60,64,68,72,76,80], color = (0.375, 0.191, 0.570, 1), edgecolor = 'black', linewidth = 1.8)
    plt.gca().set_ylim([0,9])
    plt.title("Escape the Cosmic Microwave Background! \n Distribution of the Number of Rolls to Escape")
    plt.ylabel("Count")
    plt.xlabel("Number of Rolls to Escape")

# set size of text to a readable size
plt.rcParams.update({'font.size': 24})

# set up figure
fig = plt.figure()
# only one figure is requires
ax1 = fig.add_subplot(1,1,1)



# using the histogram parameters from function animate, allow the histogram to
# dynamically update as more data is added to the file "histData.txt"
ani = animation.FuncAnimation(fig, animate, interval=1000)
plt.show()
