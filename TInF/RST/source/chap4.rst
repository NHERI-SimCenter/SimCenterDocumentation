.. _sec_TInF-usage:

Usage
==================

The workflow for adding parameters for various kinds of turbulence inflow models to your 
OpenFOAM model is as follows.

**Step 1: Source Selection**
    Start the Turbulence Inflow Tool (TInF) and on the opening screen select the Source Tab
    (:numref:`fig_TInF01`, item 1).  Use the locate button (:numref:`fig_TInF01`, item 3) to navigate to your OpenFOAM input tree.  

    .. _fig_TInF01:
    .. figure:: _images/TInF-01.png

	Start page - Source selection

    .. _fig_TInF02:
    .. figure:: _images/TInF-02.png

	Model tree selection (MacOS version shown, but similar on Windows systems)

    :numref:`fig_TInF02` shows a sample selection. The distribution comes with simple example input located
    in installed application folder.  Your provided input must at least contain the folders \texttt{0},
    \texttt{constant}, and \texttt{system}. Navigate to the parent folder (:numref:`fig_TInF02`, item 2) and
    press open (:numref:`fig_TInF02`, item 3).

    .. _fig_TInF04:
    .. figure:: _images/TInF-04.png

	Boundary patch selection

    The tool will display your selection (:numref:`fig_TInF04`, item 2), parse your boundary condition
    definition and provide you with a list of found boundary patches (:numref:`fig_TInF04`, item 3).  If your folder does not contain a parsable boundary patch definition, the folder will be displayed in red and no boundary patch selection will be offered.

    Use the pull-down menu to select the proper boundary patch to which the turbulence inflow conditions will be applied.


**Step 2: Parameter Definition**
    In the Parameters tab (:numref:`fig_TInF07` and  :numref:`fig_TInF08`, item 1), first select the desired method.

    .. _fig_TInF07:
    .. figure:: _images/TInF-07.png

	Parameter selection tab -- top of page

    .. _fig_TInF08:
    .. figure:: _images/TInF-08.png

	Parameter selection tab -- bottom of page


    Based on the selected method, additional parameters will be collected.  The particular parameters and
    their meaning are discussed in detail in Chapter :ref:`sec:TInF-theory`.
    Depending on selected model and sub-options, as well as your screen size, you may need to scroll down to
    get access to all parameter fields (:numref:`fig_TInF07` and  :numref:`fig_TInF08`, item 2).
    
    .. note:: the window manager on MacOS is hiding any scroll bar until you attempt to slide the parameter fields up.

**Step 3: Export Changes to your Model**

    Once all parameters have been defined, you are ready to export the necessary changes to your model definition files.

    .. _fig_TInF09:
    .. figure:: _images/TInF-09.png

	Export panel

    In the Export panel (:numref:`fig_TInF09`, item 1), verify that the correct boundary patch is selected
    (:numref:`fig_TInF09`, item 2).
    This is the same as what is selected in the Source panel (:numref:`fig_TInF04`, item 3). Actually, those fields are linked and changes to either will automatically sync the other.

    Once you are certain that the correct patch has been selected, press the Export button
    (:numref:`fig_TInF09`, item 3) to write the updated boundary definition files.  Existing files will be saved to name.orig.

    .. warning:: Only one copy of the original file will be made.  Subsequent exports will treat the previously modified files as the source to be saved.  Any older versions will be overwritten without further warning.




