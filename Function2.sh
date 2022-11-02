#!/bin/bash
# Mendeklarasikan fungsi
function nama {
    echo "Siapa namamu?"
    read nama
}
function npm {
    echo "Sebutkan npm mu"
    read npm
    echo -e "Hai $nama dengan npm $npm, Selamat datang \n di praktikum sistem operasi yang seru ini ya!"
}

#memanggil fungsi
nama
npm
