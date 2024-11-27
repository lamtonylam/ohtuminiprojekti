def inproceeding_bibtex_parser(inproceedings):
    bibtex = ""
    for i in inproceedings:
        inproceedings_dict = i.to_dict()

        bibtex = bibtex + f"@inproceedings{{{i.reference_id},\n"

        # loops through the single inproceeding entry and adds their data to bibtex string
        for ref_type, value in inproceedings_dict.items():
            typestring = f"{ref_type} =  {{{value}}},\n"
            bibtex = bibtex + "    " + typestring

        # remove the last comma from the last reference type entry
        bibtex = bibtex[:-2]

        # last curly bracket for the references
        # line breaks for references
        bibtex = bibtex + "\n}\n\n"

    print(bibtex)

    return bibtex
