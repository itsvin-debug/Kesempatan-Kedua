label chapter1_start:

    play music "audio/BACKSOUNDKKC.mp3" volume 0.1

    "setelah sampai disekolah, lu parkir terlebih dahulu motornya dan mulai memasuki gerbang sekolah"

    "Rio berjalan dengan muka yang sangat bahagia"

    "saat sedang asik jalan jalan tiba tiba...."

    "PLAKKK"

    "ada yang memukul pundak Rio dari belakang"

    r "eh-"

    "lu merasa tidak asing dengan tepukan itu"

    "saat lu menoleh kebelakang"

    "ada seorang pria yang tidak asing dikehidupanlu, ya itu sahabat lu sendiri yang bernama Kael"

    k "gilee, kita satu sekolah lagi nih"

    r "ya"

    "Tanpa lu sadari muka lu tersenyum bahagia karena bisa lihat sahabat lu lagi"

    k "dih stress lu ya? senyum sendiri gitu kek orang gila atau jangan jangan lu suka gu-"

    r "NAJIS GAKLAH GILA"

    k "hahaha gua kira lu belok"

    k "tapi kenapa lu senyum senyum gitu?"

    r "akhirnya gua bisa liat lu lagi"

    k "maksudnya?"

    "Kael bertanya dengan wajah yang sedikit aneh"

    r "gapapa lupain aja, buru ah kedalem nanti telat kita"

    "akhiirnya lu berdua lari ke sekolah itu"

    o "CEPET DONG LAMA BANGET YANG TELAT AKAN DIHUKUM PUSH UP SERATUS KALI!!!"

    "muka osis itu terlihat sok garang dan suara yang sok tegar"

    k "eh yo, liat deh tuh muka osis sok garang banget. bro berpikir sedang farming aura hahaha"

    "Kael mengejek osis itu namun dia tidak sadar kalau suaranya sangat keras"

    r "woi suara lu keras beg-"

    o "WOI KALIAN BERDUA!!"

    "sebelum menyelesaikan pembicaraan osis itu menunjuk lu berdua.."

    "ternyata pendengaran osis itu sungguh tajam"

    o "KALIAN BERDUA NGEJEK SAYA YA TADI?"

    k "eh-"

    r "eh engg-"

    "lu panik tapi lu mencoba untuk menjawab"

    r "eh engga bang kita cuman ngobrol biasa"

    o "GAK USAH BOHONG LU PIKIR KUPING GUA TULI? CEPET LU BERDUA KESINI!!"  

    r "LAH KITAKAN GAK NGAPA NGAPAIN KOK KEDEPAN?"

    o "OH LU BERANI NGELAWAN? UDAH SOK JAGO LU SAMPE BERANI GINI?"

    "karena lu kepancing emosi lu langsung adu bacot dengan osis itu, namun hal itu adalah kesalahan terbesar"

    "sekarang lu malah jadi pusat perhatian publik"

    "namun tiba tiba..."

    r "eh?"

    "lu balik ke masa sebelum kejadian lu ribut ama osis tersebut, lu masih bingung dan juga kaget kalau diri kenapa bisa balik ke masa itu"

    o "WOI SINI LU BERDUA MAJU KE DEPAN!!"

    "lu masih mematung diam karena kejadian aneh tersebut"

    o "WOI JANGAN MELAMUN LU"

    r "eh?"

    k "eh yo kok ngelamun sih"

    o "WOI LU ITU YANG NGELAMUN"

    r "ya bang?"

    o "MAJU SINI MALAH BENGONG LU"

    r "loh kenapa maju kan kita gak ngapa ngapain?"

    o "Oh gitu ya?"

    "muka osis itu terlihat marah"

    o "YA SUDAH KALAU GITU!"

    "sebelum lu sempat menjawab osis itu malah menarik tangan lu dan mendorongnya"

    r "ADUH!"

    r "APASIH LU BANG RESE BANGET"

    o "OH BERANI LAWAN YA?"

    "muka osis itu terlihat tambah marah"

    o "BERANI LU SAMA GUA?"

    "muka lu terlihat bingung karena tidak mengerti maksud osis tersebut"

    r "hah?"

    o "UDAH SOK JAGO LU SAMPE BERANI GINI?!"

    "lu yang gak tahan akhirnya kepancing emosi"

    r "APA LU BILANG? LU YANG SOK JAGO DISINI!!"

    o "WAH BERANI NIH ORANG"

    "akhirnya lu berdua ribut dan menjadi tontonan publik"

    "namun....."

    "..."

    "dan ya lu balik lagi ke masa sebelum kejadian lu debat ama osis itu"

    "Lu heran kenapa bisa balik lagi ke waktu itu tanpa lu sadari dan lu mulai mencerna dan membuat kesimpulan liar. Apakah kalau lu gagal dalam suatu hal lu bakal kembali ke waktu itu untuk membuat suatu hal itu menjadi berhasil atau tidak? Karena penasaran lu mencoba nya lagi"

    "karena penasaran lu mencoba cari ribut lagi dengan osis itu, dan ya hasilnya sama aja lu gagal lagi dan balik lagi ke waktu itu"

    "dan kesimpulan liar lu itu benar ternyata"

    o "WOI CEPET SINI MALAH MELAMUN"

    "lu penasaran apa yang terjadi jika diri lu maju ke depan, akhirnya lu memutuskan untung maju ke depan"

    r "ya bang?"

    o "PUSH UP SEKARANG LU BERDUA SEBANYAK 30 KALI"

    r "lah?"

    menu:

        "menolak perintah osis tersebut":
            
            r "lah ngapain push up? kita salah apa?"

            o "BANYAK ALESAN CEPET KERJAIN"

            r "APASIH KITA KAN GAK NGAPA NGAPAIN KOK DISURUH PUSH UP?"

            o "OH UDAH BERANI NGEBOHONG NIH?"

            r "GAK NGEBOHONG LU JUGA DARI TADI NYARI RIBUT"

            o "WAH BERANI BANGET NIH ORANG"

            "akhirnya lu debat lagi dengan osis tersebut karena lu nolak hukuman push up"
            jump game_over1

        "ikutin perintah osis itu":
            
            r "ya bang"

            k "eh yo gimana ini?"

            r "udah ikutin aja"

            "akhirnya lu berdua ngelakuin apa yang osis tadi suruh"

            jump good_ending1

