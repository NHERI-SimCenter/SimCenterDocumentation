.. _lblInstallation:

*******************
Running Application
*******************

SimCenter Applications can be run in one of two ways:

#. As a Desktop Application

#. Through your Browser

As A Desktop Application
------------------------

All SimCenter applications can be downloaded from the |ResearchTools| page and run as a local application. The advantage of such an approach is that the applications start instantaneously, you can utilize the local files on your desktop in the applications as inputs, you can process the results again on your desktop. The disadnatage of the approach is that it requires downloading the application, and if you are on a Mac downloading and installing an x86 version of **Python**. This section walks you through the installation process on Windows and macOS operating systems from downloading the application to testing that it has been installed correctly.

.. toctree::
   :maxdepth: 2

   install_Windows
   install_macOS
   setupTACC

 
Through Your Browser
--------------------

SimCenter applications can also be run through your browser using DesignSafe resources. **8** compute nodes at TACC have been set aside for this purpose (the **simcenter** queue), allowing 8 individuals to simultaneously be running different simcenter applications. The advantage of this approach is that no installtion of the application is needed. The disadntages being typically a delay in starting the application, files that you want to work on have to be uploaded to TACC to run with the application, extra processing of the results again required the files be downloaded to your local desktop, and you need a **TACC allocation** to use this feature.


.. note::

   #. When in the browser, files you wish to use with the application, e.g. OpenSees scripts, experiemental datasets, have to be uploaded to **TACC** to your **WORK** directory at TACC. As shown in the video, this can be done using **DesignSafe Data Depot** or you can do using **scp**.
   #. Jobs by default go to the **simcenter* queue, a special queue with access to **8** compute nodes set aside by TACC for these applications. If these are busy, i.e. your job seems to take forever to go from the **queueing**state to the **running** state, you can cancel the job request and try a different queue.


      .. note::

	 The browser option is utilizing docker images run from a machine running Linux. For users familiar with docker, these applications are available through dockerhub. Another way to run the applications is using `docker images <https://hub.docker.com/u/fmckenna>`_. 
	 
	 Utilzing Docker
	 ---------------

The ability to run the applications in the browser is made possible through the use of **docker** images that have been created. For users of **docker** these same images can be run locally. To access your local files in the running docker containers, it is advised to bind your $HOME directory when the container starts. The following command can be used to run the application in a docker container:




      

   
