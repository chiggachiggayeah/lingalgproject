# Jordan Hall and Eric Chen
# Writing Comparison Project
# Math 22, Professor Rockmore, 14F.

# Finds the distance between two vectors.
# @A, @B: vectors that contain the frequency of the tracked words.
# @return: the distance between the two vectors.
def compareVectors(A, B):
	if len(A) != len(B):
		return
	distance = 0
	for i in range(len(A)):
		coordDist = (A[i] - B[i])*(A[i] - B[i])
		distance = distance + coordDist

	return distance

# Appends a vector to a file.
# @A: the vector that we are writing to the file.
# @filename: name of the file we are writing to.
# @return: does not return anything.
def writeVectorToFile(A, filename):
	f = open(filename,'a')
	for i in range(len(A)):
		f.write(str(A[i]) + " ")
	f.write("\n")
	f.close()

def test():
	print "Testing compareVectors function"
	A = [1, 2]
	B = [2, 4]
	print "A is " + str(A), "B is " + str(B)
	print "distance squared is " + str(compareVectors(A,B))

	writeVectorToFile(A, "myfile.txt")

test()