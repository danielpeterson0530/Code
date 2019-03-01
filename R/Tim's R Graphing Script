library(ggplot2)
library(tidyverse)
#read csv file into data frame
spore <- read.csv(file.choose(), header = T)

#code to change order
spore$strain <- factor(spore$strain, levels = c("WT", "DEL", "com"))



plot1 <- ggplot(data = spore) +
  aes(x = strain, y = count, fill = strain) +
  geom_bar(stat = "identity", width = 0.7, colour = "black" ) +
  geom_errorbar(aes(ymin=count, ymax=count+error), width=.1) +
  facet_wrap(. ~ time, strip.position = "bottom") + #place label below stain based on a vector
  geom_text(aes(y=count+error, label= c("a" , "b" , "a", "a" , "b" , "a")), vjust=-0.5, size = 5.5)+ #error analysis
  scale_x_discrete(labels= c(expression(paste("WT")), 
                             #expression(paste(Delta,italic("hbxA"))),       # adds grouping bar
                             expression(paste(underline("          "),paste(underline(Delta)),paste(underline(italic("hbxA          "))))),
                             expression(paste("Com")))) +                #change strain labels
  theme(axis.text = element_text(color = 'black'),
        text = element_text(size = 18),                  #change text size
        panel.spacing = unit(0, "lines"),
        legend.position="none",                            #remove legend box
        strip.background = element_blank(),
        strip.placement = "outside",
        strip.text.x = element_text(hjust= 0.45, color = 'black'),                 #adjust time label postion
        panel.background = element_rect(fill = "white", colour = "white"),
        panel.border = element_blank(), axis.line = element_line())+                 #only show x and y axis
  labs(x= "", y = expression(paste("Conidia( x", 10^{6},")/m",m^{2})), fill ="") +
  scale_y_continuous(expand = c(0,0), limits=c(0, 10))+             #bring graphs down to x axis no space and change y axis height
  scale_fill_manual("legend", values=c("WT"= "#999999", "DEL" = "#CCCCCC",  "com" = "#666666"))+         #change color of bars
  geom_segment(aes(x = 3, y= 0, xend = 4, yend =0))                    #seperate timepoints
print(plot1)

#uncomment to save to physical file
#ggsave("PATH/NAME.tiff", plot1, width = 5.5, height = 5.5)
