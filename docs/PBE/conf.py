#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# SimCenter - General documentation build configuration file
#

# -- SimCenter App selection -------------------------------------------------

#app_name = 'EE-UQ'
app_name = 'PBE'

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys
sys.path.insert(0, os.path.abspath('.'))
sys.path.append(os.path.abspath('../'))
sys.path.append(os.path.abspath('../sphinx_ext/'))

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
"""	

# app-specific settings

if app_name == 'PBE':

	project = 'Performance Based Engineering Application'
	copyright = '2019, The Regents of the University of California'
	author = 'Adam Zsarnóczay'

	tags.add('PBE_app')

	rst_prolog += """\
.. |full tool name| replace:: Performance Based Engineering Application
.. |short tool name| replace:: PBE app
.. |short tool id| replace:: PBE
.. |tool github link| replace:: `PBE Github page`_
.. _PBE Github page: https://github.com/NHERI-SimCenter/PBE
.. |tool version| replace:: 2.0
"""

	html_logo = 'SimCenter_PBE_logo.png'

elif app_name == 'EE-UQ':
	project = 'Earthquake Engineering Application with Uncertainty Quantification'
	copyright = '2019, The Regents of the University of California'
	author = 'Frank McKenna'

	tags.add('EE_UQ_app')
	toc_filter_exclude = ['PBE',]

	rst_prolog += """
.. |full tool name| replace:: Earthquake Engineering Application with Uncertainty Quantification
.. |short tool name| replace:: EE-UQ app
.. |short tool id| replace:: EE-UQ
.. |tool github link| replace:: `EE-UQ Github page`_
.. _EE-UQ Github page: https://github.com/NHERI-SimCenter/EE-UQ
.. |tool version| replace:: 2.0
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
	'style_nav_header_background': '#F2F2F2' #64B5F6 #607D8B
}

html_css_files = [
	'css/custom.css'
]

html_secnum_suffix = " "

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['../_static']

# For a full list of configuration options see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html
