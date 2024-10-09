http://pbp.cs.ui.ac.id/sean.farrel/nvloo


Tugas 2

1. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
    a. Membuat Sebuah Proyek Django Baru
        Langkah:
        Install Django dengan perintah: pip install django.
        Buat proyek baru dengan perintah: django-admin startproject nama_proyek.
        Ini akan membuat direktori baru dengan struktur dasar Django, termasuk manage.py, settings.py, dan folder lainnya yang penting untuk pengaturan proyek.
    b. Membuat Aplikasi dengan Nama 'main'
        Langkah:
        Navigasi ke direktori proyek: cd nama_proyek.
        Buat aplikasi baru dengan perintah: python manage.py startapp main.
        Ini akan membuat folder main yang berisi file seperti models.py, views.py, dan urls.py.
    c. Melakukan Routing pada Proyek untuk Menjalankan Aplikasi 'main'
        Langkah:
        Di dalam nama_proyek/nama_proyek/settings.py, tambahkan 'main', ke dalam INSTALLED_APPS.
        Buat file urls.py di dalam folder aplikasi main (jika belum ada), dan tambahkan rute di dalamnya.
        Di dalam nama_proyek/nama_proyek/urls.py, impor include dari django.urls dan tambahkan path menuju main.urls seperti berikut:
        from django.urls import include, path

        urlpatterns = [
            path('', include('main.urls')),
        ]
    d. Membuat Model 'Product' dengan Atribut
        Langkah:
        Buka main/models.py dan buat model seperti berikut:
        from django.db import models

        class Product(models.Model):
            name = models.CharField(max_length=100)
            price = models.DecimalField(max_digits=10, decimal_places=2)
            description = models.TextField()
            
            def __str__(self):
                return self.name
        Setelah itu, jalankan perintah python manage.py makemigrations dan python manage.py migrate untuk membuat dan menjalankan migrasi.
    e. Membuat Fungsi pada views.py untuk Menampilkan Nama Aplikasi dan Nama/Kelas
        Langkah:
        Buka main/views.py dan buat fungsi untuk merender template HTML:
        from django.shortcuts import render

        def home(request):
            context = {
                'app_name': 'Main',
                'student_name': 'Nama Anda',
                'student_class': 'Kelas Anda'
            }
            return render(request, 'home.html', context)
    f. Routing pada urls.py untuk Mempetakan Fungsi pada views.py
        Langkah:
        Di dalam main/urls.py, tambahkan kode untuk memetakan fungsi:
        from django.urls import path
        from . import views

        urlpatterns = [
            path('', views.home, name='home'),
        ]
    g. Deployment ke PWS
        Langkah:
        Pertama, pastikan aplikasi sudah siap untuk deployment. Buat file Procfile dan tambahkan:
        web: gunicorn nama_proyek.wsgi
        Gunakan layanan seperti PythonAnywhere untuk melakukan deployment. Upload proyek ke platform dan konfigurasikan domain untuk bisa diakses publik.


2. Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.
![plot](./bagan.png)

Proses Request-Response pada Aplikasi Django
Request:
Client membuat request ke server dengan URL tertentu.
urls.py memetakan request tersebut ke fungsi yang ada di views.py.
views.py mengakses data dari models.py (jika diperlukan) dan mengirimkannya ke template HTML.
Template HTML mengembalikan halaman dengan data yang sudah diolah ke client sebagai response.
Kaitan:

urls.py: Menentukan rute URL untuk permintaan.
views.py: Menangani logika bisnis dan menentukan apa yang akan ditampilkan.
models.py: Berinteraksi dengan database untuk menyimpan atau mengambil data.
Template HTML: Menampilkan data yang sudah diolah ke pengguna.


3. Jelaskan fungsi git dalam pengembangan perangkat lunak!
Git digunakan untuk version control, membantu pengembang melacak perubahan kode, berkolaborasi dengan tim, mengelola versi proyek, dan memulihkan versi kode sebelumnya jika terjadi kesalahan.


