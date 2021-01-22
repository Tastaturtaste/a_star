import os
import subprocess
import sys
from setuptools import sandbox

def make_source_dist():
    try:
        subprocess.check_call([sys.executable, '-m','pep517.build','--source','.','--out-dir=./dist/'])
        return True
    except:
        print("No source distribution build! Is pep517 installed?", file=sys.stderr)
        return False
def make_wheel_dist():
    try:
        subprocess.check_call([sys.executable, '-m','pip','wheel','./','--w','./dist', '--no-deps'])
        return True
    except:
        print("No wheel distribution build! Is wheel installed?", file=sys.stderr)
        return False

if __name__ == "__main__":
    #print("Activating virtual environment...")
    #subprocess.run(os.getcwd() + "/venv/Scripts/activate", shell=True)
    make_source_dist()
    make_wheel_dist()