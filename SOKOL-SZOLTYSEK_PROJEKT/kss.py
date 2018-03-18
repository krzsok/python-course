
# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a script file.

Autor : Krzysztof Sokół-Szołtysek
"""
#import Gnuplot
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as ss
import pylab as pl
import sys
import os


seed = 100
Matricescount = 500
defaultParams = True

def main_menu():
    os.system('clear')
    
    print ("\n\n\n\n\nWelcome,\n")
    print ("Please choose the feature you want to see:")
    print ("1. Semicircular distribution(might take a while)")
    print ("2. Eigenvalues concentration")
    print ("3. Marchenko-Pastur distribution")
    print ("4. Kappa averages comparison")
    print ("5. Mean and stadard deviation of traces")
    print ("------CONFIGURATION---------")
    print ("6. Toggle use of custom parametres - currently :" + " OFF" if defaultParams else "6. Toggle use of custom parametres - currently : ON" )
    print ("7. Set custom parametres")
    print ("\n0. Quit")
    choice = input(" >>  ")
    exec_menu(choice)
 
    return

    
def exec_menu(ch):
    os.system('clear')
    
    if ch == '':
        main_menu()
    elif ch == '1':
        semicircular()
    elif ch == '2':
        eigenHeatMap()
    elif ch == '3':
        MarchenkoPastur()
    elif ch == '4':
        KappaAverages()
    elif ch == '5':
        meanAndStandard()
    elif ch == '6':
        global defaultParams
        defaultParams = not defaultParams
        main_menu()
    elif ch == '7':
        print("enter no. of matrices and seed(preferably between 100 and 200) divided by whitespace")
        raw = input(" >>  ")
        param = [int(s) for s in raw.split() if s.isdigit()]
        print (param)
        print (type(param))
        setParametres(param[0],param[1])
        main_menu()               
    elif ch == '0':
        sys.exit()
    else:
        print("invalid argument, try again")
    return

def setParametres(n,m):
    global seed
    global Matricescount
    Matricescount = n #600 for D. ; 1 for F.
    seed = m 
    
def getMatrices():

    return [np.matrix(np.sqrt(1/seed) * np.random.randn(seed, seed)) for i in range(Matricescount)] # np.sqrt(1/n) * np.mat  


#C.
def meanAndStandard():
    if defaultParams : setParametres(50,192)
    G = getMatrices()
    GxGt = [g * np.transpose(g) for g in G]
    t = [np.trace(gxgt) for gxgt in GxGt]
    #print(t)
    print("mean t:", end= ' ')
    print(np.mean(t))
    print("standard deviation t:", end= ' ')
    print(np.std(t))



#D.
def semicircular():
    
    if defaultParams : setParametres(600,192)
    G = getMatrices()
    H=[((g + np.transpose(g)) / np.sqrt(2)) for g in G]
    EV=[np.linalg.eigvalsh(h) for h in H]
    plt.hist(EV, normed=True, bins='sqrt')
    r = ss.semicircular.rvs(size=100, scale=2)
    plt.hist(r, bins='sqrt',normed=True,color='r',alpha=0.4)
    plt.show()


#E.
def eigenHeatMap():
    
    if defaultParams : setParametres(100,192)
    G = getMatrices()
    cEV = [np.linalg.eigvals(g) for g in G]
    Real = np.real(cEV)
    Imag = np.imag(cEV)
    plt.hist2d(Real.ravel(),Imag.ravel(), bins=np.sqrt(seed * Matricescount), normed = False)
    plt.show()



#F.
def MarchenkoPastur():
    if defaultParams : setParametres(1,192)
    G = getMatrices()
    GxGt = [g * np.transpose(g) for g in G]
    W = [gxgt / np.trace(gxgt) for gxgt in GxGt]
    rEV = [np.linalg.eigvalsh(w) for w in W]
    x=[rev * seed for rev in rEV]
    plt.hist(x, alpha = 0.7, bins='sqrt', normed = False, range = [0,7])
    pl.ylim([0,100])
    plt.show()



#G.
def KappaAverages():
    
    if defaultParams : setParametres(600,192)
    G = getMatrices()
    SV = [np.linalg.svd(g, compute_uv = False) for g in G]
    #Sigmamax = [np.amax(sv) for sv in SV]
    #Sigmamin = [np.amin(sv) for sv in SV]
    #print(Sigmamax)
    #print(Sigmamin)
    K = [np.amax(sv) / np.amin(sv) for sv in SV]
    #print(K)
    print("Kappa:")
    #print(K)
    print("mean K:") 
    print(np.mean(K))
    print("std K:")
    print(np.std(K))
    #print("log(Kappa)")
    #print(np.log(K))
    print("mean logarithm:")
    print(np.mean(np.log(K)))
    print("logarithmic average:")
    print(np.exp(np.mean(np.log(K))))
    print("std of log average:")
    print(np.std(np.log(K)))


if __name__ == "__main__":
    # Launch main menu
    while True:
        main_menu()
