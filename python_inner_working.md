## #Python Inner Working

Python code ---> Byte Code(mostly remain hidden) --> Virtual Machine[Python Virtual Machine]
==> Python code compile to byte code (low level and platform independent).
--> Byte code runs faster.

.pyc --> compiled python (frozen binaries)

**pycache** --> Source change and python Version

eg. hello_chai.cpython-312.pyc

- works only for imported files.
- not for top level files.

## #Python Virtural Machine (PVM)

- code loop to iterate byte code
- Run time engine
- Also known as python interpreter

Byte Code is "not" Machine code.

- python specific interpretation
  - cpython (Standard implementation), jython, IronPython, stakeless, PyPy
