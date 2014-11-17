# Jordan Hall and Eric Chen
# Writing Comparison Project
# Math 22, Professor Rockmore, 14F.

import argparse
import string
import os

# Constructs the vector for a given paper
# @prof_file - the full path of the file to read from.
# @filename - just the filename, without the full path
# @startIndex - the index where we start keeping track of words and their freqs
# returns - the vector for that file
def construct_vector(prof_file, filename, func_dict, startIndex = 4):
	doc_vector = [0] * (len(func_dict) + startIndex)
	counter = 0
	for line in open(prof_file):
		if counter == 0:
			doc_vector[0] = filename
			counter = 1
		if counter < startIndex:
			doc_vector[counter] = line.strip()
			counter += 1
			continue
		line_list = line.split()
		for el in line_list:
			el = el.lower().strip(string.punctuation)
			try:
				func_dict[el]
			except KeyError:
				continue #go to next word
			#else get the value which is the index and increment
			doc_vector[func_dict[el]] += 1
	return doc_vector

# Writes the entry in the given index for each vector into the file.
# This will be used to construct strings, which will be labels for the Matlab graphs.
# The labels will be surrounded in single-quotes in the file.
# @vector_list - the list of vectors
# @index - the index in each vector that we are writing to the file.
def getLabels(vector_list, filename, index):
	f = open(filename,'a')
	f.write("labels = {")
	for vector in vector_list:
		f.write("\'" + str(vector[index]) + "\'")
		f.write(";...\n")
	f.write("};")
	f.close()

# Writes the vectors to a Matlab compatible matrix.
# @vector_list - the list of vectors representing papers.
# @filename - the name of the file that will contain the Matlab data.
def writeMatlabFile(vector_list, filename, startIndex=4):
	f = open(filename,'a')
	f.write("papers = [")
	for vector in vector_list:
		f.write(str(vector[startIndex]))
		for i in range(startIndex, len(vector)):
			f.write(" " + str(vector[i]))
		f.write(";...\n")
	f.write("];")
	f.close()

# Normalizes the vectors so that a word's score depends on the frequency of other words in the paper.
# Makes it so that longer papers do not have higher frequencies for all words.
# Edits the vector_list in place.
def normalizeVectors(vector_list, startIndex = 4):
	for vector in vector_list:
		sum = 0
		for i in range(startIndex, len(vector)):
			sum += vector[i]
		for i in range(startIndex, len(vector)):
			vector[i] = float(vector[i])/sum
	return vector_list

# Makes the dictionary of words that we are looking for in prof papers
# and maps the words to a corresponding index for each vector.
# @startIndex - the index in each vector where we start keeping track of the freq of each word.
def makeWordDict(startIndex=4):
	words = ["the", "be", "to", "of", "and", "a", 'in', 'that','have','I',
	'it','for','not','on','with','he','as','you','do','at','this', 'but','his','by',
	'from','they','we','say','her','she','or','an','will','my','one','all','would',
	'there','their','what','so','up','out','if','about','who','get','which','go','me']
	counter = startIndex
	wordDict = {}
	for word in words:
		wordDict[word] = counter
		counter += 1
	return wordDict

# Makes the vectors from a file that has all the already formed vectors in written form.
# @vector_file: the file that has the vectors in it.
# @word_dict: the dictionary that contains the words that we are looking for in the prof papers.
def reconstruct_vector(vector_file, word_dict, startIndex=4):
    #professor name(space)paper_title(space)word_index(space)freq word_index(space)freq...
    #brookes federalism_paper 2 10 3 10 4 13 5 10 ...
    vector_list = [] #hold the vectors

    for line in open(vector_file):
        sline = line.split()
        new_vec = [0] * (startIndex + len(word_dict))
        for i in range(startIndex):
        	new_vec[i] = sline[i]
        for i in xrange(startIndex,len(sline),2):
            word_index = sline[i]
            word_freq = sline[i+1]
            if not word_index.isalpha():
                #start constructing the vector
                new_vec[int(word_index)] = int(word_freq)
        vector_list.append(new_vec)
    return vector_list #not sure if this is how we want it. Func words don't automatically have this index, right?

