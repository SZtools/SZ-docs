# Configuration file for the Sphinx documentation builder.

import sphinx_rtd_theme

# -- Project information
project = 'SZ plugin guide'
copyright = '2024, Giacomo Titti'
author = 'Giacomo Titti'

release = 'dev'
version = 'dev'

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

# -- Add paths that contain templates here, relative to this directory.
#templates_path = ['_templates']


# -- Options for HTML output
#html_title = 'Susceptibility Zoning plugin Guide'
html_theme = 'sphinx_rtd_theme'

# -- Add any paths that contain custom static files (such as style sheets) here, relative to this directory.
html_static_path = ['_static']

# -- Add custom CSS files
html_css_files = ['custom.css']

# -- Options for the theme.
html_theme_options = {
    'navigation_depth': 3,  # Adjust depth as needed
    'collapse_navigation': True,  # Keep sidebar open by default
    'sticky_navigation': True,  # Make sidebar navigation sticky
}

# html_use_index = True

# -- Options for EPUB output
epub_show_urls = 'footnote'
