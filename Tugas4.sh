echo -n "Input bilangan ganjil: ";
read ganjil;

a=0

until [ ! $ganjil -gt $a ]
do
   echo $ganjil
   ganjil=$((ganjil-2))
done
