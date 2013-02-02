(def scope
     (fn (a b)
         (let ((c 3))
           (+ a b c))))

(print (scope 1 2))
