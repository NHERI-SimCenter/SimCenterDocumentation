#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# SimCenter - General documentation build configuration file
#

# -- SimCenter App selection -------------------------------------------------
# Selects which app's documentation to build

import os, sys
from datetime import datetime

app_name = os.path.expandvars("$SIMDOC_APP")
APPS = [
    "R2DTool",
    "PBE",
    "EE-UQ",
    "WE-UQ",
    "HydroUQ",
    "quoFEM",
    "BRAILS",
    "pelicun",
    "requirements"
]
if app_name in APPS:
    # `make` was invoked from root, all env vars should already be defined.
    pass
else:
    pass
    #app_name = 'R2DTool'
    #app_name = 'PBE'
    #app_name = 'EE-UQ'
    app_name = 'WE-UQ'
    app_name = 'HydroUQ'
    #app_name = 'quoFEM'
    #app_name = 'pelicun'

    os.environ["SIMDOC_APP"] = app_name
    os.environ["SIMCENTER_DEV"] = os.path.abspath("../../")


app_abrev = app_name.split("-")[0].replace("Tool", "")
app_abrev2 = (
    app_name.replace("-", "").replace("Tool", "").replace("requirements", "RTM")
)
app_name2 = app_name.replace("Tool", "")
loc_app_dir = os.path.abspath(f"../../{app_name}")

print(f"app_name =  {app_name} ({app_abrev}, {app_abrev2})")

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
sys.path.append(os.path.abspath("./sphinx_ext/"))
sys.path.append(os.path.abspath("./modules/"))
# Add files for the example page template to path
sys.path.append(os.path.abspath("./modules/tmpl_0007/"))

if app_name == "pelicun":
    sys.path.insert(0, os.path.abspath("."))
    sys.path.insert(0, os.path.abspath("../"))
# -----------------------------------------------------------------------------

# Add any Sphinx extension modules 
extensions =  [
    "sphinx_design",
    "sphinx-jsonschema",
    "sphinxcontrib.bibtex",
    "toctree_filter",
    "sphinxcontrib.images",
    "sphinx.ext.extlinks",
    "rendre.sphinx",
    "sphinx.ext.autodoc",
    "crate.sphinx.csv",
#    "sphinx_panels",
#    "sphinxcontrib.spelling",
#    'sphinx_toolbox.collapse',
    'sphinx_tabs.tabs',
]

source_suffix = {
    ".rst": "restructuredtext",
}

numfig = True
numfig_secnum_depth = 4

math_number_all = True
math_eqref_format = "({number})"
math_numfig = True

html_theme_options = {
    "logo_only": True,
    "prev_next_buttons_location": None,
    "style_nav_header_background": "#F2F2F2",
}
html_logo = f"common/figures/{app_name2}-Logo.png"

# Some apps overwrite the copyright to include additional entities
copyright = f"{str(datetime.today().year)}, The Regents of the University of California"

tags.add(f"{app_abrev2}_app")

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.

# TODO: try to consolidate this to have no more than two exclude patterns per app
exclude_patterns = (
    [
        "**/*desktop*",
        "**/*response*",
        "**/*PBE*",
        "**/pbdl-*",
        "**/*pelicun*",
        "**/*WEUQ*",
        "**/*WE[-_]UQ*",
        "**/weuq-*",
        "**/*wind*",
        "**/*EEUQ*",
        "**/*EE[-_]UQ*",
        "**/eeuq-*",
        "**/*earthquake*",
        "**/*TinF*",
        "**/*TInF*",
        "**/*quoFEM*",
        "**/*QUOFEM*",
        "**/qfem*",
        "**/Hydro*",
        "Hydro*",
        "**/hydro/*",
        "**/*hydro*",

        "common/user_manual/examples/desktop/E*",  # R2D examples
        "**/R2D*",
        "reqments.rst",
        "common/reqments/index.rst",
        "common/reqments/testbeds.rst",
        "common/reqments/rWhale.rst",
        "common/reqments/allRequirements.rst",
        "common/reqments/All-Requirements.rst",
        "common/reqments/edRequirements.rst",
        "common/reqments/bigRequirements.rst",
        "common/user_manual/examples/desktop/gallery.rst",
        # Apparently obsolete pages, consider deleting
        "**/*old*",
        "**/_*",  # consider files beginning with underscore as marked for eventual removal
        "**/_downloadApp.rst",
        "**/_testInstall.rst",
        "**/downloadPython.rst",
        "**/install_WindowsOld.rst",
    ]
    + [f"**{app}*" for app in APPS if app != app_name]
    + [f'**{app.replace("-","")}*' for app in APPS if app != app_name]
)

