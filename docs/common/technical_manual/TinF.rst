.. _lblTurbulanceInflowTheory:

Turbulence Inflow
=================

Introduction
------------

In computational wind engineering (CWE), generation of inflow turbulence satisfying prescribed
mean-velocity profiles, turbulence spectra, spatial and temporal correlations is of great
importance for the accurate evaluation of wind effects on buildings and structures. More
specifically, the task is to generate a turbulent velocity field :math:`\boldsymbol{u}(\boldsymbol{x},t)` with the form

.. math::
    
    \boldsymbol{u}(\boldsymbol{x},t) = \boldsymbol{U}(\boldsymbol{x},t)+\boldsymbol{u}'(\boldsymbol{x},t)


where :math:`\boldsymbol{U}(\boldsymbol{x},t)` and :math:`\boldsymbol{u}'(\boldsymbol{x},t)` are
the mean and fluctuating velocities at the position :math:`\boldsymbol{x}`. The turbulent
velocity field :math:`\boldsymbol{u}` and its fluctuation :math:`\boldsymbol{u}'` need to satisfy a number of properties which are list below:


* :math:`\boldsymbol{u}'` should be spatially and temporally correlated.

    \item :math:`\boldsymbol{u}'` needs to have prescribed Reynolds stresses tensor
    :math:`R_{ij}(\boldsymbol{x}) = \overline{u_i'u_j'}(\boldsymbol{x})` where :math:`u_i'`
    (:math:`i=1,2,3`) is the :math:`i`-th component of :math:`\boldsymbol{u}'`  and the over line denotes the time average.

* :math:`\boldsymbol{u}'` needs to have prescribed integral length scales :math:`L_{ij}(\boldsymbol{x},\boldsymbol{e})`

    .. math::
	
	L_{ij}(\boldsymbol{x},\boldsymbol{e}) = \int_{0}^{\infty} \rho_{ij}(\boldsymbol{x},r\boldsymbol{e})\ \mathrm{d}r,

    where :math:`\rho_{ij}(\boldsymbol{x},\boldsymbol{e})` is the correlation function given by

    .. math::
	
	\rho_{ij}(\boldsymbol{x},\boldsymbol{e}) = \frac{\overline{u_i'(\boldsymbol{x},t)u_j'(\boldsymbol{x}+\boldsymbol{e},t)}}{\overline{u_i'(\boldsymbol{x},t)u_j'(\boldsymbol{x},t)}}.

* :math:`\boldsymbol{u}` should fulfil the divergence free constraint :math:`\nabla \cdot \boldsymbol{u} = 0`.

* :math:`\boldsymbol{u}'` should have prescribed correlation functions :math:`\rho_{ij}(\boldsymbol{x},\boldsymbol{e})` or spectra.



Several methodologies have been proposed for this purpose which can be classified into three
general categories: precursor simulation methods, recycling methods and synthetic methods.
Compared with precursor simulation and recycling methods, the synthetic methods in general offer
a more practical and relatively efficient approach to generate inflow turbulence, and is
therefore chosen as the subject of this section. Research activities on synthetic turbulence
generation have been vigorous over the past decades and have branched out into several
categories of techniques :cite:`wu2017`, including the synthetic random Fourier method
:cite:`kraichnan1970,hoshiya1972`, the synthetic digital filtering method :cite:`klein2003` 
and the synthetic eddy methods :cite:`jarrin2006`.
A brief introduction regarding to these techniques is given below and emphasis is placed on their abilities to capture the statistical characteristics as well as the spatial and temporal coherence of turbulence. Also note that since real turbulence is very complex, in most cases, not all of the above listed features can be fulfilled. There is always some adaptation time required for the artificial turbulence to evolve into real turbulence. Fulfilling the properties above with the synthetic turbulence is important to minimize the adaptation time or length.

Synthetic Random Fourier Method
------------

The so-called synthetic random Fourier method (SRFM) attempts to model turbulent flow field indirectly by imposing constraints on uncorrelated random fields through an energy spectrum to account for the spatial and temporal correlations, which can be further classified into two groups. 
The first group of the SRFM was based on the pioneering work in :cite:`hoshiya1972` and :cite:`shinozuka1972` on the simulation of multi-correlated random processes using a weighted amplitude wave superposition (WAWS) method. This approach has an advantage that both the targeted power- and cross-spectra can be imposed in the generation process so that the prescribed target characteristics can be maintained. A major drawback of this method is that the generated turbulence does not satisfy the continuity equation of the flow, or in other words, the divergence-free condition is not guaranteed. As a consequence it would take enormous effort for the solver to enforce the continuity by correcting the turbulence inflow inserted into the computational domain, and the statistical characteristics of the corrected flow field differs from the target values.

