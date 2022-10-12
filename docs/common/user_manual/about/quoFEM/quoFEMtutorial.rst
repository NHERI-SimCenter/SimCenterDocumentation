.. _lbltutorialQUOFEM:


*****
Running quoFEM Using a Python Script
*****

Before We Start
----------------
If you have not yet installed quoFEM, please see 

   * :ref:`Install quoFEM<lblInstallation>`
   * :ref:`Run quoFEM without installation<lblquoFEM_DCV>`



.. |DesignSafe| raw:: html

    <a href="https://www.designsafe-ci.org/" target="_blank">DesignSafe</a>

.. |Texas Super Computing Center (TACC)| raw:: html

    <a href="https://www.tacc.utexas.edu/" target="_blank">Texas Super Computing Center (TACC)</a>


.. |OpenSeesPy example manual| raw:: html

          <a href="https://openseespydoc.readthedocs.io/en/latest/src/examples.html" target="_blank">OpenSeesPy example manual</a>

.. |14.1.1. Elastic Truss Analysis| raw:: html

          <a href="https://openseespydoc.readthedocs.io/en/latest/src/truss.html" target="_blank">14.1.1. Elastic Truss Analysis</a>


.. role:: uqblue

Running an Analysis
----------------
This tutorial will show how a model written/interfaced in python script can be used for global sensitivity analysis. 

.. tabbed:: Step 0 


  :uqblue:`Step 0. Preparing a python model`

     Let us grab **a python script** from |OpenSeesPy example manual|.


       .. figure:: figures/step2_openseesPy.svg
           :align: center
           :figclass: align-center

           Download OpenSeespy Elastic Truss Analysis

     Please follow the steps:

        1. In |OpenSeesPy example manual|, navigate to **Structural Example - Elastic Truss Analysis**
        2. In |14.1.1. Elastic Truss Analysis| page, click download button. Create a **new folder** named ``TrussExample`` and save ``ElasticTruss.py`` in the folder.

          .. important::

               It is important to save the model in a **new folder** instead of root, desktop or downloads

        3. :badge:`Test,badge-primary` if the input script ``ElasticTruss.py`` runs successfully using commend prompt (Windows) or terminal (Mac). To do this,  navigate into ``TrussExample`` folder using 'cd' command and type the following. 

          .. code:: console

             {$PathToPythonExe} ElasticTruss.py

          where ``{$PathToPythonExe}`` should be replaced with the python path found in the preference window.

          .. figure:: figures/step1_preference_default.svg
               :align: center
               :figclass: align-center
               :width: 800

               Find the python path in ``File``-``Preference`` in the manu bar

          According to ``ElasticTruss.py``, the analysis should print out "Passed!", meaning the model ran successfully.

          .. figure:: figures/step0_openseespy_test.svg
             :align: center
             :figclass: align-center

             Testing ``ElasticTruss.py``

          Now we are ready to run probabilistic analysis using this model.

          .. important::
               openseespy, numpy and matplotlib libraries are readily available in quoFEM because:

               * Windows 
                    quoFEM is bundled with a python executable which have those packages pre-installed. See :ref:`here<lblFEM>`.
               * macOS 
                    In the :ref:`installation steps<lblInstallMac>`, the command ``pip3 install nheri_simcenter --upgrade`` will include those packages

               It is important to test the model using the "correct" python executable the quoFEM uses, which is **that shown in the preference**. See :ref:`here<lblFEM>` to read more on python versions and installing additional packages.
               

.. tabbed:: Step 1


  :uqblue:`Step 1. Modifying the model script`


     We now need to indicate quoFEM what are the input **random variables (RVs)** and output **Quantities of Interest (QoIs)**. Let us consider the following setup:

       * **Four RVs**: height (:math:`H`), elastic modulus (:math:`E`), horizontal node (:math:`P_x`), vertical load (:math:`P_y`)
       * **Two QoIs**: horizontal and vertical displacements of node 4 (:math:`u_x` and :math:`u_y`)

     To convey this information to quoFEM, the following steps are needed.

     1. Create ``params.py`` that contains the below four lines, in the folder ``TrussExample``:

       .. literalinclude:: params.py
          :language: py

       This indicates quoFEM the list RVs

     2. Modify the main script ``ElasticTruss.py`` as follows (the modified parts are highlighted)

       .. tabs::

            .. tab:: Modified

               .. literalinclude:: ElasticTruss_quo.py
                  :language: py
                  :emphasize-lines: 5,20,28,42, 76,77     


            .. tab:: Original

               .. literalinclude:: ElasticTruss.py
                  :language: py
                  :emphasize-lines: 5,20,28,42, 76,77     


       In particular,

        * Import ``params.py`` on top of the main script
        * Replace the hard-coded values of RVs with the variables ``H``, ``E``, ``Px``, and ``Py``
        * Write QoI values (``ux`` and ``uy``) to ``results.out``

     3. :badge:`Test,badge-primary` your new python script using the same command used in Step 0. 

        .. code:: console

           {$PathToPythonExe} ElasticTruss.py

        This time, ``results.out`` should be created in the folder ``TrussExample``, which contains the following two values.

        .. figure:: figures/step1_results.svg
            :align: center
            :figclass: align-center
            :width: 500

            Created results.out


     **If the test was successful, remove all the files except** ``ElasticTruss.py`` and ``params.py``. This model can now be readily imported in quoFEM.

     .. important::

          It is important to remove ``results.out`` file after testing.

