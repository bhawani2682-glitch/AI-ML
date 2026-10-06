from numpy import *


quantity = [3,4,5]
price = [1,2,3]      
cost = dot(quantity, price)
print(cost)


king = array([0.29,0.68])
queen = array([0.51, 0.71])
similarity_soure = dot(king , queen)/(linalg.norm(king) * linalg.norm(queen))

print(similarity_soure)