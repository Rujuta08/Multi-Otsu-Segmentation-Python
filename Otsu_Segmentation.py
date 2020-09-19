import numpy as np
import math
from skimage.measure import compare_ssim
from skimage import data, io, img_as_ubyte
import matplotlib.pyplot as plt
from skimage.filters import threshold_multiotsu
import PSO


def multiotsu_plot(img,regions,thresholds,imgname, funname):

    '''Display input image, thresholds on histogram and final segmented image'''
    fig,ax = plt.subplots(nrows = 1, ncols = 2, figsize = (10,3.5))

    #Plot histogram and thresholds obtained from multi-otsu
    ax[0].hist(img.ravel(),bins = 255)
    ax[0].set_title('Histogram')
    for t in thresholds:
        ax[0].axvline(t, color='r')

    #Plot multi-otsu result
    ax[1].imshow(regions,cmap = 'gray')
    ax[1].set_title('Multi-otsu result')
    ax[1].axis('off')

    plt.subplots_adjust()
    #plt.show()
    plt.savefig(str(imgname)+'newsegmented_Class_'+str(len(thresholds)+1)+'_Optfn_'+str(funname)+'_Avgplot.png')


def fun_multiotsu(t):
    ip = normProba * np.linspace(0,spaceSize-1,spaceSize)
    if (len(t) > 1):
        t = sorted(t)
    invalidThresh = 0
    threshStart = 0
    threshEnd = 0
    omega = []
    mu = []
    sigmasq = []

    #Class occurance probability: omega
    #Class mean probability: mu
    for thr in range(len(t)+1):
        #if thr == 0:
         #   threshStart = 0

        if thr == len(t):
            threshEnd = spaceSize   
        else:
            threshEnd = t[thr]
            
        omega.append(sum(normProba[threshStart:threshEnd]))
        
        if omega[thr] == 0:
            mu.append(0)
            invalidThresh = 1
        else:
            mu.append(sum(ip[threshStart:threshEnd])/omega[thr])           

        if thr <= len(t)-1:
            threshStart = t[thr]


    #Total mean
    mu_total = sum(ip)
    lin = np.linspace(0,spaceSize-1,spaceSize)

    #Class variances sigmasq
    for thr in range(len(t)+1):
        if thr == 0:
            threshStart = 0

        if thr == len(t):
            threshEnd = spaceSize
        else:
            threshEnd = t[thr]

        if omega[thr] == 0:
            sigmasq.append(0)
        else:
            pcv = (lin[threshStart:threshEnd] - mu[thr])**2
            p_mul = normProba[threshStart:threshEnd]/omega[thr]
            sigmasq.append(np.sum(np.multiply(pcv,p_mul)))

        if thr<= len(t)-1:
            threshStart = t[thr]

    if invalidThresh == 1:
        fitness = float("inf")
    else:
        #fitness using within class variance
        fitness = np.sum(np.multiply(omega,sigmasq))
        
    return (fitness)

imgname = 'lena_gray.png'
img = io.imread(imgname)
img = img_as_ubyte(img)

## display the image
#io.imshow(img)

'''create the histogram'''
histogram, bin_edges = np.histogram(img, bins=256, range=(0, 255))

'''Initialize Parameters'''
spaceSize = len(histogram)
print('Spacesize: ',spaceSize)
totalPixels = sum(histogram)
print('Total pixels: ',totalPixels)
normProba = histogram/totalPixels

threshMin = 1
threshMax = len(histogram)

#The number of classes (m) in which the image is to be segmented is given as:
# m = thresh + 1
thresh = 4 #should be in range (1,256)
t = 0 #minimization problem
pop = 30
itr = 300
c1 = 2.4
vmax = 6
desired = 0
objfname = 'Multi-threshold OTSU'
lim = [threshMin,threshMax]
runs = 1

'''Using PSO Optimization to find out optimal threshold values for segmentation'''
thr = []
fits = []
psnrs = []
runtime = []
for r in range(runs):
    sol = PSO.pso(itr,thresh,fun_multiotsu,pop,lim,c1,vmax,desired,objfname)
    print('Objective Function: ',sol.objfname)
    print('Method: ',sol.optimizer)
    print('Global best: ',sol.best)
    print('Best Threshold: ',sol.bestIndividual)
    print('Execution Time: ',sol.executionTime,' secs')

    thresholds = sorted(sol.bestIndividual)
    print('Thresholds: ',thresholds)
    thr.append(thresholds)
    runtime.append(sol.executionTime)
    fits.append(sol.best)

    regions = np.digitize(img,bins = thresholds)
    output = img_as_ubyte(regions)

    mse = np.sum((output - img)**2)/(img.shape[0]*img.shape[1])
    psnr = 10*math.log10((255**2)/mse)
    print("PSNR: ",psnr)
    psnrs.append(psnr)

thravg = np.mean(thr,axis = 0)
thravg = thravg.astype(int)
avgruntime = np.mean(runtime)
avgfits = np.mean(fits)
psnravg = np.mean(psnrs)

classes = thresh + 1
regionsavg = np.digitize(img,bins = thravg)
outputavg = img_as_ubyte(regionsavg)

    
multiotsu_plot(img,regionsavg,thravg,imgname,'PSO')
