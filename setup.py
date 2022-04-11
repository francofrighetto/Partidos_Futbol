from cx_Freeze import setup, Executable
import sys 

base = None 
if sys.platform == "win32":
    base = "Win32GUI"
setup (
    name="Partidos",
    version="1.3",
    description ="Partidos",
    executables = [Executable("code.py",base=base, icon="river.ico")]
)