toc_filter_exclusions = [
    "desktop",
    "response",
    "earthquake",
    "wind",
    "hydro",
    "R2D",
    "PBE",
    "quoFEM",
    "Hydro",
    "notQuoFEM",
    "notR2D",
    "WEUQ",
    "EEUQ",
    "TinF",
    "TInF",
    "S3hark",
    "pelicun",
    "docTestbeds",
    "docDLDB"    
]



# -- Project information -----------------------------------------------------

#
# Basic app-specific links and data
#---------------------------------------


rst_prolog = f"""
.. |fmk| replace:: **fmk**
.. |figDownload| replace:: :numref:`figDownload-{app_abrev}`
.. |figDownloadWin| replace:: :numref:`figDownloadWin-{app_abrev}`
.. |figGenericUI| replace:: :numref:`figGenericUI-{app_abrev}`
.. |figUI| replace:: :numref:`figUI-{app_abrev}`
.. |figWinUI| replace:: :numref:`figWinUI-{app_abrev}`

.. |app| replace:: {app_name2} app
.. |appName| replace:: {app_name2} app
.. |short tool id| replace:: {app_name2}
.. |short tool name| replace:: {app_name2} app
.. |appLink| replace:: `{app_name2} Download`_
.. |tool github link| replace:: `{app_name2} Github page`_
.. |githubLink| replace:: `{app_name2} Github page`_
.. |messageBoard| replace:: `Message Board`_
.. |app requirements| replace:: :ref:`lblRequirements`

.. _{app_name2} Github page: https://github.com/NHERI-SimCenter/{app_name}

.. |EE-UQ short name| replace:: EE-UQ app
.. |EE-UQ app link| replace:: `EE-UQ app`_
.. _EE-UQ app: https://simcenter.designsafe-ci.org/research-tools/ee-uq-application/
.. |user survey link| replace:: `user survey`_
.. _user survey: https://docs.google.com/forms/d/e/1FAIpQLSfh20kBxDmvmHgz9uFwhkospGLCeazZzL770A2GuYZ2KgBZBA/viewform?usp=sf_link
.. |ResearchTools| replace:: `SimCenter Research Tools`_
.. _SimCenter Research Tools: https://simcenter.designsafe-ci.org/research-tools/overview/
.. |userSurveyLink| replace:: `user survey`_

.. |PelicunDocs| replace:: `Pelicun Documentation`_
.. _Pelicun Documentation: https://nheri-simcenter.github.io/pelicun/

.. |OpenSees| replace:: **OpenSees**
.. |OpenSeesLink| replace:: `OpenSees`_
.. _OpenSees: https://opensees.berkeley.edu
.. |OpenSeesDownload| replace:: `OpenSees Download`_
.. _OpenSees Download: https://opensees.berkeley.edu/OpenSees/user/download.php
.. |OpenSeesPy| replace:: **OpenSeesPy**

.. |Tcl| replace:: **Tcl**

.. |PythonDownload| replace:: `Python.org`_
.. _Python.org: https://www.python.org/downloads/release/python-386/

.. |Dakota| replace:: **Dakota**
.. |DakotaLink| replace:: `Dakota`_
.. _Dakota: https://dakota.sandia.gov/
.. |DakotaDownload| replace:: `Dakota Download`_
.. _Dakota Download: https://dakota.sandia.gov/download.html
.. |Dakota Theory Manual| replace:: `Dakota Theory Manual`_
.. _Dakota Theory Manual: https://dakota.sandia.gov/sites/default/files/docs/6.11/Theory-6.11.0.pdf

.. |FEAPpv| replace:: **FEAPpv**
.. |FeapLink| replace:: `FEAPpv`_
.. _FEAPpv: http://projects.ce.berkeley.edu/feap/feappv/
.. |FEAPpvDownload| replace:: `FEAPpv`_
.. |FEAPpv Theory Manual| replace:: `FEAPpv Manual`_
.. _FEAPpv Manual: http://projects.ce.berkeley.edu/feap/feappv/manual_51.pdf

.. |requirements| replace:: **REQUIREMENTS**
.. |DesignSafe| replace:: `DesignSafe`_
.. _DesignSafe: https://designsafe-ci.org
.. |smelt| replace:: `smelt`_
.. _smelt: https://github.com/NHERI-SimCenter/smelt
.. |s3harkName| replace:: *s*\ :sup:`3`\ *hark*
.. |br| raw:: html

    <br>

"""

