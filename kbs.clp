(defrule line-equals
(line ?i ?x)
(line ?j ?x)
=>
(assert (fired-rule line-equals))
(assert (line-eq ?i ?j)))

(defrule is-segitiga-sama-sisi
(n-point 3)
(line-eq 1 2)
(line-eq 2 3)
=> 
(assert (matched-fact n-point 3))
(assert (matched-fact line-eq 1 2))
(assert (matched-fact line-eq 2 3))
(assert (fired-rule is-segitiga-sama-sisi))
(assert (segitiga-sama-sisi true)))

(defrule is-segitiga-sama-kaki
(n-point 3)
(line-eq ?i ?j)
=>
(assert (matched-fact n-point 3))
(assert (matched-fact line-eq ?i ?j))
(assert (fired-rule is-segitiga-sama-kaki))
(assert (segitiga-sama-kaki true)))

(defrule is-segitiga-siku
(n-point 3)
(point ?id ?x ?y 90)
=>
(assert (matched-fact n-point 3))
(assert (matched-fact point ?x ?y 90))
(assert (fired-rule is-segitiga-siku))
(assert (segitiga-siku true)))

(defrule is-segitiga-tumpul
(n-point 3)
(point ?id ?x ?y ?angle)
(test (> ?angle 90))
=>
(assert (matched-fact n-point 3))
(assert (matched-fact point ?x ?y 90))
(assert (fired-rule is-segitiga-tumpul))
(assert (segitiga-tumpul true)))

(defrule is-sama-kaki-tumpul
(n-point 3)
(segitiga-sama-kaki true)
(segitiga-tumpul true)
=>
(assert (matched-fact n-point 3))
(assert (matched-fact segitiga-sama-kaki true))
(assert (matched-fact segitiga-tumpul true))
(assert (fired-rule is-sama-kaki-tumpul))
(assert (segitiga-sama-kaki-tumpul true)))

(defrule is-sama-kaki-siku
(n-point 3)
(segitiga-sama-kaki true)
(segitiga-siku true)
=>
(assert (matched-fact n-point 3))
(assert (matched-fact segitiga-sama-kaki true))
(assert (matched-fact segitiga-siku true))
(assert (fired-rule is-sama-kaki-siku))
(assert (segitiga-sama-kaki-siku true)))

(defrule is-sama-kaki-lancip
(n-point 3)
(segitiga-sama-kaki true)
=>
(assert (matched-fact n-point 3))
(assert (matched-fact segitiga-sama-kaki true))
(assert (fired-rule is-sama-kaki-lancip))
(assert (segitiga-sama-kaki-lancip true)))

(defrule is-segitiga-lancip
(n-point 3)
=>
(assert (matched-fact n-point 3))
(assert (fired-rule is-segitiga-lancip))
(assert (segitiga-lancip true)))

(defrule is-segilima-sama-sisi
(n-point 5)
(point 1 ?a ?b ?x)
(point 2 ?c ?d ?x)
(point 3 ?e ?f ?x)
(point 4 ?g ?h ?x)
(point 5 ?i ?j ?x)
=>
(assert (matched-fact n-point 5))
(assert (matched-fact all-five-angles-equal))
(assert (fired-rule is-segilima-sama-sisi))
(assert (segilima-sama-sisi true)))

(defrule is-segilima
(n-point 5)
=>
(assert (matched-fact n-point 5))
(assert (fired-rule is-segilima))
(assert (segilima true)))

(defrule is-segienam-sama-sisi
(n-point 6)
(point 1 ?a ?b ?x)
(point 2 ?c ?d ?x)
(point 3 ?e ?f ?x)
(point 4 ?g ?h ?x)
(point 5 ?i ?j ?x)
(point 6 ?k ?l ?x)
=>
(assert (matched-fact n-point 6))
(assert (matched-fact all-six-angles-equal))
(assert (fired-rule is-segienam-sama-sisi))
(assert (segienam-sama-sisi true)))

(defrule is-segienam
(n-point 6)
=>
(assert (matched-fact n-point 6))
(assert (fired-rule is-segienam))
(assert (segienam true)))

(defrule is-jajar-genjang-a
(n-point 4)
(line-eq 1 2)
(line-eq 3 4)
=>
(assert (n-point 4))
(assert (matched-fact line-eq 1 2))
(assert (matched-fact line-eq 3 4))
(assert (fired-rule is-jajar-genjang))
(assert (jajar-genjang true)))

