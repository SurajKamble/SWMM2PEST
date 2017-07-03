import sys, os
sys.path.append('.')
sys.path.append('..')
path = sys.path
from cx_Freeze import setup, Executable

packages = []

includes = ["Core", "Py_UI_Files", "Images", "numpy.core._methods", "numpy.lib.format", "pyqtgraph.debug", "pyqtgraph.ThreadsafeTimer"]

options = {
    'build_exe': {
        'packages': packages,
        'includes': includes,
        'path': path,
        'include_files': ['epa1.ico'],
    }
}


setup(
    name = "SWMM2PEST",
    version = "1.0",
    description = "SWMMM2PEST",
    options = options,
    executables = [Executable("LoadFirstPage.py", targetName="SWMM2PEST.exe", base = "Win32GUI",
                              icon="epa1.ico")]
)