# Proyek Akhir: Menyelesaikan Permasalahan Perusahaan Edutech

## Business Understanding

Jaya Jaya Maju merupakan salah satu perusahaan multinasional yang telah berdiri sejak tahun 2000. Ia memiliki lebih dari 1000 karyawan yang tersebar di seluruh penjuru negeri. Walaupun telah menjadi menjadi perusahaan yang cukup besar, Jaya Jaya Maju masih cukup kesulitan dalam mengelola karyawan. Hal ini berimbas tingginya attrition rate (rasio jumlah karyawan yang keluar dengan total karyawan keseluruhan) hingga lebih dari 10%.

Untuk mencegah hal ini semakin parah, manajer departemen HR ingin meminta bantuan Anda mengidentifikasi berbagai faktor yang mempengaruhi tingginya attrition rate tersebut. Selain itu, ia juga meminta Anda untuk membuat business dashboard untuk membantunya memonitori berbagai faktor tersebut. Selain itu, mereka juga telah menyediakan dataset yang dapat Anda unduh melalui tautan berikut: [Jaya Jaya Maju](https://github.com/dicodingacademy/dicoding_dataset/tree/main/employee).

### Permasalahan Bisnis

Human Resource adalah sumber daya yang krusial untuk setiap organisasi. Organisasi menghabiskan banyak waktu dan uang untuk merekrut dan membina karyawan mereka, sehingga akan menjadi kerugian besar apabila karyawan meninggalkan perusahaan. Sehingga Attrition rate dapat meningkatkan biaya rekrutmen, perekrutan, dan pelatihan pengganti di industri, sedangkan sebaliknya pengurangan attrition rate dapat mengurangi produksi, dan membawa keuntungan di perusahaan.

Alasan untuk karyawan meninggalkan perusahaan bisa bermacam-macam dan bervariasi dari ketidakpuasan karena gaji rendah, kurang atau tidak adanya kesempatan pertumbuhan karir, pengawasan karyawan yang buruk, keinginan untuk bergabung dengan perusahaan yang memiliki kehadiran global, kurangnya pengakuan, kurangnya kebebasan berekspresi di organisasi, dan kurangnya pemanfaatan bakat dan keterampilan individu. Oleh karena itu, dalam situasi di mana semakin banyak karyawan yang meninggalkan organisasi, penting adanya upaya untuk manangani hal tersebut.

Contoh beberapa upaya yang dapat dilakukan untuk mengurangi attrition rate adalah sebagai berikut:
1. Mengidentifikasi faktor dan alasan yang memengaruhi tingginya tingkat Attrition di perusahaan.
2. Membuat Model untuk memprediksi apakah karyawan berisiko untuk meninggalkan perusahaan, sebagai bentuk usaha preventif di masa depan.
3. Membuat dashboard untuk memantau dan menganalisis faktor-faktor yang berkontribusi terhadap attrition rate.

### Cakupan Proyek

1. Penggunaan data dari dataset Jaya Jaya Maju untuk melakukan eksplorasi data, analisis statistik, dan pembuatan model prediktif.
2. Analisis faktor-faktor yang mempengaruhi attrition rate berdasarkan pengelompokan tertentu.
3. Pembuatan dashboard interaktif yang menyajikan informasi mengenai faktor-faktor relevan yang memengaruhi tingkat attriton rate.

### Persiapan

Sumber data: https://github.com/dicodingacademy/dicoding_dataset/blob/main/employee/employee_data.csv

Menjalankan proses prediksi:

Dengan asumsi bahwa dataset mempunyai struktur dan fitur sesuai dengan dataset sekarang, serta sudah dibersihkan

```
import python

new_data = pd.read_csv('new_data.csv')

X_new = python.preprocess_data(new_data)

prediction_logistic, prediction_svm, prediction_random_forest = python.predict_with_models(X_new)
```



## Business Dashboard

link: https://lookerstudio.google.com/reporting/e8c69760-e127-4277-9175-6b0351f4824a

Dashboard yang telah dibuat, disesuaikan dengan analisis yang didapat dari dataset, sehingga dapat memonitor dan memberi informasi hal-hal penting yang berkaitan dengan Attrion rate. Berikut penjelasan mengenai parameter-paramter pada dashboard:

1. Score card Employee Count: Total seluruh karyawan di perusahaan saat ini (mengacu pada dataset bersih).

2. Score card Attrition: Total karyawan attrition yang meninggalkan perusahaan. Secara umum apabila nilainya kecil akan semakin baik.

3. Score card Attriton Rate: Persentase jumlah Attrition terhadap jumlah karyawan secara keseluruhan (Employee Count). Merupakan indikator utama yang perhatikan di kasus ini, semakin rendah nilainya akan semakin baik.

4. Score card Avg Age: Rataan dari usia karyawan yang meninggalkan perusahaan. Indikator untuk menilai kebanyakan karyawan yang meninggalkan perusahaan berada pada usia muda atau tua. Dapat di analisis lebih lanjut dengan grafik Age group

5. Score card Avg Monthly Income: Rataan dari usia karyawan yang meninggalkan perusahaan. Indikator untuk menilai kebanyakan karyawan yang meninggalkan perusahaan berada pada pendapatan bulanan tinggi atau rendah. Dapat di analisis lebih lanjut dengan grafik Monthly Income Group

6. Score card Avg Total Working Years: Nilai rataan dari usia karyawan yang meninggalkan perusahaan. Indikator untuk menilai seberapa lama pengalaman kerja karyawan yang meninggalkan perusahaan.

7. Grafik Attrition by Age: Pengelompokan karyawan yang meninggalkan perushaan berdasarkan 5 rentang usia. Tiap grup/rentang usia dapat di monitor secara terpisah untuk mengetahui kaitannya dengan parameter lain seperti monthly income, jobrole, gender, marital status, dan satisfaction level. Pemfokusan ini dapat berguna untuk menemukan solusi terbaik untuk mengurangi attrition di rentang usia tertentu.

8. Grafik Attrition by Monthly Income: Pengelompokan karyawan yang meninggalkan perusahaan berdasarkan rentang pendapatan bulanan mereka. Parameter ini berkorelasi dengan monthly income dan juga dapat dimonitor secara terpisah untuk tiap grupnya, serta dihubungkan terutama kaitannya dengan Job Role dan satisfaction. Semakin banyak karyawan attrition di grup monthly income rendah mengindikasikan karyawan yang menginkan pendapatan lebih kompetitif, ekspektasinya tidak terpenuhi, atau yang lainnya.

9. Grafik Attrition by Job Satisfaction: Pengelompokan karyawan yang meninggalkan perusahaan berdasarkan kategori kepuasannya terhadap pekerjaan. Dapat digunakan sebagai indikator penyebab attrition apabila kebanykan nilainya di kategori rendah, akan tetapi penilaian ini tidak selalu sesuai. Semakin banyak di kategori tinggi (high/very high) akan semakin baik.

10. Grafik Attrition by Environtment Satisfaction: Pengelompokan karyawan yang meninggalkan perusahaan berdasarkan kategori kepuasannya lingkungan kerja. Dapat digunakan sebagai indikator penyebab attrition kebanyakan nilainya di kategori rendah, akan tetapi penilaian ini tidak selalu sesuai. Semakin banyak di kategori tinggi (high/very high) akan semakin baik.

11. Tabel Top Attrition by Job Role: Memperlihatkan 5 Job Role dengan attrition rate tertinggi di perusahaan, beserta dengan jumlah karyawannya. Selain untuk memonitor, dapat digunakan untuk mengidentifikasi prioritas JobRole yang harus diutamakan. Biasanya peringkat tertinggilah yang harus diutamakan, akan tetapi bila Job Role di isi oleh sedikit karyawan, maka juga perlu ada perhatian lebih karena pengurangan 1 orang saja dapat berdampak lebih signifikan dari pada JobRole dengan total karyawan yang banyak.

12. Pie Attrition by gender dan marital status: Memberikan informasi proporsi, jumlah, dan persentase terkait gender dan marital status dari karyawan yang meinggalkan perusahaan. Selain memonitor, dapat menjadi pedoman untuk solusi yang sesuai untuk mengurangi attrition agar sesuai demografi karyawan, seperti kompensasi pernikahan, tunjangan, dan kebijakan terkait kesetaraan gender.

13. Filter Department: Opsional apabila ingin memfokuskan hanya pada department tertentu.


## Conclusion
- Berdasarkan dataset yang diberikan, secara singkat menghasilkan kesimpulan analisis sebagai berikut:

    1. Tingkat pengurangan karyawan cenderung lebih tinggi pada mereka yang sering bepergian dibandingkan dengan mereka yang jarang bepergian. Karyawan yang sering bepergian juga cenderung memiliki tarif per jam, harian, bulanan, dan pendapatan bulanan yang lebih rendah dibandingkan dengan kategori lainnya.

    2. Departemen Penjualan memiliki tingkat pengurangan karyawan tertinggi meskipun memiliki lebih sedikit karyawan dibandingkan dengan departemen R&D. Tidak ada korelasi yang jelas antara pendapatan dan tingkat pengurangan karyawan dalam departemen.
    
    3. Peran pekerjaan tertentu seperti Sales Representative, Laboratory Technician, Human Resource, Research Scientist, dan Sales Executive memiliki tingkat pengurangan yang jauh lebih tinggi dibandingkan dengan Job Role lain. Peran-peran ini biasanya memiliki karyawan yang lebih muda, dengan pendapatan lebih rendah dan masa kerja lebih pendek, yang menunjukkan adanya pola potensial.

    4. Mayoritas karyawan berada pada JobLevel 1 dan 2, dengan tingkat pengurangan karyawan tertinggi terdapat pada karyawan JobLevel 1, khususnya mereka yang berperan sebagai Research Scientist.

    5. Karyawan yang keluar dari perusahaan cenderung berusia lebih muda dan memiliki pendapatan bulanan yang lebih rendah dibandingkan dengan angkatan kerja secara keseluruhan. Selain itu, karyawan yang masih lajang memiliki tingkat pengurangan karyawan yang lebih tinggi dibandingkan dengan karyawan yang sudah menikah atau bercerai.

- Pembuatan model menggunakan algoritma SVM menghasilkan model yang cukup dapat digunakan untuk memprediksi attrition berdasarkan variabel2 yang ada dalam dataset, akan tetapi peningkatan kemampuan model sangat dibutuhkan, terutama menggunakan dataset yang lebih banyak atau tanpa adanya label attriton yang kosong.

- Dashboard memiliki beberapa informasi yang dapat dimonitor terkait attrion rate di perusahaan ini. Dimana seperti yang telah diketahui masalah utama adalah faktor karyawan attrition dengan umur, gaji, total working years cukup rendah, yang kebanyakan berkumpul pada JobRole tertentu. Selain itu informasi tambahan juga dapat dikaitkan dengan gender dan Marital status.

### Rekomendasi Action Items (Optional)

Berikan beberapa rekomendasi action items yang harus dilakukan perusahaan guna menyelesaikan permasalahan atau mencapai target mereka.

- action item 1
    Melihat pola utama attrition di perusahaan yang mana terbanyak ada pada usia cukup muda, monthly income rendah, dan total working years rendah. Maka direkomendasikan untuk melakukan aksi yang difokuskan karyawan muda/pengalaman rendah. Hal ini dapat berupa penawaran program peluang pertumbuhan karir, insentif/bonus, pengembangan karir, pengaturan kerja yang fleksibel, pekerjaan yang berorientasi pada tujuan, dan budaya perusahaan yang ramah karyawan baru.
- action item 2
    Terkait JobRole tertentu yang lebih tinggi dari pada yang lainnya, dapat dilakukan aksi tambahan berupa peningkatan Job satisfaction dan meningkatkan budaya purpose-driven work. Selain itu, perlunya penelusuran lebih dalam terutama pada Sales Representative dan Human Resource yang memiliki jumlah total karyawan terendah menggunakan variabel selain yang ada pada dataset, dikarenakan hasil analisis satisfaction, monthlyincome, dan age belum memberikan informasi konkret.
- action item 3
    Kebanyakan karyawan attrition yang berada pada status single, sehingga program khusus untuk menarik perhatian karyawan single seperti bantuan pernikahan mungkin dapat membantu menurunkan tingkat attrition
- action item 4
    Berkaitan dengan attrition yang lebih tinggi pada karyawan yang sering melakukan perjalanan. Dapat dilakukan aksi seperti penyesuaian/pemberian bonus, peningkatan tarif per jam/harian/ bulanan untuk para karyawan yang bepergian, atau bisa dengan pembagian schedule karyawan yang berpergian, sehingga tidak berfokus pada beberapa karyawan saja.
- action item 5
    Berkaitan dengan pemanfaatan model untuk memprediksi mana karyawan yang beresiko meninggalkan perusahaan, dapat menggunakan model yang telah dibuat akan tetapi akan lebih baik jika dikembangkan lebih jauh, serta menggunakan dataset yang lebih baik (tanpa adanya missing value)