The second group of the SRFM was initiated by the work in :cite:`kraichnan1970` on
divergence-free homogeneous isotropic turbulence synthesis through the superposition of random
harmonic functions. :cite:`smirnov2001` took a step forward by combing Kraichnan's technique
with scaling and orthogonal transformation operations in a procedure known as the random flow
generation (RFG) which allows to generate inhomogeneous and anisotropic turbulence. However the
scaling operation introduced in the RFG technique can result in a velocity field that is not
divergence-free for inhomogeneous turbulence. Modifications to enforce the divergence-free
constraint for inhomogeneous turbulence was discussed in :cite:`yu2014`. A major drawback of RFG
technique is that the power-spectra of the generated turbulence only follows Gaussian's spectra
model, so it is not suitable for simulating flows in atmospheric boundary layer.
:cite:`huang2010` revisited Kraichnan's method and proposed a technique called DSRFG (for
discretizing and synthesizing random flow generation) which allows to generate turbulent inflow
from any prescribed spectrum. Instead of using the scaling and orthogonal transformation, the
anisotropy of turbulence is realized by modifying the distribution strategy of the wave vector
in Kraichnan's original method. A drawback of the DSRFG technique is that it produces
fluctuating velocities with high correlation due to the fact that in this method the spatial
correlation is modelled by a parameter which is not a function of frequency but a constant
value. Inspired by the DSRFG method, :cite:`castro2017` proposed some modifications to this
technique to obtain the velocity field that had a better match with the target turbulent
statistics. This method, known as modified discretizing and synthesizing random flow generation
(MDSRFG), is capable of removing the dependence of statistic quantities of synthetic turbulence
on spectra discretization resolution. :cite:`aboshosha2015` also proposed a technique called consistent discrete RFG (CDRFG) to accurately model the target spectra and the coherence function. In both two methods mentioned above, the parameter that characterizes the spatial correlation is expressed as a function of frequency to account for the damping of coherence with the increase of frequency. An attractive feature of second group of SRFM is that the generation procedures are usually independent at each point and each time-instant so that it can be easily accelerated by conducting parallel computation, although the generated random flow may not satisfy the continuity equation. 


.. _section3:
Synthetic Eddy Method
------------

The synthetic eddy method (SEM) initiated by :cite:`jarrin2006` is based on the classical view
of turbulence as a superposition of the representative coherent eddies. In the SEM, the flow is
assumed to consist of randomly distributed turbulent spots, and each turbulent spot is modelled
by a three-dimensional shape function with compact support and satisfies a proper normalization
condition. The spots are then assumed to be convected through an inlet plane with a reference
velocity using Taylor's frozen turbulence hypothesis. The resulting inflow turbulence is then
reconstructed using the method proposed by to recover the desired statistical characteristics
and to account for the conditions of inhomogeneity and anisotropy. The choice of the shape
function plays an important role in the SEM since it is directly related to the two-point
autocorrelation function, and consequently the power spectrum of the synthetic turbulence.
Enforcement of the continuity condition in the SEM was discussed in :cite:`poletto2013`.

A brief introduction on the SEM presented by :cite:`jarrin2006` is given as follows. To start
with, the turbulent spot mentioned above can be represented as eddies defined by shape function
:math:`f` which has a compact support on :math:`[-1,1]` and has the normalization

.. math::
    :label: normalization

    \int_{-1}^1 f^2(x) \mathrm{d}x = 1


The inflow plane on which we want to generate the synthetic turbulence with the SEM is basically
a finite set of points :math:`S =
\{\boldsymbol{x}_1,\boldsymbol{x}_2,\ldots,\boldsymbol{x}_s\}`. The first step is to create a
box of eddies :math:`B` surrounding :math:`S` which is going to contain the synthetic eddies. It is defined by

.. math::
    
    B = \big\{(x_1,x_2,x_3)\in \mathbb{R}^3: x_{i,\text{min}}<x_i<x_{i,\text{max}}\big\}


where

.. math::
    
    x_{i,\text{min}} = \text{min}(x_i-\sigma_i(\boldsymbol{x})), \quad x_{i,\text{max}} = \text{max}(x_i+\sigma_i(\boldsymbol{x})), \quad \boldsymbol{x}\in S


The volume of the box of eddies is noted by :math:`V_B`. In the synthetic eddy method, the
velocity signal generated by :math:`N` eddies has the representation

.. math::
    :label: SEMvelocity

    u_i(\boldsymbol{x}) = U_i(\boldsymbol{x}) + \frac{1}{\sqrt{N}}\sum_{k=1}^N a_{ij} \epsilon_j^k f_{\boldsymbol{\sigma}(\boldsymbol{x})}(\boldsymbol{x}-\boldsymbol{x}^k)


where :math:`\boldsymbol{x}` represent the coordinates of computational points and
:math:`\boldsymbol{x}^k` represent the coordinates of eddies. The coefficient :math:`a_{ij}`
results from the Cholesky decomposition of a prescribed Reynolds stress tensor :math:`R_{ij}`

.. math::
    :label: LundCoefficients

    \left(\begin{matrix}
    \sqrt{R_{11}} & 0 & 0 \\
    R_{21}/a_{11} & \sqrt{R_{22}-a_{21}^2} & 0 \\
    R_{31}/a_{11}  & (R_{32}-a_{21}a_{31})/a_{22} & \sqrt{R_{33}-a_{31}^2-a_{32}^2}
    \end{matrix}\right)


