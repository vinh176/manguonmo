import Horcner as H
import numpy as np
import matplotlib.pyplot as plt

def Lagrange(x, y):
    n = len(x)
    Tab = np.zeros((n, n))
    s1 = np.ones(n)
    s2 = np.zeros(n)
    temp = []
    P = []
    for i in range (0, n):
        for j in range (0, n):
            if (i != j):
                Tab[i, j] = x[i] - x[j]
                s1[i] = s1[i] * Tab[i, j]
        s2[i] = y[i] / s1[i]
    
    for i in range (0, n):
        t = x.copy()
        t.remove(t[i])
        temp.append(t)
    
    for i in range (0, n):
        P1 = H.poly_mul(temp[i])
        t = np.array([e  for e in P1])
        print("\nloop No.", i)
        
        P = H.poly_add(P, P1*s2[i])
        print(P)
        print("====================================")
    
    return P

if __name__ == "__main__":
    M = np.array([[1, 3.6],
                  [2, 5.1],
                  [3, 6.2],
                  [4, 7.1],
                  [5, 8.0],
                  [6, 8.7],
                  [7, 9.4],
                  [8, 10.1],
                  [9, 10.7],
                  [10, 11.3],
                  [12, 12.4],
                  [14, 13.4],
                  [16,14.3],
                  [18,15.2],
                  [20, 16.0],
                  [25, 17.9],
                  [30, 19.6],
                  [35, 21.1],
                  [40, 22.6],
                  [45, 24.0],
                  [50, 25.3],
                  [60, 27.7],
                  [70, 29.9],
                  [80, 31.9],
                  [90, 33.9],
                  [100, 35.7],
                  [150, 43.7],
                  [200, 50.5],
                  [250, 56.5],
                  [300, 61.9],
                  [400, 71.4],
                  [500, 79.9],
                  [1000, 112.9],
                  [2000, 159.7]])
01    x1 = M[15:30, 0]
    y1 = M[15:30, 1]
    x = []
    y = []
    for i in range (len(x1)):
        x.append(x1[i])
        y.append(y1[i])
    P = Lagrange(y, x)
    #print(y)
    print(H.eval_poly(P, 20))
    #plt.plot(x, y)