4. Menurut Anda, dari semua framework yang ada, mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak?
Menurut saya berdasarkan tutorial - tutorial sebelumnya dan tugas - tugas yang ada, Django adalah framework yang lengkap (batteries-included), dengan dokumentasi yang baik, memudahkan pemula untuk memahami dasar-dasar pengembangan aplikasi web secara menyeluruh, termasuk routing, model, dan views.


5. Mengapa model pada Django disebut sebagai ORM?
ORM (Object-Relational Mapping) menghubungkan model dalam bentuk objek Python dengan database relasional seperti PostgreSQL atau MySQL, sehingga pengembang bisa bekerja dengan database tanpa menulis query SQL langsung, cukup dengan metode Python. Adanya hubungan - hubungan terkait objek yang satu dengan yang lain juga menjadikan alasan Django dijadikan permulaan pembelajaran seperti pada pertanyaan sebelumnya.


Tugas 3
1. Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?
    Dalam sebuah platform, data delivery merujuk pada proses pengiriman dan penerimaan data antara komponen atau aplikasi yang berbeda. Data delivery penting karena platform biasanya tidak berdiri sendiri; mereka berinteraksi dengan aplikasi lain (misalnya, aplikasi mobile, web service, database, API). Tanpa data delivery yang baik, platform tidak akan bisa bertukar informasi secara efisien, yang pada akhirnya dapat mengakibatkan pengalaman pengguna yang buruk atau masalah teknis. Data delivery memastikan bahwa:
    a. Data dikirim dan diterima secara akurat dan aman.
    b. Platform sinkron dengan layanan eksternal yang terhubung.
    c. Pengalaman pengguna realtime dapat dicapai (misalnya, update langsung di aplikasi).


2. Menurutmu, mana yang lebih baik antara XML dan JSON? Mengapa JSON lebih populer dibandingkan XML?
    Menurut saya, XML lebih baik daripada JSON. Perbandingannya sebagai berikut:
        XML:
            - Struktur lebih kompleks dan mendukung penanda (markup) yang kaya.
            - Mendukung atribut dan namespace, sehingga sering digunakan dalam sistem enterprise yang butuh struktur hierarkis lebih ketat.
            - Lebih berat karena sintaksnya yang verbose.
        JSON:
            - Lebih ringan dan mudah dibaca oleh manusia maupun mesin.
            - Sering digunakan untuk API modern karena formatnya sederhana (hanya pasangan kunci-nilai).
            - Memiliki integrasi langsung dengan JavaScript, membuatnya lebih populer di web development.
    Mengapa JSON lebih populer dibandingkan XML?
        - Lebih ringkas dan mudah dikelola.
        - Lebih cepat diparsing oleh browser dan bahasa pemrograman modern.
        - Lebih kompatibel dengan layanan RESTful API yang kini banyak digunakan oleh platform web dan   mobile.
        - Menyediakan struktur yang cukup sederhana untuk kebanyakan kasus penggunaan web.


3. Jelaskan fungsi dari method is_valid() pada form Django dan mengapa kita membutuhkan method tersebut?
    Method is_valid() pada form Django digunakan untuk memvalidasi input yang dimasukkan ke dalam form. Jika form tersebut berisi data yang benar (sesuai dengan aturan validasi yang telah didefinisikan di model atau form), maka method ini akan mengembalikan True, dan data yang valid akan tersedia dalam cleaned_data. Jika ada data yang tidak valid, method ini akan mengembalikan False, dan Django akan otomatis mengisi form dengan pesan kesalahan yang sesuai.

    Terkait alasan mengapa membutuhkan method tersebut adalah untuk memastikan data yang di-submit pengguna sesuai dengan aturan yang kita buat (misalnya, format email yang benar, tidak ada field yang kosong).
    Mencegah injeksi data berbahaya atau input yang tidak sesuai dengan ekspektasi sistem.


