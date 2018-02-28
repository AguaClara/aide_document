# AguaClara AIDE Document

This is a tool for combining .yaml data files with Markdown templates via the Jinja2 templating engine to produce complete Markdown/.pdf files.

# Installation Instructions

## Installing `aide_document`

### Via `pip`

1. Ensure that you have `pip` installed by running `pip -V`. `pip` comes with Python 2 >=2.7.9 or Python 3 >=3.4, but if you don't have it, [follow these instructions](https://pip.pypa.io/en/stable/installing/ "Pip Installation Instructions").
2. Run `pip install aide_document --user` anywhere.

### Via `git`

1. Ensure that you have `git` installed by running `git --version`. If you don't have it, [get it here](https://git-scm.com/downloads "Git Installation") and configure it [using these instructions](https://git-scm.com/book/en/v2/Getting-Started-First-Time-Git-Setup "Git Configuration").
2. Run `git clone https://github.com/AguaClara/aide_document.git` in the location of your choice.

If you choose to install via `git`, be sure to put the `aide_document` folder in the same directory as the files that utilize the package.

## Installing a LaTeX Engine

To convert markdown to pdf using pandoc, you must install TeX Live, a LaTeX engine for your operating system. Here are installation files for each OS:
* [Windows](http://mirror.ctan.org/systems/texlive/tlnet/install-tl-windows.exe "Windows TeX Live Installation File")
* [MacOS](http://tug.org/cgi-bin/mactex-download/MacTeX.pkg "MacOS MacTeX Installation File") (Note: this is MacTeX, an optimized variant of TeX Live.)
* [Linux](http://mirror.ctan.org/systems/texlive/tlnet/install-tl-unx.tar.gz "Linux TeX Live Installation File")

# About

## Semester Goals

The AIDE Document sub-team's goals for the Spring 2018 semester are to use Jinja2 to parse YAML input and convert it to Markdown/.pdf files conforming to templates provided by AIDE Design.
## Team

| Name           | Role   | Email             |
|----------------|--------|-------------------|
| Matan Presberg | Lead   | mgp64@cornell.edu |
| Karan Newatia  | Member | kn348@cornell.edu |
| Oliver Leung   | Member | oal22@cornell.edu |
| Yilin Lu       | Member | yl668@cornell.edu |

## Reports and Presentations