# Finds the distance between two vectors.
# @A, @B: vectors that contain the frequency of the tracked words.
# @return: the distance between the two vectors.
def compareVectors(vect1, vect2, startIndex = 4):
	if len(vect1) != len(vect1):
		return
	distance = 0
	for i in range(startIndex, len(vect1)):
		coordDist = (vect1[i] - vect2[i])*(vect1[i] - vect2[i])
		distance = distance + coordDist

	return distance

# Appends a vector to a file.
# @A: the vector that we are writing to the file.
# @filename: name of the file we are writing to.
# @return: does not return anything.
def writeVectorToFile(A, filename, startIndex = 4):
	f = open(filename,'a')
	for i in range(len(A)):
		if i >= startIndex:
			f.write(str(i) + " ")
		f.write(str(A[i]) + " ")
	f.write("\n")
	f.close()



def test1():
	print "Testing compareVectors function"
	A = [1, 2]
	B = [2, 4]
	print "A is " + str(A), "B is " + str(B)
	print "distance squared is " + str(compareVectors(A,B))
	writeVectorToFile(A, "myfile.txt")

def reconstructVectorsTest(filename):
	word_dict = makeWordDict()
	vectors= reconstruct_vector(filename, word_dict)
	return vectors
def constructVectorTest():
	word_dict = makeWordDict()
	vect = construct_vector("prof_file", word_dict)
	print vect

def createVectorsforPapers(folder):
	word_dict = makeWordDict()
	vector_list = []
	for filename in os.listdir(folder):
		full_path = folder + "/" + filename
		vector = construct_vector(full_path, filename, word_dict)
		vector_list.append(vector)
	for vect in vector_list:
		writeVectorToFile(vect, "prof_vectors.txt")

def createVectorsforPapers(folder):
	word_dict = makeWordDict()
	vector_list = []
	for filename in os.listdir(folder):
		full_path = folder + "/" + filename
		vector = construct_vector(full_path, filename, word_dict)
		vector_list.append(vector)
	for vect in vector_list:
		writeVectorToFile(vect, "prof_vectors.txt")

# Read the papers, makes the vectors, and writes the vectors to a file.
# @folder - should be "papers", in quotes.
def makeMatlabData(folder):
	word_dict = makeWordDict()
	vector_list = []
	for filename in os.listdir(folder):
		full_path = folder + "/" + filename
		vector = construct_vector(full_path, filename, word_dict)
		vector_list.append(vector)
	normalizeVectors(vector_list)
	writeMatlabFile(vector_list, "matlabData")

#makeMatlabData("papers")

# Read the papers, makes the vectors, and writes the subject of each paper to a file.
# @folder - should be "papers", in quotes.
def makeLabels(folder):
	word_dict = makeWordDict()
	vector_list = []
	for filename in os.listdir(folder):
		full_path = folder + "/" + filename
		vector = construct_vector(full_path, filename, word_dict)
		vector_list.append(vector)
	normalizeVectors(vector_list)
	writeMatlabFile(vector_list, "matlabData")
	getLabels(vector_list, "matlabLabels", 2)

makeLabels("papers")

#createVectorsforPapers("papers")
#reconstructVectorsTest("prof_vectors.txt")


#constructVectorTest()
#test()

# Eric - Not sure what this does.
def make_func_dict(func_file):
	i = 0
	myfuncdict = {}
	for line in open(func_file):
		sline = line.split()
		print sline
		myfuncdict[sline[0]] = i
		i += 1
	return myfuncdict

# if __name__ == "__main__":
#     print "whaddup"
#     parser = argparse.ArgumentParser(description="Command line parser")
#     parser.add_argument('-f', required="True")
#     parser.add_argument('-o', required="True")
#     parser.add_argument('-r', nargs="*", required="True")
#     args = vars(parser.parse_args())
#     prof_files = args["r"]
#     out_file = args["o"]
#     f = open(out_file, 'w+')
#     func_word_file = args["f"]
#     #how to have a list of args
#     func_dict = make_func_dict(func_word_file)
#     print func_dict.values()
#     print func_dict.keys()
#     for file in prof_files:
#         vector = construct_vector(file, func_dict)
#         #WRITE TO SOME FILE
#         print "hey"
#         for val in vector:
#             f.write(str(val))
