Verification
================

An easy way to verify proper installation and operation of the TInF Tool is through the set of example modeling files
distributed as part of the installation.  In order to validate your installation, first copy the folder ::

    C:\Program Files\SimCenter Apps\SimCenterTInF\Examples

on Windows 10, or ::

    /Applications/SimCenter Apps/SimCenterTInF/Examples

on MacOS, to your Desktop or Document folder.

This folder contains, among others, the following files:

#.
	*Examples/building/0/U*:

	.. literalinclude:: validation/ExampleInput/building/0/U.orig
	
#. 
	and *Examples/building/system/controlDict*:

	.. literalinclude:: validation/ExampleInput/building/system/controlDict.orig
	

Now run the TInF Tool on that copy by selecting *Desktop\\Examples*
(or, if you placed your copy in the Documents folder, *Documents\\Examples*), and 

* under "select what boundary to modify" select *inlet*

* under "method selection" select *synthetic eddy*

* use defaults for the rest

* click the EXPORT button (once). The files will be written on the first click. It is not recommended to click the EXPORT button more than once.

\
As a result, there will be two modified and one entirely new file with the contents as follows.

#.
	modified *Examples/building/0/U*:

	.. literalinclude:: validation/ExampleInput/building/0/U


#.
	modified *Examples/building/system/controlDict*:

	.. literalinclude:: validation/ExampleInput/building/system/controlDict


#.
	and added *Examples/building/constant/inflowProperties*:

	.. literalinclude:: validation/ExampleInput/building/constant/inflowProperties
	

