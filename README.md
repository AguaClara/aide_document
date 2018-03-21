# AguaClara AIDE Document

This package has the following functionality:
1. Combine `.yaml` data files and `.md` templates to produce readable documentation files
2. Convert documentation files to a variety of filetypes
2. Translate documentation files to different languages

# Installation Instructions

## 1. Install `aide_document`

1. Ensure that you have `pip` installed by running `pip -V` in your terminal/command line. `pip` comes with Python 2 >=2.7.9 or Python 3 >=3.4, but if you don't have it, [follow these instructions](https://pip.pypa.io/en/stable/installing/ "Pip Installation Instructions").
2. Run `pip install aide_document`.

## 2. Install Pandoc

Pandoc is required for converting Markdown files to PDF. More detailed installation instructions can be found [here](https://pandoc.org/installing.html).
* [Windows Installation File](https://github.com/jgm/pandoc/releases/download/2.1.2/pandoc-2.1.2-windows.msi "Windows Pandoc Installation File")
* MacOS: in Terminal, run `brew install pandoc`
* [Linux Installation File](https://github.com/jgm/pandoc/releases/download/2.1.2/pandoc-2.1.2-1-amd64.deb "Linux Pandoc Installation File")

## 3. Install a LaTeX Engine

To convert Markdown to PDF using Pandoc, you must install TeX Live for your operating system. Here are installation files for each OS:
* [Windows](http://mirror.ctan.org/systems/texlive/tlnet/install-tl-windows.exe "Windows TeX Live Installation File")
* [MacOS](http://tug.org/cgi-bin/mactex-download/MacTeX.pkg "MacOS MacTeX Installation File") (Note: this is MacTeX, an optimized variant of TeX Live.)
* [Linux](http://mirror.ctan.org/systems/texlive/tlnet/install-tl-unx.tar.gz "Linux TeX Live Installation File")

# Using the Package

You can make documentation files and convert them between various filetypes:

```python
from aide_document import convert
```

Within `convert`, there are the following self-explanatory functions:
- `yaml_to_md(input_name, output_name, template_name)`
- `md_to_pdf(input_filename, output_filename)`
- `docx_to_md(input_filename, output_filename)`

You can also translate the file on a line by line basis:

```python
from aide_document import translate
```

Within `translate`, there are the following self-explanatory functions:
- `translate(input_name, source_language, target_language, output_name)`