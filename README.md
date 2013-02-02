Pyrens
======

Pyrens is an experimental Lisp runtime for Python. A basic Lisp syntax and Python interoperability are currently supported, as documented below. Please see the *examples* folder for more detailed code samples.

Built-In
--------
```lisp
; A few basic operations
(> & args)
(< & args)
(+ & args)
(- & args)
(* & args)
(= & args)

; Branching
(if expression then [else])

; A generic printing facility
(print "Hello World!")
```

Definitions
-----------

```lisp
(def myvalue 17)
```

Lists
-----

Lists are represented internally by Python tuples.

```lisp
(def mylist (list 1 2 3 4 5))

(print "List: " mylist)  ; (1, 2, 3, 4, 5)
(nth mylist 0)   ; 1
(nth mylist 5)   ; None
(first mylist)   ; 1
(last mylist)    ; 5
(count mylist)   ; 5
(rest mylist)    ; (2, 3, 4, 5)
(pop mylist)     ; (2, 3, 4, 5) - as a new list

(def plus5
  (fn (i)
    (+ i 5)))

(print (map plus5 mylist)) ; (6, 7, 8, 9, 10) - as a new list
```

Functions
---------

```lisp
(def add3
  (fn (a b c)
    (+ a b c)))

(print (add3 1 2 3))
```

Let Expressions
---------------
```lisp
(def add2plus7
  (fn (a b)
    (let ((c 5)
          (d 2))
      (+ a b c d))))

(print (add2plus7 1 2))
```

Python Interop
--------------
```lisp
(import requests)

(def fetch
  (fn (url)
    (requests.get url)))

(print (fetch "http://www.google.com/"))
```

Usage
-----
The **run.py** script in the root folder will generate .py files for every .lisp file in the **examples** folder. If you would like to play with Pyrens, I suggest simply adding examples of your own. I hope to eventually provide a stand-alone script to execute .lisp files directly.

Contact
-------
Please contact me at spligak@gmail.com or file an issue with any suggestions you might have!
