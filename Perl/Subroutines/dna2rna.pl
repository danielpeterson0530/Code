#Perl subroutine to convert dna to rna
sub dna2rna {
   my $dna = shift @_;
   $dna =~ tr/Tt/Uu/;
   return $dna
}