4. Mengapa kita membutuhkan csrf_token saat membuat form di Django? Apa yang dapat terjadi jika kita tidak menambahkan csrf_token pada form Django? Bagaimana hal tersebut dapat dimanfaatkan oleh penyerang?
    CSRF (Cross-Site Request Forgery) adalah serangan di mana penyerang dapat membuat pengguna tanpa sadar mengirimkan request ke server yang tampaknya sah. Dengan menambahkan csrf_token pada form, Django membuat token unik yang disertakan di setiap form yang di-submit. Token ini divalidasi oleh server untuk memastikan bahwa request tersebut memang berasal dari pengguna yang sah, bukan dari penyerang.
    Ketika tidak menambahkan csrf_token pada form maka server tidak bisa memverifikasi asal request, sehingga menjadi lebih rentan terhadap serangan CSRF. Penyerang dapat:
    Mengambil alih sesi pengguna dan melakukan tindakan seperti mengirim data tanpa persetujuan.
    Memanfaatkan sesi pengguna untuk mengubah data atau menjalankan aksi yang tidak diinginkan.


5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
    a. Membuat Form dan Model:
    Membuat ProductOrderForm di forms.py dengan menambahkan field untuk email dan phone_number.
    Memastikan model Product di models.py menyimpan informasi produk, termasuk email dan phone_number jika diperlukan.

    b. Membuat Template Form:
    Membuat template order_form.html yang berisi form HTML untuk menerima input dari pengguna, seperti email, phone_number, dan informasi produk.
    Menggunakan {{ form.as_table }} untuk merender form di template.

    c. Mengatur View:
    Menambahkan fungsi order_gpu di views.py untuk menangani permintaan GET dan POST, serta memproses form jika valid.
    Form yang diisi pengguna akan disimpan jika valid.

    d. Routing URL:
    Menambahkan URL pattern di urls.py untuk menampilkan form pemesanan GPU, sehingga pengguna dapat mengakses halaman pemesanan melalui URL /order/.

    e. Testing:
    Menguji apakah form dapat menampilkan dan menerima input dari pengguna dengan benar serta menyimpan data ke dalam database jika diperlukan.

![plot](./xml.png)
![plot](./json.png)
![plot](./xml_id.png)
![plot](./json_id.png)


Tugas 4
1. Apa perbedaan antara HttpResponseRedirect() dan redirect()
HttpResponseRedirect():

Ini adalah kelas respons di Django yang digunakan untuk mengalihkan pengguna ke URL yang ditentukan. Ketika Anda menggunakan HttpResponseRedirect(), Anda harus memberikan URL lengkap sebagai argumennya.

Contoh penggunaannya:
from django.http import HttpResponseRedirect

def my_view(request):
    return HttpResponseRedirect('/some-url/')
redirect():


Ini adalah fungsi yang lebih tinggi dan lebih mudah digunakan. Fungsi ini dapat menerima argumen dalam beberapa bentuk: URL, nama view (name), atau model instance. Jika diberikan nama view, redirect() akan menangani URL reverse untuk Anda.

Contoh penggunaannya:
from django.shortcuts import redirect

def my_view(request):
    return redirect('some_view_name')  # Mengalihkan berdasarkan nama view

2. Jelaskan cara kerja penghubungan model Product dengan User!
Penghubungan model Product dengan User dilakukan dengan menggunakan ForeignKey. Berikut adalah langkah-langkah untuk menghubungkan model:

Mendefinisikan Model:

Tambahkan field ForeignKey pada model Product yang merujuk ke model User.
Contoh definisi model:
from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    name = models.CharField(max_length=100)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)  # Menghubungkan dengan User
    ...
Migrasi Database:

Jalankan perintah makemigrations dan migrate untuk menerapkan perubahan ke database.
Penggunaan di Views:

