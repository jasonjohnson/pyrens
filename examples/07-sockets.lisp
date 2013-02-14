(def sock (socket-create))

(socket-connect sock "google.com" 80)

(def http-request
     (fn (verb path)
         (str verb " " path " HTTP/1.1\r\n\r\n")))

(socket-write sock (http-request "GET" "/"))
(print (socket-read sock))

(socket-close sock)
