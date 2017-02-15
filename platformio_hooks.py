import subprocess
import os.path

#determine git version string
version=subprocess.check_output(["git", "describe"]).rstrip()
version_file="src/Version.ino"

#create headerfile
version_h="""
#undef BUILD_NOTES
#define BUILD_NOTES "{}"
""".format(version)

#only overwrite file if version changed to prevent useless rebuilds
prev_version_h=""
if os.path.isfile(version_file):
    with open(version_file,'r') as fh:
        prev_version_h=fh.read()

if prev_version_h!=version_h:
    with open(version_file,'w') as fh:
        fh.write(version_h)
