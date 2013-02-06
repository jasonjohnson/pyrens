(def mylist (list 1 2 3 4 5))
(def mylist2 (list 6))
(def mylist3 (list 7 (+ 7 1)))

(def mystrings (list "Pyrens" "is" "awesome!"))

(def plus5
     (fn (i)
         (+ 5 i)))

(def counter
     (fn (s)
         (count s)))

(print "List: " mylist)
(print "My Strings: " mystrings)

(print (nth mylist 0))
(print (nth mylist 1))
(print (nth mylist 2))
(print (nth mylist 3))
(print (nth mylist 4))

(print "Count: " (count mylist))
(print "First: " (first mylist))
(print "Last: " (last mylist))
(print "Rest: " (rest mylist))
(print "Pop: " (pop mylist))

(print (map plus5 mylist))

(def mylenghts (map counter mystrings))

(print (first mylenghts))
(print (rest mylenghts))

(print mylist2)
(print (cons 5 mylist2))
