
(ns solution
   (:gen-class)
   (:require [clojure.java.io :as io]))

(defn Example []
   (with-open [rdr (clojure.java.io/reader "example.txt")]
   (reduce conj [] (line-seq rdr))))
(Example)