The coefficient :math:`\epsilon_j^k` (:math:`j=1,2,3`) is is the uniformly random intensity
factor of values :math:`+1` or :math:`-1`, and :math:`f_{\boldsymbol{\sigma}(\boldsymbol{x})}
(\boldsymbol{x}-\boldsymbol{x}^k)` is the velocity distribution at :math:`\boldsymbol{x}` of the
eddy located at :math:`\boldsymbol{x}^k` defined as follows:

.. math::
    :label: velocityShape

    f_{\boldsymbol{\sigma}(\boldsymbol{x})} (\boldsymbol{x}-\boldsymbol{x}^k) = \sqrt{\frac{V_B}{\sigma_1\sigma_2\sigma_3}}f\left(\frac{x_1-x_1^k}{\sigma_1}\right)f\left(\frac{x_2-x_2^k}{\sigma_2}\right)f\left(\frac{x_3-x_3^k}{\sigma_3}\right)


where :math:`\boldsymbol{\sigma}=(\sigma_1,\sigma_2,\sigma_3)^T`. The position of the eddies
:math:`\boldsymbol{x}^k` before the first time step are independent from each other and taken
from a uniform distribution over the box of eddies :math:`B`. The eddies are convected through
the box of eddies :math:`B` with the mean velocity :math:`\boldsymbol{U}(\boldsymbol{x})`. At
each time step, the new position of eddy :math:`k` is given by

.. math::
    
    \boldsymbol{x}^k(t+\varDelta t) = \boldsymbol{x}^k(t)+\boldsymbol{U}(\boldsymbol{x}^k)\varDelta t


where :math:`\varDelta t` is the time step of the simulation. If an eddy :math:`k` is convected
out of the box :math:`B`, then it is immediately regenerated randomly with in the region

.. math::
    
    B_{\varDelta t} = \left\{ \boldsymbol{x}\notin B, \ \boldsymbol{x}+\boldsymbol{U}(\boldsymbol{x})\varDelta t \in B \right\}


with a new random intensity vector :math:`\epsilon_j^k`. :math:`B_{\varDelta t}` denotes the
region in which regenerated eddy :math:`\boldsymbol{x}^k(t) \in B_{\varDelta t}` dose not effect the synthetic velocity at the inflow plane until the next time-step.

Mean flow and Reynolds stresses
^^^^^^^^^^^^^^^^

The mean value of the velocity signal :eq:`SEMvelocity` can be expressed as

.. math::
    
    \left\langle u_i \right\rangle = U_i(\boldsymbol{x}) + \frac{1}{\sqrt{N}}\sum_{k=1}^N \left\langle a_{ij} \varepsilon_j^k f_{\boldsymbol{\sigma}(\boldsymbol{x})}(\boldsymbol{x}-\boldsymbol{x}^k) \right\rangle


where the angles denote the mean operator. The independence between the random variables
:math:`\boldsymbol{x}^k` and :math:`\varepsilon_j^k` in the mean operator implies that

.. math::
    
    \left\langle a_{ij} \varepsilon_j^k f_{\boldsymbol{\sigma}(\boldsymbol{x})}(\boldsymbol{x}-\boldsymbol{x}^k) \right\rangle = a_{ij} \left\langle\varepsilon_j^k\right\rangle  \left\langle f_{\boldsymbol{\sigma}(\boldsymbol{x})}(\boldsymbol{x}-\boldsymbol{x}^k)  \right\rangle


The term :math:`\langle\varepsilon_j^k\rangle = 0` since the intensities of the eddies is either
:math:`1` or :math:`-1` with equal probability. Consequently, we obtain

.. math::
    
    \left\langle u_i \right\rangle = U_i(\boldsymbol{x}).


The Reynolds stresses :math:`\langle u_i u_j \rangle` of the synthesized write

.. math::
    
    \langle u_i u_j \rangle = \frac{1}{N}\sum_{k=1}^N\sum_{k=1}^N a_{im}a_{jn} \langle \varepsilon_m^k \varepsilon_n^l \rangle \langle f_{\boldsymbol{\sigma}(\boldsymbol{x})}(\boldsymbol{x}-\boldsymbol{x}^k) f_{\boldsymbol{\sigma}(\boldsymbol{x})}(\boldsymbol{x}-\boldsymbol{x}^l) \rangle


Using again the independence between the random variables :math:`\boldsymbol{x}^k` and :math:`\varepsilon_j^k`, the above equation reduces to

.. math::
    
    \langle u_i u_j \rangle = \frac{1}{N}\sum_{k=1}^N a_{im}a_{jm} \langle f_{\boldsymbol{\sigma}(\boldsymbol{x})}^2(\boldsymbol{x}-\boldsymbol{x}^k)


The term

.. math::
    
    \langle f_{\boldsymbol{\sigma}(\boldsymbol{x})}^2(\boldsymbol{x}-\boldsymbol{x}^k) \rangle = \int_{\mathbb{R}^3} p(\boldsymbol{y}) f_{\boldsymbol{\sigma}(\boldsymbol{x})}^2(\boldsymbol{x}-\boldsymbol{x}^k) = 1


follows from the fact that :math:`\boldsymbol{x}^k` follows a uniform distribution over :math:`B`, i.e. 

