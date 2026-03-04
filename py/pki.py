import os
import sys
import shutil

sr = sys.argv[1]
er = sys.argv[2]

def _install():
    shutil.copytree(src=sr, dst=er)

if __name__ == "__main__":
    _install()