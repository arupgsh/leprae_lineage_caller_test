from helper import *

scheme = dr_scheme_parser('../dr_list.csv')

#test for filename input and parsing
fl = dir_dict(sys.argv[1])
for f,v in fl.items():
    vard = vcf_dict(f,v)
    print(match_vars(vard, scheme))
