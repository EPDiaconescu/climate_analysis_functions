from pylab import plot, show, savefig, xlim, figure, \
                hold, ylim, legend, boxplot, setp, axes

def setBoxColors(bp):
    setp(bp['boxes'][0], color='blue',facecolor='blue')
    setp(bp['caps'][0], color='blue',linewidth=2)
    setp(bp['caps'][1], color='blue',linewidth=2)
    setp(bp['whiskers'][0], color='blue',linestyle='-', linewidth=2)
    setp(bp['whiskers'][1], color='blue',linestyle='-', linewidth=2)
    setp(bp['fliers'], marker='*',markersize=8, markerfacecolor='black')
#    setp(bp['fliers'][1], color='blue')
    setp(bp['medians'][0], color='white',linewidth=3)

    setp(bp['boxes'][1], color='red',facecolor='red')
    setp(bp['caps'][2], color='red',linewidth=2)
    setp(bp['caps'][3], color='red',linewidth=2)
    setp(bp['whiskers'][2], color='red',linestyle='-', linewidth=2)
    setp(bp['whiskers'][3], color='red',linestyle='-', linewidth=2)
    setp(bp['fliers'], marker='*',markersize=8, markerfacecolor='black')
#    setp(bp['fliers'][3], color='red')
    setp(bp['medians'][1], color='white',linewidth=3)

#Example : boxX=boxplot(dataH50, positions = [1.3, 1.7], patch_artist=True,widths = 0.3)
#          setBoxColors(boxX)