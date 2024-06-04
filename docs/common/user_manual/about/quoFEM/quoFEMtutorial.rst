*************************
Getting Started Tutorial
*************************

Before We Start
----------------
If you have not yet installed quoFEM, please see 

   * :ref:`Install quoFEM<lblInstallation>`
   * :ref:`Run quoFEM without installation<lblquoFEM_DCV>`

.. important::
     If you just downloaded quoFEM, but have previously used the older version of it or other SimCenter tools, it is recommended to reset the cached path values by pressing the ``reset`` button in ``File``-``Preferences``.



.. |Texas Super Computing Center (TACC)| raw:: html

    <a href="https://www.tacc.utexas.edu/" target="_blank">Texas Super Computing Center (TACC)</a>


.. |OpenSeesPy example manual| raw:: html

          <a href="https://openseespydoc.readthedocs.io/en/latest/src/examples.html" target="_blank">OpenSeesPy example manual</a>

.. |Elastic Truss Analysis| raw:: html

          <a href="https://openseespydoc.readthedocs.io/en/latest/src/truss.html" target="_blank">Elastic Truss Analysis</a>


.. role:: uqblue

quoFEM for a Python Model Interface
-------------------------------------------------
This tutorial will show how a **deterministic** model written/interfaced in a Python script can be used for **Uncertainty Quantification** analysis, using an example of global sensitivity analysis. 


    * **Step 0**. Prepare a Python Model
    * **Step 1**. Modify the Model Script to Define Random Variables and Quantities of Interest
    * **Step 2**. Run quoFEM
    * **Step 3**. Run quoFEM at DesignSafe



