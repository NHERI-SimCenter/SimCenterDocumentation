.. _lbl-SensorsMPM:

-------
Sensors
-------

Sensors are used to measure physical quantities such as force, pressure, etc. within the simulation. Fundamentally, a sensor is a function that maps the state of the simulation within some specified space to a scalar or vector value. These functions are often "higher-order", i.e. reduction operations such as max or add. 

Defining a sensor in MPM involves specifying the sensor type, the material point variable to measure, and the region of the domain to measure. The sensor type is specified using the ``sensor_type`` parameter, and the material point variable to measure is specified using the ``mp_var`` parameter. The region of the domain to measure is specified using the ``region`` parameter. The sensor type can be one of the following:
