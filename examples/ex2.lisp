(def testing
    (fn (x y z)
        (* (let ((a (fn (a1 a2) (+ a1 a2)))
                 (b (* 72 8 2))
                 (c 3456))
                 (* (a 2 2) b c)) x y z)))

(print (testing 1 2 3))
