import subprocess
import os.path

#determine git version string
version=subprocess.check_output(["git", "describe", "--long", "--dirty=-changed"]).rstrip()

print("ESPeasy git-version: "+version)

version_file="src/Version.h"

#create headerfile
version_h="""
#define BUILD_GIT "{}"
""".format(version)

#only overwrite file if version changed to prevent useless rebuilds
prev_version_h=""
if os.path.isfile(version_file):
    with open(version_file,'r') as fh:
        prev_version_h=fh.read()


if prev_version_h!=version_h:
    with open(version_file,'w') as fh:
        fh.write(version_h)
