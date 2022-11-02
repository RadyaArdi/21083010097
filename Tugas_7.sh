#!/bin/bash
#Mendeklarasikan fungsi
Panjang() {
       echo "Masukkan panjang : "
       read Panjang
}
Lebar() {
    echo "Masukkan lebar : "
    read Lebar
}
Luas() {
    let luas=$Panjang*$Lebar
    echo "Luas Persegi :
$luas"
    read Luas
}

#Memanggil fungsi
Panjang
Lebar
Luas
