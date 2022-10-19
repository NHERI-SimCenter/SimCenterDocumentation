.. _sec_TInF-theory:
.. _chap_theory:

Theory
======

Introduction
------------

In computational wind engineering (CWE), generation of inflow turbulence satisfying prescribed mean-velocity profiles, turbulence spectra, spatial and temporal correlations is of great importance for the accurate evaluation of wind effects on buildings and structures. More specifically, the task is to generate a turbulent velocity field :math:`\mathbf{u}(\mathbf{x},t)` with the form

.. math::

        \mathbf{u}(\mathbf{x},t) = \mathbf{U}(\mathbf{x},t)+\mathbf{u}'(\mathbf{x},t)


where :math:`\mathbf{U}(\mathbf{x},t)` and :math:`\mathbf{u}'(\mathbf{x},t)` are the mean and fluctuating velocities at the position :math:`\mathbf{x}`. The turbulent velocity field :math:`\mathbf{u}` and its fluctuation :math:`\mathbf{u}'` need to satisfy a number of properties which are list below:

* :math:`\mathbf{u}'` should be spatially and temporally correlated.

* :math:`\mathbf{u}'` needs to have prescribed Reynolds stresses tensor :math:`R_{ij}(\mathbf{x}) = \langle u_i'u_j'\rangle(\mathbf{x})` where :math:`u_i'` (:math:`i=1,2,3`) is the :math:`i`-th component of :math:`\mathbf{u}'`  and the angles denote the time average.

* :math:`\mathbf{u}'` needs to have prescribed integral length scales :math:`L_{ij}(\mathbf{x},\mathbf{e})`

.. math::

        L_{ij}(\mathbf{x},\mathbf{e}) = \int_{0}^{\infty} \rho_{ij}(\mathbf{x},r\mathbf{e})\ \mathrm{d}r,


where :math:`\rho_{ij}(\mathbf{x},\mathbf{e})` is the correlation function given by

.. math::

        \rho_{ij}(\mathbf{x},\mathbf{e}) = \frac{\langle u_i'(\mathbf{x},t)u_j'(\mathbf{x}+\mathbf{e},t)\rangle}{\langle u_i'(\mathbf{x},t)u_j'(\mathbf{x},t) \rangle}.


* :math:`\mathbf{u}` should fulfil the divergence free constraint :math:`\nabla \cdot \mathbf{u} = 0`.

* :math:`\mathbf{u}'` should have prescribed correlation functions :math:`\rho_{ij}(\mathbf{x},\mathbf{e})` or spectra.

Several methodologies have been proposed for this purpose which can be classified into three general categories: precursor simulation methods, recycling methods and synthetic methods. Compared with precursor simulation and recycling methods, the synthetic methods in general offer a more practical and relatively efficient approach to generate inflow turbulence, and is therefore chosen as the subject of this section. Research activities on synthetic turbulence generation have been vigorous over the past decades and have branched out into several categories of techniques :cite:`wu2017`, including the synthetic random Fourier method :cite:`kraichnan1970,hoshiya1972`, the synthetic digital filtering method :cite:`klein2003` and the synthetic eddy methods :cite:`jarrin2006`. A brief introduction regarding to these techniques is given below and emphasis is placed on their abilities to capture the statistical characteristics as well as the spatial and temporal coherence of turbulence. Also note that since real turbulence is very complex, in most cases, not all of the above listed features can be fulfilled. There is always some adaptation time required for the artificial turbulence to evolve into real turbulence. Fulfilling the properties above with the synthetic turbulence is important to minimize the adaptation time or length.

Synthetic Random Fourier Method
-------------------------------

The so-called synthetic random Fourier method (SRFM) attempts to model turbulent flow field indirectly by imposing constraints on uncorrelated random fields through an energy spectrum to account for the spatial and temporal correlations, which can be further classified into two groups.
The first group of the SRFM was based on the pioneering work in :cite:`hoshiya1972` and :cite:`shinozuka1972` on the simulation of multi-correlated random processes using a weighted amplitude wave superposition (WAWS) method. This approach has an advantage that both the targeted power- and cross-spectra can be imposed in the generation process so that the prescribed target characteristics can be maintained. A major drawback of this method is that the generated turbulence does not satisfy the continuity equation of the flow, or in other words, the divergence-free condition is not guaranteed. As a consequence it would take enormous effort for the solver to enforce the continuity by correcting the turbulence inflow inserted into the computational domain, and the statistical characteristics of the corrected flow field differs from the target values.

The second group of the SRFM was initiated by the work in :cite:`kraichnan1970` on divergence-free homogeneous isotropic turbulence synthesis through the superposition of random harmonic functions. :cite:`smirnov2001` took a step forward by combing Kraichnan's technique with scaling and orthogonal transformation operations in a procedure known as the random flow generation (RFG) which allows to generate inhomogeneous and anisotropic turbulence. However the scaling operation introduced in the RFG technique can result in a velocity field that is not divergence-free for inhomogeneous turbulence. Modifications to enforce the divergence-free constraint for inhomogeneous turbulence was discussed in :cite:`yu2014`. A major drawback of RFG technique is that the power-spectra of the generated turbulence only follows Gaussian's spectra model, so it is not suitable for simulating flows in atmospheric boundary layer. :cite:`huang2010` revisited Kraichnan's method and proposed a technique called DSRFG (for discretizing and synthesizing random flow generation) which allows to generate turbulence from any prescribed spectrum. Instead of using the scaling and orthogonal transformation, the anisotropy of turbulence is realized by modifying the distribution strategy of the wave vector in Kraichnan's original method. A drawback of the DSRFG technique is that it produces fluctuating velocities with high correlation due to the fact that in this method the spatial correlation is modelled by a parameter which is not a function of frequency but a constant value. Inspired by the DSRFG method, :cite:`castro2017` proposed some modifications to this technique to obtain the velocity field that had a better match with the target turbulent statistics. This method, known as modified discretizing and synthesizing random flow generation (MDSRFG), is capable of removing the dependence of statistic quantities of synthetic turbulence on spectra discretization resolution. :cite:`aboshosha2015` also proposed a technique called consistent discrete RFG (CDRFG) to accurately model the target spectra and the coherence function. In both two methods mentioned above, the parameter that characterizes the spatial correlation is expressed as a function of frequency to account for the damping of coherence with the increase of frequency. An attractive feature of second group of SRFM is that the generation procedures are usually independent at each point and each time-instant so that it can be easily accelerated by conducting parallel computation, although the generated random flow may not satisfy the continuity equation.


.. _sectionDFM:

Digital Filtering Method
------------------------

The digital filtering method (DFM) initiated by :cite:`klein2003` attempts to model the spatial and temporal coherence of inflow turbulence through the digital filtering uncorrelated random data, and account for inhomogeneity and anisotropy using the method proposed by :cite:`lund1998`. It is relatively easy to implement and is able to reproduce the first and second order one-point statistics as well as auto-correlation function. However, the synthetic turbulence generated by DFM does not satisfy the continuity equation. :cite:`kim2013` offered a promising approach to enforce the divergence-free constraint in the DFM by inserting the synthetic turbulence on a transverse plane near the inlet and relying on pressure-velocity coupling to do the correction. From a computational wind engineering point of view, the ability of DFM to impose a two-point spatial correlation directly is very attractive.

A brief introduction on the filtering method by :cite:`klein2003` is stated as follows. In order to create two-point correlations, let :math:`r_m` be a series of random data with zero mean and unity variance, then

.. math::

        u_m = \sum_{n=-N}^N b_n r_{m+n}


defines a convolution or a digital linear non-recursive filter. The :math:`b_n` are filter coefficients and :math:`N` is related to the length of the filter. The independence between two different random numbers :math:`r_m` and :math:`r_n` implies that :math:`\langle r_m r_n \rangle = 0` for :math:`m \neq n` and consequently the two-point correlation between :math:`u_{m}` and :math:`u_{m+k}` writes

.. math::
        :label: SDF1
        
        R_{uu}(k\Delta x) = \frac{\langle u_{m} u_{m+k} \rangle}{\langle u_{m} u_{m} \rangle} = \sum_{j=-N+k}^N b_j b_{j-k} / \sum_{j=-N}^N b_j^2


where :math:`\Delta x` is the grid spacing. Note that :math:`u_{m}` and :math:`u_{m+k}` can be interpolated as the values of a random variable field (e.g., velocity) at two distinct grid points with a distance :math:`k\Delta x` defined on a one dimensional axis. It is straightforward to tell :eq:`SDF1` defines a relation between the filter coefficients and the correlation function of :math:`u_m` (denoted by :math:`R_{uu}` hereafter). This suggests that a prescribed correlation function can be reproduced through a careful determination of the filter coefficients. Also note that the coefficients should be determined such that the resulting correlation function fulfil some basic properties like :math:`R_{uu}(0)=1`, :math:`R_{uu}(\infty) = 0` and the prescribed integral length scales.

For a general target correlation function, the filter coefficients :math:`b_n` can be computed by solving a system of non-linear equations in the form of :eq:`SDF1` with a multidimensional Newton iteration method. The procedure can be taken from a standard textbook and needs no further comment. However, for a Gaussian or an exponential type of correlation function, there exists a simple but approximate prescribed solution. More specifically, for a Gaussian correlation function in the form of

.. math::
        :label: gaussian
        
        R(r) = \mathrm{exp}\left(-\frac{\pi r^2}{4L^2}\right)


where :math:`r` is the distance and :math:`L` is the length scale. It is possible to approximately reproduce :eq:`gaussian` by computing the filter coefficients as

.. math::

        b_k = \tilde{b}_k / \left( \sum_{j=-N}^N \tilde{b}_j^2 \right)^{1/2}


where

.. math::

        \tilde{b}_k = e^{-\frac{\pi k^2}{2n^2}}


The width :math:`N` of the filter should be chosen such that :math:`N\geq 2n` (where :math:`n=L\Delta x_1`) to ensure the accuracy of the approximation. On the other hand, for an exponential correlation function

.. math::

        R(r) = \mathrm{exp}\left(-\frac{\pi |r|}{2L}\right)


It is suggested by :cite:`xie2008` to evaluate the filter coefficients using

.. math::
        :label: exponential
        
        b_k = \tilde{b}_k / \left( \sum_{j=-N}^N \tilde{b}_j^2 \right)^{1/2}


where

.. math::

        \tilde{b}_k = e^{-\frac{\pi|k|}{n}}


Again, the width :math:`N` of the filter should be chosen such that :math:`N\geq 2n` (where :math:`n=L\Delta x`) to ensure the accuracy of the approximation. Now we have finished the discussion of the digital filtering method for one-dimensional case. Such a technique of generating spatially (or temporally) correlated data from general random numbers can be easily extended to three dimensional case by introducing multi-index filter coefficients :math:`b_{ijk}` defined as

.. math::

        b(i,j,k) = b_{ijk} = b_i \cdot b_j \cdot b_k


