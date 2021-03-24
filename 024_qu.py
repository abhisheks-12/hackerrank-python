N = 4
MATRIX = [ [ 0, 0, 1, 0 ], 
		[ 0, 0, 1, 0 ], 
		[ 0, 1, 0, 0 ], 
		[ 0, 0, 1, 0 ] ] 

def knows(a, b): 
	
	return MATRIX[a][b] 

# Returns -1 if celebrity 
# is not present. If present, 
# returns id (value from 0 to n-1). 
def findCelebrity(n): 
	
	# Base case 
	if (n == 1): 
		return n - 1
	
	# Find the celebrity with n-1 
	# persons 
	id_ = findCelebrity(n - 1) 
	
	# If there are no celebrities 
	if (id_ == -1): 
		return n - 1
	
	# If the celebrity knows the 
	# nth person 
	elif (knows(id_, n - 1) and
	not(knows(n - 1, id_))): 
		return n - 1
		
	# If the nth person knows the 
	# celebrity then return the id 
	elif (knows(n - 1, id_) and
	not(knows(id_, n - 1))): 
		return id_ 

	# If there is no celebrity 
	return - 1

# Returns -1 if celebrity 
# is not present. If present, 
# returns id (value from 0 to n-1). 
# a wrapper over findCelebrity 
def Celebrity(n): 
	
	# Find the celebrity 
	id_ = findCelebrity(n) 
	
	# Check if the celebrity found 
	# is really the celebrity 
	if (id_ == -1): 
		return id_ 
	else: 
		c1 = 0
		c2 = 0

		# Check the id is really the 
		# celebrity 
		for i in range(n): 
			if (i != id_): 
				c1 += knows(id_, i) 
				c2 += knows(i, id_) 
		
		# If the person is known to 
		# everyone. 
		if (c1 == 0 and c2 == n - 1): 
			return id_ 
		
		return -1

# Driver code 
if __name__ == '__main__': 
	
	n = 4
	id_ = Celebrity(n) 
	
	if id_ == -1: 
		print("No celebrity") 
	else: 
		print("Celebrity ID", id_) 

# This code is contributed by UnworthyProgrammer


	return C 
	

if __name__ == '__main__': 
	
	n = 4
	id_ = findCelebrity(n) 
	
	if id_ == -1: 
		print("No celebrity") 
	else: 
	print("Celebrity ID ", id_) 