.. math::
    :label: distribution

    p(\boldsymbol{y}) = 
    \begin{cases}
    \frac{1}{V_B} & \boldsymbol{y} \in B \\
    0 & \boldsymbol{y} \notin B
    \end{cases}.


Finally, we arrive at

.. math::
    :label: ReynoldsStresses

    \langle u_i u_j \rangle = \frac{1}{N}\sum_{k=1}^N a_{im}a_{jm} = R_{ij}


Hence the Reynolds stresses of the velocity fluctuations generated by the SEM reproduce exactly the input Reynolds stresses.

Two-point correlation
^^^^^^^^^^^^^^^^

The two-point cross-correlation of the velocity fluctuations writes

.. math::
    :label: twoPointCorrelations0

    R_{ij}(\boldsymbol{x},\boldsymbol{r}) = \langle u_i(\boldsymbol{x},t) u_j(\boldsymbol{x}+\boldsymbol{r},t) \rangle


where :math:`\boldsymbol{r} = (r_1,r_2,r_3)` is a vector defining the relative positions between the two points at which the velocity correlations are computed. By :eq:`SEMvelocity` and the linearity of the statistical mean, we obtain

.. math::
    
    R_{ij}(\boldsymbol{x},\boldsymbol{r}) = \frac{1}{N}\sum_{k=1}^N\sum_{k=1}^N a_{im}a_{jn} \langle \varepsilon_m^k \varepsilon_n^l \rangle \langle f_{\boldsymbol{\sigma}(\boldsymbol{x})}(\boldsymbol{x}-\boldsymbol{x}^k) f_{\boldsymbol{\sigma}(\boldsymbol{x}+\boldsymbol{r})}(\boldsymbol{x}+\boldsymbol{r}-\boldsymbol{x}^l) \rangle 


Using again the independence between the positions :math:`\boldsymbol{x}^k` and the intensities
:math:`\varepsilon^k` of the eddies, this yields

.. math::
    :label: twoPointCorrelations1

    R_{ij}(\boldsymbol{x},\boldsymbol{r}) = \frac{1}{N}\sum_{k=1}^N a_{im}a_{jm} \langle f_{\boldsymbol{\sigma}(\boldsymbol{x})}(\boldsymbol{x}-\boldsymbol{x}^k) f_{\boldsymbol{\sigma}(\boldsymbol{x}+\boldsymbol{r})}(\boldsymbol{x}+\boldsymbol{r}-\boldsymbol{x}^k) \rangle 


By :eq:`distribution`, the term in the mean operator writes

.. math::
    :label: twoPointCorrelations2

    \langle f_{\boldsymbol{\sigma}(\boldsymbol{x})}(\boldsymbol{x}-\boldsymbol{x}^k) f_{\boldsymbol{\sigma}(\boldsymbol{x}+\boldsymbol{r})}(\boldsymbol{x}+\boldsymbol{r}-\boldsymbol{x}^k) \rangle = \frac{1}{V_B} \int_B f_{\boldsymbol{\sigma}(\boldsymbol{x})}(\boldsymbol{x}-\boldsymbol{y}) f_{\boldsymbol{\sigma}(\boldsymbol{x}+\boldsymbol{r})}(\boldsymbol{x}+\boldsymbol{r}-\boldsymbol{y}) \mathrm{d}\boldsymbol{y}


Inserting :eq:`twoPointCorrelations2` back to :eq:`twoPointCorrelations1` and using
:eq:`velocityShape`, this yields

.. math::
    :label: twoPointCorrelations3

    R_{ij}(\boldsymbol{x},\boldsymbol{r}) = R_{ij} \cdot \prod_{l=1}^3 \left[f_{\boldsymbol{\sigma}(\boldsymbol{x})} *f_{\boldsymbol{\sigma}(\boldsymbol{x}+\boldsymbol{r})} \right](r_l)


where :math:`∗` denotes the convolution product. For homogeneous turbulence where integral
length scales :math:`\boldsymbol{\sigma}(\boldsymbol{x}) =
\boldsymbol{\sigma}(\boldsymbol{x}+\boldsymbol{r}) =(\sigma,\sigma,\sigma)^T`, the two-point
cross-correlation tensor :math:`R_{ij}(\boldsymbol{x},\boldsymbol{r})` only depends on
:math:`\boldsymbol{r}` and consequently :eq:`twoPointCorrelations3` simplifies to 

.. math::
    :label: twoPointCorrelations4

    R_{ij}(\boldsymbol{r}) = R_{ij} \cdot \prod_{l=1}^3 \left[f*f\right]\left(\frac{r_l}{\sigma}\right)


Recall the integral length scale :math:`L_{ij}` is defined as the integral of the two-point
correlation :math:`R_{ij}(\boldsymbol{x},\boldsymbol{r})` in a particular direction and is thus
proportional to :math:`\sigma`. By integrating :eq:`twoPointCorrelations4`, one easily
verifies that (for homogeneous turbulence) :math:`L_{ij}=C_f\sigma` in every direction where
:math:`C_f` only depends on the choice of :math:`f`. 