external_links = {
    "github": f"https://github.com/NHERI-SimCenter/{app_name}",
}
# Create inline :github: directive for convenient linking to files on github
extlinks = {
    "github": (f'{external_links["github"]}/tree/master/%s', f"Github"),
}


if app_name == "R2DTool":
    external_links["examplesgithub"] = f"https://github.com/NHERI-SimCenter/R2DExamples"
    extlinks["examplesgithub"] = f'{external_links["examplesgithub"]}/tree/master/%s', f"examplesgithub"


examples_url = f"https://github.com/NHERI-SimCenter/{app_name}/tree/master/Examples/"

#
# Examples
#---------------------------------------------------

# gallery data sources
rendre_config = {
    "targets": {
        "examples": {
            #"data-file": [os.path.normpath(f"{loc_app_dir}/Examples/index.json")],
            "data-file": [os.path.normpath(f"../build/{app_name}_Examples.json")],
            "defaults": {"link": "./%%:base/README"},
        },
        "backend": {
            # "data-file": os.path.normpath(f'../../{app_name}/Examples/index.json')
        },
    }
}
example_config = rendre_config["targets"]["examples"]
sync_examples = False

#- Example links ----------------
import yaml
with open("../examples.yaml","r") as f:
    example_yaml = yaml.load(f,Loader=yaml.Loader)
example_config.update(example_yaml[app_name])

examples_url = f"https://github.com/NHERI-SimCenter/quoFEM/tree/master/Examples/"
extlinks.update(
    {
        f"qfem-{i:04}": (f"{examples_url}/qfem-{i:04}/%s", f"qfem-{i:04}")
        for i in range(1, 99)
    }
)

examples_url = f"https://github.com/NHERI-SimCenter/WE-UQ/tree/master/Examples/"
extlinks.update(
    {
        f"weuq-{i:04}": (f"{examples_url}/weuq-{i:04}/%s", f"weuq-{i:04}")
        for i in range(1, 99)
    }
)

examples_url = f"https://github.com/NHERI-SimCenter/EE-UQ/tree/master/Examples/"
extlinks.update(
    {
        f"eeuq-{i:04}": (f"{examples_url}/eeuq-{i:04}/%s", f"eeuq-{i:04}")
        for i in range(1, 99)
    }
)

examples_url = f"https://github.com/NHERI-SimCenter/PBE/tree/master/Examples/"
extlinks.update(
    {
        f"pbdl-{i:04}": (f"{examples_url}/pbdl-{i:04}/%s", f"pbdl-{i:04}")
        for i in range(1, 99)
    }
)

examples_url = f"https://github.com/NHERI-SimCenter/R2DExamples/tree/master/"
extlinks.update(
    {
        f"r2dt-{i:04}": (f"{examples_url}/r2dt-{i:04}/%s", f"r2dt-{i:04}")
        for i in range(1, 20)
    }
)

examples_url = f"https://github.com/NHERI-SimCenter/HydroUQ/tree/master/Examples/"
extlinks.update(
    {
        f"hdro-{i:04}": (f"{examples_url}/hdro-{i:04}/%s", f"hdro-{i:04}") 
        for i in range(1, 20)
    }
)

#
# App-specific settings
#------------------------------------------------------
docTestbeds = "True"


