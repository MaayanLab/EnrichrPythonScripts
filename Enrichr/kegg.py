__author__ = 'maximkuleshov'

from Bio.KEGG import REST
from collections import defaultdict


def main():
    for pwid in ['hsa', 'mmu']:
        human_pathways = REST.kegg_list('pathway', pwid).read()

        pathways = [line for line in human_pathways.strip().split('\n')]

        # Get the genes for pathways and add them to a list
        pathways_dict = defaultdict(list)
        for pathway in pathways:
            entry, description = pathway.split('\t')
            pathway_file = REST.kegg_get(entry).read()  # query and read each pathway

            # iterate through each KEGG pathway file, keeping track of which section
            # of the file we're in, only read the gene in each pathway
            current_section = None
            for line in pathway_file.rstrip().split('\n'):
                section = line[:12].strip()  # section names are within 12 columns
                if not section == '':
                    current_section = section

                if current_section == 'GENE':
                    if len(line[12:].split('; ')) > 1:
                        gene_identifiers, *gene_description = line[12:].split('; ')
                        gene_id, gene_symbol = gene_identifiers.split()
                        pathways_dict[description.split(' - ')[0]].append(gene_symbol)

        with open('{0}.gmt'.format(pwid), 'w') as pw_file:
            out_pw = ['{0}\t\t{1}\n'.format(desc, '\t'.join(sorted(pathways_dict[desc])))
                      for desc in sorted(pathways_dict) if len(pathways_dict[desc]) > 4]
            pw_file.writelines(out_pw)
    return None


if __name__ == '__main__':
    main()