(def power
     (fn (arg1 arg2 arg3)
         (if (> (* arg1 arg2 arg3) 20)
             100
             200)))

(print (power 1 2 3))
