#luis rivera
#11/14/21

#problem 4 is trying to find a unique iteam

def list(l):
    r = [] #r is a list with unique iteams
    for i in l:
        r.append(i)
    return r

x = [1,3,3,3,6,2,3,5]
print(list(x))

