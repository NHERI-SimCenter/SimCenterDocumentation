.. _lblquoFEM_DCV:

Running in Your Browser
-----------------------

It is possible to run quoFEM remotely at DesignSafe through your browser using `NICE DCV <https://aws.amazon.com/hpc/dcv/>`_, a high-performance remote display protocol that provides users with a remote desktop experience. Running |app| in this manner requires that you create a directory in DataDepot and upload your working files to that directory. The advantage of using the remote desktop service is that you don't have to install |app|, the disadvantage is that you have to upload and download files and will sometimes have to wait a while for your application to start.

To launch |app| in your browser you select the following `link <https://www.designsafe-ci.org/rw/workspace/#!/quoFEM-frontera-1.0.0>`_. This will open up a page as shown below:

.. _figDCV_quoFEM:

.. figure:: quoFEM.png
	:align: center
	:figclass: align-center

This page requires that you fill in the following:

 #. Working directory: the directory that contains the files that you want to work on. You can drag a directory from the data depot browser on the left into this input.
 #. Email Address: The address to which an email will be sent when the job runs. The email will contain a link to follow to the actual running job.
 #. Desktop Resolution: select the desktop screen size for the visualization.
 #. Maximum Job runtime: The maximum time you expect this job to run. Note that after this amount of time, your job will be killed by the job scheduler.
 #. Job name: A descriptive name you want to associate with the job.
 #. Job output archive location (optional): location where the job output should be archived;
 #. Node Count: Number of requested process nodes for the job. Note ONLY USE 1 here, as only 1 Node is used.
 #. Processors per Node: numbers of cores per node for the job.

Once all information has been entered you can select the **RUN** button to launch the job. Depending on how busy the `**Frontera** <https://https://portal.tacc.utexas.edu/system-monitor>`_ at TACC is, your job may start within 30 sec, or it may take longer. When it starts an email will be sent to the address provided in the input containing a link to the running application, and if you have remained on the page a popup page will appear with a **CONNECT** button, which when pressed will take you to same address contained in the email. The page it takes you to is as shown below:

.. _figDCV_quoFEM:

.. figure:: dcvLogin.png
	:align: center
	:figclass: align-center

On this page, you must re-enter your DesignSafe username and password.

.. warning::

   #. You must be part of the **DCV** allocation at DesignSafe to run this. If you do not have such an allocation, you can request membership by submitting a `ticket to DesignSafe <https://www.designsafe-ci.org/help/new-ticket/>`_. If you do not have a membership, this last login step will fail even if you have provided your correct information!

   #. DesignSafe has a limited number of licenses at its disposal, so your job may not always run.

