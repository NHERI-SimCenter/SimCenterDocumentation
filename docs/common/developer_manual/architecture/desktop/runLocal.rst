.. _lblrunLocal:

Run Locally on Your Desktop
===========================

Running applications locally on a personal desktop is convenient for running small-scale jobs and debugging. For larger jobs, the applications are available on DesignSafe for utilizing high-performance computing resources.

1. Follow the directions in :ref:`How to Build <lblHowtoBuild>` to install the backend applications on your local desktop. Move the applications folder to a separate directory (such as ``C:/rWHALE/``).

2. Prepare the input files in a folder called ``input_data``, then zip the folder. You may use this example input file set (:download:`input_data_eq.zip <files/input_data_eq.zip>`) as a template.

3. Prepare workflow settings in the configuration file. You may use the example configuration file (:download:`rWHALE_config_eq.json <files/rWHALE_config_eq.json>`) as a template.


    - Set ``'runDir'`` to the path containing the ``input_data`` folder. If the configuration file is in the same directory, set ``'remoteDir'='...'``.
    - Set ``'localAppDir'`` to the path containing the applications folder (such as ``C:/rWHALE/``).
    - Specify applications for each workflow step and their inputs. For more details on the format of the configuration file, see :ref:`Inputs <lblInputs>`.

Depending on the required application-specific inputs, the final file directory structure may follow a format such as:

::

    rWHALE
    ├── applications
    └── cantilever_example
        ├── rWHALE_config.json
        └── input_data
            ├── model
            ├── records
            ├── EDPspecs.json
            └── input_params.csv

3. The workflow is run through the command window by calling on python and specifying paths to the application files, input files, and desired location for the results folder.

.. code-block::

    python <path to RDT_workflow.py> <path to rWHALE_config.json> --registry <path to WorkflowApplications.json> --referenceDir <path to input_data folder> -w <path to output results folder>



    where:
    - **<path to RDT_workflow.py>** is the full path to the file "RDT_workflow.py" in the applications folder, i. e. "C:/rWHALE/applications/Workflow/RDT_workflow.py"
    - **<path to rWHALE_config.json>** is the full path to the provided file "rWHALE_config.json", i. e. "C:/rWHALE/rWHALE_config.json"
    - **<path to WorkflowApplications.json>** is the full path to the file "WorkflowApplications.json" in the applications folder, i. e. "C:/rWHALE/applications/Workflow/WorkflowApplications.json"
    - **<path to input_data folder>** is the full path to the folder with all input files, i. e. "C:/rWHALE/cantilever_example/input_data/"
    - **<path to output results folder>** is the full path to the folder where results will be saved, i. e. "C:/rWHALE/cantilever_example/results"




4. In the command window, the workflow will output the following messages:

.. literalinclude:: files/log.txt
    :linenos:
    :emphasize-lines: 1
