.. _lblScalingWindTunnelData

Scaling Wind Tunnel Data
========================

In general, the physical size of the model used in a wind tunnel test will be different from the real world structure. As a consequence of this scaling, laws of `similitude <https://en.wikipedia.org/wiki/Similitude_(model)>`_ are used to convert the data coming from a wind tunnel experiment to forces acting on the real structure. 


Wind Tunnel Data
----------------

The data obtained from a wind tunnel typically contains the following:

#. Building dimensions. For example, for a cuboid-shaped building, this would contain: height, breadth(width) and depth.
#. Time interval. The time step, :math:`\Delta t`, or frequency, :math:`f`, of the data.
#. Time history of pressure tap data. This data is provided as the pressure coefficient, :math:`C_p` and is a dimensionless parameter.
#. Location of pressure taps.


Time Step for Real Structure Transient Analysis
-----------------------------------------------

Due to similitude, is is necessary to convert the time step :math:`\Delta t_M` or frequency :math:`f_M` obtained from wind tunnel data to one that is used in the transient analysis of the full-scale structure, :math:`\Delta t_R` or :math:`f_R`. (note: the subscript :math:`M` is used for model parameter and subscript :math:`R` for real-world structure). This is done by determining some scale factors which relate ratios of quantity in model scale to quantity in real world scale.


1. Length factor, :math:`\lambda_L = \frac{D_M}{D_R}`

2. Time factor: :math:`\lambda_T= \frac{\Delta t_M}{\Delta t_R}`

3. Velocity factor: :math:`\lambda_V= \frac{V_M}{V_R}`

where :math:`D` represents the length dimension, :math:`\Delta t` the time step, and :math:`V` the velocity.

There is a relationship between these scaling factors obtained from the definition of velocity (:math:`V = \frac{D}{\Delta t}`) which is

.. math::
 \lambda_V =\frac{\lambda_ L}{\lambda_t}


It is this relationship which can then be used to determine :math:`\Delta t_R`

.. math::

   \Delta t_R = \Delta t_M *  \lambda T = \Delta t_M * \frac{\lambda_V}{\lambda_L}

It should be noted that the model and the real structure should have geometric similarity. This means that the model should scale similarly in all directions to the real world structure. In calculations used in SimCenter the length factor hL is calculated using the height of the real structure and the height of the model.

Force Calculation on Real Structure Floors
------------------------------------------

The pressure at a location in the real structure corresponding to a pressure tap location in the model can be obtained from
the following equation:

.. math::

   P_R = C_p * 0.5*\rho * {V_R}^2

where :math:`V_R` is the wind speed and :math:`\rho` the full scale air density, typically :math:`1.225kg/m^3`. It should be noted that the pressures in
the wind tunnel are not needed, this is because :math:`C_p` is a dimensionless parameter :cite:`parkDatabaseassistedDesignEquivalent2018`. It should also be noted that it is essential that the wind speed :math:`V_R` have same basis as the model wind speed :math:`V_M`, i.e. averaging period, elevation, and vertical profile.

The forces on the structure can be calculated by integrating the pressures over the external surface area of the building.

.. math::
   F = \int\limits_A P_R

As the pressures are not known for all points on the building, the approximation used is to break the building into a number of sections and assuming the pressure is constant over that section determine the force on the section and from that the force on the building. In the SimCenter application, the current approach is for each story to divide the surface of the building story into a number of sections. For each section we determine the closest tap location to obtain a :math:`C_p` for that section. The force and moment contributed to the floor above and below the section are done assuming simply supported beam theory.

.. math::
   F_A = \sum\limits_{sections} F_{A^{section}} = \sum\limits_{sections} * F^{section} * \frac{b}{(a+b)} = \sum\limits_{sections} A^{section} * C_p^{section} * 0.5 * \rho *  V_R^2 * \frac{b}{(a+b)}

.. math::
   M_A =  \sum\limits_{sections} A^{section} * F_a *  c


where :math:`F_A` represents force on floor *A* due to section between floors *A* and *B* and  :math:`M_A` the moment contribution due to these sections. These are calculated from :math:`F_{A section}` the force contribution to floor *A* due to a particular section, :math:`a` distance from centroid of section to floor *A*, :math:`b` distance from centroid of section to floor *B*, and :math:`c` distance from centroid of section to centroid of building face.


