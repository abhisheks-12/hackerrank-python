
import math


def isPower(n) :
	if (n==1) :
		return True

	for x in range(2,(int)(math.sqrt(n))+1) :
		y = 2
		p = (int)(math.pow(x, y))

		
		
		while (p<=n and p>0) :
			if (p==n) :
				return True
			
			y = y + 1
			p = math.pow(x, y)
		
		
	return False
	
for i in range(12) :
	if (isPower(i)) :
		print(i,end=" ")
		

