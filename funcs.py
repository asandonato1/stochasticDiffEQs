import numpy as np

def sdeSimulation(steps, x0, sigma,theta):
    xList, tList = [], []
    nList = []
    t = 0
    h = 1/steps
    X = x0

    for _ in range(int(steps)): 

        eps = np.random.normal(0, 1)
        X = X - h*theta*X + sigma*eps*(h)**0.5
        xList.append(X)
        t += h
        tList.append(t)
        nList.append(sigma*eps*(h)**0.5)

    return xList, tList, nList


def blackScholesSDE(steps, x0, sigma, r, T=1.0): # previously used for separate simulations
    xList = [x0]  
    tList = [0.0]  
    h = T / steps  
    
    X = x0
    t = 0.0
    
    for _ in range(steps):
        dW = np.random.normal(0, np.sqrt(h)) # epsilon = sqrt(...)blabla
        X = X + r * X * h + sigma * X * dW + 1/2*sigma**2 * X * (dW**2 - h)
        
        t += h
        xList.append(X)
        tList.append(t)
    
    return xList, tList

def blackScholes(steps, x0, sigma, r, t = 1): # the function that is actually used in the notebook
    outList = [] 
    xList = []
    errorList = []
    h = t/steps
    #delta_t = t[1] - t[0] if len(t) > 1 else t[0]
    t = 0
    tList = []
    
    x = x0
    X = x0
    for _ in range(steps):
        Bt = np.random.normal(0, 1)
        x = x * np.exp((r - 0.5 * sigma**2) * h + sigma * np.sqrt(h) * Bt)

        dW = Bt*np.sqrt(h) # epsilon = sqrt(...)blabla
        X = X + r * X * h + sigma * X * dW + 1/2*sigma**2 * X * (dW**2 - h)

        t += h
        outList.append(x)
        xList.append(X)
        errorList.append((X - x)**2)
        tList.append(t)
    
    return outList, tList, xList, errorList