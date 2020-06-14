# tcl script to place abs difference between 2 numbers in output file results.out
set D [expr abs($a-$b)]

set outputFile [open "results.out" "w"]
puts $outputFile $D
close $outputFile