.. _lbl-MaterialMPM:

--------
Material
--------

Water, plastic, concrete, sand, steel, clay, rubber, etc. are some of the material presets that can be used to define the bodies. Constitutive laws are selected based on the material preset with appropriate initial values for the material properties. Constitutive laws are used to define the material behavior under different loading conditions. Options include:

#. **Isotropic Fluid with Viscous Shear Stress / J-Fluid:** This is used to define a basic Newtonian fluid. The material properties include density, bulk modulus, derivative of the bulk modulus with respect to pressure, and dynamic viscosity.
#. **Fixed-Corotated / Neo-Hookean:** This is used to define solid hyperelastic material behavior under large strains. The material properties include Young's modulus, Poisson's ratio, and density.
#. **Drucker-Prager:** This is used to define solid/granular material behavior under large strains. The material properties include Young's modulus, Poisson's ratio, density, and the Drucker-Prager parameters.
#. **Non-Associative Cam-Clay:** This is used to define solid/granular material behavior under large strains. The material properties include Young's modulus, Poisson's ratio, density, and the Non-Associative Cam-Clay parameters.


Material properties are defined in the ``Material`` tab and are specific to the chosen constitutive law/material model. The material properties include:

#. **Density:** This refers to the density of the material. This is defined in terms of the mass per unit volume. The units are generally in kg/m\ :sup:`3`.
#. **Young's Modulus:** This refers to the stiffness of the material. This is defined in terms of the force per unit area. The units are generally in Pa.
#. **Poisson's Ratio:** This refers to the ratio of the lateral strain to the longitudinal strain. This is a dimensionless quantity.
#. **Bulk Modulus:** This refers to the measure of the material's resistance to uniform compression. This is defined in terms of the force per unit area. The units are generally in Pa.
#. **Viscosity:** This refers to the measure of the material's resistance to flow. This is defined in terms of the force per unit area. The units are generally in Pa * sec.
