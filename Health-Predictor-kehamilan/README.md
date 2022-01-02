# Fetal Health Predictor
![Project Poster](/gambar/poster.png "Project Poster")

Anggota Kelompok: 
1. Ihsan Maulana Riyadi (Ketua)
2. Angel Metanosa Afinda
3. Muhammad Yanuar Pribadi
4. Tubagus Ibrohim

---

## Latar Belakang Masalah
Kemampuan penyelenggaraan pelayanan kesehatan suatu bangsa diukur dengan menentukan tinggi rendahnya angka kematian ibu dan janin dalam 100.000 persalinan hidup, namun pada kenyataannya angka kematian perinatal masih tinggi. Angka kematian yang tinggi dapat dihindari dengan cara memberikan layanan kesehatan yang maksimal ketika masa bersalin. Secara global, sekitar 130 juta kelahiran terjadi setiap tahun. Diantaranya 303.000 kematian ibu, 2.6 juta bayi lahir mati, dan 2.7 juta bayi meninggal dalam masa neonatal. 

Intrauterine Fetal Death (IUFD) adalah kematian yang terjadi saat usia kehamilan > 20 minggu dan janin sudah mencapai ukuran 500 gram atau lebih. Umumnya IUFD terjadi menjelang persalinan saat kehamilan sudah memasuki usia 32 minggu dan istilah lahir mati (stillbirth) yang merupakan hasil konsepsi dalam keadaan mati yang telah mencapai usia kehamilan 28 minggu, sering digunakan bersamaan dengan IUFD. Kematian janin merupakan hasil akhir dari gangguan pertumbuhan janin, gawat janin, atau infeksi
## Output
Sehingga dari masalah tersebut kami berharap dengan pembuatan model yang telah dibuat dengan model algoritma Random Forest kemudian melewati RandomziedSearchCV (akurasi 93.6%) ini dan web lokal, walaupun dalam praktiknya model ini hanya dapat digunakan apabila sebagian besar datanya mengandung data dari alat CTG atau Cardiotocograms, yaitu alat yang dapat mendeteksi denyut jantung janin. Sehingga aplikasi web ini masih terbatas dalam penggunaannya, terutama di Indonesia, karena hanya beberapa rumah sakit yang mempunyai alat tersebut. Target kami fokus ditujukan kepada para profesional di bidang kesehatan ibu & anak, yaitu di ranah dokter kandungan. Prediktor ini diharap dapat meminimalisir dan mencegah hal-hal yang tidak diinginkan pada saat janin masih dalam kandungan.

Variabel ouput sendiri terdiri dari tiga macam, yaitu normal, suspect, dan pathological. Normal adalah kondisi janin tidak terkena penyakit/ sehat, suspect artinya ada tanda-tanda kondis janin tidak sehat, dan pathological adalah kondisi janin sudah terkena penyakit yang kemudian dapat mengancam keselamatan ibu dan janin. 
## User Guidance :

Pre-requisites :
Terinstall python
Memiliki library flask , pandas , dan joblib

Tata cara penggunaan :
1. Buka cmd pada folder tempat file diekstrak
2. Run di cmd python app.py
3. Html akan muncul silahkan prediksi fetal health