Ketika produk baru ditambahkan, pastikan untuk menyetel owner produk tersebut ke pengguna yang sedang login.
def add_product(request):
    if request.method == 'POST':
        product = Product(name=request.POST['name'], owner=request.user)
        product.save()

3. Apa perbedaan antara authentication dan authorization, apakah yang dilakukan saat pengguna login? Jelaskan bagaimana Django mengimplementasikan kedua konsep tersebut.
Authentication:
Proses untuk memverifikasi identitas pengguna. Ini biasanya dilakukan melalui login dengan username dan password.
Saat pengguna login, sistem memeriksa kredensial yang dimasukkan dan mengidentifikasi siapa pengguna tersebut.

Authorization:
Proses untuk menentukan apakah pengguna yang telah terautentikasi memiliki izin untuk melakukan tindakan tertentu atau mengakses sumber daya tertentu.
Setelah pengguna berhasil login, sistem akan memeriksa hak akses dan peran pengguna untuk menentukan apa yang dapat mereka lakukan.

1. Apa perbedaan antara HttpResponseRedirect() dan redirect()?
HttpResponseRedirect():

Ini adalah kelas respons di Django yang digunakan untuk mengalihkan pengguna ke URL yang ditentukan. Ketika Anda menggunakan HttpResponseRedirect(), Anda harus memberikan URL lengkap sebagai argumennya.
Contoh penggunaannya:
python

from django.http import HttpResponseRedirect

def my_view(request):
    return HttpResponseRedirect('/some-url/')
redirect():

Ini adalah fungsi yang lebih tinggi dan lebih mudah digunakan. Fungsi ini dapat menerima argumen dalam beberapa bentuk: URL, nama view (name), atau model instance. Jika diberikan nama view, redirect() akan menangani URL reverse untuk Anda.
Contoh penggunaannya:
python

from django.shortcuts import redirect

def my_view(request):
    return redirect('some_view_name')  # Mengalihkan berdasarkan nama view
2. Jelaskan cara kerja penghubungan model Product dengan User!
Penghubungan model Product dengan User dilakukan dengan menggunakan ForeignKey. Berikut adalah langkah-langkah untuk menghubungkan model:

Mendefinisikan Model:

Tambahkan field ForeignKey pada model Product yang merujuk ke model User.
Contoh definisi model:
python

from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    name = models.CharField(max_length=100)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)  # Menghubungkan dengan User
    ...
Migrasi Database:

Jalankan perintah makemigrations dan migrate untuk menerapkan perubahan ke database.
Penggunaan di Views:

Ketika produk baru ditambahkan, pastikan untuk menyetel owner produk tersebut ke pengguna yang sedang login.
python

def add_product(request):
    if request.method == 'POST':
        product = Product(name=request.POST['name'], owner=request.user)
        product.save()
3. Apa perbedaan antara authentication dan authorization?
Authentication:

Proses untuk memverifikasi identitas pengguna. Ini biasanya dilakukan melalui login dengan username dan password.
Saat pengguna login, sistem memeriksa kredensial yang dimasukkan dan mengidentifikasi siapa pengguna tersebut.
Authorization:

Proses untuk menentukan apakah pengguna yang telah terautentikasi memiliki izin untuk melakukan tindakan tertentu atau mengakses sumber daya tertentu.
Setelah pengguna berhasil login, sistem akan memeriksa hak akses dan peran pengguna untuk menentukan apa yang dapat mereka lakukan.

Implementasi di Django:
Django memiliki sistem authentication yang built-in untuk mengelola login/logout dan memverifikasi identitas pengguna, yang dalam kasus ini terdapat fungsi login dan logout yang termasuk dalam built in Django.
Untuk authorization, Django menggunakan sistem permission yang bisa dikonfigurasi pada model dan view yang identik, yang dalam kasus ini, setiap user hanya dapat melihat produk yang ditambahkannya masing - masing.

