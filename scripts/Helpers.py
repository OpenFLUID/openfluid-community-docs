import errno
import os
import string
import subprocess


##############################################################################


ScriptDir = os.path.dirname(os.path.abspath(__file__))
ScriptLabel = os.path.basename(ScriptDir)
BaseDir = os.path.dirname(ScriptDir)
RessLabel = 'resources'
RessDir = os.path.join(BaseDir, RessLabel)
SrcDir = os.path.join(BaseDir, 'src')
BuildDir = os.path.join(BaseDir, '_build')


##############################################################################


def makedirs(Path):
    try:
        os.makedirs(Path)
    except OSError as E:
        if E.errno == errno.EEXIST and os.path.isdir(Path):
            pass
        else:
            raise


##############################################################################


def execCommand(Cmd, Cwdir):
    Pcs = subprocess.Popen(Cmd,
                           stderr=subprocess.STDOUT,
                           stdout=subprocess.PIPE,
                           cwd=Cwdir)
    for Ln in Pcs.stdout:
        print(Ln, end='')


##############################################################################


def getGeneratedWarning(resourcePath, scriptPath):
    txt = f"""---
message: |-
  WARNING : This page has been automatically generated. Do not edit directly.
  To modify this page:
  * edit the '{resourcePath}' file to update the source data
  * execute the '{scriptPath}' script to generate this file
---"""
    return txt + "\n\n"


##############################################################################


def slugify(S):
    """To slugify a string"""
    # If this function is not adequate, install extensive pip library:
    #    https://pypi.org/project/python-slugify/ (slugify function for unicode)
    LinkableChars = ''.join(ch for ch in string.printable if ch.isalnum())+"-"

    CleanedS = S.strip().lower().replace(" ", "-")
    CleanedS = "".join(ch for ch in CleanedS if ch in LinkableChars)
    return CleanedS


##############################################################################


def generateTableOfContent(RefTxt):
    TableOfContent = "## Table of content\n"

    for line in RefTxt.split("\n"):
        if line.startswith("##"):
            LineTxt = line.strip("#").strip()
            InternalLink = slugify(LineTxt)
            if line.startswith("### "):  # Level 3
                TableOfContent += f"    - [{LineTxt}](#{InternalLink})\n"
            else:  # Level 2
                TableOfContent += f"- <strong>{LineTxt}</strong>\n"
    return TableOfContent
