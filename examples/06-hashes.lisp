(def myhash1 (hash "key1" (list 1 2 3) "key2" 2))
(def myhash2 (hash "key3" 3))
(def myhash3 (merge myhash1 myhash2))

(print (get myhash1 "key1"))
(print (get myhash1 "key2"))

(print myhash2)

(print myhash3)
(print (nth (get myhash3 "key1") 0))

(print (count myhash3))
