#menginputkan semester yang sedang ditempuh oleh mahasiswa
echo -n "input : "
read semester

#mendeklarasikan array dari  nilai IPSMhs (IPS Mahasiswa)
declare -a IPSMhs

i=0
#dari semester yang telah diinputkan dikurangi 1
let jumlah=$semester-1

#memeriksa nilai indeks yang sama dengan jumlah
while [ $i -le $jumlah ];
do
	let nilai=$i+1
	printf " " $nilai;
	read nilaiIPSMhs;
	IPSMhs[$i]=$nilaiIPSMhs;
	let total=total+$nilaiIPSMhs;
	let i=$i+1;
done

let IPK=$total/$semester
echo "IPS mhs = " $total "/" $semester
echo "IPK mhs = " $IPK
