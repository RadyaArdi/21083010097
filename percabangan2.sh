#!/bin/bash

printf "Jajan apa yang kamu suka ?\n"
printf "pentol ?\n"
printf "batagor ?\n"
printf "cireng ?\n"

read jajan

case "$jajan" in
  "pentol")
    echo "Pentol buk mah wenak slur!"
    ;; 
 "batagor")
    echo "Batagore mas budi mantap bat"
    ;;
  "cireng")
    echo "Cirenge kanting rasane unch-unch"
    ;;
  *)
    echo "Makanan yang kamu suka ga enak hehe"
esac