.. tabbed:: Step 2


  :uqblue:`Step 2. Running quoFEM`


     quoFEM has four input taps - UQ, FEM, RV, EDP(QoI)- that guide user to provide the required inputs for the UQ analysis


     1. **UQ (Uncertainty Quantification)**

        We define the UQ method of interest. We will use ``dakota``-``Sensitivity Analysis`` for this example, but once the user prepares the input script according to Step 1, they can use it for any :ref:`UQ analysis supported in quoFEM<lblUQ>` without additional modifications.

        .. figure:: figures/step2_UQ.PNG
            :align: center
            :figclass: align-center
            :width: 1200

            UQ Panel

     2. **FEM (Finite Element Model or any simulation model)**

        Import the two model scripts prepared in Step 1 here.

        .. figure:: figures/step2_FEM.PNG
            :align: center
            :figclass: align-center
            :width: 1200

            FEM Panel

        The postprocessing script is not needed in this example because the ``results.out`` is already printed in the main script. See :ref:`here<lblFEM>` for more about the postprocessing script     


     3. **RV (Random Variables)**

        Reading ``params.py``, quoFEM auto-populates the RVs as follows.

        .. figure:: figures/step2_RV.PNG
            :align: center
            :figclass: align-center
            :width: 1200

            RV Panel

        Then one can modify their distribution types and parameters. Further, if you believe the some variables are correlated, use correlation button to specify the values.


        .. figure:: figures/step2_RV_corr.PNG
            :align: center
            :figclass: align-center
            :width: 300

            Correlation Window

     4. **EDP (Engineering Demand Parameters) or QoI (Quantities of Interest)**

        Because our python script will write two values in ``results.out`` file, we will specify two QoI as follows.

        .. figure:: figures/step2_QoI.PNG
            :align: center
            :figclass: align-center
            :width: 1200

            EDP Panel

        The order should match that written in the ``results.out`` file, and the specified name of QoIs are used only for the display in this example. Please see :ref:`here<lblQUO_QOI>` to learn about vector QoIs which have length greater than 1 


     When all the fields are filled in, click the the **Run** button, and the analysis will be performed. The program will go into "not responding", but that means analysis is running. You can check the progress status in your **Local Working directory** which can be found in the preference window. The number attached to 'workdir.' indicates the simulation index, and each folder contains the details for each simulation run.

        .. figure:: figures/step2_RES1.PNG
            :align: center
            :figclass: align-center
            :width: 600

            Working directories


     Once analysis is done, move on to the RES tab.

     **RES (Results)**

        The results indicate that the horizontal displacement is most sensitive to the height while vertical displacement is more sensitive to elastic modulus and vertical force. 

        .. figure:: figures/step2_RES2.PNG
            :align: center
            :figclass: align-center
            :width: 1200

            RES - Summary

        And this can be confirmed by the strong trend observed in the scatter plots.

        .. figure:: figures/step2_RES3.PNG
            :align: center
            :figclass: align-center
            :width: 1200

            RES - Data Values - Scatter plot of ``H`` and ``disp_x`` 

        The right/left mouse buttons (fn-clink, option-click, and command-click replaces the left click on Mac) will allow the users to draw various scatter plots, histograms, and cumulative mass plots from the sample points.

        See :ref:`Dakota<lbluqTechnical>` or :ref:`SimCenterUQ<lbluqSimTechnical>` theory manual to learn more about the sensitivity analysis and the difference between main and total indices. Note that the results will be different when probability distribution changes (i.e. when amount of uncertainty in each input variable changes), and users can test different conditions simply by changing distribution in the UQ tab.

.. tabbed:: Step 3

  :uqblue:`Step 3. Running at DesignSafe`

     Users can run the same analysis using high-performance computer at |DesignSafe| at |Texas Super Computing Center (TACC)|. For this, login to DesignSafe by clicking **Login** on the right upper corner of quoFEM, or by clicking **RUN at DesignSafe** Button

        .. figure:: figures/step3_Login.PNG
            :align: center
            :figclass: align-center
            :width: 400

            Login window

     If you don't have the DesignSafe account, sign up at |DesignSafe|.

     Then by clicking **RUN at DesignSafe**, one can specify the options. Please see :ref:`here<lbl-usage>` for more details.


        .. figure:: figures/step3_Run.PNG
            :align: center
            :figclass: align-center
            :width: 1200

            Run at DesignSafe


     By clicking **Submit**, the jobs will be automatically submitted to DeisgnSafe. (See :ref:`here<lblArchitecture>` to learn more about "What happens when **RUN at DesignSafe** button is clicked"). Depending how busy the **Frontera** at TACC is, your job may start within 30 sec or it may take longer. By clicking **GET from DesignSafe**, one can check the status. The major stages are **Queued**, **Running**, and **Finished**. 


        .. figure:: figures/step3_Jobs.PNG
            :align: center
            :figclass: align-center
            :width: 1200

            Run at DesignSafe

     Once the status is changed to **Finished**, select the job name and click **Retrieve Data**. The quoFEM will load the data. The created results files can be found in your **Remote working directory** which can be found in the preference window. Further, by signing in to DesignSafe and navigating to **Workspace - Tools & Applications - Jobs Status** (at the right-hand side edge). click **More info** and **View** button.


        .. figure:: figures/step3_DesignSafe1.svg
            :align: center
            :figclass: align-center
            :width: 1200

            DesignSafe - Job status

        .. figure:: figures/step3_DesignSafe2.svg
            :align: center
            :figclass: align-center
            :width: 400

            DesignSafe - See results files

     It will show the results files and logs created by quoFEM.

.. tabbed:: Moving forward..

  :uqblue:`Things to Consider`

    * **Installing additional Python packages**

        Please read :ref:`here<lblFEM>` about pip-installing python packages / changing the python version.

    * **When your model consists of more than one script**

        Import only one main python file in the FEM tab, and put all (and only) the files required to run the analysis in the same folder. quoFEM will automatically copy all the files/subfolders in the same directory of the main **Input Script** to the working directory.
