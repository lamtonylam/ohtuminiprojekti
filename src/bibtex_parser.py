def reference_bibtex_parser(references):
    bibtex = ""
    for i in references:
        references_dict = {
            k: v
            for k, v in i.to_dict().items()
            if v is not None and k not in {"id", "reference_id", "created_at"}
        }

        bibtex = bibtex + \
            f"@{references_dict['reference_type']}{{{i.reference_id},\n"

        # loops through the single inproceeding entry and adds their data to bibtex string
        for ref_type, value in references_dict.items():
            typestring = f"{ref_type} =  {{{value}}},\n"
            bibtex = bibtex + "    " + typestring

        # remove the last comma from the last reference type entry
        bibtex = bibtex[:-2]

        # last curly bracket for the references
        # line breaks for references
        bibtex = bibtex + "\n}\n\n"

    return bibtex
