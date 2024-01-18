model BasicBuilder -ndm 3 -ndf 6
node 1 0 0 0 
fix 1 1 1 1 1 1 1 
node 2 0 0 3.6 -mass 284190 284190  0.0  0.0  0.0 2.8419e-05 
fix 2 0 0 1 1 1 1 
node 3 0 0 7.2 -mass 284190 284190  0.0  0.0  0.0 2.8419e-05 
fix 3 0 0 1 1 1 1 
uniaxialMaterial Hysteretic 1 2.11012e+06 0.0342929 6.33037e+06 0.822315 6.33037e+06 1 -2.11012e+06 -0.0342929 -6.33037e+06 -0.822315 -6.33037e+06 -1 0.8 0.8 0 0 0.1
uniaxialMaterial Hysteretic 2 1.40675e+06 0.0228619 4.22025e+06 0.54821 4.22025e+06 1 -1.40675e+06 -0.0228619 -4.22025e+06 -0.54821 -4.22025e+06 -1 0.8 0.8 0 0 0.1
element zeroLength 1 1 2 -mat 1 1 -dir 1 2
element zeroLength 2 2 3 -mat 2 2 -dir 1 2
loadConst -time 0.0
#timeSeries Path 101 -dt 0.005 -factor [expr 1 * 1 * 1 ] -values { -1.46509e-05 8.24738e-06 -2.26001e-05 1.46955e-05 -2.63045e-05 ..... -3.42224e-05  }
#timeSeries Path 102 -dt 0.005 -factor [expr 1 * 1 * 1 ] -values { 7.15223e-06 -2.4271e-05 1.94678e-05 -3.62861e-05 2.96503e-05 ...... -0.000675427  }
pattern UniformExcitation 101 1 -fact 1 -accel 101
set numStep 60000
set dt 0.005
pattern UniformExcitation 102 2 -fact 1 -accel 102
set numStep 60000
set dt 0.005
set numberOfStories 2
recorder EnvelopeNode -file 1-AIM.json0.max_abs_acceleration.response.0.out -timeSeries 101 102  -node 1 -dof 1 2  accel
recorder EnvelopeNode -file 1-AIM.json0.max_abs_acceleration.response.1.out -timeSeries 101 102  -node 2 -dof 1 2  accel
recorder EnvelopeNode -file 1-AIM.json0.max_rel_disp.response.1.out -node 2 -dof 1 2  disp
recorder EnvelopeDrift -file 1-AIM.json0.max_drift.response.0.1.1.out -iNode 1 -jNode 2 -dof 1 -perpDirn 3
recorder EnvelopeDrift -file 1-AIM.json0.max_drift.response.0.1.2.out -iNode 1 -jNode 2 -dof 2 -perpDirn 3
recorder EnvelopeNode -file 1-AIM.json0.max_abs_acceleration.response.2.out -timeSeries 101 102  -node 3 -dof 1 2  accel
recorder EnvelopeNode -file 1-AIM.json0.max_rel_disp.response.2.out -node 3 -dof 1 2  disp
recorder EnvelopeDrift -file 1-AIM.json0.max_drift.response.1.2.1.out -iNode 2 -jNode 3 -dof 1 -perpDirn 3
recorder EnvelopeDrift -file 1-AIM.json0.max_drift.response.1.2.2.out -iNode 2 -jNode 3 -dof 2 -perpDirn 3
recorder EnvelopeDrift -file 1-AIM.json0.max_roof_drift.response.0.2.1.out -iNode 1 -jNode 3 -dof 1 -perpDirn 3
recorder EnvelopeDrift -file 1-AIM.json0.max_roof_drift.response.0.2.2.out -iNode 1 -jNode 3 -dof 2 -perpDirn 3

# Perform the analysis
numberer RCM
constraints Transformation
system Umfpack
integrator Newmark 0.5 0.25
test NormUnbalance 1.0e-2 10 
algorithm Newton
analysis Transient -numSubLevels 2 -numSubSteps 10
set xDamp 0.0995633;
set lambdaN [eigen 3];
set lambdaI [lindex $lambdaN [expr 1 -1]];
set lambdaJ [lindex $lambdaN [expr 3 -1]];
set lambda1 [lindex $lambdaN 0]
set omega1 [expr pow($lambda1,0.5)];
set omegaI [expr pow($lambdaI,0.5)];
set omegaJ [expr pow($lambdaJ,0.5)];
set alphaM [expr $xDamp*(2*$omegaI*$omegaJ)/($omegaI+$omegaJ)];
set betaKinit [expr 0 *2.0*$xDamp/($omegaI+$omegaJ)];
set betaKcomm [expr 0 *2.0*$xDamp/($omegaI+$omegaJ)];
set betaKcurr [expr 1 *2.0*$xDamp/($omegaI+$omegaJ)];
rayleigh $alphaM $betaKcurr $betaKinit $betaKcomm;
set lambdaN [eigen 1];
set lambda1 [lindex $lambdaN 0]
set T1 [expr 2*3.14159/$lambda1]
set dTana [expr $T1/20.]
if {$dt < $dTana} {set dTana $dt}
analyze [expr int($numStep*$dt/$dTana)] $dTana 
remove recorders 
