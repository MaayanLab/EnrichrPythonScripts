__author__ = 'maximkuleshov'
from collections import defaultdict

import re

def main():
    tsv = open('in/gwas_catalog_v1.0.2-associations_e95_r2019-03-01.tsv.txt').readlines()[1:]
    out = defaultdict(lambda: defaultdict(set))
    for line in tsv:
        line = line.strip().split('\t')
        # efo = line[35].replace('http://www.ebi.ac.uk/efo/EFO_', 'EFO:').split(', ')
        disease = line[7]
        for g in re.split(r',\s|\\|\s*;\s*|\sx\s|\s*/\s*', re.sub(r'\S*\s\S*', '', re.sub(r'\s*-\s*', '-', line[13]))):
            if ' ' in g:
                print(g)
        reported_genes = filter(lambda x: False if x in {'NR', '', None, 'intergenic', 'Intergenic', 'dessert'} else True, set(re.split(r',\s|\\|\s*;\s*|\sx\s|\s*/\s*', line[13])))
        # mapped_genes = filter(None, set(re.split(r'\s*,\s*|\s-\s|\s*;\s*', line[14])))
        # out[disease]['efo'] = out[disease]['pmid'].union(efo)
        # out[disease]['genes'] = out[disease]['genes'].union(set(reported_genes).union(set(mapped_genes)))
        out[disease]['genes'] = out[disease]['genes'].union(set(reported_genes))

    temp = '{0}\t\t{1}\n'
    with open('gmt/gwas_catalog.gmt', 'w+') as gmt_out:
        for term in sorted(out.keys()):
            genes = '\t'.join(sorted(out[term]['genes']))
            # efos = ', '.join(sorted(out[term]['efo']))

            if len(out[term]['genes']) >= 5:
                gmt_out.write(temp.format(term, genes))

    return None


if __name__ == '__main__':
    main()