#R script to generate a GO enrichment horizontal bar chart with pval labels
library(ggplot2)
library(extrafont)
library(forcats)
#font_import()
#loadfonts(device = "win")

filename = "goenrichment_results.tab"

printtable = read.table(file = filename, sep='\t', header=TRUE)

ggplot(printtable, aes(x=TERM, y=(log10(pval_adjust)*-1), fill=ONTOLOGY)) + 
  geom_bar(stat = "identity", width=0.9)  +
  ylab("-log10(p_val_adj)") + 
  theme_classic() +
  scale_fill_manual(values=c("firebrick", "cornflowerblue"), labels = c("Biological\nProcess", "Molecular\nFunction")) + 
  coord_flip() + 
  theme(text=element_text(family="Calibri", face="italic", size=12),
        panel.border = element_blank(),
        panel.grid.major = element_blank(),
        panel.grid.minor = element_blank(),
        axis.line = element_blank(),
        axis.ticks = element_blank(),
        axis.text.x = element_blank(),
        axis.title.x = element_blank(),
        axis.title.y = element_blank(),
        legend.position="left",
        legend.direction = "horizontal",
        legend.title = element_blank(),
        legend.text=element_text(family="Calibri", face="plain", size=10)) +
  geom_text(aes(label=formatC(pval_adjust, format = "e", digits = 2)), family="Calibri", fontface="plain", hjust=-0.2, size=3) +
  aes(x = fct_reorder(TERM, pval_adjust, .desc = TRUE)) +
  scale_y_continuous(name="Stopping distance", limits=c(0, 50))