4. Bagaimana Django mengingat pengguna yang telah login? Jelaskan kegunaan lain dari cookies dan apakah semua cookies aman digunakan?
Django menggunakan sesi untuk mengingat pengguna yang telah login. Ketika pengguna login, Django membuat sesi untuk pengguna tersebut dan menyimpannya di database.

Cookies:
Django menggunakan cookie untuk menyimpan sesi ID. Cookie ini dikirim ke browser pengguna dan digunakan untuk mengidentifikasi sesi saat pengguna melakukan permintaan berikutnya.
Kegunaan lain dari cookies:
Cookies dapat digunakan untuk menyimpan preferensi pengguna, data pelacakan, dan informasi lainnya.
Tidak semua cookies aman. Cookies yang menyimpan informasi sensitif harus diatur dengan pengaturan keamanan yang tepat, seperti HttpOnly dan Secure.

5.Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).

Implementasi Registrasi, Login, dan Logout:
Buat view untuk registrasi, login, dan logout. Gunakan form Django untuk menangani input pengguna.
Gunakan UserCreationForm untuk registrasi dan authenticate() serta login() untuk login.

Buat Dua Akun Pengguna:
Buat dua akun pengguna melalui admin panel Django atau menggunakan shell.
Buat dummy data untuk produk dengan menghubungkan setiap produk ke akun pengguna yang sesuai.

Hubungkan Model Product dengan User:
Tambahkan ForeignKey dari model Product ke model User seperti yang dijelaskan di atas.

Tampilkan Detail Informasi Pengguna yang Login:
Di template, gunakan {% if user.is_authenticated %} untuk menampilkan username pengguna dan informasi lain yang relevan.

Terapkan Cookies untuk Last Login:
Setel cookie di view saat pengguna login, dan ambil nilai cookie di halaman utama.

Menangani Error dan Pengujian:
Uji semua fungsi yang diimplementasikan, termasuk login, logout, dan pengelolaan produk untuk memastikan semuanya berfungsi dengan baik.
![plot](./dummy1.png)
![plot](./dummy2.png)

Tugas 5
1. Jika terdapat beberapa CSS selector untuk suatu elemen HTML, jelaskan urutan prioritas pengambilan CSS selector tersebut!
Inline Style (paling tinggi)
ID Selector (#id)
Class Selector (.class), attribute, dan pseudo-class (:hover, :focus)
Tag Selector (h1, p)


2. Mengapa responsive design menjadi konsep yang penting dalam pengembangan aplikasi web? Berikan contoh aplikasi yang sudah dan belum menerapkan responsive design!
Responsive design memastikan aplikasi dapat diakses dengan baik di berbagai perangkat dengan ukuran layar berbeda. Ini penting karena semakin banyak pengguna mengakses web melalui ponsel.

Contoh yang Menerapkan: Google — tata letak dan elemen seperti tombol beradaptasi dengan ukuran layar.
Contoh yang Tidak Menerapkan: Aplikasi web lama yang hanya dioptimalkan untuk desktop


3. Jelaskan perbedaan antara margin, border, dan padding, serta cara untuk mengimplementasikan ketiga hal tersebut!
Margin: Ruang di luar elemen, digunakan untuk mengatur jarak antara elemen lain.
Border: Garis yang mengelilingi elemen, membatasi konten dari padding dan margin.
Padding: Ruang di dalam elemen antara border dan konten, membuat konten tidak menempel langsung pada border.
Contoh implementasi:
.box {
    margin: 20px;
    padding: 10px;
    border: 2px solid black;
}

4. Jelaskan konsep flex box dan grid layout beserta kegunaannya!
Flexbox: Sistem layout 1 dimensi, berguna untuk mengatur elemen secara row atau column. Contohnya adalah menyusun elemen secara horizontal di navbar.
Grid Layout: Sistem layout 2 dimensi yang lebih fleksibel, berguna untuk membuat layout grid kompleks seperti galeri gambar.
Kegunaan:

Flexbox untuk menyusun elemen sebaris (horizontal atau vertikal).
Grid untuk membuat tata letak lebih kompleks dengan baris dan kolom.

5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial)!
Fungsi Edit dan Delete: Implementasikan view untuk menangani form edit dan logika delete produk.
Kustomisasi Halaman:
Kustomisasi halaman login, register, dan tambah produk dengan Tailwind.
Buat daftar produk dengan card yang menarik, responsif dengan grid.
Navbar Responsif: Implementasikan navbar dengan hamburger menu di mobile, dan tampilan horizontal di desktop.
Penanganan Kondisi Produk Kosong: Tampilkan gambar dan pesan ketika tidak ada produk yang tersimpan.

