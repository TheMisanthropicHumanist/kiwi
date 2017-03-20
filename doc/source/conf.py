#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# kiwi documentation build configuration file, created by
# sphinx-quickstart on Fri Feb  5 11:03:18 2016.
#
import sys
from os.path import abspath, dirname, join, normpath
import shlex
import sphinx_rtd_theme

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
_path = normpath(join(dirname(__file__), "../.."))
sys.path.insert(0, _path)

# autodoc imports all from kiwi, thus we need the global log
from kiwi import logger


# -- General configuration ------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.extlinks',
    'sphinx.ext.todo',
    'sphinx.ext.ifconfig',
    'sphinx.ext.viewcode',
    'sphinxcontrib.spelling',
    'sphinx.ext.autodoc'
]

docopt_ignore = [
    'kiwi.cli',
    'kiwi.tasks.system_build',
    'kiwi.tasks.system_prepare',
    'kiwi.tasks.system_update',
    'kiwi.tasks.system_create',
    'kiwi.tasks.result_list',
    'kiwi.tasks.result_bundle',
    'kiwi.tasks.image_resize',
    'kiwi.tasks.image_info'
]

def remove_module_docstring(app, what, name, obj, options, lines):
    if what == "module" and name in docopt_ignore:
        del lines[:]

def setup(app):
    app.connect("autodoc-process-docstring", remove_module_docstring)

spelling_lang = 'en_US'
spelling_show_suggestions = True
spelling_ignore_acronyms = True
spelling_ignore_importable_modules = True
spelling_ignore_python_builtins = True
spelling_ignore_pypi_package_names = True
spelling_word_list_filename = 'spelling_wordlist.txt'

# Add any paths that contain templates here, relative to this directory.
templates_path = ['.templates']

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
# source_suffix = ['.rst', '.md']
source_suffix = '.rst'

# The encoding of source files.
source_encoding = 'utf-8-sig'

# The master toctree document.
master_doc = 'index'

default_role="py:obj"

# General information about the project.
project = u'kiwi'
copyright = u'2016, Marcus Schäfer'
author = u'Marcus Schäfer'

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
version = u'9.4.1'
# The full version, including alpha/beta/rc tags.
release = version

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = 'en'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
exclude_patterns = []

# If true, '()' will be appended to :func: etc. cross-reference text.
#add_function_parentheses = True

# If true, the current module name will be prepended to all description
# unit titles (such as .. function::).
#add_module_names = True

# If true, sectionauthor and moduleauthor directives will be shown in the
# output. They are ignored by default.
#show_authors = False

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# A list of ignored prefixes for module index sorting.
#modindex_common_prefix = []

# If true, keep warnings as "system message" paragraphs in the built documents.
#keep_warnings = False

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = True

extlinks = {
    'issue': ('https://github.com/SUSE/kiwi/issues/%s', '#'),
    'pr': ('https://github.com/SUSE/kiwi/pull/%s', 'PR #'),
    'ghkiwi': ('https://github.com/SUSE/kiwi/blob/master/%s', '')
}


autosummary_generate = True

# -- Options for HTML output ----------------------------------------------

#html_short_title = '%s-%s' % (project, version)
#html_last_updated_fmt = '%b %d, %Y'
#html_split_index = True
html_logo = 'img/kiwi-logo.png'

html_sidebars = {
   '**': [
          'localtoc.html', 'relations.html',
          'about.html', 'searchbox.html',
         ]
}

html_theme = "sphinx_rtd_theme"

html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]

html_theme_options = {
    'collapse_navigation': False,
    'display_version': False
}

# -- Options for manual page output ---------------------------------------

# The man page toctree documents.
kiwi_doc = 'manual/kiwi'
result_list_doc = 'manual/result_list'
result_bundle_doc = 'manual/result_bundle'
system_prepare_doc = 'manual/system_prepare'
system_update_doc = 'manual/system_update'
system_build_doc = 'manual/system_build'
system_create_doc = 'manual/system_create'
image_resize_doc = 'manual/image_resize'
image_info_doc = 'manual/image_info'

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    (
        kiwi_doc,
        'kiwi', u'Creating Operating System Images',
        [author],
        2
    ),
    (
        result_list_doc,
        'kiwi::result::list',
        u'List build results',
        [author],
        2
    ),
    (
        result_bundle_doc,
        'kiwi::result::bundle',
        u'Bundle build results',
        [author],
        2
    ),
    (
        system_prepare_doc,
        'kiwi::system::prepare',
        u'Prepare image root system',
        [author],
        2
    ),
    (
        system_create_doc,
        'kiwi::system::create',
        u'Create image from prepared root system',
        [author],
        2
    ),
    (
        system_update_doc,
        'kiwi::system::update',
        u'Update/Upgrade image root system',
        [author],
        2
    ),
    (
        system_build_doc,
        'kiwi::system::build',
        u'Build image in combined prepare and create step',
        [author],
        2
    ),
    (
        image_resize_doc,
        'kiwi::image::resize',
        u'Resize disk images to new geometry',
        [author],
        2
    ),
    (
        image_info_doc,
        'kiwi::image::info',
        u'Provide detailed information about an image description',
        [author],
        2
    )
]

# If true, show URL addresses after external links.
#man_show_urls = False