(defrule is-jajar-genjang-b
(n-point 4)
(line-eq 1 3)
(line-eq 2 4)
=>
(assert (n-point 4))
(assert (matched-fact line-eq 1 3))
(assert (matched-fact line-eq 2 4))
(assert (fired-rule is-jajar-genjang))
(assert (jajar-genjang true)))

(defrule is-jajar-genjang-c
(n-point 4)
(line-eq 1 4)
(line-eq 2 3)
=>
(assert (n-point 4))
(assert (matched-fact line-eq 1 4))
(assert (matched-fact line-eq 2 3))
(assert (fired-rule is-jajar-genjang))
(assert (jajar-genjang true)))

(defrule is-layang-layang-a
(n-point 4)
(point 1 ?x ?y ?angle)
(point 3 ?j ?k ?angle)
=>
(assert (matched-fact n-point 4))
(assert (matched-fact angle1-equals-angle3))
(assert (fired-rule is-layang-layang))
(assert (layang-layang true)))

(defrule is-layang-layang-b
(n-point 4)
(point 2 ?x ?y ?angle)
(point 1 ?j ?k ?angle)
=>
(assert (matched-fact n-point 4))
(assert (matched-fact angle1-equals-angle2))
(assert (fired-rule is-layang-layang))
(assert (layang-layang true)))

(defrule is-segiempat-beraturan
(jajar-genjang true)
(point 1 ?a ?b ?x)
(point 2 ?c ?d ?x)
(point 3 ?e ?f ?x)
(point 4 ?g ?h ?x)
=>
(assert (matched-fact jajar-genjang true))
(assert (matched-fact all-four-angles-equal))
(assert (fired-rule is-segiempat-beraturan))
(assert (segiempat-beraturan true)))

(defrule is-segiempat-tidak-beraturan
(n-point 4)
=> 
(assert (matched fact n-point 4))
(assert (fired-rule is-segiempat-tidak-beraturan))
(assert (segiempat-tidak-beraturan true)))

(defrule is-trapesium-sama-kaki-a
(n-point 4)
(line-eq 1 3)
(point 2 ?x ?y ?angle-a)
(point 3 ?i ?j ?angle-b)
(> ?angle-a 90)
(> ?angle-b 90)
=>
(assert (matched-fact n-point 4))
(assert (matched-fact line-eq 1 3))
(assert (matched-fact angle2-tumpul))
(assert (matched-fact angle3-tumpul))
(assert (fired-rule is-trapesium-sama-kaki))
(assert (trapesium-sama-kaki true)))

(defrule is-trapesium-sama-kaki-b
(n-point 4)
(line-eq 1 3)
(point 2 ?x ?y ?angle-a)
(point 3 ?i ?j ?angle-b)
(< ?angle-a 90)
(< ?angle-b 90)
=>
(assert (matched-fact n-point 4))
(assert (matched-fact line-eq 1 3))
(assert (matched-fact angle2-lancip))
(assert (matched-fact angle3-lancip))
(assert (fired-rule is-trapesium-sama-kaki))
(assert (trapesium-sama-kaki true)))

(defrule is-trapesium-sama-kaki-c
(n-point 4)
(line-eq 2 4)
(point 3 ?x ?y ?angle-a)
(point 4 ?i ?j ?angle-b)
(> ?angle-a 90)
(> ?angle-b 90)
=>
(assert (matched-fact n-point 4))
(assert (matched-fact line-eq 2 4))
(assert (matched-fact angle2-tumpul))
(assert (matched-fact angle3-tumpul))
(assert (fired-rule is-trapesium-sama-kaki))
(assert (trapesium-sama-kaki true)))

(defrule is-trapesium-sama-kaki-d
(n-point 4)
(line-eq 2 4)
(point 3 ?x ?y ?angle-a)
(point 4 ?i ?j ?angle-b)
(> ?angle-a 90)
(> ?angle-b 90)
=>
(assert (matched-fact n-point 4))
(assert (matched-fact line-eq 2 4))
(assert (matched-fact angle2-lancip))
(assert (matched-fact angle3-lancip))
(assert (fired-rule is-trapesium-sama-kaki))
(assert (trapesium-sama-kaki true)))

(defrule is-angle-rightest
(point 1 ?a ?b ?l)
(point 2 ?c ?d ?i)
(point 3 ?e ?f ?j)
(point 4 ?g ?h ?k)
=>
(assert (angle-rightest (max ?a ?c ?e ?g))))

