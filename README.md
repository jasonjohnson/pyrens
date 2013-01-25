Pyrens
======

Pyrens is an experimental Lisp runtime for Python. It is not considered production-worthy.


Objectives
----------
* Full file conversion, from .lisp to .py
* Full Python interop
* Support a large subset of Common Lisp language features
* Good Python citizenship. Generated files will practice proper namespacing, documentation and styling
* Identify features more easily abstracted into the Pyrens runtime than implemented in Python directly


Example
-------

Given an s-expression:

```lisp
(if (> 2 (+ 9 7))
    (+ 1 1)
    700)
```

Using the reader, it will be exploded into a Python data structure:

```python
['if', ['>', '2', ['+', '9', '7']], ['+', '1', '1'], '700']
```

Using the code generator, this expression is translated into a series of function calls targeting the runtime:

```python
"_if(_gt(2,_add(9,7)),_add(1,1),700)"
```

This being valid Python, it can be evaluated to its result:

```python
print eval("_if(_gt(2,_add(9,7)),_add(1,1),700)") # prints '700'
```


Functions
---------

In the case of functions, they can be defined with the keyword *defun* and require a name, arguments and a single expression for a body. Given the expression:

```lisp
(defun power (arg1 arg2 arg3)
    (if (> (* arg1 arg2 arg3) 20)
        100
        200))
```

The generated Python code will be:

```python
def power(arg1,arg2,arg3): return _if(_gt(_mul(arg1,arg2,arg3),20),100,200)
```

Functions are currently a top-level special case in the code generation process.


Ideas
-----
* Support for function definitions and their invocation
* Support for string literals in the reader


Contact
-------
Please contact me at spligak@gmail.com or file an issue with any suggestions you might have!
