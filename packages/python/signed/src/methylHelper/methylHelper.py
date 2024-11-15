import glob
import polars as pl
import matplotlib as plt


#functions
#1. read list of overlaps files
#2. ploting facet by conditions
# define promoters

# def read_modkit_pileups(paths):
#     tableMpileup = pl.scan_csv(paths, separator="\t",
#                 has_header=False,
#                 schema_overrides={
#                 "Chromosome": str,
#                 "Start": int,
#                 "End": int,
#                 "name": str, 
#                 "score": int,
#                 "strand": str,
#                 "tstart": int,
#                 "tend": int,
#                 "color": str,
#                 "coverage": int,
#                 "freq": float,
#                 "mod": int,
#                 "canon": int,
#                 "other": int,
#                 "del": int,
#                 "fail": int,
#                 "diff": int,
#                 "nocall": int,
#         },
#         include_file_paths="path"
#         )
#     return tableMpileup

    
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
        self.fpath = paths
    def read_modkit_pileups(self):
        tableMpileup = pl.scan_csv(self.fpath, separator="\t",
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
    def getHeadTable(self):
        mpileup=self.read_modkit_pileups().pl.select(["Chromosome", "Start", "End", "freq"])
        headMpileUp=mpileup.head().collect()
        return headMpileUp
        
        

def topVariableCpGs(df):
    #df; polars data frame
    df.r
    return pass
    


        ###################test run teh fun ###############
paths_bed = glob.glob("/data1/greenbab/users/ahunos/apps/workflows/methylation_workflows/DNAme_Ref_LINE1/outputs/rerun_test/results/prepareBedFiles/*/*minCov10.bed", recursive=True)

mpileup_df=mpielup(paths_bed)
mpileup_df.getHeadTable()
# mpileup_df.getHeadTable()





samplePileUp
samplePileUp = mpileup_df.read_modkit_pileups().with_columns(pl.concat_str(["Chromosome", "Start", "End","strand"], separator=":").alias("chrStartEndStrand")).select(["chrStartEndStrand","freq", "path"]).with_columns(pl.col("path").str.extract(r'D-[a-zA-Z0-9]+-\d+', 0)).collect().sample(1000).pivot(values = "freq", columns="path", index="chrStartEndStrand")#.collect()



samplePileUp.mean_horizontal()

samplePileUp.with_columns(any_horizontal == null)

samplePileUp.with_columns(pl.concat_list(["D-0-1", "D-0-3","D-0-2"]).list.std().alias("freq_newName"))

# samplePileUp.with_columns(
#     pl.std_horizontal("D-0-1", "D-0-3","D-0-2")
#       .round(2)
#       .alias('std')
# )




std(["D-0-1", "D-0-3","D-0-2"]).round(2).alias("std_freq"))

    samplePileUp.mean_horizontal().alias("mean_freq"),
    samplePileUp.std_horizontal().alias("mean_freq")
)

samplePileUp = samplePileUp.with_columns(
    samplePileUp.mean_horizontal().alias("mean_freq"),
    samplePileUp.std_horizontal().alias("mean_freq")
)

samplePileUp.with_columns(
    pl.rows().sum().alias("sum_freq")
)


def custom_function(row):
    # Example: Return the sum of all non-null values in the row
    return sum(value for value in row.values() if value is not None)

# Use `pl.struct()` to pass all columns to `map`
samplePileUp = samplePileUp.with_columns(
    pl.struct(samplePileUp.columns).map(custom_function).alias("custom_stat")
)

# samplePileUp.with_columns(mean_horizontal())
# .alias("extracted_pattern")
# mpileup_df.read_modkit_pileups().head().select(["Chromosome", "Start", "End", "freq","strand"]).with_columns(pl.concat_str(["Chromosome", "Start", "End","strand"], separator=":").alias("chrStartEndStrand")).collect()

# mpileup_df.read_modkit_pileups().head().select(["Chromosome", "Start", "End", "freq"]).with_columns(pl.concat_str([pl.col("Chromosome"),pl.col("Start"), pl.col("End")])).collect()



# pivot(values = "")

# mpileup_df.head().collect()

samplePileUp.with_columns(pl.col(["D-0-1", "D-0-3", "D-0-2"]).list.std().alias("unique_std_freq"))