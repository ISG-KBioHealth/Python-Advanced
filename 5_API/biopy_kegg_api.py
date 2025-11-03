from Bio.KEGG import REST

human_pathways = REST.kegg_list("pathway", "hsa").read()

pathways = []
for line in human_pathways.rstrip().split("\n"):
    entry, description = line.split("\t")
    if "repair" in description.lower():
        pathways.append(entry)
        print(entry, description)
print(pathways)

genes = []
for pathway in pathways:
    pathway_file = REST.kegg_get(pathway).read()
    current_section = None
    for line in pathway_file.rstrip().split("\n"):
        section = line[:12].strip()
        if not section == "":
            current_section = section
            if current_section == "GENE":
                gene_identifiers, gene_description = line[12:].split("; ")
                gene_id, gene_symbol = gene_identifiers.split()
                if gene_symbol not in genes:
                    genes.append(gene_symbol)
print("pathway에 연관된 유전자는 {} 이다".format(",".join(genes)))