label game_over1:
    scene bg BLACK
    with fade
    play sound "marioGV.mp3"
    show text "{color=#ff0000}{size=200}GAME OVER{/size}{/color}" at game_over_pos
    n "waduh bro jangan ribut ama osis mending kita turutin aja apa yang dia suruh, jangan keras kepala nanti alhasil lu malah ribut lagi"
    menu:
        "Memulai Ulang (Restart)":
            jump start
        "Kembali ke Lobby (Main Menu)":
            return
    with fade

label good_ending1:

    "walaupun lu menjadi pusat perhatian karena di hukum akhirnya lu berhasil menyelesaikan hukumannya dan lu disuruh baris ke belakang oleh osis itu"

    k "ck, sialan banget tuh osis"

    r "lu sendiri yang ngejek dia dongo"

    k "ya masa kedengeran sih"

    r "ya kedengeran lah dongo lu suaranya berisik tadi sama kita tadi baris di depan"

    "akhirnya setelah selesai lu sekarang pembagian gugus dan lu berdua sekelas lagi"

    r "yah gila udah satu sekolah sekarang satu gugus lagi, heran dah gua"

    k "sama gua juga heran, takdir kali bareng my sahabat mana duduknya sebelahan lagi"

    r "huekk cuh, sahabat macam apa ini yang buat sahabatnya sendiri kena hukum"

    k "ya itu mah osisnya aja yang gak jelas"

    r "ah lu samanya jugalah"

    "setelah lama lama berbincang akhirnya pebimbing gugus lu datang"

    "dan apesnya pebimbing lu osis yang tadi"

    k "yahh- kok dia sih"

    r "..."

    o "oke kalian semua diam dulu, gua ama temen gua mau kenalin diri cuman temen gua ini masih belum kesini kemungkinan nanti dia nyusul"

    o "kenalin nama gua haikal haraka, gua pebimbing gugus ini yaitu gugus 3"

    k "ah bodoamat nama lu siapa kek"

    "lu ngedenger suara samar - samar kalau beruk sebelah lu lagi bergumam"

    o "nah sekarang coba kalian kenalin diri satu - satu mulai tinggal dimana, dari smp apa, dan alasan kalian masuk sini. Mulai dari meja depan pojok kanan"

    "mereka mulai memperkenalkan diri satu - satu "

    "tanpa lu sadari sekarang beruk sebelah lu yang mulai perkenalan diri"

    k "e-e-e-e kenalin nama gua Kael.."

    "Lu gak peduli tapi ada satu hal yang mengganjal"

    "yaitu muka osis itu terlihat sinis dan seperti tersenyum tipis seperti memiliki rencana jahat"

    r "wah sial, nih osis dendam kayaknya"

    "sekarang giliran lu perkenalan diri. Lu mulai ngenalin diri seperti biasa namun setelah selesai mengenalkan diri..."

    o "oh namanya Kael dan rio"

    "walaupun nada osis itu pelan tapi lu ngedenger yang dia bicarain"

    k "eh yo, kayaknya tuh osis dendam deh ama kita"

    r "ya gua juga tau"

    "namun di tengah sesi perkenalan tiba - tiba"

    c "permisi, boleh saya masuk?"

    o "...."

    o "boleh"

    "akhirnya osis kedua itu masuk ruangan"

    "betapa kagetnya kalau osis kedua itu ternyata cewek cantik"

    "dan beruk sebelah lu jelas kayak cacing kepanasan"

    k "woi yo, gile tuh kakak kelas cantik amat jir. Apakah ini my bini gue?"

    r "stress lu setiap ketemu cewek cantik pasti kek gini"

    k "jelaslah masa lu gak tertarik? jangan jangan lu sukanya cow-"

    "lu megang pundak Kael"

    r "denger baik - baik ya sat, gua ini masih suka cewek gua gak tertarik bukan berarti gua belok. Mending lu sadar diri dah kalau lu di depan cermin yang keluar bukan manusia tapi bekantan"

    k "wah sialan lu asu, mana ada sesama ras saling ngatain hahaha"

    r "hahaha"

    i "WOI LU BERDUA BERISIK BANGET SIH DARI TADI!!"

    