Fourier analysis can also be used to obtain the spectra of the synthetic turbulence. Note that
the velocity spectrum tensor :math:`\phi_{ij}(k)` is the Fourier transform of the two-point correlation tensor 

.. math::
    
    \phi_{ij}(\boldsymbol{k}) = \mathcal{F}_{\boldsymbol{k}}\left\{R_{ij}(\boldsymbol{r})\right\}


Recall the convolution theorem for cross-correlation states that 

.. math::
    
    \mathcal{F}_{\boldsymbol{k}}\left\{f * f\right\} = |\mathcal{F}_{\boldsymbol{k}}\left\{f\right\}|^2


Hence the spatial velocity spectrum tensor can be expressed as

.. math::
    
    \phi_{ij}(\boldsymbol{k}) = R_{ij}\sigma^3 \cdot \prod_{l=1}^3|\mathcal{F}_{k_l\sigma}\left\{f\right\}|^2


where :math:`\boldsymbol{k} = (k_1,k_2,k_3)`. More specifically for instance, the
one-dimensional spectra in the :math:`x` direction is

.. math::
    
    E_{ij}(k) = R_{ij}\sigma^3 \cdot |\mathcal{F}_{k_l\sigma}\left\{f\right\}|^2


Two-time correlation
^^^^^^^^^^^^^^^^

The two-time correlation tensor of the velocity, denoted by :math:`R_{ij}(\boldsymbol{x},\tau)`,
is the correlation between :math:`u_i(\boldsymbol{x},t)` and :math:`u_j(\boldsymbol{x},t+\tau)`
at times :math:`t` and :math:`t + \tau` respectively, i.e.,

.. math::
    :label: twoTimeCorrelation0

    R_{ij}(\boldsymbol{x},\tau) = \langle u_i(\boldsymbol{x},t) u_j(\boldsymbol{x},t+\tau) \rangle.


By :eq:`SEMvelocity` and the linearity of the statistical mean, we have

.. math::
    :label: twoTimeCorrelation1

    R_{ij}(\boldsymbol{x},\tau) = \frac{1}{N}\sum_{k=1}^N\sum_{k=1}^N a_{im}a_{jn} \langle \varepsilon_m^k(t) \varepsilon_n^l(t+\tau) f_{\boldsymbol{\sigma}(\boldsymbol{x})}(\boldsymbol{x}-\boldsymbol{x}^k(t)) f_{\boldsymbol{\sigma}(\boldsymbol{x})}(\boldsymbol{x}-\boldsymbol{x}^l(t+\tau)) \rangle 


The independence between the position :math:`\boldsymbol{x}^k` and intensity
:math:`\varepsilon_m^k` of different eddies implies that, for :math:`k \neq l`, the statistical
mean in :eq:`twoTimeCorrelation1` can be split as follows

.. math::
    
    \langle \varepsilon_m^k(t) \rangle \langle \varepsilon_n^l(t+\tau) \rangle \langle f_{\boldsymbol{\sigma}(\boldsymbol{x})}(\boldsymbol{x}-\boldsymbol{x}^k(t)) \rangle \langle f_{\boldsymbol{\sigma}(\boldsymbol{x})}(\boldsymbol{x}-\boldsymbol{x}^l(t+\tau)) \rangle = 0


Consequently :eq:`twoTimeCorrelation1` reduces to

.. math::
    :label: twoTimeCorrelation2

    R_{ij}(\boldsymbol{x},\tau) = \frac{1}{N}\sum_{k=1}^N a_{im}a_{jn} \langle \varepsilon_m^k(t) \varepsilon_n^k(t+\tau) f_{\boldsymbol{\sigma}(\boldsymbol{x})}(\boldsymbol{x}-\boldsymbol{x}^k(t)) f_{\boldsymbol{\sigma}(\boldsymbol{x})}(\boldsymbol{x}-\boldsymbol{x}^k(t+\tau)) \rangle 


Before computing the term in the angles, we define :math:`B_{\tau} \in B`  such that all eddies
that present in :math:`B_{\tau}` at time :math:`t` will be convected far enough so that they
will be recycled at least once before time :math:`t+\tau`

.. math::
    
    B_{\tau} = \left\{\boldsymbol{x}\in B, \ \boldsymbol{x}+\tau \boldsymbol{U}(\boldsymbol{x}) \in B \right\}


If :math:`\boldsymbol{x}^k(t)\in B_{\tau}`, then it is going to be recycled between time
:math:`t` and :math:`t+\tau` and hence both :math:`\boldsymbol{x}^k(t+\tau)` and
:math:`\varepsilon_m^k(t+\tau)` will be independent of their previous values. The contribution
of an eddy :math:`k` located within the region where :math:`\boldsymbol{x}^k(t) \in B_{\tau}` to
the term in the angles of :eq:`twoTimeCorrelation2` is thus zero. On the contrary if
:math:`\boldsymbol{x}^k(t) \in B_{\tau}`, the eddy :math:`k` will remain inside of the box
:math:`B` at time :math:`t + \tau` and hence :math:`\varepsilon_m^k(t+\tau) =
\varepsilon_m^k(t)` and :math:`\boldsymbol{x}^k(t+\tau)
=\boldsymbol{x}^k(t)+\tau\boldsymbol{U}(\boldsymbol{x}^k)`. Thus both
:math:`\varepsilon_n^k(t+\tau) =  \varepsilon_n^k(t)` and :math:`\boldsymbol{x}^k(t+\tau)`
depend on the previous position :math:`\boldsymbol{x}^k(t)` of eddy :math:`k` relative to
:math:`B_{\tau}`. By :eq:`ReynoldsStresses` and the definition of :math:`B_{\tau}`,
:eq:`twoPointCorrelations0` can then be replaced by

