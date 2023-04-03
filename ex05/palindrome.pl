#!/usr/bin/perl
use strict;
use warnings;

print "Enter a string to check if it's a palindrome: ";
my $input = <STDIN>;
chomp($input);

my $reversed = reverse($input);
$reversed =~ s/[^a-zA-Z0-9]//g;
$input =~ s/[^a-zA-Z0-9]//g;
$reversed = lc($reversed);
$input = lc($input);

if ($input eq $reversed) {
    print "The given string is a palindrome.\n";
} else {
    print "The given string is not a palindrome.\n";
}
