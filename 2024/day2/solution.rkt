#lang racket


(define (mapToInts lst)
  (map string->number lst))

(define (allPositive lst)
  (for/and ([x lst])
    (positive? x)))

(define (allNegative lst)
  (for/and ([x lst])
    (negative? x)))

; create a new list with the differences between each element

(define (differenceHelper lst acc)
  (if (null? (cdr lst))
      acc
      (differenceHelper (cdr lst) (cons (- (car lst) (cadr lst)) acc))))

(define (differences lst)
  (reverse (differenceHelper lst '())))

(define (toPositive lst)
  (map abs lst))

(define (isMonotone lst)
  (or (allPositive (differences lst) )
      (allNegative (differences lst))))


(define (allBetween1And3 lst)
  (for/and ([x lst])
    (and (<= 1 x) (<= x 3))))

(define (isSafe lst)
  (and (isMonotone lst) (allBetween1And3 (toPositive (differences lst)))))

(define (processLine line) 
  (isSafe (mapToInts (string-split line " "))))

(define (true? x)
  (eq? x #t))

; construct all possible sublists (with 1 element missing)
; and check if any of them are safe
(define (isSafe2 lst)
  (ormap isSafe
         (for/list ([i (in-range (length lst))])
           (append (take lst i) (drop lst (add1 i))))))

(define (processLine2 line) 
  (isSafe2 (mapToInts (string-split line " "))))

(count true? (map processLine (file->lines "input.txt")))

(count true? (map processLine2 (file->lines "input.txt")))
  