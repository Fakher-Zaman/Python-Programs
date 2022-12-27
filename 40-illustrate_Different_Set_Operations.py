'''
The following Set operations illustrate here:
1-Union
2-Intersection
3-Difference
4-Symmetric Difference
'''

setA = set(input("Enter the set A: "))
setB = set(input("Enter the set B: "))

print("\nsetA = ", setA)
print("setB = ", setB)

union = setA | setB
print("\nThe union of setA and setB = ", union)
intersection = setA & setB
print("The intersection of setA and setB = ", intersection)
difference = setA - setB
print("The difference of setA and setB = ", difference)
symmetricDiff = setA ^ setB
print("The Symmetric Difference of setA and setB = ", symmetricDiff)