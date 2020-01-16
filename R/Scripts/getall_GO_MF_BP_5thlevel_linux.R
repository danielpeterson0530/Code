#/usr/bin/env Rscript
### R script to get all level 5 GO terms for Biological Process and Moloecular Function and write to file
### runs in commandline linux

#if (!requireNamespace("BiocManager", quietly = TRUE))
#  install.packages("BiocManager")
#BiocManager::install("GO.db")

suppressMessages(library(GO.db))


getAllBPChildren <- function(goids)
{
  ans <- unique(unlist(mget(goids, GOBPCHILDREN), use.names=FALSE))
  ans <- ans[!is.na(ans)] # Remove GO IDs that do not have any children
}

level1_BP_terms <- getAllBPChildren("GO:0008150")
level2_BP_terms <- getAllBPChildren(level1_BP_terms)
level3_BP_terms <- getAllBPChildren(level2_BP_terms)
level4_BP_terms <- getAllBPChildren(level3_BP_terms)
level5_BP_terms <- getAllBPChildren(level4_BP_terms)
for (val in level5_BP_terms)
{
cat(val, "\n")
}
#write(level5_BP_terms, file="all_fifthlevel_bp_goids.txt", sep="\n")

getAllMFChildren <- function(goids)
{
  ans <- unique(unlist(mget(goids, GOMFCHILDREN), use.names=FALSE))
  ans <- ans[!is.na(ans)]
}

level1_MF_terms <- getAllMFChildren("GO:0003674")
level2_MF_terms <- getAllMFChildren(level1_MF_terms)
level3_MF_terms <- getAllMFChildren(level2_MF_terms)
level4_MF_terms <- getAllMFChildren(level3_MF_terms)
level5_MF_terms <- getAllMFChildren(level4_MF_terms)
for (val in level5_BP_terms)
{
cat(val, "\n")
}
#write(level5_MF_terms, file="all_fifthlevel_mf_goids.txt", sep="\n")
