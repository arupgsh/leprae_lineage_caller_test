import os
import sys
from glob import glob
import gzip
import re


"""
Usage: python3 helper.py "../filtered_vcfs/*.vcf.gz" 

"""

def dir_dict(uinp)->dict:
    #extract names and file locations for input files
    fl = glob(uinp)
    fnd = {}
    for fp in fl:
        fn = os.path.basename(fp)
        fnd[fn] = fp
    return fnd

def vcf_dict(fname,vcf)->dict:
    vd = {}
    var_l = set()
    if vcf.endswith('vcf.gz'):
        v = gzip.open(vcf,'rt').readlines()
    else:
        v = open(vcf, 'r').readlines()
    for l in v:
        if l.startswith('#'):
            continue
        l = l.strip('\n').split('\t')
        alt = l[4].split(',')
        for al in alt:
            var_l.add(str(l[1])+'_'+l[3]+'_'+al)
    vd[fname] = var_l
    return vd

#test for filename input and parsing
#fl = dir_dict(sys.argv[1])

#for f,v in fl.items():
#    print(vcf_dict(f,v))

def dr_scheme_parser(scheme)->dict:
    dr_dict = {}
    with open(scheme,'r') as dr:
        for l in dr:
            if l.startswith('Genomic') or l.endswith('-\n'):
                continue
            l = l.strip('\n').split(',')
            #split multi alleles
            alleles = l[2].split(';')
            for allele in alleles:
                if not dr_dict.get(l[3]):
                    dr_dict[l[3]] = []
                k = l[0]+'_'+l[1]+'_'+allele
                dr_dict[l[3]].append(k)
    return dr_dict

#test the drug resistance scheme
#print(dr_scheme_parser('../dr_list.csv'))

#drug resistance caller to be moved to helper
def match_vars(vard, scheme)->dict:
    dr_data = {}
    for k, v in vard.items():
        sample_name = k
        var_list = v
    for k, v in scheme.items():
        for m in v:
            if m in var_list:
                dr_data[sample_name] = dr_data.get(sample_name, [])+[k +'('+m+')']
    return dr_data
