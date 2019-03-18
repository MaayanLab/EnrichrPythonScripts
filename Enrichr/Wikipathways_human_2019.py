from collections import defaultdict


def main():
    wp_gmt = open('gmt/wikipathways-20190310-gmt-Homo_sapiens.gmt.txt').readlines()[1:]
    # noinspection PyTypeChecker
    human_gene = defaultdict(lambda: '', dict(
        line.split('\t')[1:3] for line in open('reference/Homo_sapiens.gene_info').readlines()[1:] if
        line.split('\t')[9] == 'protein-coding'))

    template = '{0}_{1}\t\t{2}\n'

    with open('gmt/wp_mouse.gmt', 'w+') as gmt_out:
        for row in wp_gmt:
            term, uri, *genes = row.strip().split('\t')
            genes = list(filter(None, [human_gene[gene] for gene in genes]))
            term_name, version, id, species = term.split('%')
            if len(genes) > 4:
                line = template.format(term_name.replace(' ', '_'), id, '\t'.join(genes)).replace('\t \t', '\t')
                gmt_out.write(line)


if __name__ == '__main__':
    main()
