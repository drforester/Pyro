'''
The Cell Players:
    0 : Empty
    1 : Defender
    2 : Mine
    3 : Metamorph
    4 : Invader
    
'''

import numpy as np
from utils.custom_plots import show_img, write_img
from utils.neighbors import getAdjacency

outdir = './output'
imgH, imgW = (72, 128) # a smallish world map
#imgH, imgW = (72*2, 128*2) # a bigger world map

nbStates = 5

# initialize the world
Img = np.random.randint(nbStates, size=(imgH, imgW))
# reduce number of flames in first frame
for ii in range(imgH):
    for jj in range(imgW):
        if Img[ii,jj]==4 and np.random.randint(2):
            Img[ii,jj] = 0
        
adjacency_distance = 1

iframe = 0
while True:
    # identify the types of each cell's neighbors and follow rules to update the world array
    for ii in range(imgH):
        for jj in range(imgW):
            # identify neighbors out to distance = adjacency_distance
            for d in [x for x in range(1, adjacency_distance+1)]:
                adjacency = getAdjacency(d)
                neighbors = ([(x[0]+ii, x[1]+jj) for x in adjacency])
                # remove any cells that would lie outside the array
                neighbors = [x for x in neighbors if (0<x[0]<imgH) and (0<x[1]<imgW)]
                # determine the count of each kind of neighbor
                vals = [Img[x] for x in neighbors]
                counts = [vals.count(x) for x in range(nbStates)]
    
                # APPLY THE RULES

                ''' THE CELL VALUE IS 0: EMPTPY SPACE '''
                if Img[ii,jj] == 0:
                    if counts[4] >= 3:
                        Img[ii][jj] = 4
                    if (counts[0] < 2 and counts[3] >= 1 and counts[4] > 2):
                        Img[ii][jj] = 3

                ''' THE CELL VALUE IS 1 '''
                if Img[ii][jj] == 1:
                    # remove a randomly selected neighbor
                    k = np.random.randint(len(neighbors))
                    Img[neighbors[k]] = 0
    
                ''' THE CELL VALUE IS 2 '''
                if Img[ii][jj] == 2:
                    # remove all neighbors
                    if ( (counts[3] > 0) and (counts[4] > 0) ):
                        for k in neighbors:
                            Img[k] = 0
                    # a 2 with at least one 3 neighbor becomes a 3
                    if counts[3] > 0:
                        Img[ii][jj] = 3

                ''' THE CELL VALUE IS 3 '''
                if Img[ii][jj] == 3:
                    if (counts[4] == 8): # a 3 surrounded by 4's becomes a 2
                        Img[ii][jj] = 2

                ''' THE CELL VALUE IS 4 '''
                if Img[ii][jj] == 4:
                    if (counts[3] > 1):
                        Img[ii][jj] = 2


    
    ImgDisp = np.dstack([Img, Img, Img]) # make an RGB image
    ImgDisp[Img==1] = np.array([110,110,110]) # color the defender grey
    ImgDisp[Img==2] = np.array([80,80,255]) # color the mine blue
    ImgDisp[Img==3] = np.array([100,255,100]) # color the metamorph greenish
    ImgDisp[Img==4] = np.array([255,0,0]) # color the invader red
    show_img(ImgDisp, ask=False)
    ifstr = str(iframe).zfill(4)
    #write_img(ImgDisp, ifstr, outdir)

    iframe += 1