if app_name == "HydroUQ" or app_name == "Hydro":

    project = "Hydro-UQ"
    copyright = f"2018-{str(datetime.today().year)}, The Regents of the University of California"
    author = "Justin Bonus, Ajay B Harish, Frank McKenna"

    tags.add("tsunami")
    tags.add("stormsurge")
    tags.add("response")
    tags.add("notQuoFEM")
    tags.add("notR2D")
    tags.add("Hydro")
    tags.add("desktop_app") # JB - Added this, but it may not be necessary

    toc_filter_exclusions.remove("Hydro")
    toc_filter_exclusions.remove("desktop")
    toc_filter_exclusions.remove("response")
    toc_filter_exclude = toc_filter_exclusions

    exclude_patterns.remove("**/*desktop*")
    exclude_patterns.remove("**/*earthquake*")
    exclude_patterns.remove("**/*hydro*")
    exclude_patterns.remove("**/*response*")
    exclude_patterns.remove("**/Hydro*")
    exclude_patterns.remove("Hydro*")
    exclude_patterns.remove("**/hydro/*")

    # TODO: fix these temporary changes
    exclude_patterns.append("**/user_manual/usage/desktop/earthquake/*")
    exclude_patterns.append("**/*architectureLevel4.rst*")
    exclude_patterns.append("**/reqments/index.rst")
    exclude_patterns.append("**/requirements/bigRequirements.rst")
    #exclude_patterns.append("**/DakotaSensitivity.rst")
    #exclude_patterns.append("**/DakotaReliability.rst")
    exclude_patterns.append("**/DakotaParameterEstimation.rst")
    exclude_patterns.append("**/DakotaInverseProblems.rst")
    exclude_patterns.append("**/damping.rst") # Added below to be more consistent with quofem - JB
    exclude_patterns.append("**/desktop/hydro-*")
    exclude_patterns.append("**/testbeds/*")
    # END TODO
    # exclude_patterns.append("**/desktop/FEM.rst")
    # exclude_patterns.append("**/desktop/GI.rst")
    # exclude_patterns.append("**/desktop/SIM.rst")

    html_theme_options.update(
        {
            "analytics_id": "...",  # TODO: add analytics ID
        }
    )
    #master_doc = "Hydro"
    master_doc = "index"
    sync_examples = True

    rst_prolog += f"""
.. |full tool name| replace:: Water-borne Hazards Engineering with Uncertainty Quantification
.. |test example| replace:: :ref:`hdro-0001`
.. |tool version| replace:: 3.0
.. _Message Board: https://simcenter-messageboard.designsafe-ci.org/smf/index.php?board=17.0
.. _Hydro Download: https://www.designsafe-ci.org/data/browser/public/designsafe.storage.community/SimCenter/Software/HydroUQ
.. _HydroUQ Download: https://www.designsafe-ci.org/data/browser/public/designsafe.storage.community/SimCenter/Software/HydroUQ
.. |figMissingCRT| replace:: :numref:`figMissingCRT-HydroUQ`
.. |contact person| replace:: Justin Bonus (bonus@berkeley.edu), Ajay B Harish (ajaybh@berkeley.edu), Frank Mckenna (fmk@berkeley.edu), NHERI SimCenter, University of California Berkeley

"""

elif app_name == "R2DTool":

    project = "Regional Resilience Determination Tool"

    author = "Frank McKenna, Stevan Gavrilovic, Jinyan Zhao, Kuanshi Zhong, Adam Zsarnoczay, Barbaros Cetiner, Sang-ri Yi, Pedro Arduino, Wael Elhaddad"
    sync_examples = True

    tags.add("desktop_app")
    tags.add("earthquake")
    tags.add("response")
    tags.add("notQuoFEM")
    tags.add("docTestbeds")

    toc_filter_exclusions.remove("R2D")
    toc_filter_exclusions.remove("desktop")
    toc_filter_exclusions.remove("earthquake")
    toc_filter_exclusions.remove("response")
    toc_filter_exclusions.remove("notQuoFEM")
    toc_filter_exclusions.remove("docTestbeds")
    toc_filter_exclude = toc_filter_exclusions

    exclude_patterns.remove("**/*desktop*")
    exclude_patterns.remove("**/*earthquake*")
    exclude_patterns.remove("**/*response*")
    exclude_patterns.remove("**/R2D*")
    exclude_patterns.remove("common/user_manual/examples/desktop/E*")

    # TODO: fix these temporary changes
    exclude_patterns.append("**/user_manual/usage/desktop/FEM.rst")
    exclude_patterns.append("**/user_manual/usage/desktop/SIM.rst")
    exclude_patterns.append("**/user_manual/usage/desktop/GI.rst")
    exclude_patterns.append("**/user_manual/usage/desktop/response/*")
    exclude_patterns.append("**/user_manual/usage/desktop/earthquake/*")
    exclude_patterns.append("**/*architectureLevel4.rst*")
    exclude_patterns.append("**/requirements/bigRequirements.rst")
    exclude_patterns.append("**/DakotaSensitivity.rst")
    exclude_patterns.append("**/DakotaReliability.rst")
    exclude_patterns.append("**/DakotaParameterEstimation.rst")
    exclude_patterns.append("**/DakotaInverseProblems.rst")
    # END TODO

    rst_prolog += f"""\
.. |full tool name| replace:: Regional Resilience Determination Tool
.. |test example| replace:: :ref:`r2dt-0006`
.. _Message Board: https://simcenter-messageboard.designsafe-ci.org/smf/index.php?board=8.0
.. _R2D Download: https://www.designsafe-ci.org/data/browser/public/designsafe.storage.community/SimCenter/Software/R2Dt
.. |tool version| replace:: 4.1
.. |figMissingCRT| replace:: :numref:`figMissingCRT`
.. |contact person| replace:: Frank McKenna, NHERI SimCenter, UC Berkeley, fmckenna@berkeley.edu

"""
    html_theme_options.update(
        {
            "analytics_id": "...",  # TODO: add analytics ID
        }
    )

