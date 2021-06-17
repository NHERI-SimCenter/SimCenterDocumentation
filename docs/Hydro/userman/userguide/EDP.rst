.. _lbl-EDPDemPara:

******************************************
EDP: Demand Parameters
******************************************

This panel is where the user selects which outputs will be displayed when
the simulation runs. There are several options available in the pull-down.

#. Standard
#. User Defined

Standard
--------

When the user selects this option, there are no additional
inputs required. The standard EDP generator will ensure the
max absolute value of the following is obtained:


#. Relative Floor displacements:
#. Absolute Floor Accelerations
#. Interstory Drifts

The results will contain results for these in abbreviated form:

#. PFD peak relative floor displacement Event#-PFD-FLOOR-CLINE
#. PFA peak floor acceleration Event#-PFA-FLOOR-CLINE
#. PID peak inter-story drift: Event#-PID-STORY-CLINE

.. note::   

   Floors are numbered starting at floor 0, and stories are numbered starting at story 1.

User Defined
------------
As shown in :numref:`userEDP`, this panel allows users to determine their own output and process it. When using this option, the user provides additional data:

.. _userEDP:

.. figure:: figures/userDefinedEDP.png
    :align: center
    :figclass: align-center

    User Defined EDP panel.


1. Additional Input: These are additional commands invoked by the analysis application before the transient analysis is performed. For example, for OpenSees, this would be a script containing a series of recorder commands. A recorder file passed to OpenSees might look like the following:

  .. code:: tcl

     recorder EnvelopeNode -file node.out -node 1 2 3 4 -dof 1 disp
     recorder EnvelopeElement -file ele.out -ele 1 2 3 forces

2. Postprocess Script: This is a python or Tcl script invoked after the finite element application has run. It must be provided by the user. Its purpose is to process the output files and create a single file, namely results.out. This file must contain a single line with as many entries as EDP's specified. 

For example, a python postprocessing file that would take the outputs from the recorder commands of the previous code block to create the results file needed by the applications might look like the following:

    .. literalinclude:: postprocess.py
            :language: python
           
A Tcl file might look like the following:

.. code:: tcl
      
      set nodeIn [open node.out r]
      while { [gets $nodeIn data] >= 0 } {
         set maxDisplacement $data
      }
      puts $maxDisplacement

      # create file handler to write results to output & list into which we will put results
      set resultFile [open results.out w]
      set results []

      # for each quanity in list of QoI passed
      #  - get nodeTag
      #  - get nodal displacement if valid node, output 0.0 if not
      #  - for valid node output displacement, note if dof not provided output 1'st dof
      
      foreach edp $listQoI {
         set splitEDP [split $edp "_"]  
         set nodeTag [lindex $splitEDP 1]
             if {[llength $splitEDP] == 3} {
                set dof 1
         } else {
                set dof [lindex $splitEDP 3]
         } 
         set nodeDisp [lindex $maxDisplacement [expr (($nodeTag-1)*2)+$dof-1]]
         lappend results $nodeDisp
      }
      
.. warning::

   The name of the output file must be **results.out**.
       
3.  Response Parameters. This is an area in which the user
  associates a variable name with the column of the results output
  file. If the process script has an array of strings named named
  EDP's the script, the Response Parameters will be initially set with
  these values from the script.