.. math::
    :label: twoTimeCorrelation3

    R_{ij}(\boldsymbol{x},\tau) = R_{ij} \int_{B/B_{\tau}}f_{\boldsymbol{\sigma}(\boldsymbol{x})}(\boldsymbol{x}-\boldsymbol{y}) f_{\boldsymbol{\sigma}(\boldsymbol{x})}(\boldsymbol{x}-(\boldsymbol{y}+\tau\boldsymbol{U}_c)) \ \mathrm{d}\boldsymbol{y}


Since :math:`\boldsymbol{y}\in B_{\tau}` leads to
:math:`f_{\boldsymbol{\sigma}(\boldsymbol{x})}(\boldsymbol{x}-(\boldsymbol{y}+\tau\boldsymbol{U}))=0`,
the integral over :math:`B/B_{\tau}` in the above expression can be extended to an integral over
:math:`B`. Besides :math:`\boldsymbol{y}\in B` suggests
:math:`f_{\boldsymbol{\sigma}(\boldsymbol{x})}(\boldsymbol{x}-\boldsymbol{y})=0` as previously
demonstrated, therefore the integral in :eq:`twoTimeCorrelation3` can be further extended to
an integral over :math:`\mathbb{R}^3`. Using :eq:`velocityShape`, we finally arrive at

.. math::
    :label: twoTimeCorrelation4

    R_{ij}(\boldsymbol{x},\tau) = R_{ij} \cdot \prod_{l=1}^3[f*f]\left(\frac{\tau U_{l}(\boldsymbol{x})}{\sigma_l(\boldsymbol{x})}\right)


In the case where the mean velocity is in the x-direction only :math:`\boldsymbol{U} = (U,0,0)`
and the target turbulence is homogeneous, :eq:`twoTimeCorrelation4` simplifies to

.. math::
    
    R_{ij}(\boldsymbol{x},\tau) = R_{ij} [f*f]\left(\frac{\tau U(\boldsymbol{x})}{\sigma(\boldsymbol{x})}\right)


Thus the two-time correlation of the signal at time :math:`\tau` is simply the autocorrelation
function of :math:`f` at separation distance :math:`\tau U /\sigma`. By integrating the above
equation it can be proved that the integral time scale of the signal writes :math:`T = \sigma/U
C_f` where :math:`C_f` is a coefficient only depends on the choice of :math:`f`. Since the
synthetic velocity is a stationary process, the information the two-time cross-correlation
tensor :math:`R_{ij}(\boldsymbol{x},\tau)` contains can be re-expressed in terms of the wave number velocity spectrum tensor which writes

.. math::
    
    \phi_{ij}(\boldsymbol{x},\omega) = \mathcal{F}_{\omega}\{R_{ij}(\boldsymbol{x},\tau)\}


Using again the convolution theorem as expressed, the above expression simplifies to

.. math::
    
    \phi_{ij}(\boldsymbol{x},\omega) = R_{ij}\frac{\sigma}{|U|} |\mathcal{F}_{\omega\sigma / |U|}\{f\}|^2


Commonly used velocity shape functions
^^^^^^^^^^^^^^^^

We list three commonly used velocity shape functions :math:`f` below for reference. There are the tent function, the step function and the truncated Gaussian function.

* Tent function

    .. math::
	:label: ftent

	f(x) =
	\begin{cases}
	\sqrt{\frac{3}{2}}(1-|x|), & 0 \leq |x| < 1 \\
	0, & |x| \geq 1
	\end{cases}


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


    .. math::
	
	[f*f](r) = 
	\begin{cases}
	e^{-9r^2/2} & \leq |r| < 2 \\
	0, & |r|\geq 2
	\end{cases}


    where :math:`C` is a constant that ensures :math:`f` satisfies the normalization
    :eq:`normalization`.



.. _section4:
Digital filtering method
---------------------

The synthetic digital filtering method (SDFM) initiated by :cite:`klein2003` attempts to model
the spatial and temporal coherence of turbulent inflow through the digital filtering
uncorrelated random data, and account for inhomogeneity and anisotropy using the method proposed
by :cite:`lund1998`. It is relatively easy to implement and is able to reproduce the first and
second order one-point statistics as well as autocorrelation function. However, the synthetic
turbulence generated by SDFM does not satisfy the continuity equation. :cite:`kim2013` offered a promising approach to enforce the divergence-free constraint in the SDFM by inserting the synthetic turbulence on a transverse plane near the inlet and relying on pressure-velocity coupling to do the correction. From a computational wind engineering point of view, the ability of SDFM to impose a two-point spatial correlation directly is very attractive.

