.. _lbl-jobs:

******
Jobs
******

Overview
========

Application workflows can be executed as **Local Jobs** (on your computer) or as **Remote Jobs** (on a supercomputer via DesignSafe). This page explains how to run, view, share, and clean up both kinds of jobs.

.. contents:: On this page
   :local:
   :backlinks: none

Local Jobs
==========

What are Local Jobs?
--------------------

Local Jobs run **on your computer** using your machine's CPU/GPU and local storage.

.. important::

   Local runs are great for small to moderate studies and quick iteration. Heavy UQ with large ensembles is usually better suited for Remote Jobs.


How to Run (Local)
------------------

- Click ``RUN`` to launch the workflow on your machine.

.. note::

   The UI will switch to the results tab when the run completes. Any errors will be shown in the log pane.


How to View Files (Local)
-------------------------

1) Open ``File`` / ``Preferences`` on the top bar and locate the path under **Local Jobs Directory**.  
2) Navigate to that directory and open the ``tmp.SimCenter`` folder.

.. note::

   You need to have ran a local job workflow for this folder to be populated with files for viewing. We recommend running the first ``Example`` on the top bar.

Typical local job contents:

+------------------+-----------------------------------------------+
| Folder           | Description                                   |
+==================+===============================================+
| ``workdir``      | Per-sample working dirs and raw simulation    |
|                  | artifacts (can be large).                     |
+------------------+-----------------------------------------------+
| ``templatedir``  | Generated workflow and template inputs.       |
+------------------+-----------------------------------------------+
| ``results``      | Aggregated results, statistics, plots.        |
+------------------+-----------------------------------------------+

.. warning::

   The ``workdir`` can grow quickly for CFD/FEM cases. Clean old runs regularly to reclaim disk space.


How to Delete (Local)
---------------------

- Easiest: start a **new** local run; the app will clean the previous job as needed.
- Manual: delete the ``tmp.SimCenter`` folder from your **Local Jobs Directory**.

.. warning::

   Deleting ``tmp.SimCenter`` removes **all** local job artifacts for the current session. Make backups if needed.


Remote Jobs (DesignSafe/TACC)
=============================

What are Remote Jobs?
---------------------

Remote Jobs run **on supercomputers**. While the SimCenter approach is general (could support many providers in theory), the application **currently supports TACC systems via DesignSafe**.

.. note::

   Examples include Stampede3 and Frontera at TACC, launched through the tapis API automatically in SimCenter applications.


How to Run on DesignSafe
------------------------

1) Click ``RUN at DesignSafe``.  
2) Set a unique ``Job Name`` to find it easily later.  
3) Configure reservation parameters:
   - ``Num Node``, ``Num Processors Per Node``, ``Max Run Time``  
   - Consult the **TACC Stampede3 user guide** for limits and best practices.
4) Set a valid ``TACC Allocation``. Common value today: ``DesignSafe-SimCenter``:  
   - This may change; users may need their **own** allocation in the future.
5) Choose an ``Archive System ID`` (DesignSafe project where outputs are saved):
   - Default is ``designsafe.storage.default`` (your personal space).  
   - To use a **project**, click ``Refresh Projects`` and select one you belong to.
6) If you did **not** use the default archive system, set an ``Archive System Dir``:
   - Use a unique, organized path such as (fill in appropriate fields): ``{app_name}/{user_name}/{job_name}``.
   - When filled in for an example user: ``HydroUQ/bonusj/example_job``.
7) Click ``Submit`` to queue the job at TACC.

.. important::

   Use a **generous** ``Max Run Time``. Too small and the scheduler may kill your run before post-processing finishes.


How to Retrieve Files (Remote)
------------------------------

- Click ``GET from DesignSafe``.  
- Right-click your job and select ``Retrieve Data``.

This downloads the **most important** products (e.g., statistics, summaries) to your **Remote Jobs Directory** on your computer. Large per-sample artifacts may be omitted; see “How to View Files” below to access everything through the DesignSafe website.

.. note::

   Retrieval is only possible after the job status is **FINISHED**. See “How to Refresh Jobs” below.


How to View Files (Remote)
--------------------------

There are **two** ways to inspect remote outputs:

1) View **retrieved** files on your computer
   ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

   - Retrieve files as described above in "How to Retrieve Files (Remote)".
   - Open ``File`` / ``Preferences`` and note the **Remote Jobs Directory**.
   - Go to that path and open ``tmp.SimCenter``.

   You will typically see:

   +------------------+-------------------------------------------------------+
   | Folder           | Description                                           |
   +==================+=======================================================+
   | ``results``      | Key results and statistical data from your workflow.  |
   +------------------+-------------------------------------------------------+
   | ``templatedir``  | Workflow and template files used across simulations.  |
   +------------------+-------------------------------------------------------+

   .. note::

      You will **not** see ``workdir`` here. Remote jobs often produce massive per-sample files unsuitable for bulk download. To browse everything (including ``workdir``), use method 2.

2) View **all** files on DesignSafe (web)
   ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

   - Click ``GET from DesignSafe``.  
   - Right-click your job and select ``Open Job Folder``.  
   - Log into DesignSafe to browse and download **any** file or folder.

.. warning::

   Full CFD/MPM outputs can be very large. Prefer selective downloads to avoid long transfers and storage bloat.


How to Refresh Jobs (Remote)
----------------------------

- Click ``GET from DesignSafe``.  
- Right-click your job and select ``Refresh Job``.

The ``STATUS`` column updates (e.g., ``RUNNING``, ``FAILED``, ``FINISHED``). Once **FINISHED**, you can retrieve data.

How to View Metadata (Remote)
-----------------------------

- Click ``GET from DesignSafe``.  
- Right-click your job and select ``View Job Metadata`` to open the DesignSafe page with full `job details <https://www.designsafe-ci.org/workspace/history>`_.

How to Share (Remote)
---------------------

- Click ``GET from DesignSafe``.  
- Right-click your job and select ``Share Job``.  
- Enter one or more DesignSafe usernames (comma-separated).

.. important::

   The job's ``Archive System ID`` must **not** be ``designsafe.storage.default``. Sharing requires that outputs are in a **project** area where the recipients are members. Manage project membership via DesignSafe `My Projects <https://www.designsafe-ci.org/data/browser/projects>`_.

.. note::

   You must be the **Owner** of the job to share it. Check the ``Owner`` column in the jobs table.


How to Delete (Remote)
----------------------

- Click ``GET from DesignSafe``.  
- Right-click your job and select ``Delete Job``.

This **hides** the job from your table but **does not** remove all files on DesignSafe. To fully delete job data, use the DesignSafe `website <https://www.designsafe-ci.org/data/browser/tapis/designsafe.storage.default/>`_ to remove files from the archive project.

.. warning::

   Deletion on the `website <https://www.designsafe-ci.org/data/browser/tapis/designsafe.storage.default/>`_ is permanent. Confirm you have downloaded anything you might need before removing files.
