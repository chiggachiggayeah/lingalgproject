import argparse

print "hey"

def make_func_dict(func_file):
    i = 0
    myfuncdict = {}
    for line in open(func_file):
        sline = line.split()
        print sline
        myfuncdict[sline[0]] = i
        i += 1
    return myfuncdict

def construct_vector(prof_file, func_dict):
    doc_vector = [0] * len(func_dict)
    for line in open(prof_file):
        line_list = line.split()
        for el in line_list:
            try:
                func_dict[el]
            except KeyError:
                continue #go to next word
            #else get the value which is the index and increment
            doc_vector[func_dict[el]] += 1
    return doc_vector

def reconstruct_vector(vector_file, func_dict):
    #professor name(space)paper_title(space)word_index(space)freq word_index(space)freq...
    #brookes federalism_paper 2 10 3 10 4 13 5 10 ...
    vector_list = [] #hold the vectors
    #line_count = 0
    for line in open(vector_file):
        line_count += 1
        sline = line.split()
        new_vec = [0] * len(func_dict.values())
        for i in range(len(sline)):
            if not sline[i].isalpha():
                #start constructing the vector
                j = i;
                while not j >= len(sline) - 1:
                    new_vec[j] = int(sline[j+1])
                    j += 2
                vector_list.append(new_vec)
                break
    return vector_list #not sure if this is how we want it. Func words don't automatically have this index, right?

if __name__ == "__main__":
    print "whaddup"
    parser = argparse.ArgumentParser(description="Command line parser")
    parser.add_argument('-f', required="True")
    parser.add_argument('-o', required="True")
    parser.add_argument('-r', nargs="*", required="True")
    args = vars(parser.parse_args())
    prof_files = args["r"]
    out_file = args["o"]
    f = open(out_file, 'w+')
    func_word_file = args["f"]
    #how to have a list of args
    func_dict = make_func_dict(func_word_file)
    print func_dict.values()
    print func_dict.keys()
    for file in prof_files:
        vector = construct_vector(file, func_dict)
        #WRITE TO SOME FILE
        print "hey"
        for val in vector:
            f.write(str(val))
