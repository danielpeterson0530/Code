#perl subroutine to check if correct number of arguments is given
sub checkArgs {
   if (scalar @ARGV != 1) {die "usage: perl tool.pl ./inFile"}
}
