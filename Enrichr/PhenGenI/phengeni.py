from collections import defaultdict


def main():
    f = open('PheGenI_Association_full.tab').read().strip().split('\n')[1:]
    d = defaultdict(list)
    for l in f:
        crumbs = l.split('\t')
        trait = crumbs[1]
        context = crumbs[3]
        gene1 = crumbs[4].upper()
        gene2 = crumbs[6].upper()
        d[trait].extend([gene1, gene2])

    l = []
    for k, v in d.items():
        term = '{}\t\t{}'.format(k, '\t'.join(sorted(list(set(v)))))
        l.append(term)

    with open('PhenGenI_Association_2021.gmt', 'w') as f:
        f.write('\n'.join(l))

    return


if __name__ == '__main__':
    main()