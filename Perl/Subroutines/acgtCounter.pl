#Perl subroutine to return the nucleotide counts for acgt for a DNA sequence string
sub acgtCounter {
        $seq = shift @_;
        my ($a, $c, $g, $t) = ($seq =~ s/A/A/ig, $seq =~ s/C/C/ig, $seq =~ s/G/G/ig, $seq =~ s/T/T/ig);
        return ($a, $c, $g, $t);
}
