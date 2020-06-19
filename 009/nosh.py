import nashpy as nash
import numpy as np
P1=np.array([[0,-1,1],[1,0,-1],[-1,1,0]])
rps=nash.Game(P1)
print(rps)