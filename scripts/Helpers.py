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
SrcDir = os.path.join(BaseDir,'src')
BuildDir = os.path.join(BaseDir,'_build')


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


def execCommand(Cmd,Cwdir):
  Pcs = subprocess.Popen(Cmd,
                         stderr=subprocess.STDOUT,
                         stdout=subprocess.PIPE,
                         cwd=Cwdir)
  for Ln in Pcs.stdout:
    print(Ln,end='')


##############################################################################


def getProcessedWarning(resourcePath, scriptPath):
  txt = f"""<!-- 
CAUTION: this page was generated. 
To change it:
- edit the file {resourcePath} 
- execute the script {scriptPath}
-->"""
  return txt + "\n\n"


##############################################################################


LinkableChars = ''.join(ch for ch in string.printable if ch.isalnum())+"-"

def keepPrintable(S):
  """To slugify a string"""
  # If not enough, install extensive pip library:
  #    https://pypi.org/project/python-slugify/ (slugify function for unicode)
  CleanedS = S.strip().lower().replace(" ", "-")
  CleanedS = "".join(ch for ch in CleanedS if ch in LinkableChars)
  return CleanedS


def generateTableOfContent(RefTxt):
  TableOfContent = "## Table of content\n"

  for l in RefTxt.split("\n"):
    if l.startswith("##"):
      LineTxt = l.strip("#")
      InternalLink = keepPrintable(LineTxt)
      if l.startswith("### "): # Level 3
        TableOfContent += f"    - [{LineTxt}](#{InternalLink})\n"
      else: # Level 2
        TableOfContent += f"- <strong>{LineTxt}</strong>\n"
  return TableOfContent