elif app_name == "PBE":

    project = "Performance Based Engineering Application"

    author = (
        "Adam Zsarnóczay, Frank McKenna, Stevan Gavrilovic, Kuanshi Zhong, Chaofeng Wang, Michael Gardner, Wael Elhaddad"
    )
    sync_examples = True

    tags.add("PBE_app")
    tags.add("desktop_app")
    tags.add("earthquake")
    tags.add("notQuoFEM")
    tags.add("notR2D")

    toc_filter_exclusions.remove("PBE")
    toc_filter_exclusions.remove("desktop")
    toc_filter_exclusions.remove("earthquake")
    toc_filter_exclusions.remove("notQuoFEM")
    toc_filter_exclusions.remove("notR2D")
    toc_filter_exclusions.remove("docDLDB")    
    toc_filter_exclude = toc_filter_exclusions

    exclude_patterns.remove("**/*desktop*")
    exclude_patterns.remove("**/pbdl-*")
    exclude_patterns.remove("**/*earthquake*")
    exclude_patterns.remove("**/*PBE*")

    # TODO: fix these temporary changes
    exclude_patterns.append("**/*architectureLevel4.rst*")
    exclude_patterns.append("**/DakotaSensitivity.rst")
    exclude_patterns.append("**/DakotaReliability.rst")
    exclude_patterns.append("**/DakotaParameterEstimation.rst")
    exclude_patterns.append("**/DakotaInverseProblems.rst")
    exclude_patterns.append("**/resEE.rst")
    # END TODO


    rst_prolog += """\
.. |full tool name| replace:: Performance Based Engineering Application
.. _Message Board: https://simcenter-messageboard.designsafe-ci.org/smf/index.php?board=7.0
.. _PBE Download: https://www.designsafe-ci.org/data/browser/public/designsafe.storage.community/%2FSimCenter%2FSoftware%2FPBE
.. |tool version| replace:: 3.3
.. |test example| replace:: :ref:`pbdl-0001`
.. |figMissingCRT| replace:: :numref:`figMissingCRT-PBE`
.. |contact person| replace:: Adam Zsarnóczay, NHERI SimCenter, Stanford University, adamzs@stanford.edu

"""

    html_theme_options.update({
        "analytics_id": "UA-158130480-3",
        "navigation_depth": -1,
        })

