#perl subroutine to print out the index of each array element
sub array_index_print {
   while ((my $i, my $x) = each @_) {
      print "$i:$x\n"
   }
}
