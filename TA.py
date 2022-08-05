from platform import java_ver
import numpy as np
import vg

data = np.loadtxt("./1GPa.txt")
np.set_printoptions(precision = 3,suppress = True)


data = np.delete(data, np.where(np.logical_or(data[:,2] < 14, data[:,2] > 60))[0], axis = 0) # In my example, I need to do this to select the data I want

po = data[0::3,2:6]
ph1 = data[1::3,2:6]
ph2 = data[2::3,2:6]

x = []
for i in range(len(po)):
    for j in range(len(ph1)):
        for k in range(len(ph2)):
            #if i != j and i != k and j != k:	#This case can be used in the same vector from group 
            if 1 < np.linalg.norm(po[i] - ph1[j]) < 2.5 and 1< np.linalg.norm(po[i] - ph2[k]) < 2.5 : #2.5 is the maximum length of OH
                a=po[i] - ph1[j]
                b=po[i] - ph2[k]
                x.append(vg.angle(a,b))
                print(vg.angle(a,b))


print(x)
print(np.mean(x,axis=0))
print(np.std(x,axis=0))
np.savetxt("./1GPa.data",x,fmt = "%.02f")