elif app_name == "EE-UQ":
    project = "Earthquake Engineering with Uncertainty Quantification"
    author = (
        "Frank McKenna, Kuanshi Zhong, Michael Gardner, Adam Zsarnoczay, Sang-ri Yi, Aakash Bangalore Satish, Charles Wang, Wael Elhaddad"
    )

    tags.add("desktop_app")
    tags.add("response")
    tags.add("earthquake")
    tags.add("notQuoFEM")
    tags.add("notR2D")

    toc_filter_exclusions.remove("EEUQ")
    toc_filter_exclusions.remove("desktop")
    toc_filter_exclusions.remove("earthquake")
    toc_filter_exclusions.remove("response")
    toc_filter_exclusions.remove("notQuoFEM")
    toc_filter_exclusions.remove("notR2D")
    toc_filter_exclude = toc_filter_exclusions

    exclude_patterns.remove("**/*EEUQ*")
    exclude_patterns.remove("**/eeuq-*")
    exclude_patterns.remove("**/*desktop*")
    exclude_patterns.remove("**/*earthquake*")
    exclude_patterns.remove("**/*response*")
    exclude_patterns.remove("**/*EE[-_]UQ*")

    sync_examples = True


    rst_prolog += """
.. |full tool name| replace:: Earthquake Engineering with Uncertainty Quantification Application (EE-UQ)
.. |tool version| replace:: 3.5
.. |test example| replace:: :ref:`eeuq-0001`
.. _EE-UQ Download: https://www.designsafe-ci.org/data/browser/public/designsafe.storage.community//SimCenter/Software/EE_UQ
.. _Message Board: https://simcenter-messageboard.designsafe-ci.org/smf/index.php?board=6.0
.. |figMissingCRT| replace:: :numref:`figMissingCRT-EE`
.. |contact person| replace:: Frank McKenna, NHERI SimCenter, UC Berkeley, fmckenna@berkeley.edu

"""

    html_theme_options.update({"analytics_id": "UA-158130480-1"})

elif app_name == "quoFEM":
    project = "Quantified Uncertainty with Optimization for the FEM"
    copyright = f"2018-{str(datetime.today().year)}, The Regents of the University of California"
    author = "Frank McKenna, Adam Zsarnóczay, Sang-ri Yi, Aakash Bangalore Satish, Nikhil Padhye"

    tags.add("desktop_app")
    tags.add("notR2D")
    tags.add("quoFEM_app")

    toc_filter_exclusions.remove("desktop")
    toc_filter_exclusions.remove("quoFEM")
    toc_filter_exclusions.remove("notR2D")
    toc_filter_exclude = toc_filter_exclusions

    exclude_patterns.remove("**/*desktop*")
    exclude_patterns.remove("**/*quoFEM*")
    exclude_patterns.remove("**/qfem*")

    # TODO: fix these temporary changes
    exclude_patterns.append("**/*architectureLevel4.rst*")
    exclude_patterns.append("**/resEE.rst")
    exclude_patterns.append("**/damping.rst")
    exclude_patterns.append("**/desktop/FEM.rst")
    exclude_patterns.append("**/desktop/GI.rst")
    exclude_patterns.append("**/desktop/SIM.rst")
    exclude_patterns.append("**/desktop/quo-*")
    exclude_patterns.append("**/testbeds/*")
    # END TODO

    sync_examples = True

    rst_prolog += f"""
.. |full tool name| replace:: Quantified Uncertainty with Optimization for the Finite Element Method (quoFEM)
.. |test example| replace:: :ref:`qfem-0001`
.. |tool version| replace:: 3.5
.. _quoFEM Download: https://www.designsafe-ci.org/data/browser/public/designsafe.storage.community//SimCenter/Software/quoFEM
.. _Message Board: https://simcenter-messageboard.designsafe-ci.org/smf/index.php?board=4.0
.. |figMissingCRT| replace:: :numref:`figMissingCRT`
.. |contact person| replace:: Frank McKenna, NHERI SimCenter, UC Berkeley, fmckenna@berkeley.edu

"""
    html_theme_options.update({"analytics_id": "UA-158130480-4"})

