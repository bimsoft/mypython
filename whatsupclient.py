
import json
import requests

print ("This is start of what's up client...")



def diff():
    
    eng = [2,3,4,5,6,7,8,9]
    fr = [10,1,2,3,11,21,55,6,8]
    if 1 <= len(eng)  <=1000:
        loc = []
        for x in eng:
            if x not in fr:
                loc.append(x)
    else:
        return 0
        
    return len(loc)
        
def narcottis_num(val):
	tot = 0
	l = len(str(val))
	for x in str(val):
		tot += int(x)**l

	if val == tot:
		return True
	else:
		return False

def find_triplets(l):
    count = len(l)
    
    find = False
    for x in range(count-2):
        for y in range(x+1, count-1):
            for z in range(y+1, count):
                if (l[x] + l[y] + l[z] == 0):
                    print ("[", l[x] ,"," ,l[y] ,"," ,l[z], "]")
                    find = True
    if find == False:
        print ("Did not find")

def josephus_survivor(n, k):
    v = 0
    for i in range(1, n + 1): 
    	v = (v + k) % i
    return v + 1	


if __name__ =="__main__":
    #print (narcottis_num(1634))
    find_triplets([1,3,-1,-9,0,-3,-2])