Tugas 6

1. Jelaskan manfaat dari penggunaan JavaScript dalam pengembangan aplikasi web!
JavaScript adalah bahasa pemrograman yang digunakan untuk membuat aplikasi web interaktif dan dinamis. Berikut adalah beberapa manfaatnya:

- Interaktivitas: JavaScript memungkinkan pengembang untuk menambahkan elemen interaktif, seperti animasi, pemrosesan form secara real-time, dan validasi input tanpa perlu memuat ulang halaman.
- Responsif: Dengan JavaScript, elemen-elemen pada halaman dapat diubah dan diperbarui secara langsung tanpa harus meminta seluruh halaman dari server. Ini meningkatkan responsivitas dan kecepatan aplikasi web.
- Single Page Applications (SPA): Dengan JavaScript, framework seperti React, Vue, dan Angular digunakan untuk membangun SPA, di mana halaman tidak perlu dimuat ulang sepenuhnya ketika pengguna berpindah antar halaman.
- Komunikasi Asynchronous: JavaScript memungkinkan penggunaan AJAX dan Fetch API untuk komunikasi dengan server secara asynchronous, sehingga halaman web dapat mengambil atau mengirim data tanpa perlu memuat ulang halaman secara keseluruhan.
- Manajemen DOM: JavaScript memungkinkan manipulasi elemen DOM (Document Object Model) untuk mengubah, menambah, atau menghapus elemen HTML, memperbarui tampilan secara dinamis sesuai dengan interaksi pengguna.

2. Jelaskan fungsi dari penggunaan await ketika kita menggunakan fetch()! Apa yang akan terjadi jika kita tidak menggunakan await?
await digunakan untuk menunggu hasil dari operasi asinkron seperti fetch() sebelum melanjutkan ke kode berikutnya. Ketika kita menggunakan fetch(), ia mengembalikan Promise, yang menunjukkan bahwa hasil dari operasi tersebut mungkin belum tersedia (asinkron). Dengan menambahkan await, kita memastikan bahwa kita menunggu hingga fetch() selesai (hasilnya tersedia) sebelum melanjutkan ke langkah berikutnya.

Jika kita tidak menggunakan await, maka JavaScript tidak akan menunggu hasil dari fetch(), dan akan langsung melanjutkan eksekusi kode berikutnya. Ini bisa menyebabkan Promise tidak selesai pada saat kita mencoba memproses hasil dari fetch(), sehingga kita mungkin mengakses data yang belum ada atau terjadi kesalahan.

3. Mengapa kita perlu menggunakan decorator csrf_exempt pada view yang akan digunakan untuk AJAX POST?
Django secara default mengaktifkan CSRF (Cross-Site Request Forgery) protection untuk semua permintaan POST. CSRF adalah serangan di mana penyerang dapat memanfaatkan identitas pengguna yang sah untuk mengirim permintaan berbahaya.