elif app_name == "WE-UQ":
    project = "Wind Engineering with Uncertainty Quantification"
    # author = 'Frank McKenna'
    author = "Frank McKenna, Abiy F. Melaku, Fei Ding, Jiawei Wan, Peter Mackenzie-Helnwein, Wael Elhaddad, Michael Gardner, Dae Kun Kwon"

    tags.add("desktop_app")
    tags.add("response")
    tags.add("wind")
    tags.add("notQuoFEM")
    tags.add("notR2D")

    toc_filter_exclusions.remove("WEUQ")
    toc_filter_exclusions.remove("desktop")
    toc_filter_exclusions.remove("wind")
    toc_filter_exclusions.remove("response")
    toc_filter_exclusions.remove("notQuoFEM")
    toc_filter_exclusions.remove("notR2D")
    toc_filter_exclude = toc_filter_exclusions

    exclude_patterns.remove("**/*WEUQ*")
    exclude_patterns.remove("**/*desktop*")
    exclude_patterns.remove("**/*wind*")
    exclude_patterns.remove("**/*response*")
    exclude_patterns.remove("**/*TinF*")
    exclude_patterns.remove("**/*WE[-_]UQ*")
    exclude_patterns.remove("**/weuq-*")

    exclude_patterns.append("**/testbeds/*")
    #exclude_patterns.append("**/DakotaSensitivity.rst")
    #exclude_patterns.append("**/DakotaReliability.rst")
    exclude_patterns.append("**/DakotaParameterEstimation.rst")
    exclude_patterns.append("**/DakotaInverseProblems.rst")

    sync_examples = True

    html_theme_options.update({"analytics_id": "UA-158130480-2"})

    rst_prolog += f"""
.. |full tool name| replace:: Wind Engineering with Uncertainty Quantification Application
.. |test example| replace:: :ref:`weuq-0001`
.. |tool version| replace:: 3.2
.. _WE-UQ Download: https://www.designsafe-ci.org/data/browser/public/designsafe.storage.community//SimCenter/Software/WE_UQ
.. _Message Board: https://simcenter-messageboard.designsafe-ci.org/smf/index.php?board=5.0
.. |figMissingCRT| replace:: :numref:`figMissingCRT-WE`
.. |contact person| replace:: Frank McKenna, NHERI SimCenter, UC Berkeley, fmckenna@berkeley.edu

"""



elif app_name == 'pelicun':

    project = 'pelicun'
    copyright = f'(c) 2018-{str(datetime.today().year)}, Leland Stanford Junior University and The Regents of the University of California'
    author = 'Adam Zsarnóczay, Kuanshi Zhong'

    tags.add("pelicun")

    toc_filter_exclusions.remove("pelicun")
    toc_filter_exclude = toc_filter_exclusions

    exclude_patterns.remove("**/*pelicun*")

    # Note that we redefines rst_prolog here for pelicun because it is so different from other apps that there is not much to keep from above
    rst_prolog = f"""
.. |fmk| replace:: **fmk**

.. |pelicun expanded| replace:: Probabilistic Estimation of Losses, Injuries, and Community resilience Under Natural hazard events
.. |full tool name| replace:: pelicun library
.. |tool version| replace:: 3.0.0

.. |app| replace:: pelicun library
.. |appName| replace:: pelicun library
.. |short tool id| replace:: pelicun
.. |short tool name| replace:: pelicun

.. |contact person| replace:: Adam Zsarnóczay, NHERI SimCenter, Stanford University, adamzs@stanford.edu

.. |appLink| replace:: `pelicun Download`_
.. _pelicun Download: https://github.com/NHERI-SimCenter/pelicun

.. |tool github link| replace:: `pelicun Github page`_
.. |githubLink| replace:: `pelicun Github page`_
.. _pelicun Github page: https://github.com/NHERI-SimCenter/pelicun

.. |messageBoard| replace:: `Message Board`_
.. _Message Board: https://simcenter-messageboard.designsafe-ci.org/smf/index.php?board=7.0

.. |app requirements| replace:: :ref:`lblRequirements`

.. |userSurveyLink| replace:: `user survey`_
.. |user survey link| replace:: `user survey`_
.. _user survey: https://docs.google.com/forms/d/e/1FAIpQLSfh20kBxDmvmHgz9uFwhkospGLCeazZzL770A2GuYZ2KgBZBA/viewform?usp=sf_link

.. |ResearchTools| replace:: `SimCenter Research Tools`_
.. _SimCenter Research Tools: https://simcenter.designsafe-ci.org/research-tools/overview/

.. |PythonDownload| replace:: `Python.org`_
.. _Python.org: https://www.python.org/downloads/release/python-386/

.. |requirements| replace:: **REQUIREMENTS**
.. |DesignSafe| replace:: `DesignSafe`_
.. _DesignSafe: https://designsafe-ci.org

.. |br| raw:: html

    <br>

"""

    extensions = extensions + [
        "sphinx.ext.autodoc",
        "sphinx.ext.todo",
        "sphinx.ext.mathjax",
        "sphinx.ext.viewcode",
        "sphinx.ext.githubpages",
        "numpydoc",
        "sphinx.ext.autosummary",
        "sphinx.ext.intersphinx",
        "sphinx.ext.coverage",
        "sphinx.ext.doctest",
    ]

    numpydoc_show_class_members = True
    numpydoc_class_members_toctree = False
    autodoc_member_order = "bysource"
    autoclass_content = "both"

    import glob

    autosummary_generate = glob.glob("source/*.rst")

    master_doc = "index"

    language = None

    pygments_style = "sphinx"

    html_theme_options.update({"analytics_id": "UA-158130480-7"})

    htmlhelp_basename = "pelicundoc"


