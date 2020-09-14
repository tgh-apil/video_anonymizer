from cx_Freeze import setup, Executable

base = None    

executables = [Executable("video_anon.py", base=base)]

packages = ["idna", "cv2"]
options = {
    'build_exe': {    
        'packages':packages,
    },    
}

setup(
    name = "APIL Echo Anonymizer",
    options = options,
    version = "1.0",
    description = 'removes header and footer from echo clips',
    executables = executables
)
