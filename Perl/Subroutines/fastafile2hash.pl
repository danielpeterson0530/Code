#perl subroutine to make hash from fasta filename
sub fastafile2hash {
   my %fasta_hash = ();
   my $header = '';

   open(fh, shift @_);
   while (my $line = <fh>) {
      chomp $line;
      $line =~ s/^\s*$//;
      if ($line =~ m/^(>.*)$/) {
         $header = $1;
      } else {
         $fasta_hash{"$header"} .= $line;
             }
      }
   close(fh);
   return %fasta_hash;
}