elif app_name == "requirements":
    # master_doc = 'common/reqments/index'
    master_doc = "reqments"
    project = "SimCenter Requirements Traceability Matrix"
    exclude_patterns = [
        "common/user_manual/*",
        "common/front-matter/*",
        "common/developer_manual/*",
        "common/testbeds/*",
        "common/reqments/reqQUOFEM.rst",
        "common/reqments/Common.rst",
        "common/reqments/EEUQ.rst",
        "common/reqments/PBE.rst",
        #"common/reqments/WEUQ.rst",
        "common/reqments/WE-UQ-Requirements.rst",
        "common/reqments/allRequirements.rst",
        "common/reqments/bigRequirements.rst",
        "common/reqments/edRequirements.rst",
        "common/reqments/reqPelicun.rst",
        "common/reqments/reqQUOFEM.rst",
        "common/Hydro/*",
        "common/technical_manual/*",
        ".DS_Store",
        "common/reqments/index.rst",
        "index.rst",
        "Hydro.rst",
        "Hydro/*",
    ]  # + [f'**/{app}*' for app in APPS if app != 'requirements']
    author = "NHERI SimCenter"
    tags.add("requirements")
    pdf_break_level = 2
    latex_elements = {"extraclassoptions": "openany,oneside"}

    rst_prolog = f"""
.. |floatList| replace:: *list float*
.. |integerList| replace:: *list integer*
.. |intList| replace:: *list integer*
.. |listFloat| replace:: *list float*
.. |listInteger| replace:: *list integer*
.. |listInt| replace:: *list integer*
.. |list| replace:: *list*
.. |string| replace:: *string*
.. |float| replace:: *float*
.. |integer| replace:: *integer*

"""

elif app_name == 'Bootcamp':
    project = 'SimCenter Programming Bootcamp'
    copyright = '2020'
    author = 'Peter Mackenzie-Helnwein, Frank McKenna'

# -- General configuration ----------------------------------------------

rst_prolog += f"""
.. |developers| replace:: {", ".join(f"**{auth}** " for auth in author.split(", "))}
"""


bibtex_bibfiles = ["common/references.bib"]

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

exclude_patterns += ["_build/*", "Thumbs.db", ".DS_Store", "**/_archive/*"]

# -- Options for HTML output ---------------------------------------------

html_theme = "sphinx_rtd_theme"

html_css_files = ["css/custom.css"]

html_secnum_suffix = " "

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ["_static", "_static/css/"]

# -- Options for LATEX output -------------------------------------------

# latex_docclass = {
#    r'manual': 'simcenterdocumentation',
#    r'howto': 'simcenterdocumentation'
# }
latex_elements = {"extraclassoptions": "openany,oneside"}
latex_documents = [
    (
        "index",
        app_name + ".tex",                # tex output file
        project,                          # Document title
        author.replace(", ", " \\and "),  # authors
        "manual",                         # latex theme
    )
]
latex_logo = "common/figures/NSF_SimCenter_NO TEXT_SimCenter.png"


spelling_lang='en_US'
tokenizer_lang='en_US'
spelling_show_suggestions=True
spelling_word_list_filename = ["spelling.txt"]
spelling_exclude_patterns=['ignored_*']


# sync files for examples
if sync_examples:
    # TODO: Temporary fix
    if not example_config:
        import yaml
        with open("../examples.yaml","r") as f:
            example_config = yaml.load(f,Loader=yaml.Loader)["HydroUQ"]
    # Load the `sync_files` routine from ./modules/sync_files.py
    from sync_files import sync_files
    if app_name == "R2DTool":
        sync_files(
        src_dir=os.path.abspath(f"../../R2DExamples"),
        dst_dir="common/user_manual/examples/desktop",
        config=example_config,)
    else:    
        sync_files(
            src_dir=os.path.abspath(f"../../{app_name}/Examples"),
            dst_dir="common/user_manual/examples/desktop",
            config=example_config,
        )

