#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# SimCenter - General documentation build configuration file
#

# -- SimCenter App selection -------------------------------------------------

#app_name = 'EE-UQ'
#app_name = 'PBE'
app_name = 'WE-UQ'

print('app_name = ' + app_name)


# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#

import os
import sys
sys.path.append(os.path.abspath('./sphinx_ext/'))
# sys.path.insert(0, os.path.abspath('.'))

# -- Project information -----------------------------------------------------

# shared among all SimCenter docs 

numfig = True
numfig_secnum_depth = 2

rst_prolog = """
.. |EE-UQ short name| replace:: EE-UQ app
.. |EE-UQ app link| replace:: `EE-UQ app`_
.. _EE-UQ app: https://simcenter.designsafe-ci.org/research-tools/ee-uq-application/
.. |user survey link| replace:: `user survey`_
.. _user survey: https://docs.google.com/forms/d/e/1FAIpQLSfh20kBxDmvmHgz9uFwhkospGLCeazZzL770A2GuYZ2KgBZBA/viewform?usp=sf_link
.. |ResearchTools| replace:: `SimCenter Research Tools`_
.. _SimCenter Research Tools: https://simcenter.designsafe-ci.org/research-tools/overview/
.. |OpenSees| replace:: **OpenSees**
.. |userSurveyLink| replace:: `user survey`_
.. |Tcl| replace:: **Tcl**
.. |OpenSeesLink| replace:: `OpenSees`_
.. _OpenSees: https://opensees.berkeley.edu
.. |OpenSeesDownload| replace:: `OpenSees Download`_
.. _OpenSees Download: https://opensees.berkeley.edu/OpenSees/user/download.php
.. |Dakota| replace:: **Dakota**
.. |DakotaLink| replace:: `Dakota`_
.. _Dakota: https://dakota.sandia.gov/
.. |DakotaDownload| replace:: `Dakota Download`_
.. _Dakota Download: https://dakota.sandia.gov/download.html
.. |requirements| replace:: **REQUIREMENTS**
.. |DesignSafe| replace:: `DesignSafe`_
.. _DesignSafe: https://designsafe-ci.org
.. |smelt| replace:: `smelt`_
.. _smelt: https://github.com/NHERI-SimCenter/smelt
"""	

# app-specific settings

if app_name == 'PBE':

	project = 'Performance Based Engineering Application'
	copyright = '2019, The Regents of the University of California'
	author = 'Adam Zsarnóczay'

	tags.add('PBE_app')
	toc_filter_exclude = ['EEUQ','WEUQ']

	rst_prolog += """\
.. |full tool name| replace:: Performance Based Engineering Application
.. |short tool name| replace:: PBE app
.. |short tool id| replace:: PBE
.. |tool github link| replace:: `PBE Github page`_
.. _PBE Github page: https://github.com/NHERI-SimCenter/PBE
.. |app| replace:: PBE app
.. |appName| replace:: PBE app
.. |messageBoard| replace:: `Message Board`_
.. _Message Board: https://simcenter-messageboard.designsafe-ci.org/smf/index.php?board=7.0
.. |githubLink| replace:: `PBE Github page`_
.. |appLink| replace:: `PBE Download`_
.. _PBE Download: https://www.designsafe-ci.org/data/browser/public/designsafe.storage.community/%2FSimCenter%2FSoftware%2FPBE
.. |tool version| replace:: 2.0
.. |figDownload| replace:: :numref:`figDownloadPBE`
.. |figUI| replace:: :numref:`figUI-PBE`
.. |figGenericUI| replace:: :numref:`figGenericUI-PBE`
.. |figMissingCRT| replace:: :numref:`figMissingCRT-PBE`
"""

	html_logo = 'common/SimCenter_PBE_logo.png'

elif app_name == 'EE-UQ':
	project = 'Earthquake Engineering with Uncertainty Quantification'
	copyright = '2019, The Regents of the University of California'
	author = 'Frank McKenna'

	tags.add('EEUQ_app')
	toc_filter_exclude = ['PBE','WEUQ']

	rst_prolog += """
.. |full tool name| replace:: Earthquake Engineering with Uncertainty Quantification Application
.. |short tool name| replace:: EE-UQ app
.. |short tool id| replace:: EE-UQ
.. |tool github link| replace:: `EE-UQ Github page`_
.. _EE-UQ Github page: https://github.com/NHERI-SimCenter/EE-UQ
.. |tool version| replace:: 2.0
.. |app| replace:: EE-UQ app
.. |appName| replace:: EE-UQ app
.. |githubLink| replace:: `EE-UQ Github page`_
.. |appLink| replace:: `EE-UQ Download`_
.. _EE-UQ Download: https://www.designsafe-ci.org/data/browser/public/designsafe.storage.community//SimCenter/Software/EE_UQ
.. |messageBoard| replace:: `Message Board`_
.. _Message Board: https://simcenter-messageboard.designsafe-ci.org/smf/index.php?board=6.0
.. |figUI| replace:: :numref:`figUI-EE`
.. |figDownload| replace:: :numref:`figDownloadEE`
.. |figGenericUI| replace:: :numref:`figGenericUI-EE`
.. |figMissingCRT| replace:: :numref:`figMissingCRT-EE`
"""	

	html_logo = 'common/SimCenter_PBE_logo.png'

elif app_name == 'WE-UQ':
	project = 'Wind Engineering with Uncertainty Quantification'
	copyright = '2019, The Regents of the University of California'
	author = 'Frank McKenna'

	tags.add('WEUQ_app')
	toc_filter_exclude = ['PBE','EEUQ']

	rst_prolog += """
.. |full tool name| replace:: Wind Engineering Application with Uncertainty Quantification
.. |short tool name| replace:: WE-UQ app
.. |short tool id| replace:: WE-UQ
.. |tool github link| replace:: `WE-UQ Github page`_
.. _WE-UQ Github page: https://github.com/NHERI-SimCenter/WE-UQ
.. |tool version| replace:: 2.0
.. |app| replace:: WE-UQ app
.. |appName| replace:: WE-UQ app
.. |githubLink| replace:: `WE-UQ Github page`_
.. |appLink| replace:: `WE-UQ Download`_
.. _WE-UQ Download: https://www.designsafe-ci.org/data/browser/public/designsafe.storage.community//SimCenter/Software/WE_UQ
.. |messageBoard| replace:: `Message Board`_
.. _Message Board: https://simcenter-messageboard.designsafe-ci.org/smf/index.php?board=6.0
.. |figUI| replace:: :numref:`figUI-WE`
.. |figDownload| replace:: :numref:`figDownloadWE`
.. |figGenericUI| replace:: :numref:`figGenericUI-WE`
.. |figMissingCRT| replace:: :numref:`figMissingCRT-WE`
"""	

	html_logo = 'common/SimCenter_PBE_logo.png' #TODO: replace with EE-UQ logo!

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.

extensions = [
	'sphinxcontrib.bibtex',
	'toctree_filter'
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'sphinx_rtd_theme'

html_theme_options = {
	'logo_only': True,
	'prev_next_buttons_location': None,
	'style_nav_header_background': '#F2F2F2' 
}



#
#	'style_nav_header_background': '#F2F2F2' #64B5F6 #607D8B

html_css_files = [
	'css/custom.css'
]

#	'css/custom.css'#

html_secnum_suffix = " "

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# For a full list of configuration options see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html
