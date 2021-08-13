# site response configuration file
set soilThick 99.0
set numLayers 198
# layer thickness - bottom to top
set layerThick(1) 0.50
set nElemY(1) 1
set sElemY(1) 0.500
set layerThick(2) 0.50
set nElemY(2) 1
set sElemY(2) 0.500

# ...
# ...

# motion file (used if the input arguments do not include motion)
set accFile  xInput.acc
set dispFile xInput.disp
set velFile  xInput.vel
set timeFile xInput.time
set numEvt 2
set accFile2  yInput.acc
set dispFile2 yInput.disp
set velFile2  yInput.vel
set rockVs 760.0
set omega1 8.59
set omega2 42.95
