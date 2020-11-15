.. _lblrunRemote:

**************************
Run Remotely on DesignSafe
**************************

There are two ways to run the applications remotely on DesignSafe: one is through the `Data Depot <https://www.designsafe-ci.org/data/browser/>`_ user interface on DesignSafe, where job details are submitted through a Jupyter notebook. The other is by calling on Tapis CLI directly through Ubuntu.


Prepare Input Files
==========================

1. Prepare the input files in a folder called ``input_data``, then zip the folder. You may use this example input file set (:download:`input_data.zip <files/input_data.zip>`) as a template.


2. Prepare workflow settings in the configuration file. You may use the example configuration file (:download:`rWHALE_config_remote.json <files/rWHALE_config_remote.json>`) as a template.


      - Set ``'runDir'`` to ``/tmp/rWhale/``.
      - Set ``'localAppDir'`` to ``/tmp/rWhale/``.
      - Specify applications for each workflow step and their inputs. For more details on the format of the configuration file, see :ref:`Inputs <lblInputs>`.


3. Upload the zipped ``input_data`` file and configuration file to "My Data" on the DesignSafe `Data Depot <https://www.designsafe-ci.org/data/browser/>`_.


4. Upload the :download:`CreateLauncherTasks script <files/CreateLauncherTasks.py>` and a Jupyter notebook with commands for setting up the job on Tapis. You can use this example Jupyter notebook (:download:`run_rWHALE.ipynb <files/run_rWHALE.ipynb>`) as a template.

.. _figContext:

.. figure:: figures/DS_data_depot.png
   :align: center
   :figclass: align-center



Run Job Through Jupyter
==========================

This method uses Jupyter notebook to run the job, accessing Tapis CLI in the backend.


5. Click on the run_rWHALE.ipynb notebook, then click "Open in Jupyter". You will be taken to a new page for editing and running the Jupyter notebook.

.. literalinclude:: files/run_rWHALE.py
   :language: python
   :linenos:


6. Specify settings for running the job on Stampede2. Submit the job by running all cells in the Jupyter notebook.

.. jsonschema:: App_Schema.json#/properties/runRemote




Submit Job Through Tapis
==========================

This method submits the job using Tapis CLI directly. If using Windows,  this is executed in the Ubuntu subsystem.

5. First, ensure that Tapis CLI is installed on your computer. Open a Ubuntu window and install Tapis CLI using ``pip``:

      ``pip install tapis-cli``


Or, install Tapis CLI from Github:

::
      git clone https://github.com/TACC-Cloud/tapis-cli-ng.git
      cd tapis-cli-ng/
      pip install --upgrade --user .


6. Set up a Tapis session on each host where you will use the Tapis CLI. This is a one-time operation where you will be asked to agree to terms, select a tenant, and finally enter a username and password for that tenant. Run the command:

      ``tapis auth init``


You will see an output in the Ubuntu window similar to the following.

      - Select "y" to the prompts.
      - Set ``tenant_name`` to "designsafe".
      - Set ``username`` and ``password`` to your TACC username and password.
      - Keep ``registry_url`` to ``https://index.docker.io``
      - Set ``git_username`` and ``git_token`` to your Github account details. See directions `here <https://help.github.com/en/github/authenticating-to-github/creating-a-personal-access-token-for-the-command-line>`_ for more information on generating a git token.

.. code-block::

      Use of Tapis requires acceptance of the TACC Acceptable Use Policy
      which can be found at https://portal.tacc.utexas.edu/tacc-usage-policy
      Do you agree to abide by this AUP? (type 'y' or 'n' then Return) y
      Use of Tapis requires acceptance of the Tapis Project Code of Conduct
      which can be found at https://tapis-project.org/code-conduct
      Do you agree to abide by this CoC? (type 'y' or 'n' then Return) y
      To improve our ability to support Tapis and the Tapis CLI, we would like to
      collect your IP address, operating system and Python version. No personally identifiable information will be collected. This data will only be shared in
      aggregate form with funders and Tapis platform stakeholders.
      Do you consent to this reporting? [Y/n]: Y

      +---------------+--------------------------------------+----------------------------------------+
      | Name | Description | URL |
      +---------------+--------------------------------------+----------------------------------------+
      | 3dem | 3dem Tenant | https://api.3dem.org/ |
      | agave.prod | Agave Public Tenant | https://public.agaveapi.co/ |
      | araport.org | Araport | https://api.araport.org/ |
      | bridge | Bridge | https://api.bridge.tacc.cloud/ |
      | designsafe | DesignSafe | https://agave.designsafe-ci.org/ |
      | iplantc.org | CyVerse Science APIs | https://agave.iplantc.org/ |
      | irec | iReceptor | https://irec.tenants.prod.tacc.cloud/ |
      | portals | Portals Tenant | https://portals-api.tacc.utexas.edu/ |
      | sd2e | SD2E Tenant | https://api.sd2e.org/ |
      | sgci | Science Gateways Community Institute | https://sgci.tacc.cloud/ |
      | tacc.prod | TACC | https://api.tacc.utexas.edu/ |
      | vdjserver.org | VDJ Server | https://vdj-agave-api.tacc.utexas.edu/ |
      +---------------+--------------------------------------+----------------------------------------+

      Enter a tenant name [tacc.prod]:
      tacc.prod username: taccuser
      tacc.prod password for taccuser:



7. Initialize a job with the name "RDT_test_run" by executing the command:

      ``tapis jobs init rWhale-2.1.0 --name RDT_test_run > job.json``

8. A job.json file is created. You may make changes to this file using VIM Editor, by running the command:

      ``vim job.json``

9. Edit the job.json file to specify settings for running the job on Stampede2. To make edits in the VIM Editor, type ``Ctrl+I``. To exit out of the editor, type ``:wq``.


10. Once the job.json file is prepared, submit the job by running the command:

      ``tapis jobs submit -F job.json``

An ACCEPTED status indicates the job.json was valid, and e-mail alerts (if they were specified in job.json) will track
the progress of the job. Also take note of the long hexadecimal id when you submit the job. This identifier can be
used to track progress and download results.
