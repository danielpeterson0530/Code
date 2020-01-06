#!/usr/bin/perl
use strict;
use List::Util qw ( min max );

&driver;


sub getStart {
   my ($board_size_int, $current_trial, $trial_print_step) = (shift @_, shift @_, shift @_);
   my @coordinates;
   my %board;

   foreach (1..$board_size_int) {
      my $horz_dig = $_;
      foreach (1..$board_size_int) {
         my $vert_dig = $_;
         push(@coordinates, $horz_dig . $vert_dig);
         $board{$horz_dig . $vert_dig} = 0;
      }
   }

   my $start_pt_int = int(rand(($board_size_int**2)));
   my @starting_pos = split //, $coordinates[$start_pt_int];
   my @board = %board;
   if ($current_trial % $trial_print_step == 0) {
      print "\nTrial Number: $current_trial\n";
      print "\tRandom starting point: ($starting_pos[0],$starting_pos[1])\n";
   }
   return (@board, $coordinates[$start_pt_int]);
}


sub mvKnight {
   my ($move_counter, $trial_print_step, $current_trial, $board_size_int, $current_pos, @board) = (pop @_ , pop @_ , pop @_ , pop @_ , pop @_ , @_);
   my @current_pos = split //, $current_pos;
   my ($horz_pos, $vert_pos) = (shift @current_pos, shift @current_pos);
   my %board = @board;
   $board{$horz_pos . $vert_pos} = 1;
   my @horz_mvset = qw ( 2 1 -1 -2 -2 -1 1 2 );
   my @vert_mvset = qw ( -1 -2 -2 -1 1 2 2 1 );
   my @move_list;

   for (my $i = 0; $i < 8; $i++) {
      my $vert_mv = $vert_mvset[$i];
      my $horz_mv = $horz_mvset[$i];
      my $new_hpos = $horz_pos + $horz_mv;
      my $new_vpos = $vert_pos + $vert_mv;
      my $new_pos = $new_hpos . $new_vpos;
      if ($new_hpos < 1 || $new_hpos > $board_size_int) {next;}
      if ($new_vpos < 1 || $new_vpos > $board_size_int) {next;}
      if ($board{$new_pos}) {
         next;
      } else {
         push @move_list, $new_pos;
      }
   }

   if (scalar @move_list == 0) {
      if ($current_trial % $trial_print_step == 0) {
         print "\tTotal number of cells touched: $move_counter\n";
         return $move_counter;
      }
      return $move_counter;
   }

   my $mv_rand_num = int(rand(scalar @move_list));
   my $new_current_pos = $move_list[$mv_rand_num];
   $move_counter += 1;
   $board{$new_current_pos} = 1;
   @board = %board;

   &mvKnight( @board, $new_current_pos, $board_size_int, $current_trial, $trial_print_step, $move_counter);
}


sub printResults {
   my @trial_move_counts = @_;
   print "\n----------Final Statistics----------\n";
   printf "\nTotal number of trials: %d\n", scalar @trial_move_counts;
   printf "Minimum number of squares touched: %d\n", min @trial_move_counts;
   printf "Maximum number of squares touched: %d\n", max @trial_move_counts;
   my $avg = 0;

   foreach (@trial_move_counts) {
      $avg += $_;
   }

   $avg = $avg / scalar @trial_move_counts;
   printf "Average number of squares touched: %0.2f\n", $avg;
}


sub driver {
   my ($board_size_int, $num_trials_int, $num_trial_printouts, @trial_move_counts);

   print "A Knight's Tour\n";
   print "To solve the problem of whether a knight can successfully move to each space on a board of n length and width, never touching the same space twice, and moving in a random manner. Will print the statistics based on your input ... \n";
   print "\nEnter size of board width/length: \n";
   chomp($board_size_int = <STDIN>);
   unless ($board_size_int =~ /\d+/) {die "input error"};
   print "Enter number of trials to perform: \n";
   chomp($num_trials_int = <STDIN>);
   unless ($num_trials_int =~ /\d+/) {die "input error"};
   print "Enter number of printouts for trials: \n";
   chomp($num_trial_printouts = <STDIN>);
   unless ($num_trial_printouts =~ /\d+/) {die "input error"};

   if ($num_trials_int < $num_trial_printouts) {
      $num_trial_printouts = $num_trials_int;
   }
   my $trial_print_step = int($num_trials_int / $num_trial_printouts);

   print "\n\n----------Printouts----------\n";
   for (my $current_trial = 1; $current_trial < ($num_trials_int +1); $current_trial++) {
      my @pass_board_and_start_pos = &getStart($board_size_int, $current_trial, $trial_print_step);
      push @trial_move_counts, &mvKnight(@pass_board_and_start_pos, $board_size_int, $current_trial, $trial_print_step, 1);
   }

   &printResults(@trial_move_counts);
}
