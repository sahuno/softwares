import glob
import polars as pl
import matplotlib as plt


#functions
#1. read list of overlaps files
#2. ploting facet by conditions
# define promoters

def read_modkit_pileups(paths):
    tableMpileup = pl.scan_csv(paths, separator="\t",
                has_header=False,
                schema_overrides={
                "Chromosome": str,
                "Start": int,
                "End": int,
                "name": str, 
                "score": int,
                "strand": str,
                "tstart": int,
                "tend": int,
                "color": str,
                "coverage": int,
                "freq": float,
                "mod": int,
                "canon": int,
                "other": int,
                "del": int,
                "fail": int,
                "diff": int,
                "nocall": int,
        },
        include_file_paths="path"
        )
    return tableMpileup

    
# path_bed=
# pl.read_csv()


# awk '{
# if ($6 == "+"){
#     $4 + 400;
#     $5 + 600
# } else if ($6 == "-") {
#     $4 - 400; 
#     $5 - 600
# } print $0
# }'

# awk $file

class mpielup():
    def __init__(self, paths):
        return 

    def read_modkit_pileups(self, paths):
        tableMpileup = pl.scan_csv(paths, separator="\t",
            has_header=False,
            schema_overrides={
            "Chromosome": str,
            "Start": int,
            "End": int,
            "name": str, 
            "score": int,
            "strand": str,
            "tstart": int,
            "tend": int,
            "color": str,
            "coverage": int,
            "freq": float,
            "mod": int,
            "canon": int,
            "other": int,
            "del": int,
            "fail": int,
            "diff": int,
            "nocall": int,
            },
            include_file_paths="path"
            )
        return tableMpileup

    def read_bed9(self, paths):
        bed9 = pl.scan_csv(paths, separator="\t",
            has_header=False,
            schema_overrides={
            "Chromosome": str,
            "Start": int,
            "End": int,
            "name": str, 
            "score": int,
            "strand": str,
            "tstart": int,
            "tend": int,
            "color": str,
            },
            )
        return bed9