import pathlib
import sys
import os

PROJECT_ROOT = pathlib.Path(__file__).resolve().parent.parent
sys.path.append(PROJECT_ROOT)


from config import config


with open(os.path.join(config.PROJECT_ROOT, 'src/VERSION')) as version_file:
    __version__ = version_file.read().strip()
