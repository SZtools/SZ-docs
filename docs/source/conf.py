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
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
    'sphinx.ext.viewcode',
    'sphinx_rtd_theme',
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

# -- Options for HTML output

html_theme = 'sphinx_rtd_theme'

html_static_path = ['_static']
html_css_files = ['custom.css']

# -- Options for the theme
html_theme_options = {
    'navigation_depth': 3,  # Adjust depth as needed
    'collapse_navigation': False,  # Keep sidebar open by default
    'sticky_navigation': True,  # Make sidebar navigation sticky
}

# -- Customize sidebar templates, if needed
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