Namun, ketika kita mengirim permintaan AJAX POST, CSRF token harus dikirim bersama data permintaan agar permintaan tersebut dianggap sah oleh Django. Jika kita tidak mengirim CSRF token dengan benar atau sengaja ingin mengabaikan perlindungan CSRF (misalnya dalam API atau komunikasi trusted), kita menggunakan csrf_exempt untuk menonaktifkan pemeriksaan CSRF pada view tersebut. Namun, sebaiknya penggunaan csrf_exempt dibatasi hanya pada situasi di mana tidak ada resiko keamanan, seperti API internal.

4. Pada tutorial PBP minggu ini, pembersihan data input pengguna dilakukan di belakang (backend) juga. Mengapa hal tersebut tidak dilakukan di frontend saja?
Meskipun validasi dan pembersihan input di frontend penting untuk pengalaman pengguna yang baik (misalnya, memberikan umpan balik instan), frontend tidak boleh menjadi satu-satunya garis pertahanan. Alasannya:

- Keamanan: Frontend sepenuhnya berada di sisi klien dan dapat dengan mudah dimanipulasi oleh pengguna atau penyerang. Validasi frontend dapat dilewati dengan memodifikasi kode JavaScript di browser atau mengirim permintaan langsung ke server menggunakan alat seperti Postman.
- Konsistensi: Backend adalah tempat terakhir di mana data diproses sebelum masuk ke database. Pembersihan dan validasi data di backend memastikan konsistensi, dan mencegah input yang tidak valid atau berbahaya (seperti XSS, SQL injection) masuk ke sistem.
- Integritas Data: Hanya backend yang dapat berinteraksi langsung dengan database. Jadi, untuk menjaga integritas data, backend harus bertanggung jawab untuk memastikan semua data yang disimpan sudah valid, aman, dan sesuai dengan aturan aplikasi.

5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial)!
AJAX GET: Mengambil Data Produk Milik Pengguna Logged-in
Tujuan: Untuk menampilkan daftar produk milik pengguna yang sedang login secara asinkronus menggunakan AJAX GET, tanpa perlu reload halaman.

Langkah Implementasi:

View untuk AJAX GET: Buatlah sebuah view baru di views.py yang akan mengambil data produk dari database berdasarkan pengguna yang sedang login, lalu mengirimkannya dalam format JSON.

from django.http import JsonResponse
from main.models import Product
from django.contrib.auth.decorators import login_required

@login_required
def get_product_data(request):
    # Mengambil semua produk yang dimiliki oleh user yang login
    products = Product.objects.filter(user=request.user)
    product_data = list(products.values('id', 'name', 'description', 'price', 'quantity'))
    
    return JsonResponse({'products': product_data}, status=200)
JavaScript untuk Mengambil dan Menampilkan Produk: Tambahkan kode JavaScript untuk mengambil data produk dari backend menggunakan fetch() dan menampilkannya pada halaman.

async function fetchProductData() {
    const response = await fetch("/product-data/");
    const data = await response.json();

    let productHTML = '';
    data.products.forEach((product) => {
        productHTML += `
            <div class="card bg-white p-6 rounded-lg shadow-md mb-4">
                <h3 class="text-2xl font-bold">${product.name}</h3>
                <p>${product.description}</p>
                <span class="text-green-600">Rp ${product.price}</span>
                <p>Stock: ${product.quantity}</p>
            </div>
        `;
    });
    document.getElementById('product-list').innerHTML = productHTML;
}

// Panggil fungsi fetchProductData untuk menampilkan produk saat halaman dimuat
fetchProductData();
HTML untuk Menampilkan Produk: Pastikan ada sebuah elemen <div> di halaman tempat data produk akan dimasukkan.


<div id="product-list"></div>
AJAX POST: Menambahkan Produk Baru Menggunakan Modal
Tujuan: Membuat sebuah modal form yang memungkinkan pengguna menambahkan produk baru secara asinkronus. Setelah produk berhasil ditambahkan, modal akan tertutup dan daftar produk diperbarui tanpa reload halaman.

