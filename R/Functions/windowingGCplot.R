#R function to create plot for GC content with sliding window
plotwindowingGC <- function(windowsize, inputseq)
{
  gcwindow <- seq(1, length(inputseq)-windowsize, by = windowsize) 
  n <- length(gcwindow)
  chunks <- numeric(n)
    for (i in 1:n) {
      chunk <- inputseq[gcwindow[i]:(gcwindow[i]+(windowsize-1))]
      chunkgc <-GC(chunk)
      #print(chunkgc) #uncomment to print each chunk's GC to screen
      chunks[i] <- chunkgc
    }
  plot(gcwindow,chunks,type="b",xlab="Nucleotide Start Position",ylab="GC Content", main=paste("GC Plot with windowsize:",windowsize))
}

