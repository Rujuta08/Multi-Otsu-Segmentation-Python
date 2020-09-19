import numpy as np
import random
import time
import copy
from solution import solution

'''Randomly initialize population'''
def initpop(size,dim,lb,ub,vellim):
    pop = lb + (ub-lb)*np.random.rand(size,dim)
    #make positions discrete
    pop = pop.astype(int)
    vel = vellim[0] + (vellim[1] - vellim[0])*np.random.rand(size,dim)
    return(pop, vel)


'''Determine fitness of all particles'''
def fitness(pop,f):
    fits = []
    for i in range(len(pop)):
        fits.append(f(np.array(pop[i])))
    return(fits)


'''Determine fitness and position of global best '''
def globalbest(fits,pos,gbestscore,xgbest):
    idx = fits.index(min(fits))
    if (gbestscore > fits[idx]):
        gbestscore = fits[idx]
        xgbest = pos[idx,:].copy()
    return (gbestscore, xgbest)
    

'''Determine personal best position of a particle'''
def personalbest(fits,pos,pbestscore,xpbest):
    m = pos.shape[0]
    for i in range(m):
        if(pbestscore[i] > fits[i]):
            pbestscore[i] = fits[i]
            xpbest[i,:] = pos[i,:].copy()
    return (pbestscore,xpbest)


'''Updating velocity'''
def update(w,vel,pbestpos,pos,gbestpos,velmin,velmax, lowb, uppb,c1):
    c2 = 4 - c1
    m = pos.shape[0]

    #update velocity
    const1 = c1 * np.random.rand(m,1)
    const2 = c2 * np.random.rand(m,1)

    vel = w * vel + const1 * (pbestpos - pos) + const2 * (gbestpos - pos)

    #repair velocities
    vel[vel < velmin] = random.uniform(velmin,velmax)
    vel[vel > velmax] = random.uniform(velmin,velmax)

    #update position
    pos = pos + vel
    
    #repair positions
    pos[pos < lowb] = lowb #random.uniform(lowb,uppb)
    pos[pos > uppb] =  uppb #random.uniform(lowb,uppb)

    #make position discrete
    pos = pos.astype(int)
    
    return(vel, pos)



'''Implement Particle swarm optimiztion -- minimization only'''
def pso(iteration,dim,fun,popsize,lim,c1,vmax,desired,objfun_name):

    #define upper and lower bounds
    lb = lim[0]
    ub = lim[1]
    vmin = -vmax
    vellims = [vmin,vmax]
    wmax = 0.9
    wmin = 0.1
    funeval = 0
    error = float("inf")
    max_fes = 10000*dim
    l = 0

    s = solution()
    s.dim = dim
    s.popnum = popsize
    s.objfname = objfun_name
    
    ################ Initialization ######################
    #Initialize personal best for each particle
    xpbest = np.zeros((popsize,dim))
    pbestscore = np.zeros(popsize)
    pbestscore.fill(float("inf"))

    # Initialize global best position and corresponding fitness
    xgbest = np.zeros((1,dim))
    gbestscore = float("inf")

    #generate random population and assign velocity to each particle
    pos, velocity = initpop(popsize,dim,lb,ub,vellims)

    alpha = []

    ####################################################
    print("PSO is optimizing")

    timerStart = time.time()
    s.startTime = time.strftime("%Y-%m-%d-%H-%M-%S")
    
    for l in range(iteration):
        
        fits = fitness(pos,fun)
        funeval += len(pos)

        # Find personal best
        pbestscore, xpbest = personalbest(fits,pos,pbestscore,xpbest)

        # Find global best
        gbestscore, xgbest = globalbest(fits,pos,gbestscore,xgbest)
        
        #Update w of PSO
        w = 1*((iteration-l)/iteration)

        #Update velocity and position
        velocity, pos = update(w,velocity,xpbest,pos,xgbest,vmin,vmax,lb,ub,c1)

        #alpha[l] = gbestscore
        alpha.append(gbestscore)

        error = abs(desired - gbestscore)
        
        if (l%1==0):
            print(['At iteration '+ str(l+1)+ ' the best fitness is '+ str(gbestscore)])


    timerEnd = time.time()
    s.best = gbestscore
    s.bestIndividual = xgbest
    s.endTime = time.strftime("%Y-%m-%d-%H-%M-%S")
    s.executionTime = timerEnd - timerStart
    s.convergence = alpha
    s.optimizer = "PSO"
    s.funeval = funeval
    s.error = error

    return s