Langkah Implementasi:

View untuk AJAX POST: Buat view di views.py yang akan memproses form penambahan produk dan menyimpannya ke database.

from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse

@csrf_exempt
def create_product_ajax(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description')
        price = request.POST.get('price')
        quantity = request.POST.get('quantity')

        if not name or not description or not price or not quantity:
            return JsonResponse({'error': 'All fields are required'}, status=400)

        product = Product(
            name=name,
            description=description,
            price=price,
            quantity=quantity,
            user=request.user
        )
        product.save()

        return JsonResponse({'message': 'Product added successfully!'}, status=201)
    return JsonResponse({'error': 'Invalid request method'}, status=400)
HTML untuk Modal dan Tombol Tambah Produk: Buat tombol yang akan memunculkan modal form untuk menambahkan produk baru.

<button id="openModalButton" class="bg-indigo-500 text-white p-4 rounded-lg">Add New Product</button>

<div id="productModal" class="hidden fixed inset-0 bg-gray-800 bg-opacity-50 flex items-center justify-center">
    <div class="bg-white p-6 rounded-lg shadow-lg">
        <form id="productForm">
            <label for="name">Product Name:</label>
            <input type="text" id="name" name="name" required>

            <label for="description">Description:</label>
            <textarea id="description" name="description" required></textarea>

            <label for="price">Price (Rp):</label>
            <input type="number" id="price" name="price" required>

            <label for="quantity">Quantity:</label>
            <input type="number" id="quantity" name="quantity" required>

            <button type="submit">Add Product</button>
        </form>
    </div>
</div>
JavaScript untuk AJAX POST: Tambahkan event listener pada form agar dapat menambahkan produk menggunakan AJAX dan menutup modal setelah produk berhasil ditambahkan.

document.getElementById('productForm').addEventListener('submit', async function(event) {
    event.preventDefault();  // Mencegah form submit normal
    
    const formData = new FormData(this);
    const response = await fetch('/create-product-ajax/', {
        method: 'POST',
        body: formData,
    });

    const result = await response.json();
    if (response.status === 201) {
        alert(result.message);  // Tampilkan pesan sukses
        document.getElementById('productForm').reset();  // Reset form
        document.getElementById('productModal').classList.add('hidden');  // Tutup modal
        fetchProductData();  // Refresh data produk
    } else {
        alert(result.error);  // Tampilkan pesan error
    }
});

// Function to show modal
document.getElementById('openModalButton').addEventListener('click', function() {
    document.getElementById('productModal').classList.remove('hidden');
});
Refresh Produk Secara Asinkronus: Setiap kali produk berhasil ditambahkan menggunakan AJAX POST, halaman akan diperbarui dengan fetchProductData() tanpa perlu reload halaman secara keseluruhan.

Step-by-Step Implementasi Checklist:
Menambahkan Produk Secara Asinkronus:

Buat modal dengan tombol "Add New Product" yang memicu form untuk menambahkan produk.
Implementasikan AJAX POST untuk menambahkan produk baru dengan memanggil view yang memproses data produk.
Jika berhasil, modal akan tertutup dan form akan di-reset.
Mengambil Produk Secara Asinkronus:

Buat AJAX GET untuk mengambil data produk dari backend. Data ini hanya diambil untuk produk milik pengguna yang sedang login.
Produk yang berhasil diambil akan ditampilkan di halaman dengan menambahkan elemen HTML baru.
Validasi dan Error Handling:

Jika ada field yang kosong, tampilkan pesan error di frontend dengan menampilkan alert atau pesan kesalahan.
Validasi juga dilakukan di backend dengan view create_product_ajax() untuk memastikan input produk valid.
Aspek Desain dan UX:

Modal yang muncul memberikan UX yang baik karena pengguna tidak perlu reload halaman.
Pengguna mendapatkan notifikasi langsung apakah penambahan produk berhasil atau tidak.