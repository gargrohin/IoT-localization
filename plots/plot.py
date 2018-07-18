import matplotlib.pyplot as plt
import matplotlib.animation as animation
import time

fig = plt.figure()
ax1 = fig.add_subplot(1,2,1)
ax2 = fig.add_subplot(1,2,2)
def animate(i):
    datal = open("lfinal.txt","r").read()
    datar = open("rfinal.txt","r").read() 
    datalc = open("lfinalc.txt","r").read() 
    datarc = open("rfinalc.txt","r").read() 
    dataArrayl = datal.split('\n')
    dataArrayr = datar.split('\n')
    dataArraylc = datalc.split('\n')
    dataArrayrc = datarc.split('\n')
    xarl = []
    yarl = []
    xarr = []
    yarr = []
    xarlc = []
    yarlc = []
    xarrc = []
    yarrc = []
    #print len(dataArrayl)
    for eachLine in dataArrayl:
        if len(eachLine)>1:
            x,y = eachLine.split(' ')
            xarl.append(float(x))
            yarl.append(float(y))
    
    for eachLine in dataArrayr:
        if len(eachLine)>1:
            x,y = eachLine.split(' ')
            xarr.append(float(x))
            yarr.append(float(y))
    
    for eachLine in dataArraylc:
        if len(eachLine)>1:
            x,y = eachLine.split(' ')
            xarlc.append(float(x))
            yarlc.append(float(y))        
    
    for eachLine in dataArrayrc:
        if len(eachLine)>1:
            x,y = eachLine.split(' ')
            xarrc.append(float(x))
            yarrc.append(float(y))
    
    ax1.clear()
    ax1.plot(xarlc,yarlc)
    ax1.plot(xarl,yarl, color = 'r') 
    ax2.clear()
    ax2.plot(xarrc,yarrc)
    ax2.plot(xarr,yarr, color = 'r') 


ani = animation.FuncAnimation(fig, animate, interval=100)
plt.show()
