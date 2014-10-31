import argparse

def make_func_dict(func_file, func_dict):
    i = 0
    for line in open(func_file):
        func_dict[line] = i
        i += 1

def construct_vector(prof_file, func_dict, doc_vector):
    for line in open(prof_file):
        line_list = line.split()
        for el in line_list:
            try:
                func_dict[el]
            except KeyError:
                continue #go to next word
            #else get the value which is the index and increment
            doc_vector[func_dict[el]] += 1
if _name_ ==" _main_":
    parser = argparse.ArgumentParser(description="Command line parser")
    parser.add_argument('-f', '--function_words', required="True")
    parser.add_argument('-o', '--out', required="True")
    parser.add_argument('r', '--reaad_file', required="True")
    args = vars(parser.parse_args())
