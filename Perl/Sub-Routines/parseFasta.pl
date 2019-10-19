#Perl Subroutine to create hash from large_fasta array
sub parseFasta(@large_fasta) {
        my %fasta_hash = ();
        my $header = '';

        foreach my $line (@_) {
                chomp $line;
                $line =~ s/^\s*$//;
                if ($line =~ m/^(>.*)$/) {
                        $header = $1;
                } else {
                        $fasta_hash{"$header"} .= $line;
                }
        }
        return %fasta_hash;
}
