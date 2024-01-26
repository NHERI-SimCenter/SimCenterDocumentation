# note: the variables p1 and p2 are defined as random variables in the workflow and their values are provided when the
# job is executed

set b 0.03
set mu1 0
set mu2 0

set x1 [expr $p1 - $mu1]
set x2 [expr ($p2 - $mu2) + $b * (($p1 - $mu1) ** 2 - 100)]

set f [open "results.out" "w"]
puts $f "$x1 $x2"
close $f