import os
from sage.all import load

dir = os.getcwd()
try:
    load(os.path.join(dir, "neuralcode.py"))
    load(os.path.join(dir, "iterative_canonical.spyx"))
    load(os.path.join(dir, "examples.py"))
    load(os.path.join(dir, "InductiveCirclesInclusion.py"))
    print("\nAll files loaded.")
except ValueError:
    print("Files not loaded! Ensure all files are uploaded to the root directory.")
    raise ValueError
