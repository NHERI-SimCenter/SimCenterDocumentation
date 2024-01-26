set mu1 5
set mu2 5

set x1 [expr $p1 - $mu1]
set x2 [expr $p2 - $mu2]

set v [expr ($x1 ** 2 + $x2 - 11) ** 2 + ($x1 + $x2**2 - 7) ** 2]

set f [open "results.out" "w"]
puts $f "$v"
close $f