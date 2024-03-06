from cx_Freeze import setup, Executable
import sys,os
PYTHON_INSTALL_DIR = os.path.dirname(os.path.dirname(os.__file__))
os.environ['TCL_LIBRARY'] = os.path.join(PYTHON_INSTALL_DIR, 'tcl', 'tcl8.6')
os.environ['TK_LIBRARY'] = os.path.join(PYTHON_INSTALL_DIR, 'tcl', 'tk8.6')

base = None

if sys.platform == 'win32':
    base = None


executables = [Executable("MyProject3.py", base=base)]

packages = ["idna","os","sys","cx_Freeze","tkinter","cv2","setup",
            "numpy","PIL","pandas","datetime","time"]
options = {
    'build_exe': {
            
        'packages':packages,
    },

}

setup(
    name = "ComputerVisionBox",
    options = options,
    version = "0.0.1",
    description = 'Computer Vision ToolBox',
    executables = executables
)

#write python setup build