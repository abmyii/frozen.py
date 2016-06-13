frozen.py
=========
Takes a zip and packs it into an executable so that you can run a whole program with just one file (the executable).

Usage:
frozen.py <executable_name> <zip_name> <runtime_command>

For example:
frozen.py test test.zip "python test.py"

This takes the zip "test.zip" which has a "test.py" in it and at runtime, unpacks the zip and runs that command.

requirements
============
Cython >= 0.20 (tested with 0.23.4)
