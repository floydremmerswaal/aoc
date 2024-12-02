#lang racket

(require megaparsack megaparsack/text)

(define (isMonotoneIncreasing lst)
  (apply < lst))

(define (isMonotoneDecreasing lst)
  (apply > lst))

(define (isMonotone lst)
  (or (isMonotoneIncreasing lst) (isMonotoneDecreasing lst)))

(define (mapToInts lst)
  (map string->number lst))

(define (processLine line) 
  (isMonotone (mapToInts (string-split line " "))))


(for ([line (file->lines "example.txt")])
  ;process line and count the number of "true" results  
  (print (processLine line)))