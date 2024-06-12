# Configuration file for the Sphinx documentation builder.

# -- Project information

project = 'SZ-plugin-guide'
copyright = '2024, Giacomo Titti'
author = 'Giacomo Titti'

release = '0.1'
version = '0.1.0'

# -- General configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.viewcode',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

# -- Options for HTML output

html_theme = 'sphinx_rtd_theme'

# Customize sidebar templates, if needed
html_sidebars = {
   '**': [
       'globaltoc.html',  # Global table of contents
       'relations.html',  # Next/previous links
       'sourcelink.html',  # View source link
       'searchbox.html',  # Search box
   ]
}

# -- Options for EPUB output
epub_show_urls = 'footnote'