We now briefly introduce the filtering method by :cite:`klein2003`. In order to create two-point
correlations, let :math:`r_m` be a series of random data with zero mean and unity variance, then

.. math::
    
    u_m = \sum_{n=-N}^N b_n r_{m+n}


defines a convolution or a digital linear non-recursive filter. The :math:`b_n` are filter
coefficients and :math:`N` is related to the length of the filter. The independence between two
different random numbers :math:`r_m` and :math:`r_n` implies that :math:`\langle r_m r_n \rangle
= 0` for :math:`m \neq n` and consequently the two-point correlation between :math:`u_{m}` and
:math:`u_{m+k}` writes

.. math::
    :label: SDF1

    R_{uu}(k\varDelta x) = \frac{\langle u_{m} u_{m+k} \rangle}{\langle u_{m} u_{m} \rangle} = \sum_{j=-N+k}^N b_j b_{j-k} / \sum_{-j=-N}^N b_j^2


where :math:`\varDelta x` is the grid spacing. Note that :math:`u_{m}` and :math:`u_{m+k}` can
be interpolated as the values of a random variable field (e.g., velocity) at two distinct grid
points with a distance :math:`k\varDelta x` defined on a one dimensional axis. It is
straightforward to tell :eq:`SDF1` defines a relation between the filter coefficients and the
correlation function of :math:`u_m` (denoted by :math:`R_{uu}` hereafter). This suggests that a
prescribed correlation function can be reproduced through a careful determination of the filter
coefficients. Also note that the coefficients should be determined such that the resulting
correlation function fulfil some basic properties like :math:`R_{uu}(0)=1`, :math:`R_{uu}(\infty) = 0` and the prescribed integral length scales.

For a general target correlation function, the filter coefficients :math:`b_n` can be computed
by solving a system of non-linear equations in the form of :eq:`SDF1` with a multidimensional Newton method. The procedure can be taken from a standard textbook and needs no further comment. However, for a Gaussian or an exponential type of correlation function, there exists a simple but approximate prescribed solution. More specifically, for a Gaussian correlation function in the form of

.. math::
    :label: gaussian

    R(r) = \mathrm{exp}\left(-\frac{\pi r^2}{4L^2}\right)


where :math:`r` is the distance and :math:`L` is the length scale. It is possible to
approximately reproduce :eq:`gaussian` by computing the filter coefficients as

.. math::
    
    b_k = \tilde{b}_k / \left( \sum_{j=-N}^N \tilde{b}_j^2 \right)^{1/2}


where

.. math::
    
    \tilde{b}_k = e^{-\frac{\pi k^2}{4n^2}}


The width :math:`N` of the filter should be chosen such that :math:`N\geq 2n` (where :math:`n=L\varDelta x`) to ensure the accuracy of the approximation. On the other hand, for an exponential correlation function

.. math::
    
    R(r) = \mathrm{exp}\left(-\frac{\pi |r|}{2L}\right)


It is suggested :cite:`xie2008` to evaluate the filter coefficients using

.. math::
    :label: exponential

    b_k = \tilde{b}_k / \left( \sum_{j=-N}^N \tilde{b}_j^2 \right)^{1/2}


where

.. math::
    
    \tilde{b}_k = e^{-\frac{\pi|k|}{n}}


Again, the width :math:`N` of the filter should be chosen such that :math:`N\geq 2n` (where
:math:`n=L\varDelta x`) to ensure the accuracy of the approximation. Now we have finished the
discussion of the digital filtering method for one-dimensional case. Such a technique of
generating spatially (or temporally) correlated data from general random numbers can be easily
extended to three dimensional case by introducing multi-index filter coefficients :math:`b_{ijk}` defined as

.. math::
    
    b(i,j,k) = b_{ijk} = b_i \cdot b_j \cdot b_k


