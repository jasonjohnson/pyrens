(import requests)

(def fetch
    (fn (url)
        (requests.get url)))

(print (fetch "http://www.google.com/"))

