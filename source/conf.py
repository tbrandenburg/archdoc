# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Architecture Documentation'
copyright = '2025, Your Name'
author = 'Your Name'
release = '1.0.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinxcontrib.plantuml',
    'sphinx_rtd_theme',
]

templates_path = ['_templates']
exclude_patterns = []

language = 'en'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']

# -- Options for PlantUML integration ----------------------------------------
import os
plantuml = f'java -jar {os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "plantuml.jar"))}'
plantuml_output_format = 'svg'

# -- Options for LaTeX output ------------------------------------------------
latex_elements = {
    # The paper size ('letterpaper' or 'a4paper')
    'papersize': 'a4paper',
    
    # The font size ('10pt', '11pt' or '12pt')
    'pointsize': '11pt',
    
    # Additional stuff for the LaTeX preamble.
    'preamble': r'''
        \usepackage{xcolor}
        \definecolor{TitleColor}{rgb}{0.126,0.263,0.361}
    ''',
}
