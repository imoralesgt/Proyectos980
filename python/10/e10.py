import random

N = 6
M = 4
P = 2

MIN_RANDOM = 10
MAX_RANDOM = 100


dimension1 = []

for i in range(N):
    dimension2 = []
    for j in range(M):
        dimension3 = []
        for k in range(P):
            dimension3.append(random.randrange(MIN_RANDOM, MAX_RANDOM, 1))
        
        dimension2.append(dimension3)
    
    dimension1.append(dimension2)

print(str(dimension1))
