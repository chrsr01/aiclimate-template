"""Documentation build configuration file."""

import os
import sys

cwd = os.getcwd()
parent = os.path.dirname(cwd)
sys.path.append(parent)

import aiclimate  # noqa: E402

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.doctest',
    'sphinx.ext.intersphinx',
    'sphinx.ext.todo',
    'sphinx.ext.coverage',
    'sphinx.ext.imgmath',
    'sphinx.ext.ifconfig',
    'sphinx.ext.viewcode',
    'sphinx_click.ext',
    'myst_parser',
    'sphinxcontrib.apidoc',
    'sphinx_autodoc_typehints',
]

templates_path = ['_templates']
source_suffix = {'.rst': 'restructuredtext', '.md': 'markdown'}
master_doc = 'index'

project = 'aiclimate'
copyright = '2025, AI for Climate and Environmental Sciences'

version = aiclimate.__version__
release = aiclimate.__version__

exclude_patterns = ['_build']
pygments_style = 'sphinx'
suppress_warnings = ['image.nonlocal_uri']

html_theme = 'sphinx_rtd_theme'
html_static_path = []
htmlhelp_basename = 'aiclimatedoc'

latex_elements = {}
latex_documents = [
    (
        'index',
        'aiclimate.tex',
        'aiclimate Documentation',
        'AI for Climate and Environmental Sciences',
        'manual',
    ),
]

man_pages = [
    (
        'index',
        'aiclimate',
        'aiclimate Documentation',
        ['AI for Climate and Environmental Sciences'],
        1,
    )
]

texinfo_documents = [
    (
        'index',
        'aiclimate',
        'aiclimate Documentation',
        'AI for Climate and Environmental Sciences',
        'aiclimate',
        'Scaffolds Python ML/data science projects for climate research',
        'Miscellaneous',
    ),
]

epub_title = 'aiclimate'
epub_author = 'AI for Climate and Environmental Sciences'
epub_publisher = 'AI for Climate and Environmental Sciences'
epub_copyright = '2025, AI for Climate and Environmental Sciences'

intersphinx_mapping = {
    "python": ("https://docs.python.org/3", None),
    "requests": ("https://requests.readthedocs.io/en/latest/", None),
    "click": ("https://click.palletsprojects.com/en/latest", None),
}
myst_enable_extensions = [
    "tasklist",
    "strikethrough",
    "fieldlist",
]
myst_heading_anchors = 3

apidoc_module_dir = "../aiclimate"
apidoc_output_dir = "."
apidoc_toc_file = False
apidoc_extra_args = ["-t", "_templates"]

autodoc_member_order = "groupwise"
autodoc_typehints = "none"
