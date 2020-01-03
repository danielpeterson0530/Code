#Perl subroutine to return the reverse complement of rna
sub reverseComplementRNA {;
   my $seq = shift @_;
   my $rc_seq = reverse $seq;
   $rc_seq =~ tr/AUGCaugc/UACGuacg/;
   return $rc_seq
}
