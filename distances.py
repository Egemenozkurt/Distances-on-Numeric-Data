#import required libraries
import math
#pip install scipy
from scipy.spatial.distance import cityblock
from scipy.spatial.distance import chebyshev
 
#two points in a 7 dimensional space
P1 = [10, 2, 4, -1, 0, 9, 1]
P2 = [14, 7, 11, 5, 2, 2, 18]

#Calculate distance (p=4)
p = 4
#Calculate Minkowski distance
minkowski = sum(abs(e1-e2)**p for e1, e2 in zip(P1,P2))**(1/p)


#two points in a 2 dimensional space
X1 = (5, 6)
X2 = (1, 2)

#Calculate Euclidean distance
euclidean = math.sqrt(sum([(x - y) ** 2 for x, y in zip(X1, X2)]))

#Calculate Supremum distance
supremum = max(abs(x-y) for x, y in zip(X1,X2))

#Calculate Manhattan distance 
manhattan = sum(abs(x-y) for x, y in zip(X1,X2))


#Print Minkowski Distance
print("Minkowski Distance: ",minkowski)


#Print Euclidean distance
print("\nEuclidean distance: ",euclidean)


#Print Supremum Distance
print("\nSupremum Distance: ", supremum)

#Could be also found with scipy library
print("\nSupremum Distance with chebyshev: ", chebyshev(X1,X2))


#Print Manhattan Distance
print("\nManhattan Distance: ",manhattan)

#Could be also found with cityblock library
print("\nManhattan Distance with cityblock: ", cityblock(X1, X2))
