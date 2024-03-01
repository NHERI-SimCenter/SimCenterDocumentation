.. _lblEDP:


EDP: Demand Parameters
======================

This panel is where the user selects which outputs will be displayed when
the simulation runs. There are a number of options available in the pull-down

#. Standard
#. User Defined
#. None

Standard
--------

When the user selects there are no additional
inputs required. The standard EDP generator will ensure the
the max absolute value of the following are obtained:


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
As shown in fig userEDP, this panel allows the user to determine their own output and process it. When using this option the user provides additional data:

.. figure:: figures/userDefinedEDP.png
	:align: center
	:figclass: align-center

	User Defined EDP panel.


1. Additional Input: These are additional commands that are invoked by the analysis application
   before the transient analysis is performed. For example, for OpenSees this would be a script
   containing a series of recorder commands. 

  A recorder file passed to OpenSees might look like the following:

  .. code:: tcl

     # recorder EnvelopeNode -file $filename -node $nodeTag1 ... $nodeTagN -dof $DOF1 $DOF2 disp
     recorder EnvelopeNode -file node.out -node 1 2 3 4 -dof 1 disp
     # recorder EnvelopeElement -file $filename -ele $eleTag1 ... $eleTagN forces
     recorder EnvelopeElement -file ele.out -ele 1 2 3 forces

2. Postprocess Script: This is a python or tcl script that will be invoked
  after the finite element application has run. It must be provided by
  the user. It's purpose is to process the output files and create a
  single file, results.out. This file must contain a single line with
  as many entries as EDP's specified.

  For example, a python postprocessing file that would take the outputs from the recorder commands of 
  the pervious code block to create the results file needed by the applications is illustrated as the example 
  python file below along with the tcl script for creating recorders in OpenSees.

.. collapse:: Example post-processing python file

	.. code-block:: python

		#!/usr/bin/python
		# written: fmk, adamzs 01/18
		# import functions for Python 2.X support
		from __future__ import division, print_function
		import sys
		if sys.version.startswith('2'): 
			range=xrange
			string_types = basestring
		else:
			string_types = str
		import sys
		def process_results(inputArgs):
			#
			# process output file "node.out" for nodal displacements
			#
			with open ('node.out', 'rt') as inFile:
				line = inFile.readline()
				line = inFile.readline()
				line = inFile.readline()
				displ = line.split()
				numNode = len(displ)
			inFile.close

			# now process the input args and write the results file
			outFile = open('results.out','w')

			# note for now assuming no ERROR in user data
			for i in inputArgs:
				theList=i.split('_')
				if (len(theList) == 4):
					dof = int(theList[3])
				else:
					dof = 1
				if (theList[0] == "Node"):
					nodeTag = int(theList[1])
					if (nodeTag > 0 and nodeTag <= numNode):
						if (theList[2] == "Disp"):
							nodeDisp = abs(float(displ[((nodeTag-1)*2)+dof-1]))
							outFile.write(str(nodeDisp))
							outFile.write(' ')
						else:
							outFile.write('0. ')
					else:
						outFile.write('0. ')
				else:
					outFile.write('0. ')

			outFile.close

		if __name__ == "__main__":
			n = len(sys.argv)
			responses = []
			for i in range(1,n):
				responses.append(sys.argv[i])

			process_results(responses)

.. collapse:: Example post-processing tcl file

	.. code-block:: tcl
		
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
	  
|
.. warning::

   The name of the output file used in the post-processing script must be **results.out**.
       
3.  Response Parameters. This is an area in which the user
  associates a variable name with the column of the results output
  file. If the process script has an array of strings named named
  EDP's the script, the Response Parameters will be initially set with
  these values from the script.


None
-----------

This option is used only when the user specifies a surrogate model in the SIM tab. Because a surrogate model can evaluate only the EDPs that are pre-trained, we automatically display those quantities, and do not allow users to modify the list. 

.. Note::   
   This option is not for training a surrogate model but for using a pre-trained surrogate model.