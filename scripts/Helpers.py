import os
import errno
import subprocess

###################################################


BaseDir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SrcDir = os.path.join(BaseDir,'src')
BuildDir = os.path.join(BaseDir,'_build')


###################################################


def makedirs(Path):
  try:
    os.makedirs(Path)
  except OSError as E:
    if E.errno == errno.EEXIST and os.path.isdir(Path):
      pass
    else:
      raise


###################################################


def execCommand(Cmd,Cwdir):
  Pcs = subprocess.Popen(Cmd,
                         stderr=subprocess.STDOUT,
                         stdout=subprocess.PIPE,
                         cwd=Cwdir)
  for Ln in Pcs.stdout:
    print Ln,