An algorithm for generating inflow data may look like this (alternatively one can generate a large volume of data, store it and convect it through the inflow plane by applying Taylor's hypothesis):


(a) Choose for each coordinate direction corresponding to the inflow plane a length scale
    :math:`L_y = n_y\varDelta y`, :math:`L_z = n_z\varDelta z`, a time scale :math:`T` and determine
    the filter width :math:`N_{\alpha}` (:math:`\alpha =x,y,z`) accordingly.

(b) Initialize and store three random fields :math:`R_{\alpha}` (again :math:`\alpha =x,y,z`)
    of dimensions :math:`[-N_x:N_x,-N_y+1:M_y+N_y,-N_z+1:M_z+N_z]` where :math:`M_y \times M_z` denotes the dimensions of computational gird of the inflow plane.

(c) Compute the filter coefficients :math:`b(i,j,k)` with a prescribed function or by a
multidimensional Newton method such that the resulting correlation function :eq:`SDF1` meets the target one.

(#) Applying the following filter operation for :math:`j=1,\ldots,M_y`, :math:`k=1,\ldots,M_z`

    .. math::
	
	\Psi_{\alpha}(j,k) = \sum_{i'=-N_x}^{N_x}\sum_{j'=-N_y}^{N_y}\sum_{k'=-N_z}^{N_z}b(i',j',k')R_{\alpha}(i',j+j',k+k')


    which yields the two-dimensional arrays of spatially correlated data :math:`\Psi_{\alpha}`,
    :math:`\alpha =x,y,z`.

(#) Output velocity data with the transformation

    .. math::
	
	u_i(j,k) = U_i + a_{ij}\Psi_j(j,k)


    where the coefficients :math:`a_{ij}` are given by :eq:`LundCoefficients`. This step ensures the synthetic velocity reproduces the target mean velocity and Reynolds stress tensor.

(#) Discard the first :math:`(y,z)`-plane of :math:`\Psi_{\alpha}` and shift the whole data:
    :math:`\Psi_{\alpha}(i,j,k) := R_{\alpha}(i+1,j,k)`. Fill the plane :math:`R_{\alpha}(N_x,j,k)` with new random numbers.

(#) Repeat the steps (d) :math:`\sim` (g) for each time step.



If the target correlation function is an exponential function, an alternative approach by
:cite:`xie2008` can be adopted for generating inflow turbulence which turns out to be much more
efficient than the method of :cite:`klein2003`. Instead of using the filtering operation discussed above, Xie and Castro's method obtain the temporal correlation with the expression

.. math::
    :label: temporalCorrelation

    \Psi_{\alpha}(t+\varDelta t,j,k) = \Psi_{\alpha}(t,j,k)\mathrm{exp}\left(-\frac{\pi \varDelta t}{2T} \right)+\varPsi_{\alpha}(t,j,k)\left[1-\mathrm{exp}\left(-\frac{\pi \varDelta t}{2T} \right)\right]^{0.5}


where :math:`\Psi_{\alpha}(t,j,k)` and :math:`\varPsi_{\alpha}(t,j,k)` are two set of
spatially-correlated random data resulting from a two dimensional filtering operation. For
simplicity, we write :math:`\Psi_{\alpha,0}`, :math:`\Psi_{\alpha,k}`,
:math:`\varPsi_{\alpha,0}` and :math:`\varPsi_{\alpha,k}` for :math:`\Psi_{\alpha}(t,j,k)`,
:math:`\Psi_{\alpha}(t+k\varDelta t,j,k)`, :math:`\varPsi_{\alpha}(t,j,k)` and :math:`\varPsi_{\alpha}(t+k\varDelta t,j,k)`, respectively. One easily verifies that

.. math::
    
    \begin{split}
    \left\langle \Psi_{\alpha,0}\Psi_{\alpha,k} \right\rangle &= \left\langle \Psi_{\alpha,0}\left\{\Psi_{\alpha,k-1}\left(-\frac{\pi \varDelta t}{2T} \right)+ \varPsi_{\alpha,k-1}\left[1-\mathrm{exp}\left(-\frac{\pi \varDelta t}{2T} \right)\right]^{0.5}\right\}\right\rangle \\
    & = \left\langle \Psi_{\alpha,0} \Psi_{\alpha,k-1} \right\rangle \mathrm{exp}\left(-\frac{\pi \varDelta t}{2T}\right) \\
    & \cdots \\
    & = \mathrm{exp}\left(-\frac{k\pi \varDelta t}{2T}\right)
    \end{split}


which reproduces an exponential function. An overall algorithm for generating the inflow
velocity supported by the method of :cite:`xie2008` can be stated as follows


(a) Choose for each coordinate direction corresponding to the inflow plane a length scale
    :math:`L_y = n_y\varDelta y`, :math:`L_z = n_z\varDelta z`, a time scale :math:`T` and determine
    the filter width :math:`N_{\alpha}(\alpha =x,y,z)` accordingly.

(b) Initialize and store three random fields :math:`R_{\alpha}` (again :math:`\alpha =x,y,z`)
    of dimensions :math:`[-N_y+1:M_y+N_y,-N_z+1:M_z+N_z]` where :math:`M_y \times M_z` denotes the dimensions of computational gird in the inflow plane.

(c) Compute the filter coefficients :math:`b(j,k)` with a prescribed function or by a multidimensional Newton method such that the resulting correlation function meet the target one.

(#) Applying the following filter operations for :math:`j=1,\ldots,M_y`, :math:`k=1,\ldots,M_z`

    .. math::
	
	\varPsi_{\alpha}(j,k) = \sum_{j'=-N_y}^{N_y}\sum_{k'=-N_z}^{N_z}b(j',k')R_{\alpha}(j+j',k+k')


    which yields the two-dimensional arrays of spatially correlated data :math:`\varPsi_{\alpha}`,
    :math:`\alpha =x,y,z`.

(#) Compute :math:`\Psi_{\alpha}(j,k)` with :eq:`temporalCorrelation` and output the velocity signal with the transformation

    .. math::
	
	u_i(j,k) = U_i + a_{ij}\Psi_j(j,k)


    where the coefficients :math:`a_{ij}` are given by :eq:`LundCoefficients`. Again, this step ensures the synthetic velocity reproduces the target mean velocity and Reynolds stress tensor.

(#) Repeat the steps (d) :math:`\sim` (f) for each time step.

References
----------

.. bibliography:: references.bib
   :cited:
   :style: unsrt

