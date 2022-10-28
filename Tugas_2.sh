#!/bin/bash

echo "Selamat Datang pada Latihan Soal Matematika"

echo "Input nama anda :";
read nama
echo -e "\n Halo, $nama! :)  selamat mengerjakan"

echo "Mari kita mulai!"
read latihan
if [ $latihan = "Ayo!" ]
then
  echo "tentukan angka a: 1-100"
  tentukan=$RANDOM%20
  let b=$tentukan
  echo "b=$b"
  echo "Angka a: "
  read a
  let bagi=$a/$b
  echo "a / b = $bagi"

  echo "Bagaimanakah hasilnya?"
  read hasil
  if [ $hasil == $bagi ]
  then
    echo "Jawaban kamu benar! Lanjutkan"
  else
    echo "Coba lagi yuk, jangan menyerah"
  fi

else
 echo "Yeay, belajar lagi yuk"
fi