.. tab-set::

    .. tab-item:: Step 0 

        :uqblue:`Step 0. Prepare a Python Model`

             .. grid:: 1

               .. grid-item-card::

                .. figure:: figures/step0_main.png
                    :align: center
                    :figclass: align-center
                    :width: 1200


            Let us grab **a python script** from |OpenSeesPy example manual| for this tutorial. Please follow the steps:


                1. In |OpenSeesPy example manual|, navigate to **Structural Example - Elastic Truss Analysis**
                2. In the |Elastic Truss Analysis| page, click the download button. Create a **new folder** named ``TrussExample`` and save ``ElasticTruss.py`` in the folder.

                .. figure:: figures/step2_openseesPy.svg
                    :align: center
                    :figclass: align-center
                    :width: 1200

                    Download OpenSeesPy Elastic Truss Analysis

                .. important::

                    It is important to save the model in a **new folder** instead of root, desktop or downloads

                3. :bdg-primary:`Test Your Model` Test if the input script ``ElasticTruss.py`` runs successfully using the command prompt (Windows) or terminal (Mac). To do this, navigate into ``TrussExample`` folder using :code:`cd` command and type the following. 

                 .. code:: console

                    {$PathToPythonExe} ElasticTruss.py

                 where ``{$PathToPythonExe}`` should be replaced with the python path found in the preference window.

                 .. figure:: figures/step1_preference_default.svg
                    :align: center
                    :figclass: align-center
                    :width: 800

                    Find the Python path in ``File``-``Preference`` in the menu bar

                 According to ``ElasticTruss.py``, the analysis should print out "Passed!", meaning the model ran successfully.

                 .. figure:: figures/step0_openseespy_test.svg
                    :align: center
                    :figclass: align-center
                    :width: 1200

                    Testing ``ElasticTruss.py``

                 Now we are ready to run a probabilistic analysis using this model.

                .. note::
                    openseespy, numpy, and matplotlib libraries are readily available in quoFEM because:

                    * Windows 
                            quoFEM is bundled with a Python executable which has those packages pre-installed. See :ref:`here<lblFEM>`.
                    * macOS 
                            In the :ref:`installation steps<lblInstallMac>`, the command ``pip3 install nheri_simcenter --upgrade`` will include those packages

                    It is important to test the model using the "correct" Python executable the quoFEM uses, which is **that shown in the preference**. See :ref:`here<lblFEM>` to read more on Python versions and installing additional packages.
                    

    .. tab-item:: Step 1

        :uqblue:`Step 1. Modify the Model Script to Define Random Variables and Quantities of Interest`

             .. grid:: 1

               .. grid-item-card::

                .. figure:: figures/step1_main.png
                    :align: center
                    :figclass: align-center
                    :width: 1200


            We now need to indicate quoFEM what are the input **random variables (RVs)** and output **Quantities of Interest (QoIs)**. Let us consider the following setup:

            * **Four RVs**: height (:math:`H`), elastic modulus (:math:`E`), horizontal load (:math:`P_x`), vertical load (:math:`P_y`)
            * **Two QoIs**: horizontal and vertical displacements of node 4 (:math:`u_x` and :math:`u_y`)

            To convey this information to quoFEM, the following steps are needed.

            1. Create a parameter file, :download:`params.py <params.py>`, that contains the below four lines, in the folder ``TrussExample``:

             .. literalinclude:: params.py
                :language: py

             This indicates quoFEM the list RVs

             .. note::

                The specified values are not actually used in the quoFEM analysis, because they will be overwritten according to the probability distribution specified in Step 2.

            2. Modify the main script :download:`ElasticTruss.py <ElasticTruss_quo.py>` as follows (the modified parts are highlighted in the code)


                * Import ``params.py`` on top of the main script
                * Replace the hard-coded values of RVs with the variables ``H``, ``E``, ``Px``, and ``Py``
                * Write QoI values (``ux`` and ``uy``) to ``results.out``


             .. tabs::

                    .. tab:: Modified

                        .. literalinclude:: ElasticTruss_quo.py
                            :language: py
                            :emphasize-lines: 5,20,28,42, 76,77     


                    .. tab:: Original

                        .. literalinclude:: ElasticTruss.py
                            :language: py
                            :emphasize-lines: 5,20,28,42, 76,77     

            3. :bdg-primary:`Test Your Model` Test your new Python script using the same command used in Step 0. 

                .. code:: console

                    {$PathToPythonExe} ElasticTruss.py

             This time, ``results.out`` should be created in the folder ``TrussExample``, which contains the following two values.

                .. figure:: figures/step1_results.svg
                    :align: center
                    :figclass: align-center
                    :width: 500

                    Created results.out


             **If the test was successful, remove all the files except** ``ElasticTruss.py`` and ``params.py``. This model can now be readily imported into quoFEM.

             .. important::

                It is important to remove ``results.out`` file after testing.


    .. tab-item:: Step 2

        :uqblue:`Step 2. Run quoFEM`

             .. grid:: 1

              .. grid-item-card::

                .. figure:: figures/step2_main.png
                    :align: center
                    :figclass: align-center
                    :width: 1200


            quoFEM has four input tabs - UQ, FEM, RV, EDP(QoI)- that guide users to provide the required inputs for the UQ analysis


            1. **UQ (Uncertainty Quantification)**

                We will use ``dakota``-``Sensitivity Analysis`` for this example.

                .. figure:: figures/step2_UQ.PNG
                    :align: center
                    :figclass: align-center
                    :width: 1200

                    UQ Panel

                .. Tip::
                    Once the user prepares the input script according to Step 1, they can use it for any :ref:`UQ analysis supported in quoFEM<lblUQ>` without additional modifications.

            2. **FEM (Finite Element Model or any simulation model)**

                Import the two model scripts prepared in Step 1 here.

                .. figure:: figures/step2_FEM.PNG
                    :align: center
                    :figclass: align-center
                    :width: 1200

                    FEM Panel

                The post-processing script is not needed in this example because the ``results.out`` is already printed in the main script. See :ref:`here<lblFEM>` for more about the post-processing script     


            3. **RV (Random Variables)**

                Reading ``params.py``, quoFEM auto-populates the RVs as follows.

                .. figure:: figures/step2_RV.PNG
                    :align: center
                    :figclass: align-center
                    :width: 1200

                    RV Panel

                Then one can modify their distribution types and parameters. Further, if you believe some variables are correlated, use the correlation button to specify the values.


                .. figure:: figures/step2_RV_corr.PNG
                    :align: center
                    :figclass: align-center
                    :width: 300

                    Correlation Window

            4. **EDP (Engineering Demand Parameters) or QoI (Quantities of Interest)**

                Because our Python script will write two values in ``results.out`` file, we will specify two QoI as follows.

                .. figure:: figures/step2_QoI.PNG
                    :align: center
                    :figclass: align-center
                    :width: 1200

                    EDP Panel

                The order should match that written in the ``results.out`` file, and the specified name of QoIs is used only for the display in this example. Please see :ref:`here<lblQUO_QOI>` to learn about vector QoIs that have a length greater than 1 


            When all the fields are filled in, click the **Run** button, and the analysis will be performed. **Do not press the Run button twice** - it will give you an error. You can check the progress status in your **Local Working directory** which can be found in the preference window. The number attached to 'workdir.' indicates the simulation index, and each folder contains the details for each simulation run.

                .. figure:: figures/step2_RES1.PNG
                    :align: center
                    :figclass: align-center
                    :width: 600

                    Working directories


            Once the analysis is done, move on to the RES tab.

            **RES (Results)**

                The results indicate that the horizontal displacement is most affected by the height while vertical displacement is dominated by the elastic modulus and vertical force. 

                .. figure:: figures/step2_RES2.PNG
                    :align: center
                    :figclass: align-center
                    :width: 1200

                    RES - Summary

                And this can be confirmed by the strong/weak trends observed in the scatter plots.

                .. figure:: figures/step2_RES3.PNG
                    :align: center
                    :figclass: align-center
                    :width: 1200

                    RES - Data Values - Scatter plot of ``H`` and ``disp_x`` 

                The **right/left mouse buttons** (fn-clink, option-click, or command-click replaces the left click on Mac) will allow the users to draw various scatter plots, histograms, and cumulative mass plots from the sample points.

                See :ref:`Dakota<lbluqTechnical>` or :ref:`SimCenterUQ<lbluqSimTechnical>` theory manual to learn more about the sensitivity analysis and the difference between main and total indices. 

                .. Tip::
                    The global sensitivity analysis results will be different when probability distribution changes (i.e. when the amount of uncertainty in each input variable changes), and users can test different conditions simply by changing the distributions in the RV tab.

    .. tab-item:: Step 3

        :uqblue:`Step 3. Run quoFEM at DesignSafe`

             .. grid:: 1

              .. grid-item-card::

                .. figure:: figures/step3_main.png
                    :align: center
                    :figclass: align-center
                    :width: 1200


            Users can run the same analysis using the high-performance computer at |DesignSafe| at |Texas Super Computing Center (TACC)|. For this, login to DesignSafe by clicking **Login** on the right upper corner of quoFEM, or by clicking **RUN at DesignSafe** Button

                .. figure:: figures/step3_Login.PNG
                    :align: center
                    :figclass: align-center
                    :width: 400

                    Login window

            If you don't have a DesignSafe account, you can easily sign up at |DesignSafe|.

            Then by clicking **RUN at DesignSafe**, one can specify the job details. Please see :ref:`here<lbl-usage>` for more details on the number of nodes and processors.


                .. figure:: figures/step3_Run.PNG
                    :align: center
                    :figclass: align-center
                    :width: 1200

                    Run at DesignSafe


            If one sets 32 processors, quoFEM will run 32 model evaluations simultaneously in parallel. By clicking **Submit**, the jobs will be automatically submitted to DesignSafe. (See :ref:`here<lblArchitecture>` to learn more about "What happens when **RUN at DesignSafe** button is clicked"). Depending on how busy the **Frontera** at TACC is, your job may start within 30 sec, or it may take longer. By clicking **GET from DesignSafe**, one can check the status. The major stages are **Queued**, **Running**, and **Finished**. 


                .. figure:: figures/step3_Jobs.PNG
                    :align: center
                    :figclass: align-center
                    :width: 1200

                    Run at DesignSafe

            Once the status is changed to **Finished**, select the job name and click **Retrieve Data**. The quoFEM will load the data. The results should be the same as the local analysis results.

                .. figure:: figures/step2_RES2.PNG
                    :align: center
                    :figclass: align-center
                    :width: 1200

                    Sensitivity Analysis Results from DesignSafe


            The created results files can be found in your **Remote working directory** which can be found in the preference window. Furthermore, one can access all the output files and logs created by quoFEM by signing in to |DesignSafe| and navigating in the menu bar to **Workspace - Tools & Applications - Jobs Status** (at the right-hand side edge), and clicking **More info** and **View** button (See below figures).


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


    .. tab-item:: Moving forward..

        :uqblue:`Things to Consider`

            * **Installing additional Python packages**

                On Windows, it is important to install Python packages to the correct Python executable. Please read :ref:`here<lblFEM>` about pip-installing Python packages and changing the Python version.

                .. note::
                    **When running at DesignSafe (e.g. Step 3)**, SimCenter workflow uses its own Python executable installed on the cloud computer. Currently, the only supported Python packages are those installed through the 'nheri_simcenter' package. The available list of packages includes - numpy, scipy, sklearn, pandas, tables, pydoe, gpy, emukit, plotly, matplotlib. If your model uses a package beyond this list, quoFEM analysis will fail.

                    An option to allow user-defined Python packages on DesignSafe is under implementation. Meanwhile, if you need to request to use additional Python packages, please contact us through `user forum <https://simcenter-messageboard.designsafe-ci.org/smf/index.php?board=4.0>`_.


            * **When your model consists of more than one script**

                You can import only one main Python file in the FEM tab and put all (and only) the files required to run the analysis in the same folder. quoFEM will automatically copy all the files/subfolders in the same directory of the **main input script** to the working directory.


            * **Debugging**

                When quoFEM analysis fails and the error message points you to a working directory, often the detailed error messages are written in ``ops.out`` file in the directory. Other ``.log`` and ``.err`` files can have information to help you identify the cause of the failure. Please feel free to ask us through `user forum <https://simcenter-messageboard.designsafe-ci.org/smf/index.php?board=4.0>`_.


            * **When "RUN at DesignSafe" fails**

                When the remote analysis fails while the local analysis is successful, there can be many reasons. Some common cases are Python compatibility issues and missing Python packages, as discussed earlier on this page. Another common cause is related to cross-platform compatibility (Windows/mac versus Linux). This is usually observed in the relative file paths. For example, the below works on Mac and Windows,
                
                .. code-block:: python

                    getDisp=pd.read_csv(r'TestResult\disp.out', delimiter=' ')

                but will throw an error on Linux. Below will also work on Linux.

                .. code-block:: python

                    getDisp=pd.read_csv(os.path.join('TestResult', "disp.out"), delimiter=' ')
                

            * **Questions, bug reports, and feature requests**

                We have an active `user forum <https://simcenter-messageboard.designsafe-ci.org/smf/index.php?board=4.0>`_, for any users who have questions or feature requests. The response is mostly within 24 hours and usually much less.


