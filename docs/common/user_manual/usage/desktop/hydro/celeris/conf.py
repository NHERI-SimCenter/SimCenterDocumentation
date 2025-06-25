# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html
import os
import sys
import re
from unittest.mock import MagicMock

sys.path.insert(0, os.path.abspath('../..'))

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'CelerisAi'
copyright = '2025, Lynett Wave Research Group'
author = 'Willington Rentería'
release = '0.0.1'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',    # Supports Google & NumPy docstring syntax
    'sphinx.ext.viewcode',
    'sphinx.ext.imgconverter'
]

templates_path = ['_templates']
exclude_patterns = []

latex_elements = {
    'preamble': r'\DeclareUnicodeCharacter{200B}{}',
}
# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']

napoleon_google_docstring = True
napoleon_numpy_docstring = False

# __________________________________________________
# List any modules required to Sphinx , mock out
MOCK_MODULES = [
    "numpy",
    "matplotlib",
    "matplotlib.pyplot",
    "matplotlib.colors",
    "taichi",
    "taichi.math",
    "imageio",
    "scipy.interpolate",
    "scipy"
]
class Mock(MagicMock):
    @classmethod
    def __getattr__(cls, name):
        # If it's 'f32' or 'f64', return a placeholder that prints nicely
        #if name in ("f32", "f64"):
        #    mock_obj = MagicMock()
        #    mock_obj.__name__ = f"ti.{name}"
        #    return mock_obj
        return MagicMock()

        
def process_signature(app, what, name, obj, options, signature, return_annotation):
    # If signature has MagicMock in it, replace it
    if signature and "MagicMock" in signature:
        signature = re.sub(r"<MagicMock[^>]*>", "ti.f32", signature)

    return (signature, return_annotation)

def setup(app):
    app.connect("autodoc-process-signature", process_signature)
    
for mod_name in MOCK_MODULES:
    sys.modules[mod_name] = Mock()
    
class FakeTaichiMathModule:
    """
    Minimal stand-in for 'taichi.math'.
    """
    # If your code does things like:
    #   from taichi.math import vec2, vec3, ...
    # you'd define stubs here:
    # vec2 = MagicMock()
    # vec3 = MagicMock()
    pass
import math
import types
class DummyTemplate:
    """A dummy type for ti.template."""
    pass

# Create a fake types module with an ndarray stub
class FakeTaichiTypes:
    @staticmethod
    def ndarray(dtype, ndim):
        # Return a simple placeholder or dummy type; it's only used for annotation.
        return f"ndarray(dtype={dtype}, ndim={ndim})"
    
class FakeTaichiModule:
    """
    A partial stand-in for 'taichi' itself.
    """
    @staticmethod
    def data_oriented(cls):
        return cls

    # Define attributes expected by your code
    f16 = MagicMock(name="ti.f16")
    f32 = MagicMock(name="ti.f32")
    f64 = MagicMock(name="ti.f64")
    i32 = MagicMock(name="ti.i32")
    
    # Stub for the 'kernel' decorator
    kernel = staticmethod(lambda fn: fn)
    
    #Stub for the 'template' function
    template = staticmethod(lambda: DummyTemplate)
    
    # Stub for the 'func' decorator
    func = staticmethod(lambda fn: fn)
    
    # a stub for 'pow' using math.pow
    pow = staticmethod(math.pow)
    
    # a stub for 'sqrt' using math.sqrt
    sqrt = staticmethod(math.sqrt)
    
    #a stub for 'tools'** as an empty module:
    tools = types.ModuleType("tools")
    
    # a stub for the 'types' attribute**
    types = FakeTaichiTypes()
    
    # If your code uses ti.math, we provide a 'math' attribute:
    math = FakeTaichiMathModule()

# Then assign both to sys.modules
sys.modules["taichi"] = FakeTaichiModule()
sys.modules["taichi.math"] = FakeTaichiMathModule()
sys.modules["ti"] = sys.modules["taichi"]
