#luis rivera
#11/14/21
'''
Each element in new list should be unique.
'''
#problem 4 is trying to find a unique iteam

def list(l):
    r = [] #r is a list with unique iteams
    for i in l:
        if i not in r: # if there is no same elelement in the list r
           r.append(i) #then add it to the list r
    return r

x = [1,3,3,3,6,2,3,5]
print(list(x))

