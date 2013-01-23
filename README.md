Pyrens
======

Pyrens is an experiment to develop a Lisp runtime for Python. At this time, it is not considered viable for any production use.

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
print eval("_if(_gt(2,_add(9,7)),_add(1,1),700") # prints '700'
```

Ideas
-----
* Support for function definitions and their invocation
* Support for string literals in the reader

Contact
-------
Please contact me at spligak@gmail.com or file an issue with any suggestions you might have!