An algorithm for generating inflow data may look like this (alternatively one can generate a large volume of data, store it and convect it through the inflow plane by applying Taylor's hypothesis):

(a) Choose for each coordinate direction corresponding to the inflow plane a length scale :math:`L_{22} = n_2\Delta x_2`, :math:`L_{33} = n_3\Delta x_3`, a time scale :math:`T` and determine the filter width :math:`N_{\alpha}` (:math:`\alpha =1,2,3`) accordingly.

(b) Initialize and store three random fields :math:`R_{\alpha}` (again :math:`\alpha =1,2,3`) of dimensions :math:`[-N_1:N_1,-N_2+1:M_2+N_2,-N_3+1:M_3+N_3]` where :math:`M_2 \times M_3` denotes the dimensions of computational gird of the inflow plane.

(c) Compute the filter coefficients :math:`b(i,j,k)` with a prescribed function or by a multidimensional Newton method such that the resulting correlation function :eq:`SDF1` meets the target one.

(d) Applying the following filter operation for :math:`j=1,\ldots,M_2`, :math:`k=1,\ldots,M_3`

.. math::

        \Psi_{\alpha}(j,k) = \sum_{i'=-N_1}^{N_1}\sum_{j'=-N_2}^{N_2}\sum_{k'=-N_3}^{N_3}b(i',j',k')R_{\alpha}(i',j+j',k+k')

which yields the two-dimensional arrays of spatially correlated data :math:`\Psi_{\alpha}`, :math:`\alpha =1,2,3`.

(e) Output velocity data with the transformation

.. math::

        u_i(j,k) = U_i + a_{ij}\Psi_j(j,k)


where the coefficients :math:`a_{ij}` are given by :eq:`LundCoefficients`. This step ensures the synthetic velocity reproduces the target mean velocity and Reynolds stress tensor.

(f) Discard the first :math:`(x_2,x_3)`-plane of :math:`\Psi_{\alpha}` and shift the whole data: :math:`\Psi_{\alpha}(i,j,k) = R_{\alpha}(i+1,j,k)`. Fill the plane :math:`R_{\alpha}(N_1,j,k)` with new random numbers.

(g) Repeat the steps (d):math:`\sim`(g) for each time step.

If the target correlation function is an exponential function, an alternative approach by :cite:`xie2008` can be adopted for generating inflow turbulence which turns out to be much more efficient than the method of :cite:`klein2003`. Instead of using the filtering operation discussed above, the method of :cite:`xie2008` obtain the temporal correlation with the expression

.. math::
        :label: temporalCorrelation
        
        \Psi_{\alpha}(t+\Delta t,j,k) = \Psi_{\alpha}(t,j,k)\mathrm{exp}\left(-\frac{\pi \Delta t}{2T} \right)+\varPsi_{\alpha}(t,j,k)\left[1-\mathrm{exp}\left(-\frac{\pi \Delta t}{T} \right)\right]^{0.5}


where :math:`\Psi_{\alpha}(t,j,k)` and :math:`\varPsi_{\alpha}(t,j,k)` are two set of spatially-correlated random data resulting from a two dimensional filtering operation. For simplicity, we write :math:`\Psi_{\alpha,0}`, :math:`\Psi_{\alpha,k}`, :math:`\varPsi_{\alpha,0}` and :math:`\varPsi_{\alpha,k}` for :math:`\Psi_{\alpha}(t,j,k)`, :math:`\Psi_{\alpha}(t+k\Delta t,j,k)`, :math:`\varPsi_{\alpha}(t,j,k)` and :math:`\varPsi_{\alpha}(t+k\Delta t,j,k)`, respectively. One easily verifies that

.. math::

        \begin{split}
        \left\langle \Psi_{\alpha,0}\Psi_{\alpha,k} \right\rangle &= \left\langle \Psi_{\alpha,0}\left\{\Psi_{\alpha,k-1}\left(-\frac{\pi \Delta t}{2T} \right)+ \varPsi_{\alpha,k-1}\left[1-\mathrm{exp}\left(-\frac{\pi \Delta t}{T} \right)\right]^{0.5}\right\}\right\rangle \\
        & = \left\langle \Psi_{\alpha,0} \Psi_{\alpha,k-1} \right\rangle \mathrm{exp}\left(-\frac{\pi \Delta t}{2T}\right) \\
        & \cdots \\
        & = \mathrm{exp}\left(-\frac{k\pi \Delta t}{2T}\right)
        \end{split}


which reproduces an exponential function. An overall algorithm for generating the inflow velocity supported by the method of :cite:`xie2008` can be stated as follows

(a) Choose for each coordinate direction corresponding to the inflow plane a length scale :math:`L_{22} = n_2\Delta x_2`, :math:`L_{33} = n_3\Delta x_3`, a time scale :math:`T` and determine the filter width :math:`N_{\alpha}` (:math:`\alpha =1,2,3`) accordingly.

(b) Initialize and store three random fields :math:`R_{\alpha}` (again :math:`\alpha =1,2,3`) of dimensions :math:`[-N_2+1:M_2+N_2,-N_3+1:M_3+N_3]` where :math:`M_2 \times M_3` denotes the dimensions of computational gird in the inflow plane.

(c) Compute the filter coefficients :math:`b(j,k)` with a prescribed function or by a multidimensional Newton method such that the resulting correlation function meet the target one.

(d) Applying the following filter operations for :math:`j=1,\ldots,M_2`, :math:`k=1,\ldots,M_3`

.. math::

        \varPsi_{\alpha}(j,k) = \sum_{j'=-N_2}^{N_2}\sum_{k'=-N_3}^{N_3}b(j',k')R_{\alpha}(j+j',k+k')


which yields the two-dimensional arrays of spatially correlated data :math:`\varPsi_{\alpha}`, :math:`\alpha =1,2,3`.

(e) Compute :math:`\Psi_{\alpha}(j,k)` with :eq:`temporalCorrelation` and output the velocity signal with the transformation

.. math::

        u_i(j,k) = U_i + a_{ij}\Psi_j(j,k)


where the coefficients :math:`a_{ij}` are given by :eq:`LundCoefficients`. Again, this step ensures the synthetic velocity reproduces the target mean velocity and Reynolds stress tensor.

(f) Repeat the steps (d) :math:`\sim` (f) for each time step.


.. _sectionSEM:

Synthetic Eddy Method
---------------------

The synthetic eddy method (SEM) initiated by :cite:`jarrin2006` is based on the classical view of turbulence as a superposition of the representative coherent eddies. In the SEM, the flow is assumed to consist of randomly distributed turbulent spots, and each turbulent spot is modelled by a three-dimensional shape function with compact support and satisfies a proper normalization condition. The spots are then assumed to be convected through an inlet plane with a reference velocity using Taylor's frozen turbulence hypothesis. The resulting inflow turbulence is then reconstructed using the method proposed by to recover the desired statistical characteristics and to account for the conditions of inhomogeneity and anisotropy. The choice of the shape function plays an important role in the SEM since it is directly related to the two-point auto-correlation function, and consequently the power spectrum of the synthetic turbulence. Enforcement of the continuity condition in the SEM was discussed in :cite:`poletto2013` which will be introduced later.

A brief introduction on the SEM presented by :cite:`jarrin2006` is given as follows. To start with, the turbulent spot mentioned above can be represented as eddies defined by shape function :math:`f` which has a compact support on :math:`[-1,1]` and has the normalization

.. math::
        :label: normalization
        
        \int_{-1}^1 f^2(x) \mathrm{d}x = 1


The inflow plane on which we want to generate the synthetic turbulence with the SEM is basically a finite set of points :math:`S = \{\mathbf{x}_1,\mathbf{x}_2,\ldots,\mathbf{x}_s\}`. The first step is to create a box of eddies :math:`B` surrounding :math:`S` which is going to contain the synthetic eddies. It is defined by

.. math::

        B = \big\{(x_1,x_2,x_3)\in \mathbb{R}^3: x_{i,\text{min}}<x_i<x_{i,\text{max}}\big\}


where

.. math::

        x_{i,\text{min}} = \text{min}(x_i-\sigma_i(\mathbf{x})), \quad x_{i,\text{max}} = \text{max}(x_i+\sigma_i(\mathbf{x})), \quad \mathbf{x}\in S


The volume of the box of eddies is noted by :math:`V_B`. In the synthetic eddy method, the velocity signal generated by :math:`N` eddies has the representation

.. math::
        :label: SEMvelocity
        
        u_i(\mathbf{x}) = U_i(\mathbf{x}) + \frac{1}{\sqrt{N}}\sum_{k=1}^N a_{ij} \epsilon_j^k f_{\mathbf{\sigma}(\mathbf{x})}(\mathbf{x}-\mathbf{x}^k)


where :math:`\mathbf{x}` represent the coordinates of computational points and :math:`\mathbf{x}^k` represent the coordinates of eddies. The coefficient :math:`a_{ij}` results from the Cholesky decomposition of a prescribed Reynolds stress tensor :math:`R_{ij}`

.. math::
        :label: LundCoefficients
        
        \left(\begin{matrix}
        \sqrt{R_{11}} & 0 & 0 \\
        R_{21}/a_{11} & \sqrt{R_{22}-a_{21}^2} & 0 \\
        R_{31}/a_{11}  & (R_{32}-a_{21}a_{31})/a_{22} & \sqrt{R_{33}-a_{31}^2--a_{32}^2}
        \end{matrix}\right)


The coefficient :math:`\epsilon_j^k` (:math:`j=1,2,3`) is is the uniformly random intensity factor of values :math:`+1` or :math:`-1`, and :math:`f_{\mathbf{\sigma}(\mathbf{x})} (\mathbf{x}-\mathbf{x}^k)` is the velocity distribution at :math:`\mathbf{x}` of the eddy located at :math:`\mathbf{x}^k` defined as follows:

.. math::
        :label: eddyType
        
        f_{\mathbf{\sigma}(\mathbf{x})} (\mathbf{x}-\mathbf{x}^k) = \sqrt{\frac{V_B}{\sigma_1\sigma_2\sigma_3}}f\left(\frac{x_1-x_1^k}{\sigma_1}\right)f\left(\frac{x_2-x_2^k}{\sigma_2}\right)f\left(\frac{x_3-x_3^k}{\sigma_3}\right)


where :math:`\mathbf{\sigma}=(\sigma_1,\sigma_2,\sigma_3)^T`. The position of the eddies :math:`\mathbf{x}^k` before the first time step are independent from each other and taken from a uniform distribution over the box of eddies :math:`B`. The eddies are convected through the box of eddies :math:`B` with the mean velocity :math:`\mathbf{U}(\mathbf{x})`. At each time step, the new position of eddy :math:`k` is given by

.. math::

        \mathbf{x}^k(t+\Delta t) = \mathbf{x}^k(t)+\mathbf{U}(\mathbf{x}^k)\Delta t


where :math:`\Delta t` is the time step of the simulation. If an eddy :math:`k` is convected out of the box :math:`B`, then it is immediately regenerated randomly with in the region

.. math::

        B_{\Delta t} = \left\{ \mathbf{x}\notin B, \ \mathbf{x}+\mathbf{U}(\mathbf{x})\Delta t \in B \right\}


with a new random intensity vector :math:`\epsilon_j^k`. :math:`B_{\Delta t}` denotes the region in which regenerated eddy :math:`\mathbf{x}^k(t) \in B_{\Delta t}` dose not effect the synthetic velocity at the inflow plane until the next time-step.

Mean Flow and Reynolds Stresses
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The mean value of the velocity signal :eq:`SEMvelocity` can be expressed as

.. math::

        \left\langle u_i \right\rangle = U_i(\mathbf{x}) + \frac{1}{\sqrt{N}}\sum_{k=1}^N \left\langle a_{ij} \varepsilon_j^k f_{\mathbf{\sigma}(\mathbf{x})}(\mathbf{x}-\mathbf{x}^k) \right\rangle


where the angles denote the mean operator. The independence between the random variables :math:`\mathbf{x}^k` and :math:`\varepsilon_j^k` in the mean operator implies that

.. math::

        \left\langle a_{ij} \varepsilon_j^k f_{\mathbf{\sigma}(\mathbf{x})}(\mathbf{x}-\mathbf{x}^k) \right\rangle = a_{ij} \left\langle\varepsilon_j^k\right\rangle  \left\langle f_{\mathbf{\sigma}(\mathbf{x})}(\mathbf{x}-\mathbf{x}^k)  \right\rangle


The term :math:`\langle\varepsilon_j^k\rangle = 0` since the intensities of the eddies is either :math:`1` or :math:`-1` with equal probability. Consequently, we obtain

.. math::

        \left\langle u_i \right\rangle = U_i(\mathbf{x}).


The Reynolds stresses :math:`\langle u_i u_j \rangle` of the synthesized write

.. math::

        \langle u_i u_j \rangle = \frac{1}{N}\sum_{k=1}^N\sum_{k=1}^N a_{im}a_{jn} \langle \varepsilon_m^k \varepsilon_n^l \rangle \langle f_{\mathbf{\sigma}(\mathbf{x})}(\mathbf{x}-\mathbf{x}^k) f_{\mathbf{\sigma}(\mathbf{x})}(\mathbf{x}-\mathbf{x}^l) \rangle


Using again the independence between the random variables :math:`\mathbf{x}^k` and :math:`\varepsilon_j^k`, the above equation reduces to

.. math::

        \langle u_i u_j \rangle = \frac{1}{N}\sum_{k=1}^N a_{im}a_{jm} \langle f_{\mathbf{\sigma}(\mathbf{x})}^2(\mathbf{x}-\mathbf{x}^k)


The term

.. math::

        \langle f_{\mathbf{\sigma}(\mathbf{x})}^2(\mathbf{x}-\mathbf{x}^k) \rangle = \int_{\mathbb{R}^3} p(\mathbf{y}) f_{\mathbf{\sigma}(\mathbf{x})}^2(\mathbf{x}-\mathbf{x}^k) = 1


follows from the fact that :math:`\mathbf{x}^k` follows a uniform distribution over :math:`B`, i.e.

.. math::
        :label: distribution
        
        p(\mathbf{y}) =
        \begin{cases}
        \frac{1}{V_B} & \mathbf{y} \in B \\
        0 & \mathbf{y} \notin B
        \end{cases}.


Finally, we arrive at

.. math::
        :label: ReynoldsStresses
        
        \langle u_i u_j \rangle = \frac{1}{N}\sum_{k=1}^N a_{im}a_{jm} = R_{ij}


Hence the Reynolds stresses of the velocity fluctuations generated by the SEM reproduce exactly the input Reynolds stresses.

Two-point Correlation
^^^^^^^^^^^^^^^^^^^^^

The two-point cross-correlation of the velocity fluctuations writes

.. math::
        :label: twoPointCorrelations0
        
        R_{ij}(\mathbf{x},\mathbf{r}) = \langle u_i(\mathbf{x},t) u_j(\mathbf{x}+\mathbf{r},t) \rangle


where :math:`\mathbf{r} = (r_1,r_2,r_3)` is a vector defining the relative positions between the two points at which the velocity correlations are computed. By :eq:`SEMvelocity` and the linearity of the statistical mean, we obtain

.. math::

        R_{ij}(\mathbf{x},\mathbf{r}) = \frac{1}{N}\sum_{k=1}^N\sum_{k=1}^N a_{im}a_{jn} \langle \varepsilon_m^k \varepsilon_n^l \rangle \langle f_{\mathbf{\sigma}(\mathbf{x})}(\mathbf{x}-\mathbf{x}^k) f_{\mathbf{\sigma}(\mathbf{x}+\mathbf{r})}(\mathbf{x}+\mathbf{r}-\mathbf{x}^l) \rangle


Using again the independence between the positions :math:`\mathbf{x}^k` and the intensities :math:`\varepsilon^k` of the eddies, this yields

.. math::
        :label: twoPointCorrelations1
        
        R_{ij}(\mathbf{x},\mathbf{r}) = \frac{1}{N}\sum_{k=1}^N a_{im}a_{jm} \langle f_{\mathbf{\sigma}(\mathbf{x})}(\mathbf{x}-\mathbf{x}^k) f_{\mathbf{\sigma}(\mathbf{x}+\mathbf{r})}(\mathbf{x}+\mathbf{r}-\mathbf{x}^k) \rangle


By :eq:`distribution`, the term in the mean operator writes

.. math::
        :label: twoPointCorrelations2
        
        \langle f_{\mathbf{\sigma}(\mathbf{x})}(\mathbf{x}-\mathbf{x}^k) f_{\mathbf{\sigma}(\mathbf{x}+\mathbf{r})}(\mathbf{x}+\mathbf{r}-\mathbf{x}^k) \rangle = \frac{1}{V_B} \int_B f_{\mathbf{\sigma}(\mathbf{x})}(\mathbf{x}-\mathbf{y}) f_{\mathbf{\sigma}(\mathbf{x}+\mathbf{r})}(\mathbf{x}+\mathbf{r}-\mathbf{y}) \mathrm{d}\mathbf{y}


Inserting :eq:`twoPointCorrelations2` back to :eq:`twoPointCorrelations1` and using :eq:`eddyType`, this yields

.. math::
        :label: twoPointCorrelations3
        
        R_{ij}(\mathbf{x},\mathbf{r}) = R_{ij} \cdot \prod_{l=1}^3 \left[f_{\mathbf{\sigma}(\mathbf{x})} *f_{\mathbf{\sigma}(\mathbf{x}+\mathbf{r})} \right](r_l)


where :math:`*` denotes the convolution product. For homogeneous turbulence where integral length scales :math:`\mathbf{\sigma}(\mathbf{x}) = \mathbf{\sigma}(\mathbf{x}+\mathbf{r}) =(\sigma,\sigma,\sigma)^T`, the two-point cross-correlation tensor :math:`R_{ij}(\mathbf{x},\mathbf{r})` only depends on :math:`\mathbf{r}` and consequently :eq:`twoPointCorrelations3` simplifies to

.. math::
        :label: twoPointCorrelations4
        
        R_{ij}(\mathbf{r}) = R_{ij} \cdot \prod_{l=1}^3 \left[f*f\right]\left(\frac{r_l}{\sigma}\right)


Recall the integral length scale :math:`L_{ij}` is defined as the integral of the two-point correlation :math:`R_{ij}(\mathbf{x},\mathbf{r})` in a particular direction and is thus proportional to :math:`\sigma`. By integrating :eq:`twoPointCorrelations4`, one easily verifies that (for homogeneous turbulence) :math:`L_{ij}=C_f\sigma` in every direction where :math:`C_f` only depends on the choice of :math:`f`.

Fourier analysis can also be used to obtain the spectra of the synthetic turbulence. Note that the velocity spectrum tensor :math:`\phi_{ij}(k)` is the Fourier transform of the two-point correlation tensor

.. math::

        \phi_{ij}(\mathbf{k}) = \mathcal{F}_{\mathbf{k}}\left\{R_{ij}(\mathbf{r})\right\}


Recall the convolution theorem for cross-correlation states that

.. math::

        \mathcal{F}_{\mathbf{k}}\left\{f * f\right\} = |\mathcal{F}_{\mathbf{k}}\left\{f\right\}|^2


Hence the spatial velocity spectrum tensor can be expressed as

.. math::

        \phi_{ij}(\mathbf{k}) = R_{ij}\sigma^3 \cdot \prod_{l=1}^3|\mathcal{F}_{k_l\sigma}\left\{f\right\}|^2


where :math:`\mathbf{k} = (k_1,k_2,k_3)`. More specifically for instance, the one-dimensional spectra in the :math:`x` direction is

.. math::

        E_{ij}(k) = R_{ij}\sigma^3 \cdot |\mathcal{F}_{k_l\sigma}\left\{f\right\}|^2


Two-time Correlation
^^^^^^^^^^^^^^^^^^^^

The two-time correlation tensor of the velocity, denoted by :math:`R_{ij}(\mathbf{x},\tau)`, is the correlation between :math:`u_i(\mathbf{x},t)` and :math:`u_j(\mathbf{x},t+\tau)` at times :math:`t` and :math:`t+\tau` respectively, i.e.,

.. math::
        :label: twoTimeCorrelation0
        
        R_{ij}(\mathbf{x},\tau) = \langle u_i(\mathbf{x},t) u_j(\mathbf{x},t+\tau) \rangle.


By :eq:`SEMvelocity` and the linearity of the statistical mean, we have

.. math::
        :label: twoTimeCorrelation1
        
        R_{ij}(\mathbf{x},\tau) = \frac{1}{N}\sum_{k=1}^N\sum_{k=1}^N a_{im}a_{jn} \langle \varepsilon_m^k(t) \varepsilon_n^l(t+\tau) f_{\mathbf{\sigma}(\mathbf{x})}(\mathbf{x}-\mathbf{x}^k(t)) f_{\mathbf{\sigma}(\mathbf{x})}(\mathbf{x}-\mathbf{x}^l(t+\tau)) \rangle


The independence between the position :math:`\mathbf{x}^k` and intensity :math:`\varepsilon_m^k` of different eddies implies that, for :math:`k \neq l`, the statistical mean in :eq:`twoTimeCorrelation1` can be split as follows

.. math::

        \langle \varepsilon_m^k(t) \rangle \langle \varepsilon_n^l(t+\tau) \rangle \langle f_{\mathbf{\sigma}(\mathbf{x})}(\mathbf{x}-\mathbf{x}^k(t)) \rangle \langle f_{\mathbf{\sigma}(\mathbf{x})}(\mathbf{x}-\mathbf{x}^l(t+\tau)) \rangle = 0


Consequently :eq:`twoTimeCorrelation1` reduces to

.. math::
        :label: twoTimeCorrelation2
        
        R_{ij}(\mathbf{x},\tau) = \frac{1}{N}\sum_{k=1}^N a_{im}a_{jn} \langle \varepsilon_m^k(t) \varepsilon_n^k(t+\tau) f_{\mathbf{\sigma}(\mathbf{x})}(\mathbf{x}-\mathbf{x}^k(t)) f_{\mathbf{\sigma}(\mathbf{x})}(\mathbf{x}-\mathbf{x}^k(t+\tau)) \rangle


Before computing the term in the angles, we define :math:`B_{\tau} \in B`  such that all eddies that present in :math:`B_{\tau}` at time :math:`t` will be convected far enough so that they will be recycled at least once before time :math:`t+\tau`

.. math::

        B_{\tau} = \left\{\mathbf{x}\in B, \ \mathbf{x}+\tau \mathbf{U}(\mathbf{x}) \in B \right\}


If :math:`\mathbf{x}^k(t)\in B_{\tau}`, then it is going to be recycled between time :math:`t` and :math:`t+\tau` and hence both :math:`\mathbf{x}^k(t+\tau)` and :math:`\varepsilon_m^k(t+\tau)` will be independent of their previous values. The contribution of an eddy :math:`k` located within the region where :math:`\mathbf{x}^k(t) \in B_{\tau}` to the term in the angles of :eq:`twoTimeCorrelation2` is thus zero. On the contrary if :math:`\mathbf{x}^k(t) \in B_{\tau}`, the eddy :math:`k` will remain inside of the box :math:`B` at time :math:`t + \tau` and hence :math:`\varepsilon_m^k(t+\tau) =  \varepsilon_m^k(t)` and :math:`\mathbf{x}^k(t+\tau) =\mathbf{x}^k(t)+\tau\mathbf{U}(\mathbf{x}^k)`. Thus both :math:`\varepsilon_n^k(t+\tau) =  \varepsilon_n^k(t)` and :math:`\mathbf{x}^k(t+\tau)` depend on the previous position :math:`\mathbf{x}^k(t)` of eddy :math:`k` relative to :math:`B_{\tau}`. By :eq:`ReynoldsStresses` and the definition of :math:`B_{\tau}`, :eq:`twoPointCorrelations0` can then be replaced by

.. math::
        :label: twoTimeCorrelation3
        
        R_{ij}(\mathbf{x},\tau) = R_{ij} \int_{B/B_{\tau}}f_{\mathbf{\sigma}(\mathbf{x})}(\mathbf{x}-\mathbf{y}) f_{\mathbf{\sigma}(\mathbf{x})}(\mathbf{x}-(\mathbf{y}+\tau\mathbf{U}_c)) \ \mathrm{d}\mathbf{y}


The condition :math:`\mathbf{y}\in B_{\tau}` leads to :math:`f_{\mathbf{\sigma}(\mathbf{x})}(\mathbf{x}-(\mathbf{y}+\tau\mathbf{U}))=0`. Thus, the integral over :math:`B/B_{\tau}` in :eq:`twoPointCorrelations3` can be extended to an integral over :math:`B`. Besides :math:`\mathbf{y}\in B` suggests :math:`f_{\mathbf{\sigma}(\mathbf{x})}(\mathbf{x}-\mathbf{y})=0` as previously demonstrated, therefore the integral in :eq:`twoTimeCorrelation3` can be further extended to an integral over :math:`\mathbb{R}^3`. Using :eq:`eddyType`, this yields

.. math::
        :label: twoTimeCorrelation4
        
        R_{ij}(\mathbf{x},\tau) = R_{ij} \cdot \prod_{l=1}^3[f*f]\left(\frac{\tau U_{l}(\mathbf{x})}{\sigma_l(\mathbf{x})}\right)


In the case where the mean velocity is in the :math:`x_1`-direction only :math:`\mathbf{U} = (U,0,0)` and the target turbulence is homogeneous, :eq:`twoTimeCorrelation4` simplifies to

.. math::

        R_{ij}(\mathbf{x},\tau) = R_{ij} [f*f]\left(\frac{\tau U(\mathbf{x})}{\sigma(\mathbf{x})}\right)


Thus, the two-time correlation of the signal at time :math:`\tau` is simply the auto-correlation function of :math:`f` at separation distance :math:`\tau U /\sigma`. By integrating the above equation it can be proved that the integral time scale of the signal writes :math:`T = \sigma/U C_f` where :math:`C_f` is a coefficient only depends on the choice of :math:`f`. Since the synthetic velocity is a stationary process, the information the two-time cross-correlation tensor :math:`R_{ij}(\mathbf{x},\tau)` contains can be re-expressed in terms of the wave number velocity spectrum tensor which writes

.. math::

        \phi_{ij}(\mathbf{x},\omega) = \mathcal{F}_{\omega}\{R_{ij}(\mathbf{x},\tau)\}


Using again the convolution theorem, the above expression simplifies to

.. math::

        \phi_{ij}(\mathbf{x},\omega) = R_{ij}\frac{\sigma}{|U|} |\mathcal{F}_{\omega\sigma / |U|}\{f\}|^2


Commonly Used Velocity Shape Functions
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The three commonly used velocity shape functions for :math:`f` are given below for reference which are the tent function, the step function and the truncated Gaussian function.

* Tent function

.. math::
        :label: ftent
        
        f(x) =
        \begin{cases}
        \sqrt{\frac{3}{2}}(1-|x|), & 0 \leq |x| < 1 \\
        0, & |x| \geq 1
        \end{cases}

which yields

.. math::

        [f*f](r) =
        \begin{cases}
        1-\frac{3}{2}r^2+\frac{3}{4}|r|^3, & 0 \leq |r| < 1 \\
        2-3|r|+\frac{3}{2}r^2-\frac{1}{4}|r|^3, & 1 \leq |r| <2 \\
        0, & |r|\geq 2
        \end{cases}


* Step function

.. math::
        :label: fstep
        
        f(x) =
        \begin{cases}
        \frac{1}{\sqrt{2}}, & 0 \leq |x| < 1 \\
        0, & |x| \geq 1
        \end{cases}

which yields

.. math::

        [f*f](r) =
        \begin{cases}
        1-\frac{|r|}{2}, & 0 \leq |r| < 2 \\
        0, & |r|\geq 2
        \end{cases}


* Truncated Gaussian function

.. math::
        :label: fgaussian
        
        f(x) =
        \begin{cases}
        Ce^{-9x^2/2}, & 0 \leq |x| < 1 \\
        0, & |x| \geq 1
        \end{cases}

which yields

.. math::

        [f*f](r) =
        \begin{cases}
        e^{-9r^2/4} & 0\leq |r| < 2 \\
        0, & |r|\geq 2
        \end{cases}


where :math:`C` is a constant that ensures :math:`f` satisfies the normalization :eq:`normalization`.


.. _sectionDFSEM:

Divergence Free Synthetic Eddy Method
-------------------------------------

One route to obtain a divergence free method, as suggested by :cite:`poletto2013`, is to apply the original SEM methodology to the vorticity field, which is then transformed back to the velocity field by taking the curl of it. One easily verifies that vorticity and velocity fields are linked by the following:

.. math::

        \nabla\times\omega' = \nabla(\nabla\cdot\mathbf{u}')-\nabla^2\mathbf{u}'


Because of the hypothesis of incompressible flow, the first term on the right hand side of the above equation vanishes, leading to a Poisson equation for the velocity field. The solution of this Poisson equation, achieved by using the Biot–Savart kernel, leads to the fluctuating velocity field expressed as:

.. math::
        :label: DFSEMvelocity
        
        \mathbf{u}'(\mathbf{x}) = \sqrt{\frac{1}{N}}\sum_{k=1}^N\frac{q_{\sigma}(|\mathbf{r}^k|)}{|\mathbf{r}^k|}\mathbf{r}^k\times\alpha^k


where :math:`\mathbf{r}^k=(\mathbf{x}-\mathbf{x}^k)/\sigma^k`, :math:`q_{\sigma}(|\mathbf{r}^k|)` is a suitable shape function and :math:`\alpha_i^k` are random numbers with zero average which represent the eddy intensities.

Despite the similarities between :eq:`SEMvelocity` and :eq:`DFSEMvelocity`, i.e. both including a user defined shape function and a random level eddy intensity, the lack of Lund coefficients in the second formulation poses a significant problem. Their role in the original SEM was crucial in order to allow any given turbulence state to be generated, however, they cannot be re-introduced to :eq:`DFSEMvelocity` without forgoing the divergence free condition.

In order to increase the turbulence anisotropy reproduction capabilities, the method presented by :cite:`poletto2013` employs the formulation of :eq:`DFSEMvelocity`, but with an anisotropic length-scale, :math:`\sigma_i`, employed in each of the coordinate directions, and allows a different shape function to be associated with each direction. However, such a form no longer automatically satisfies the divergence-free condition ensured by :eq:`DFSEMvelocity`, and further constraints on the shape functions need to be considered in order to retain a divergence-free field.  :cite:`poletto2013` redefine the shape functions to be of the form :math:`q_{sigma}=q|\mathbf{r}^k|^3` where :math:`q` is a function which depends on the locations :math:`\mathbf{x}` and :math:`\mathbf{x}^k`, and :math:`\mathbf{r}^k` differs slightly from its previous definition, as it now takes into account the length-scale anisotropy :math:`\mathbf{r}_{\beta}^k=(\mathbf{x}_{\beta}-\mathbf{x}_{\beta}^k)/\sigma_{\beta}^k`. The new general formulation for the velocity fluctuations thus becomes:

.. math::
        :label: DFSEMvelocity2
        
        u_{\beta}'(\mathbf{x}) = \sqrt{\frac{1}{N}}\sum_{k=1}^N q_{\beta}\left(\mathbf{x},\mathbf{x}^k,\sigma^k\right) \epsilon_{\beta j l}r_j^k \alpha_l^k



In :eq:`DFSEMvelocity2`, the cross product presented in :eq:`DFSEMvelocity` has been rewritten using the index notation for tensors, where :math:`\epsilon_{ijl}` is the Levi–Civita symbol, and no summation is implied over Greek subscripts. As noted above, with the redefined shape functions, the form of :eq:`DFSEMvelocity2` no longer automatically satisfies the divergence-free condition. However, on substituting it into the condition that :math:`\nabla\cdot\mathbf{u}'=0`, a sufficient condition for ensuring a divergence-free velocity field can be found as:

.. math::
        r_2^k\frac{\partial q_1}{x_1} = r_1^k\frac{\partial q_2}{x_2},\quad
        r_3^k\frac{\partial q_2}{x_2} = r_2^k\frac{\partial q_3}{x_3},\quad
        r_1^k\frac{\partial q_3}{x_3} = r_3^k\frac{\partial q_1}{x_1}


A simple analytically function for :math:`q_i` that satisfies the above restrictions is:

.. math::
        :label: qequation
        
        q_i =
        \begin{cases}
        \sigma_i\left[1-(d^k)^2\right], & \text{if } d^k<1 \\
        0, & \text{elsewhere}
        \end{cases}


where :math:`d^k = \sqrt{(r_j^k)^2}`.

The function :math:`q_i` with the form :eq:`qequation` is continuous everywhere, but its derivative is not strictly defined for :math:`d^k=1`, where it is only possible to define a right or left sided derivative. The above formulation thus defines a divergence-free velocity field everywhere except at the eddy surface (:math:`d^k=1`), although this formal omission is not believed to result in serious problems. The expression for the velocity obtained by substituting :eq:`qequation` into :eq:`DFSEMvelocity2` can be written as:

.. math::
        :label: DFSEMvelocity3
        
        u_{\beta}'(\mathbf{x}) = \sqrt{\frac{1}{N}}\sum_{k=1}^N \sigma_{\beta}^k\left[1-(d^k)^2\right] \epsilon_{\beta j l}r_j^k \alpha_l^k


Time-averaging the product of :eq:`DFSEMvelocity3` with itself leads to an expression for the Reynolds stresses, from which one can examine how the prescription of the length-scales, :math:`\sigma_i^k`, and intensities, :math:`\alpha_i^k`, affect the stress anisotropy associated with the synthetically generated field given by :eq:`DFSEMvelocity3`:

.. math::
        :label: DFSEMtensor
        
        \left<u_{\beta}'u_{\gamma}'\right> = \frac{1}{N}\sum_{k=1}^N\sigma_{\beta}^k\sigma_{\gamma}^k \epsilon_{\beta j l} \epsilon_{\gamma m n}\left<\left\{\left[1-(d^k)^2\right]^2r_j^kr_m^k \right\}\right>\left<\alpha_l^k\alpha_n^k\right>


On examining :eq:`DFSEMtensor`, it is clear that the eddies are independent of each other, and that their intensities are uncorrelated (so :math:`\left<\alpha_l^k\alpha_n^k\right>` for :math:`l \neq m`); as such, the predicted shear stresses (:math:`\left<u_{\beta}'u_{\gamma}'\right>` for :math:`\beta\neq\gamma`) will be zero. In order to overcome this problem, fluctuations in the global coordinate system are computed via a standard rotation transformation of the eddies generated in the local principal axes coordinate system (where the Reynolds stress tensor is diagonal):

.. math::

        u_i^{G}(\mathbf{x}) = C_1 R_{im}^{P\rightarrow G}u_m^P


where :math:`R_{im}^{P\rightarrow G}` is the rotation transformation matrix from the principal to the global coordinate system, :math:`u_i^{P}` and :math:`u_i^{G}` are the velocity fluctuations in the principal axes and global systems respectively, and :math:`C_1` is a normalization coefficient required in order to have :math:`\left<(u_i')^2\right>=1` when :math:`\left<(\alpha_l^k)^2\right>=1`:

.. math::

        C_1 = \frac{\sqrt{10V_0}\sum_{i=1}^3\sigma_i/3}{\sqrt{N}\prod_{i=1}^3\sigma_i}\mathrm{min}\{\sigma_i\}


where :math:`V_0` is the eddy box volume. For the normal stresses, the contribution from the :math:`k`-th eddy in :eq:`DFSEMtensor` thus gives

.. math::

        \left<u_{\beta}'u_{\beta}'\right>=2C_2\sigma_{\beta}^2\epsilon_{\beta l n}\left<(\alpha_l^k)^2\right>\left<(\alpha_n^k)^2\right>



where all the terms not explicitly reported are represented by :math:`C_2`. The remaining issue is to choose appropriate length-scales and eddy intensities to ensure the above will return the desired Reynolds stress statistics, over a wide range of stress anisotropy levels. For any choice of length-scale ratios (:math:`\sigma_1/\sigma_2` and :math:`\sigma_1/\sigma_3`), varying the intensity :math:`\alpha_l^k` allows one to reproduce possible turbulence anisotropy states over a particular region of the Lumley triangle. For a given the Reynolds stresses are reproduced by defining the following intensities:

.. math::
        :label: DFSEMalpha
        
        \left<(\alpha_{\beta}^k)^2\right> = \frac{\lambda_j/\sigma_j^2-2\lambda_{\beta}/\sigma_{\beta}^2}{2C_2}


where :math:`\lambda` are the normal stresses in the local principal reference system. Since the right hand side of :eq:`DFSEMalpha` must be positive, for any value of :math:`\Gamma` it is only possible to reproduce a part of the Lumley triangle. By defining a series of ratios :math:`\Gamma = \frac{\sigma_1}{\sigma_2} = \frac{\sigma_1}{\sigma_3}`, each allowing one of the regions of the Lumley triangle to be mapped, the Reynolds stress statistics with a wide range of stress anisotropy levels can be reproduced.


.. _sectionATSM:

Turbulent Spot Method with Anisotropic Vorton
---------------------------------------------

Earlier versions of the synthetic eddy method and the turbulent spot method were only able to produce turbulence which does not obey the continuity constraint in general. This was only possible for special cases (isotropic or near-isotropic turbulence). The work of :cite:`kroger2018` utilizes another approach for introducing the anisotropy into the turbulent spots, which obeys continuity and allows to reproduce strong levels of anisotropy at the same time. Their approach is basically a continuation of the vorton formulation described in :cite:`kornev2007`. The generation is performed in the coordinate system :math:`(x_1,x_2,x_3)` determined by principle axes of the Reynolds stresses. The Reynolds stresses in any other system :math:`(x_1',x_2',x_3')` are calculated by :math:`R_{ij}' = E_{pi}R_{pq}E_{qj}`, where :math:`E_{ij}` is the rotation matrix describing coordinate transformation between :math:`(x_1,x_2,x_3)` and :math:`(x_1',x_2',x_3')` axes system. Integral lengths in different coordinate systems can be found from the relation:

.. math::
        :label: Ltransform
        
        L_{ii}(x_1',x_2',x_3') = \sum_{k=1}^3E_{ki}^2\frac{R_{kk}(x_1,x_2,x_3)}{R_{ii}'(x_1',x_2',x_3')}L_{kk}(x_1,x_2,x_3)


In :eq:`Ltransform`, the vector the vector potential is scaled by a function with spherical symmetry which in the case of the spectrum of decaying turbulence gives an analytic expression:

.. math::

        \mathbf{A}(x_1,x_2,x_3) = Ce^{-\frac{1}{2}k_0^2r^2}\mathbf{\gamma}


Also note that other spectra :math:`E(k)` could be used in principle. This would result in different shapes of the inner velocity distribution. For the sake of simplicity and because it yields reasonably simple formulas, the work of :cite:`kroger2018` is restricted to this spectrum.

The spherical symmetry of :math:`\mathbf{A}(x_1,x_2,x_3)` is the reason for the isotropy of turbulence generated using these vortons. At this level, anisotropy can be introduced by stretching the coordinates individually, i.e.,

.. math::

        x_1\rightarrow x_1/\sigma_1,\quad x_2\rightarrow x_2/\sigma_2,\quad x_3\rightarrow x_3/\sigma_3


With this, the vector potential and velocity induced by the vorton are now written as:

.. math::

        \mathbf{A}=\mathrm{exp}\left[-\frac{1}{2}\left(\frac{x_1^2}{\sigma_1^2}+\frac{x_2^2}{\sigma_2^2}+\frac{x_3^2}{\sigma_3^2}\right)\right]\left(\begin{matrix}x_1\gamma_1 \\ x_2\gamma_2 \\ x_3\gamma_3\end{matrix}\right)


.. math::
        :label: anisotropicU
        
        \mathbf{u}'=\mathrm{exp}\left[-\frac{1}{2}\left(\frac{x_1^2}{\sigma_1^2}+\frac{x_2^2}{\sigma_2^2}+\frac{x_3^2}{\sigma_3^2}\right)\right]\left(\begin{matrix}\left(\frac{\gamma_2}{\sigma_3^2}-\frac{\gamma_3}{\sigma_2^2}\right)x_2x_3 \\ \left(\frac{\gamma_3}{\sigma_1^2}-\frac{\gamma_1}{\sigma_3^2}\right)x_1x_3 \\ \left(\frac{\gamma_1}{\sigma_2^2}-\frac{\gamma_2}{\sigma_1^2}\right)x_1x_2\end{matrix}\right)


Note that the multiplication with the coordinates is introduced to make the resulting Reynolds stress tensor a diagonal tensor which is identified with the diagonal matrix of eigenvalues from a principal component analysis of the prescribed Reynolds stress tensor. By aligning the :math:`x_1`, :math:`x_2`, :math:`x_3`-directions of the vorton with the principal directions of the Reynolds stress tensor, arbitrary anisotropic Reynolds stresses can be reproduced. The vorton sizes :math:`\sigma_1`, :math:`\sigma_2` and :math:`\sigma_3` and strength vector components :math:`\gamma_1`, :math:`\gamma_2` and :math:`\gamma_3` are free parameters of the vorton and can be used to match the prescribed Reynolds stresses and integral length scales.

Statistical Properties of Anisotropic Vortons
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Statistical properties can be analytically derived for homogeneous turbulence. Consider a set of fully uncorrelated vortons, i.e. :math:`\langle\gamma_{ik}\gamma_{jm}\rangle` for each pair of :math:`k`-th and  :math:`m`-th vortons with strength components :math:`i` and :math:`j`, respectively. Then the Reynolds stress :math:`R_{ij}` of the total field is equal to the sum of Reynolds stresses produced by each vorton

.. math::

        R_{ij} = \langle u_i'u_j' \rangle = \sum_{i=1}^{N}\langle u_{ik}'u_{jk}'\rangle = \sum_{i=1}^{N}R_{ij,k}.


Without loss of generality, the magnitude of the strength is set as unity, i.e. :math:`|\pm\mathbf{\gamma}|=1`. Then, the expected value of the Reynolds stress :math:`R_{ij}` at the point :math:`(0,0,0)` is

.. math::

        R_{ij} = \int_V u_i'(\mathbf{\gamma},\mathbf{x})u_j'(\mathbf{\gamma},\mathbf{x})P(\mathbf{x})\mathrm{d}V


where :math:`P(\mathbf{x})` is the probability density function in the event that the vorton is placed at the point :math:`\mathbf{x}`. For the uniform distribution :math:`P(\mathbf{x}) = N/V` is the vorton density. If the computational domain becomes infinite :math:`N` should increase, so that the vorton density remains constant:

.. math::
        :label: anisotropicR
        
        R_{ij} = \int_{-\infty}^{\infty}\int_{-\infty}^{\infty}\int_{-\infty}^{\infty}u_i'u_j'\mathrm{d}x_1\mathrm{d}x_2\mathrm{d}x_3


Substitution of velocity induced by an anisotropic vorton :eq:`anisotropicU` in :eq:`anisotropicR` results in a simple formula for the principal Reynolds stresses:

.. math::

        \begin{split}
        &R_{11} = \frac{\pi^{3/2}}{4} \frac{\sigma_1(\gamma_2\sigma_2^2-\gamma_3\sigma_3^2)^2}{\sigma_2\sigma_3} \\
        &R_{22} = \frac{\pi^{3/2}}{4} \frac{\sigma_2(\gamma_1\sigma_1^2-\gamma_3\sigma_3^2)^2}{\sigma_1\sigma_3} \\
        &R_{33} = \frac{\pi^{3/2}}{4} \frac{\sigma_3(\gamma_1\sigma_1^2-\gamma_2\sigma_2^2)^2}{\sigma_1\sigma_2}
        \end{split}


Unfortunately, there is no possibility to change the auto-correlation function since the velocities in the form of :eq:`anisotropicU` uniquely predetermine them

.. math::
        \rho_{ij}(\eta_1,\eta_2,\eta_3) = \int_{-\infty}^{\infty}\int_{-\infty}^{\infty}\int_{-\infty}^{\infty} u_i'u_j'(\eta_1,\eta_2,\eta_3) \mathrm{d}x_1\mathrm{d}x_2\mathrm{d}x_3


The calculation gives:

.. math::
        :label: anisotropicAutocorrelation
        
        \begin{split}
            &\rho_{11}(\eta_1,\eta_2,\eta_3)  = Q\frac{\sigma_1}{\sigma_2^3\sigma_3^3}\left(\gamma_2\sigma_2^2-\gamma_3\sigma_3^2\right)^2\left(\eta_2^2-2\sigma_2^2\right)\left(\eta_3^2-2\sigma_3^2\right) \\
            &\rho_{22}(\eta_1,\eta_2,\eta_3)  = Q\frac{\sigma_2}{\sigma_1^3\sigma_3^3}\left(\gamma_1\sigma_1^2-\gamma_3\sigma_3^2\right)^2\left(\eta_1^2-2\sigma_1^2\right)\left(\eta_3^2-2\sigma_3^2\right) \\
            &\rho_{33}(\eta_1,\eta_2,\eta_3)  = Q\frac{\sigma_3}{\sigma_1^3\sigma_2^3}\left(\gamma_1\sigma_1^2-\gamma_2\sigma_2^2\right)^2\left(\eta_2^2-2\sigma_2^2\right)\left(\eta_1^2-2\sigma_1^2\right)
        \end{split}


with

.. math::

        Q = \frac{\pi^{3/2}}{16}\mathrm{exp}\left[-\frac{1}{4}\left(\frac{x_1^2}{\sigma_1^2}+\frac{x_2^2}{\sigma_2^2}+\frac{x_3^2}{\sigma_3^2}\right)\right]


Also the one dimensional spectra can be calculated analytically:

.. math::

        \begin{split}
            &\Theta_{11}(k_1,0,0) = \frac{1}{2\pi}\int_{-\infty}^{\infty}\rho_{11}(\eta_1,0,0)e^{ik_1\eta_1}\mathrm{d}\eta_1 = \frac{\pi}{8}\frac{\sigma_1^2}{\sigma_2\sigma_3}\left(\gamma_2\sigma_2^2-\gamma_3\sigma_3^2\right)^2 e^{-k_1^2\sigma_1^2} \\
            &\Theta_{22}(0,k_2,0) = \frac{1}{2\pi}\int_{-\infty}^{\infty}\rho_{22}(0,\eta_2,0)e^{ik_2\eta_2}\mathrm{d}\eta_2 = \frac{\pi}{8}\frac{\sigma_2^2}{\sigma_1\sigma_3}\left(\gamma_1\sigma_1^2-\gamma_3\sigma_3^2\right)^2 e^{-k_2^2\sigma_2^2} \\
            &\Theta_{33}(k_1,0,k_3) = \frac{1}{2\pi}\int_{-\infty}^{\infty}\rho_{33}(0,0,\eta_3)e^{ik_3\eta_3}\mathrm{d}\eta_3 = \frac{\pi}{8}\frac{\sigma_3^2}{\sigma_1\sigma_2}\left(\gamma_1\sigma_1^2-\gamma_2\sigma_2^2\right)^2 e^{-k_3^2\sigma_3^2}
        \end{split}

As seen, the dependence of the one-dimensional spectra on wave number :math:`e^{k^2}` is the same as that in isotropic decaying turbulence.

Determination of Anisotropic Vorton Parameters
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Integration of the auto-correlation functions :eq:`anisotropicAutocorrelation` reveals a simple and clear interpretation of stretching parameters :math:`\sigma_i`:

.. math::
        :label: anisotropicScale
        
        \begin{split}
        &L_{11} = \int_0^{\infty}\rho_{11}(\eta_1,0,0)/\rho_{11}(0,0,0)\mathrm{d}\eta_1 = \sqrt{\pi}\sigma_1 \\
        &L_{22} = \int_0^{\infty}\rho_{22}(0,\eta_2,0)/\rho_{11}(0,0,0)\mathrm{d}\eta_2 = \sqrt{\pi}\sigma_2 \\
        &L_{33} = \int_0^{\infty}\rho_{33}(0,0,\eta_3)/\rho_{11}(0,0,0)\mathrm{d}\eta_3 = \sqrt{\pi}\sigma_3
        \end{split}


Therefore, the parameters :math:`\sigma_i` are uniquely determined from the last formulas :math:`\sigma_i =L_{ii}/\sqrt{\pi}`. The vorton strength vector :math:`\gamma` is found from the condition for Reynolds stresses:

.. math::
        :label: anisotropicSigma
        
        \begin{split}
        &\gamma_2\sigma_2^2-\gamma_3\sigma_3^2 = \pm\frac{2}{\pi}\sqrt{\frac{L_{22}L_{33}}{L_{11}}R_{11}} \\
        &\gamma_1\sigma_1^2-\gamma_3\sigma_3^2 = \pm\frac{2}{\pi}\sqrt{\frac{L_{11}L_{33}}{L_{22}}R_{22}} \\
        &\gamma_1\sigma_1^2-\gamma_2\sigma_2^2 = \pm\frac{2}{\pi}\sqrt{\frac{L_{11}L_{22}}{L_{33}}R_{33}}
        \end{split}


Since the determinant of :eq:`anisotropicSigma` is zero, a solution of the system :eq:`anisotropicSigma` is only possible if the following condition is satisfied:

.. math::
        :label: anisotropicCondition
        
        \pm\sqrt{\frac{L_{22}L_{33}}{L_{11}}R_{11}}\pm\sqrt{\frac{L_{11}L_{33}}{L_{22}}R_{22}}=\pm\sqrt{\frac{L_{11}L_{22}}{L_{33}}R_{33}}

or

.. math::

        L_{22} = \frac{\pm L_{11}L_{33}\sqrt{R_{22}}}{\pm L_{33}\sqrt{R_{11}}\pm L_{11}\sqrt{R_{33}}}


The signs before different terms are independent of each other. Therefore, the integral lengths can not be arbitrary. If two length scales :math:`L_{11}` and :math:`L_{22}` are prescribed the remaining length should satisfy the conditions above. Particularly, this solution is wrong for the isotropic turbulence since, if :math:`R_{11} = R_{22} = R_{33}` and :math:`L_{11} = L_{33} = L`, the third length is :math:`L_{22} = L/2` although all integral lengths based on longitudinal auto-correlation functions should be equal. One possible remedy of the length scale restriction is to superpose two statistically independent anisotropic vortons with different parameters at the same position. It is then possible to prescribe arbitrary combinations of length scales and Reynolds stresses. Two approaches for determination of the free parameters are proposed by :cite:`kroger2018`:

(a) Analytic Determination (Type R). In this formulation, it is intended to fulfill all prescribed Reynolds stresses at once. As becomes obvious from :eq:`anisotropicCondition`, then at least one length scale has to be constrained. A natural choice is to constrain :math:`L_{33}`, which is associated with minimum principal Reynolds stress direction :math:`R_{33}`. Thus, :math:`L_{11}` and :math:`L_{22}` remain unchanged while :math:`L_{33}` follows from:

.. math::

        L_{33} = \frac{L_{11}L_{22}\sqrt{R_{33}}}{L_{22}\sqrt{R_{11}}+L_{11}\sqrt{R_{22}}}

Finally, the vorton parameter :math:`\gamma_i` follows from

.. math::
        \begin{split}
            &\gamma_1 = 1 \\
            &\gamma_2 = \frac{1}{\sigma_2^2}\left(\gamma_1\sigma_1^2+\frac{2}{\pi}\sqrt{\frac{L_{11}L_{22}}{L_{33}}R_{33}}\right) \\
            &\gamma_3 = \frac{1}{\sigma_3^2}\left(\gamma_1\sigma_1^2+\frac{2}{\pi}\sqrt{\frac{L_{11}L_{33}}{L_{22}}R_{22}}\right)
        \end{split}

or

.. math::
        \begin{split}
            &\gamma_1 = 1 \\
            &\gamma_2 = \frac{1}{\sigma_2^2}\left(\gamma_1\sigma_1^2-\frac{2}{\pi}\sqrt{\frac{L_{11}L_{22}}{L_{33}}R_{33}}\right) \\
            &\gamma_3 = \frac{1}{\sigma_3^2}\left(\gamma_1\sigma_1^2-\frac{2}{\pi}\sqrt{\frac{L_{11}L_{33}}{L_{22}}R_{22}}\right)
        \end{split}


with :math:`\sigma_i` given by :eq:`anisotropicScale`. By determining parameters this way, Reynolds stresses are fulfilled and length scales are only approximately fulfilled. The anisotropic turbulent spot method with this kind of parameter determination is labeled by "Type R" in the work of :cite:`kroger2018`.

(b) Pseudo Inverse (Type L). In this approach, it is intended to fulfill all prescribed length scales. Although it is not possible to account for all Reynolds stresses at the same time, it is possible to formulate a minimization problem and solve for the closest possible Reynolds stress state. First, the :math:`\sigma_i` are computed from the prescribed length scales :eq:`anisotropicScale`. With fixed length scales, the Reynolds stresses follow from the following system of equations, which is unsolvable because of the zero diagonal:

.. math::

        \frac{2}{\pi}
        \begin{bmatrix}
        \sqrt{R_{11}L_{22}L_{33}/L_{11}} \\
        \sqrt{R_{22}L_{11}L_{33}/L_{22}} \\
        \sqrt{R_{33}L_{11}L_{22}/L_{33}}
        \end{bmatrix}=
        \begin{bmatrix}
        0 & \sigma_2^2 &  -\sigma_3^2 \\
        \sigma_1^2 & 0 & -\sigma_3^2 \\
        \sigma_1^2 & -\sigma_2^2 & 0
        \end{bmatrix}
        \begin{bmatrix}
        \gamma_1 \\
        \gamma_2 \\
        \gamma_3
        \end{bmatrix}


The minimization problem is solved by using the Moore-Penrose pseudo-inverse :math:`\mathbf{M}_L^+` of :math:`\mathbf{M}_L`:

.. math::

        \begin{bmatrix}
        \gamma_1 \\
        \gamma_2 \\
        \gamma_3
        \end{bmatrix}=\frac{2}{\pi}\mathbf{M}_L^+
        \begin{bmatrix}
        \sqrt{R_{11}L_{22}L_{33}/L_{11}} \\
        \sqrt{R_{22}L_{11}L_{33}/L_{22}} \\
        \sqrt{R_{33}L_{11}L_{22}/L_{33}}
        \end{bmatrix}


This way, all length scales are fulfilled, but the Reynolds stresses only approximately. The anisotropic turbulent spot method with this kind of parameter determination is labeled by "Type L".

Code Implementation
===================

The turbulence inflow tool provides a simple and efficient solution for generating a spatially and temporally correlated turbulent velocity field at the inflow of the computational domain via the open-source code,  OpenFOAM. It is developed based on the digital filtering method :cite:`klein2003,xie2008`, the synthetic eddy method :cite:`jarrin2006,poletto2013` and the turbulent spot method :cite:`kroger2018`. The back-end of the turbulence inflow tool is a custom-designed C++ library which contains a list of turbulent velocity boundary conditions developed within OpenFOAM. These boundary conditions can be used to feed the inflow plane with time-varying turbulent velocity signals. Note that the inflow tool provides the source code for two latest standard public versions of the OpenFOAM, i.e., version 6.0 and 7.0, respectively.

The tool can be mainly in two approaches. For users who are quite familiar with OpenFOAM, one can download the source code of the presented boundary conditions, compile the code locally on personal computers (or servers) and then carry out simulations as if those boundary conditions are originally available in the standard OpenFOAM. Similar to other boundary conditions available in OpenFOAM, the use of the presented boundary conditions requires adding some specific entries to the related files in an OpenFOAM project. For users who are not familiar with OpenFOAM, a user-interface (i.e., the front-end of the turbulence inflow tool), which help users to customize the related entries in the OpenFOAM project, is provided.

Before an introduction on the input entries required, it is good to have a preliminary understanding of the file system of a general OpenFOAM project first. To start with, there are usually three folders, i.e., the *0*, *constant* and *system* folders, inside a valid project. The *0* folder contains the files which specify the initial conditions and boundary conditions for different variable fields, e.g., velocity, pressure and turbulent kinetic energy. The *constant* folder includes the files storing the geometry information of the mesh and some constant parameters related to the viscosity of the fluid and the turbulence model (if required). The *system* folder contains files which concern the specification of the time-length (or steps) of simulations, the numerical schemes employed for spatially and temporal discretization, the non-linear equation solution method and other related numerical settings.

As mentioned earlier, the source code of the turbulence inflow tool provides some custom-developed boundary conditions for velocities. To implement those boundary conditions during a simulation, there are several files needs to be either modified or created accordingly. These files include: the *U* file in the *0* folder, the *inflowProperties* file in the *constant* folder and the *controlDict* file in the *system* folder. Compared to the *U* and *controlDict* files which are required by default in a standard OpenFOAM project, the *inflowProperties* file is a special item required (when necessary) by the presented boundary conditions. It is designed to store some statistical properties of the target turbulence which include mean velocities, Reynolds stresses and integral length scales.

Modifications regarding the controlDict file
----------------------------------------------

We now introduce the entries or scripts need to be defined in or added to the above mentioned three files respectively. To start with, we consider the *controlDict* file (inside the *system* folder) and an example of this file is given as follows.

.. code-block:: none

        /*--------------------------------*- C++ -*----------------------------------*\
          =========                 |
          \\      /  F ield         | OpenFOAM: The Open Source CFD Toolbox
           \\    /   O peration     | Website:  https://openfoam.org
            \\  /    A nd           | Version:  6
             \\/     M anipulation  |
        \*---------------------------------------------------------------------------*/
        FoamFile
        {
            version     2.0;
            format      ascii;
            class       dictionary;
            location    "system";
            object      controlDict;
        }
        // * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //
        
        libs ("libturbulentInflow.so");
        
        application     pisoFoam;
        
        startFrom       startTime;
        
        startTime       0;
        
        stopAt          endTime;
        
        endTime         1;
        
        deltaT          1e-3;
        
        writeControl    timeStep;
        
        writeInterval   100;
        
        purgeWrite      0;
        
        writeFormat     ascii;
        
        writePrecision  6;
        
        writeCompression off;
        
        timeFormat      general;
        
        timePrecision   6;
        
        runTimeModifiable true;
        
        // ************************************************************************* //

The only entry needs to be added to this file is the line *libs("libturbulentInflow.so")*. This line tells the fluid solver to include the complied library file *libturbulentInflow.so* prior to the simulation so that the presented boundary conditions contained in this library become available for the current simulation.

Modifications regarding the U file
------------------------------------

Subsequently, we focus on the *U* file located inside the *0* folder. It contains the information of the discrete internal field and boundary fields for the velocity at a specific time instant (see the example given below).

.. code-block:: none

        /*--------------------------------*- C++ -*----------------------------------*\
          =========                 |
          \\      /  F ield         | OpenFOAM: The Open Source CFD Toolbox
           \\    /   O peration     | Website:  https://openfoam.org
            \\  /    A nd           | Version:  6
             \\/     M anipulation  |
        \*---------------------------------------------------------------------------*/
        FoamFile
        {
            version     2.0;
            format      ascii;
            class       volVectorField;
            object      U;
        }
        // * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //
        
        dimensions      [0 1 -1 0 0 0 0];
        
        internalField   uniform (10 0 0);
        
        boundaryField
        {
            inlet
            {
                type            turbulentDFMInlet;
                filterType      exponential;
                gridFactor      1;
                filterFactor    4;
                periodicInY     true;
                periodicInZ     false;
                cleanRestart    false;
                value           $internalField;
            }
            
            inletOld
            {
                type            fixedValue;
                value           uniform (10 0 0);
            }
        
            outlet
            {
                type            zeroGradient;
            }
        
            wall
            {
                type            fixedValue;
                value           uniform (0 0 0);
            }
        }
        
        // ************************************************************************* //

The boundary conditions for velocities are all specified in the *boundaryField* dictionary, and there are several sub-dictionaries in the *boundaryField* dictionary with the names such as *inlet*, *outlet*, *wall*, etc. The name of each sub-dictionary corresponds to the name of a particular boundary patch of the mesh, and the entries contained in each sub-dictionary are the related to the boundary condition for the velocity field at the corresponding boundary patch. Let's focus on the sub-dictionary associated with the inflow patch, i.e., the *inlet* sub-dictionary. The commonly used boundary condition for the velocity at the inflow is the *fixedValue* condition (see the sub-dictionary *inletOld*). For a *fixedValue* velocity boundary, the velocities at the *inlet* patch are constant and fixed to the vector specified inside the baskets (coming after the the *values* entry) during the simulation. In our case, we would like to the velocities at the *inlet* patch to be stochastic and time-varying. For this purpose, the developed turbulence inflow package currently provides four boundary conditions in total, i.e. *turbulentDFMInlet*, *turbulentSEMInlet*, *turbulentDFSEMInlet* and *turbulentATSMInlet*. These four boundary conditions correspond to the synthetic turbulent method by :cite:`klein2003`, :cite:`jarrin2006`, :cite:`poletto2013` and :cite:`kroger2018`, respectively.

Also note that each presented boundary condition is, as a matter of fact, a derived class of the *fixedValue* boundary condition. Since the initialization of the *fixedValue* boundary condition requires the specification of the *value* entry. Therefore, this entry should be defined for the four presented boundary conditions as well. However, when one of the four presented boundary conditions is employed, the velocities at the boundary will be later overwritten by the generated turbulence velocity field and consequently the *value* entry does not have any effect here. Thus, this entry can be just specified as *$internalField;* Once the *type* entry takes the *turbulentDFMInlet*, *turbulentSEMInlet*, *turbulentDFSEMInlet* or *turbulentATSMInlet* boundary condition, there are some unique entries related to each boundary condition accordingly.

Apart from the *type* and *value* entries, there are also some identical entries shared by the four presented boundary conditions. The entries *periodicInY* and *periodicInZ* determine whether the synthetic turbulence is periodic in :math:`x_2` and :math:`x_3`-direction or not, respectively. Before we discuss the *cleanRestart* entry, it should be mentioned that the four presented boundary conditions are capable of restarting the generation of the synthetic turbulence from an old time-step. This feature is achieved by storing the necessary information and numerical quantities (obtained at the current time-step) which will affect the generation of the turbulence at the next-step. The entry *cleanRestart* determines whether to disregard those information and generate a new turbulent velocity field at the beginning of a new simulation.

.. _table_TInF_theory_01:

.. table:: Basic entries shared by the four presented boundary conditions
    :align: center
    
    +------------+----+---------------------------------------------------------------+--------------+
    |entry name  |type|descriptions                                                   |default values|
    +============+====+===============================================================+==============+
    |periodicInY |bool|if the synthetic turbulent is periodic in :math:`x_2`-direction|false         |
    +------------+----+---------------------------------------------------------------+--------------+
    |periodicInZ |bool|if the synthetic turbulent is periodic in :math:`x_3`-direction|false         |
    +------------+----+---------------------------------------------------------------+--------------+
    |cleanRestart|bool|whether to disregard old turbulence or not                     |false         |
    +------------+----+---------------------------------------------------------------+--------------+


The turbulentDFMInlet boundary condition
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

For the *turbulentDFMInlet* boundary condition, the unique entries to be specified are *filterType*, *filterFactor* and *gridFactor*. The *filterShape* entry refers to the type of the prescribed function for computing the filter coefficients, and requires a string input. When this entry is taken as *gaussian*, the coefficients are computed with :eq:`gaussian`; when this entry is taken as *exponential*, the coefficients follow from :eq:`exponential`. As discussed earlier, the digital filtering method should be employed on uniform spacing Cartesian grids. To make this method applies to more general cases, a virtual uniform spacing Cartesian grid system will be generated during the implementation. The velocity fluctuations will be first generated on this virtual grid and then interpolated to the discrete points on the inflow patch. The *gridFactor* entry defines ratio between the virtual grid spacing :math:`\Delta` with the square root of the area of the smallest face element on the inflow plane. Higher *gridFactor* leads to larger grid spacing and vice versa. Finally, the *filterFactor* entry denotes the values of :math:`N/n` where :math:`N` and :math:`n` follow from the notation in :numref:`sectionDFM`, and consequently it requires an integer input. The entries related to the *turbulentDFMInlet* boundary, their input variable types and limitations are listed in :numref:`table_TInF_theory_02`.

.. _table_TInF_theory_02:

.. table:: Entries related to the *turbulentDFMInlet* boundary condition
    :align: center
    
    +------------+------+-------------------------------+--------------+
    |entry name  |type  |descriptions                   |default values|
    +============+======+===============================+==============+
    |filterType  |string|gaussian, exponential or bessel|exponential   |
    +------------+------+-------------------------------+--------------+
    |gridFactor  |float |:math:`\geq 1`                 |1             |
    +------------+------+-------------------------------+--------------+
    |filterFactor|int   |:math:`\geq 4`                 |4             |
    +------------+------+-------------------------------+--------------+

The turbulentSEMInlet boundary condition
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

For the *turbulentSEMInlet* boundary condition, the unique entries to be specified are *eddyType* and *eddyDensity*. The *eddyType* entry refers to the type of the velocity shape function :math:`f`. It takes an string input and currently the available options are *tent*, *step* and *gaussian* which correspond to :eq:`ftent`, :eq:`fstep` and :eq:`fgaussian`, respectively. The *eddyDensity* refers to the ratio between :math:`V_B` and the sum of the eddy volumes (see :numref:`sectionSEM`). Higher *eddyDensity* leads to a larger amount of synthetic eddies. It takes an scalar input with a value no less than one. The lower bound of *eddyDensity* (taken as 1 by default) ensures the eddy box (introduced in :numref:`sectionSEM`), from a statistical point of view, can be covered up by the eddies. The unique entries for the *turbulentSEMInlet* condition are summarized in :numref:`table_TInF_theory_03`.

.. _table_TInF_theory_03:

.. table:: Entries related to the *turbulentSEMInlet* boundary condition
    :align: center
    
    +-----------+------+----------------------+--------------+
    |entry name |type  |descriptions          |default values|
    +===========+======+======================+==============+
    |eddyType   |string|tent, step or gaussian|gaussian      |
    +-----------+------+----------------------+--------------+
    |eddyDensity|float |:math:`\geq 1`        |1             |
    +-----------+------+----------------------+--------------+

The turbulentDFSEMInlet boundary condition
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

For the *turbulentDFSEMInlet* boundary condition, the only unique entry to be specified is *eddyDensity* whose meaning is identical to that of the *turbulentSEMInlet* boundary condition.


The turbulentATSMInlet boundary condition
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

For the *turbulentATSMInlet* boundary condition, the unique entries to be specified are *vortonType* and *vortonDensity*. The *vortonType* entry refers the approach parameter determination for anisotropic vortons discussed in :numref:`sectionATSM`. It takes an string input and the options currently available are *typeR* and *typeL* which correspond to :eq:`fstep` and :eq:`fgaussian`, respectively. The *vortonDensity* entry is similar to the *eddyDensity* of the *turbulentSEMInlet* boundary condition. We summarize the unique entries for the *turbulentATSMInlet* condition in :numref:`table_TInF_theory_04` for reference.

.. _table_TInF_theory_04:

.. table:: Entries related to the *turbulentATSMInlet* boundary condition
    :align: center
    
    +-------------+------+--------------+--------------+
    |entry name   |type  |descriptions  |default values|
    +=============+======+==============+==============+
    |vortonType   |string|typeR or typeL|typeR         |
    +-------------+------+--------------+--------------+
    |vortonDensity|float |:math:`\geq 1`|1             |
    +-------------+------+--------------+--------------+

A common feature shared by the entries *filterFactor*, *eddyDensity* and *vortonDensity* mentioned above is that when they are assigned with higher values, the resulting velocity fluctuations will usually have better a quality. However higher values also means a larger consumption of mathematical calculations and computational memory. Therefore, users are suggested to balance the needs between accuracy and efficient during the implementation of those boundary conditions.


Specification of the statistics of the target turbulence
--------------------------------------------------------

The aforementioned entries defined in the boundary conditions for velocities only concern the selection of the method and the corresponding parameters associated with the selected method. The generation of the synthetic turbulence also requires the statistical information of the target turbulence to be reproduced which include mean velocities, Reynolds stresses and integral length scales. There are mainly three approaches for the input of those information, i.e., *direct specification*, *interpolation* and *prescribed function*.

Direct specification
^^^^^^^^^^^^^^^^^^^^

The direct specification approach is suitable for the case in which the mean velocity, Reynolds stress and length scales on each face element of the inflow plane are known in prior. In this approach, the values of those quantities can be directly specified in the *inlet* dictionary. If they are uniformly distributed on the inflow plane, the related entries are in the form of

.. code-block:: none

        boundaryField
        {
            inlet
            {
                type            turbulentDFMInlet;
                filterType      exponential;
                gridFactor      1;
                filterFactor    4;
                periodicInY     true;
                periodicInZ     false;
                cleanRestart    false;
                value           $internalField;
                U               uniform 10;
                R               uniform (2.0 0.5 0.5 1.5 -0.5 1.0);
                L               uniform (0.3 0.3 0.3 0.2 0.2 0.2 0.1 0.1 0.1);
            }
        }

The three entries displayed in the *inlet* dictionary are *U*, *R* and *L* which represent mean velocity magnitude, Reynolds stress and length scale. If *U*, *R* and *L* are not uniformly distributed on the inlet patch, the related entries should be defined in the form of

.. code-block:: none

        boundaryField
        {
            inlet
            {
                type            turbulentDFMInlet;
                filterType      exponential;
                gridFactor      1;
                filterFactor    4;
                periodicInY     true;
                periodicInZ     false;
                cleanRestart    false;
                value           `internalField;
                U
                {
                                 1.0
                                 2.0
                                 ...
                                 6.0
                };
                R
                {
                               (2.0 0.5 0.5 1.5 -0.5 1.0)
                               (2.1 0.6 0.6 1.6 -0.6 1.1)
                               ...
                               (2.5 1.0 1.0 2.0 -1.0 1.5)
                };
                L
                {
                               (0.30 0.30 0.30 0.20 0.20 0.20 0.10 0.10 0.10)
                               (0.31 0.31 0.31 0.21 0.21 0.21 0.11 0.11 0.11)
                               ...
                               (0.35 0.35 0.35 0.25 0.25 0.25 0.15 0.15 0.15)
                };
            }
        }

It is noted that each element in *R* defines a six-component symmetric tensor of the form
:math:`(R_{11} \ R_{21} \ R_{31} \ R_{22} \ R_{32} \ R_{33})`.
For the *turbulentDFMInlet* and *turbulentSEMInlet* boundary conditions, each element in *L* defines a
general (i.e., nine-components) tensor to be entered as
(:math:`L_{11}`
 :math:`L_{12}` 
 :math:`L_{13}` 
 :math:`L_{21}`
 :math:`L_{22}` 
 :math:`L_{23}` 
 :math:`L_{31}` 
 :math:`L_{32}` 
 :math:`L_{33}`). 
For the *turbulentATSMInlet* boundary condition, each element in *L* defines a three-component vector of the form 
:math:`(L_{11} L_{22} L_{33})`.
For the *turbulentDFSEMInlet* boundary condition, each element in *L* is a scalar. The main difficultly in specifying the entries *U*,
*R* and *L* directly is to make sure that the sequence of the elements in each entry is properly sorted coping with the corresponding
faces on the inflow plane. 

Specification via interpolation
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The mean velocities, Reynolds stresses and integral length scales on the cell-faces of the inflow plane can also be specified through face interpolation. The detailed procedures are as follows:

* Create a folder with the name *boundaryData* inside the *constant* folder of a standard OpenFOAM project.

.. _fig_TInF_theory_01:

.. figure:: figures/TInF-theory-01.jpg
   :align: center
   :figclass: align-center
   :width: 800px
   
   The *boundaryData* folder

* Create another folder using the name of the inflow patch inside the above created folder.

.. _fig_TInF_theory_02:

.. figure:: figures/TInF-theory-02.jpg
   :align: center
   :figclass: align-center
   :width: 800px
   
   The *inlet* folder

* Add four empty files with the names *U*, *R*, *L* and *points*, respectively inside the *inlet* folder. These four files will be used to store the given values of the mean velocity magnitude, Reynolds stress, integral scale at some specific points and the locations of those points in the global coordinate system (of the computational domain).

* The *U* file, which stores the information of mean velocity magnitudes, should be written in the format of

.. code-block:: none

        (
        0.000000
        0.029538
        0.118110
        ...
        0.029538
        0
        )


The entries within the braces are the magnitudes of mean velocity at the corresponding points.

* The *R* file, which stores the information of Reynolds stresses, should be written in the format of

.. code-block:: none

        (
        (0.000000 0.000000 0.000000 0.000000 0.000000 0.000000)
        (0.000137 0.000000 0.000000 0.000000 0.000000 0.000053)
        (0.002183 0.000002 0.000001 0.000000 0.000000 0.000827)
        ...
        (0.000137 0.000000 0.000000 0.000000 0.000000 0.000053)
        (0.000000 0.000000 0.000000 0.000000 0.000000 0.000000)
        )

The entries within the braces are the Reynolds stress tensors at the corresponding points.

* The *L* file, which stores the information of turbulence length scales, should be written in the format of

.. code-block:: none

        (
        (0.000000 0.000000 0.000000 0.000000 0.000000 0.000000 0.000000 0.000000 0.000000)
        (0.000024 0.000024 0.000024 0.000024 0.000024 0.000024 0.000024 0.000024 0.000024)
        (0.000096 0.000096 0.000096 0.000096 0.000096 0.000096 0.000096 0.000096 0.000096)
        ...
        (0.000024 0.000024 0.000024 0.000024 0.000024 0.000024 0.000024 0.000024 0.000024)
        (0.000000 0.000000 0.000000 0.000000 0.000000 0.000000 0.000000 0.000000 0.000000)
        )

The entries within the braces are the components of the turbulence length scales at the corresponding points. Again, both the *turbulentDFMInlet* and *turbulentSEMInlet* boundary conditions employ a nine-component length scale. The *turbulentATSMInlet* and *turbulentDFSEMInlet* boundary conditions employ a three-component and one-component length scale, respectively.

* The *points* file, which stores the locations of the points in the global coordinate system, should be written in the format of

.. code-block:: none

        (
        (0.000000 0.000000 0.000000)
        (0.000000 0.000075 0.000000)
        (0.000000 0.000301 0.000000)
        ...
        (0.000000 2.000000 0.000000)
        (0.000000 2.000000 3.000000)
        )

It is noted that the points listed in this file should be able to define a single plane. That is to say the points should not locate on a single line or different planes. In summary, specification of statistics of target turbulent via interpolation is suitable for the case in which the mean velocities, Reynolds stresses and integral length scales at a group of selected points are available.

Specification via prescribed functions
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Finally, the specification of the mean velocities, Reynolds stresses and integral length scales can also be done with the prescribed functions embedded in the presented boundary conditions. The entries related to this approach are all defined in the *inflowProperties* file in the *constant* folder. To employ this approach, the first step is to define a local coordinate system and its origin. The local :math:`(x_1',x_2',x_3')` coordinate system is constructed with its :math:`x_1'`-axis being parallel to normal of the inflow plane and pointing towards the interior of the computational domain.

.. _fig_TInF_theory_03:

.. figure:: figures/TInF-theory-03.eps
   :align: center
   :figclass: align-center
   :width: 250px
   
   A sketch of the Euler angles and the :math:`N`-axis

To determine the orientation of the :math:`x_2'`- and :math:`x_3'`-axis, an entry named as *Naxis* is defined which takes a vector input. This vector represents the direction of the :math:`N`-axis (see :numref:`fig_TInF_theory_03`) where :math:`N` is the intersection line of the :math:`(x_1,x_2)`-plane and :math:`(x_1',x_2')`-plane. The :math:`x_2'`- and :math:`x_3'`-axis are then determined by :math:`\mathbf{x}_2' = \mathbf{x}_3'\times\mathbf{x}_1'` and :math:`\mathbf{x}_3' = \mathbf{x}_1'\times\mathbf{N}`. The reason why we specify the direction of the :math:`N`-axis instead of the :math:`x_2'`- or :math:`x_3'`-axis is because, once the direction of the :math:`x_1'`-axis is determined, the :math:`x_2`- and :math:`x_3`-axis cannot be specified arbitrarily since they must be parallel to the plane orthogonal to the :math:`x_1`-axis. In contrast, the direction of the :math:`N`-axis can be specified arbitrarily as long as the :math:`x_3`-components of :math:`N` is zero. The entry *Naxis* is set as :math:`(0 \ 0 \ 0)` by default. In this case, the :math:`(x_1',x_2')`-plane and :math:`(x_1,x_2)`-plane are parallel to each other and consequently the :math:`x_3`- and :math:`x_3'`-axis are align.


Now, the remaining issue is the determination of the origin of the local coordinate system. Consider a rectangular defined on the :math:`(x_2,x_3)`-plane bounding all the nodes of the inflow patch. The origin of the local coordinate system is chosen as the lower left corner of this rectangular by default. We also allow users to offset the origin through the use of the entries *yOffset* and *zOffset* which take scalars for input.

.. code-block:: none

        /*--------------------------------*- C++ -*----------------------------------*\
          =========                 |
          \      /  F ield         | OpenFOAM: The Open Source CFD Toolbox
           \    /   O peration     | Website:  https://openfoam.org
            \  /    A nd           | Version:  6
             \/     M anipulation  |
        \*---------------------------------------------------------------------------*/
        FoamFile
        {
            version     2.0;
            format      ascii;
            class       dictionary;
            location    "constant";
            object      inflowProperties;
        }
        // * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //

        Naxis                       (0 0 0);
        offset                      (0 0 0);

        UDict
        {
            referenceValue          1;
            profile                 uniform;
        }

        RDict
        {
            referenceValue          (0.1  0  0  0.1  0  0.1);
            profile                 uniform;
        }

        LDict
        {
            referenceValue          (0.3 0.2 0.1);
            profile                 uniform;
            Gamma                   (1 1 1);
        }

        // ************************************************************************* //

In addition to the entries mentioned above, there are a total of three sub-dictionaries need to be specified in the *inflowProperties* file, i.e. *UDict*, *RDict* and *LDict*, which are responsible for the specifications of the mean velocity magnitude, the Reynolds stress tensor :math:`(R_{11} \ R_{21} \ R_{31} \ R_{22} \ R_{32} \ R_{33})` and the integral length scales. For the *turbulentDFMInlet* and *turbulentSEMInlet* boundary conditions, the integral length scales should be defined in the form of (:math:`L_{11}^{x_1}` :math:`L_{11}^{x_2}` :math:`L_{11}^{x_3}` :math:`L_{22}^{x_1}` :math:`L_{22}^{x_2}` :math:`L_{22}^{x_3}` :math:`L_{33}^{x_1}` :math:`L_{33}^{x_2}` :math:`L_{33}^{x_3})`. For the *turbulentATSMInlet* boundary condition, the integral length scales should be defined in the form of :math:`(L_{11}^{x_1} \ L_{22}^{x_2} \ L_{33}^{x_3})`. Note that :math:`L_{11}^{x_1}` refers to the integral length scale obtained by integrating the two-point correlation function :math:`R_{11}(\mathbf{x})` with respect to the local :math:`x_1`-direction (i.e., the stream-wise direction) and similarly for :math:`L_{22}^{x_2}` and :math:`L_{33}^{x_3}`.

Each sub-dictionary contains the entries required for the computation of the values of the corresponding variable on the inlet boundary which are almost identical to each other. In all sub-dictionaries mentioned above, the two basic entries need to be specified are the *referenceValue* and the *profile*. For the *UDict* sub-dictionary, the *referenceValue* entry requires a scalar value for input, while a symmetric tensor is required for the *RDict* sub-dictionary. Finally, the *referenceValue* entry of the *LDict* sub-dictionary demands a vector.

On the other hand, the *profile* entry, as its name implies, defines the profile function of the corresponding variable on the inlet boundary. It takes a string variable for input, and there are only two the valid options are *uniform* and *exponential* at the present stage (expecting more in the coming future). When the *profile* entry takes *uniform*, the corresponding variable will be set universally to the reference value on the entire inflow patch; When the *profile* entry takes *exponential*, the corresponding variable will be therefore computed with an exponential function and additional entries entitled as *alpha*, *referenceAngl* and *referenceDist* should be defined as a supplement, see examples below.

.. code-block:: none

        UDict
        {
            referenceValue          1;
            profile                 exponential;
            referenceAngl           0;
            referenceDist           1.0;
            alpha                   0.1;
        }
        
        RDict
        {
            referenceValue          (0.1  0  0  0.1  0  0.1);
            profile                 exponential;
            referenceAngl           0;
            referenceDist           1.0;
            alpha                   (0.3 0.2 0.1);
        }

While the entries required for the same type of profile function are almost the same, the form of the exponential function differs in scalar variables (e.g., the mean velocity magnitude) and symmetric tensor variables (e.g., the turbulent intensity). For a scalar variable namely :math:`\phi`, the corresponding exponential function has the form

.. math::
        :label: exponentialForScalar
        
        \phi(\mathbf{x}) = \bar{\phi}\big(\frac{\mathbf{n}\cdot\mathbf{x}}{d_0}\big)^{\alpha}


where :math:`\bar{\phi}` is the reference value (defined in the *referenceValue* entry), :math:`\alpha` is the exponential coefficient  (defined by the *alpha* entry), and :math:`d_0` is a reference distance (defined by the *referenceDist* entry). The symbol :math:`\mathbf{n}` is a direction vector (located on the inflow plane) to which the spatial coordinate :math:`\mathbf{x}` (defined in the local :math:`(x_1,x_2,x_3)` coordinate system) is projected. The direction of :math:`\mathbf{n}` is specified indirectly by defining the relative angle between the local :math:`x_3`-axis and :math:`\mathbf{n}`, and this angle (ranging from 0 to 180 degrees) is specified in the *referenceAngl* entry. This reason behind such an approach is obvious, the :math:`\mathbf{n}` can not be arbitrarily specified for it is located on the local :math:`x_1x_2` (i.e., the inflow) plane. Also for obvious reasons, the reference values of the mean velocity magnitude and integral length scales should be larger than zero.

Finally, a symmetric tensor variable (e.g., the turbulent intensity) denoted by :math:`\mathbf{\phi}` for demonstration, the corresponding exponential function writes

.. math::
        :label: exponentialForTensor
        
        \mathbf{\phi}(\mathbf{x}) = \sum_{\gamma=1}^s \bar{\phi}_{\gamma}\big(\frac{\mathbf{n}\cdot\mathbf{x}}{d_0}\big)^{\alpha_{\gamma}} \mathbf{M}_{\gamma},


where :math:`\bar{\phi}_{\gamma}` (:math:`\gamma=1,2,3`) are principal values of the reference symmetric tensor :math:`\bar{\mathbf{\phi}}` (i.e., the one defined in the *referenceValue* entry). :math:`\mathbf{M}_{\gamma}` (:math:`\gamma=1,2,3`) are tensors defined by

.. math::

        \mathbf{M}_{\gamma} = \mathbf{a}_{\gamma} \otimes \mathbf{a}_{\gamma}


where :math:`\mathbf{a}_{\gamma}` are the eigenvectors of :math:`\bar{\mathbf{\phi}}`. Other symbols in :eq:`exponentialForTensor` follow from the notation in :eq:`exponentialForScalar`. Also note that in :eq:`exponentialForTensor`, the *alpha* entry requires a three-component vector, i.e., :math:`(\alpha_1 \ \alpha_2 \ \alpha_3)`, for input. The *referenceValue* requires a six-component vector, i.e., :math:`(\bar{\phi}_{11} \ \bar{\phi}_{21} \ \bar{\phi}_{31}\ \bar{\phi}_{22} \ \bar{\phi}_{32}\ \bar{\phi}_{33})`, for input, and for obvious reasons the :math:`\bar{\phi}_{11}`, :math:`\bar{\phi}_{22}` and :math:`\bar{\phi}_{33}` components should be larger than zero.


.. _table_TInF_theory_05:

.. table:: Entries listed in the inflowProperties file
    :align: center

    +--------------------+------------------+------------------------------+--------------+
    |entry name          |type              |limits                        |default values|
    +==============+=====+==================+==============================+==============+
    |              |UDict|float             |>0                            |              |
    |              +-----+------------------+------------------------------+--------------+
    |referenceValue|LDict|a vector of floats|>0                            |              |
    |              +-----+------------------+------------------------------+--------------+
    |              |RDict|a vector of floats|positive definite             |              |
    +--------------+-----+------------------+------------------------------+--------------+
    |profle              |string            |uniform, linear or exponential|uniform       |
    +--------------------+------------------+------------------------------+--------------+
    |referenceDist       |float             |>0                            |1             |
    +--------------------+------------------+------------------------------+--------------+
    |referenceAngl       |float             |(0 180)                       |0             |
    +--------------------+------------------+------------------------------+--------------+
    |Naxiss              |float             |(0 180)                       |0             |
    +--------------------+------------------+------------------------------+--------------+


References
----------

.. bibliography:: references.bib
   :cited:
   :style: unsrt