(defrule is-angle-leftest
(point 1 ?a ?b ?l)
(point 2 ?c ?d ?i)
(point 3 ?e ?f ?j)
(point 4 ?g ?h ?k)
=>
(assert (angle-leftest (min ?a ?c ?e ?g))))

(defrule is-trapesium-rata-kanan-a
(point ?s ?x ?y 90)
(angle-rightest ?x)
(point 1 ?i ?j ?angle1)
(point 2 ?k ?l ?angle2)
(neq ?angle1 ?angle2)
=>
(assert (matched-fact point ?s ?x ?y 90))
(assert (matched-fact angle-rightest ?x))
(assert (matched-fact uneven-angles))
(assert (fired-rule is-trapesium-rata-kanan))
(assert (trapesium-rata-kanan true)))

(defrule is-trapesium-rata-kanan-b
(point ?s ?x ?y 90)
(angle-rightest ?x)
(point 2 ?i ?j ?angle1)
(point 3 ?k ?l ?angle2)
(neq ?angle1 ?angle2)
=>
(assert (matched-fact point ?s ?x ?y 90))
(assert (matched-fact angle-rightest ?x))
(assert (matched-fact uneven-angles))
(assert (fired-rule is-trapesium-rata-kanan))
(assert (trapesium-rata-kanan true)))

(defrule is-trapesium-rata-kanan-c
(point ?s ?x ?y 90)
(angle-rightest ?x)
(point 3 ?i ?j ?angle1)
(point 4 ?k ?l ?angle2)
(neq ?angle1 ?angle2)
=>
(assert (matched-fact point ?s ?x ?y 90))
(assert (matched-fact angle-rightest ?x))
(assert (matched-fact uneven-angles))
(assert (fired-rule is-trapesium-rata-kanan))
(assert (trapesium-rata-kanan true)))

(defrule is-trapesium-rata-kanan-d
(point ?s ?x ?y 90)
(angle-rightest ?x)
(point 1 ?i ?j ?angle1)
(point 4 ?k ?l ?angle2)
(neq ?angle1 ?angle2)
=>
(assert (matched-fact point ?s ?x ?y 90))
(assert (matched-fact angle-rightest ?x))
(assert (matched-fact uneven-angles))
(assert (fired-rule is-trapesium-rata-kanan))
(assert (trapesium-rata-kanan true)))

(defrule is-trapesium-rata-kiri-a
(point ?s ?x ?y 90)
(angle-leftest ?x)
(point 1 ?i ?j ?angle1)
(point 2 ?k ?l ?angle2)
(neq ?angle1 ?angle2)
=>
(assert (matched-fact point ?s ?x ?y 90))
(assert (matched-fact angle-leftest ?x))
(assert (matched-fact uneven-angles))
(assert (fired-rule is-trapesium-rata-kiri))
(assert (trapesium-rata-kiri true)))

(defrule is-trapesium-rata-kiri-b
(point ?s ?x ?y 90)
(angle-leftest ?x)
(point 2 ?i ?j ?angle1)
(point 3 ?k ?l ?angle2)
(neq ?angle1 ?angle2)
=>
(assert (matched-fact point ?s ?x ?y 90))
(assert (matched-fact angle-leftest ?x))
(assert (matched-fact uneven-angles))
(assert (fired-rule is-trapesium-rata-kiri))
(assert (trapesium-rata-kiri true)))

(defrule is-trapesium-rata-kiri-c
(point ?s ?x ?y 90)
(angle-leftest ?x)
(point 3 ?i ?j ?angle1)
(point 4 ?k ?l ?angle2)
(neq ?angle1 ?angle2)
=>
(assert (matched-fact point ?s ?x ?y 90))
(assert (matched-fact angle-leftest ?x))
(assert (matched-fact uneven-angles))
(assert (fired-rule is-trapesium-rata-kiri))
(assert (trapesium-rata-kiri true)))

(defrule is-trapesium-rata-kiri-d
(point ?s ?x ?y 90)
(angle-leftest ?x)
(point 1 ?i ?j ?angle1)
(point 4 ?k ?l ?angle2)
(neq ?angle1 ?angle2)
=>
(assert (matched-fact point ?s ?x ?y 90))
(assert (matched-fact angle-leftest ?x))
(assert (matched-fact uneven-angles))
(assert (fired-rule is-trapesium-rata-kiri))
(assert (trapesium-rata-kiri true)))