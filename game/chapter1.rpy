label chapter1_start:

    play music "audio/BACKSOUNDKKC.mp3" volume 0.1

    scene bg BLACK
    show text "{color=#ff0000}{size=200}KEESOKAN HARINYA{/size}{/color}" at game_over_pos

    scene bg kamartidurkarakteru

    "keesokan harinya"

    play sound "alarm.mp3"

    "kring....kring....kring"

    stop sound

    t "hmm.....?"

    play sound "alarm.mp3"

    "kringg...kringg...kringg"

    stop sound

    show taishiro outing angry at zoom_taishiro

    t "AHHH, SIAL BERISIK BANGET SIH NIH JAM"

    hide taishiro outing angry

    "lu melihat sekarang sudah jam berapa"

    show taishiro schoolwinter surprised at zoom_taishiro

    t "astaga, gw telat bangun! udah jam 06:50 mana sekolah masuk jam 07:00 belum diperjalanan 15 menit, gw harus buru-buru siap-siap ke sekolah bisa dihukun yang ada!"

    scene bg BLACK
    show text "{color=#ff0000}{size=200}SESAMPAINYA DISEKOLAH{/size}{/color}" at game_over_pos

    scene bg sekolahgrtutup

    "sesampainya di sekolah"

    show taishiro schoolwinter happy at zoom_taishiro

    t "hufft... akhirnya sampai juga di sekolah"

    hide taishiro schoolwinter happy

    "lu melihat gerbang sekolah"

    show taishiro schoolwinter angry at zoom_taishiro

    t "ahhh sial, gerbang sekolah udah ditutup lagi!"

    t "gara gara begadang main game nih"

    menu :
        "mencoba masuk lewat gerbang belakang":
            t "mungkin gw bisa coba masuk lewat gerbang belakang, jalan andalan gw semoga aja gak ketemu penjaga"
            jump good_ending1
        


        "mencoba berbicara dengan satpam":
            hide taishiro schoolwinter happy at zoom_taishiro
            t "mungkin gw bisa coba bicara sama satpamnya"
            show moi grin at zoom_satpam
            hide taishiro schoolwinter happy at zoom_taishiro
            s "hei nak, gerbang sekolah sudah ditutup. kamu terlambat ya?"
            show taishiro schoolwinter happy at zoom_taishiro
            hide moi grin at zoom_satpam
            t "iya pak, maaf saya telat. apakah saya masih boleh masuk?"
            show moi grin at zoom_satpam
            hide taishiro schoolwinter happy at zoom_taishiro
            s "pulanglah kamu, sudah telat. besok jangan sampai terlambat lagi ya"
            show taishiro schoolwinter sad at zoom_taishiro
            hide moi grin at zoom_satpam
            t "t-t-tapi pak, saya harus masuk ke kelas"
            show moi grin at zoom_satpam
            hide taishiro schoolwinter sad at zoom_taishiro
            s "maaf nak, peraturan sudah jelas. kamu harus pulang"
            hide moi grin at zoom_satpam
            jump game_over1

label game_over1:
    scene bg BLACK
    with fade
    stop music
    play music "audio/marioGV.ogg" volume 1.0 noloop
    show text "{color=#ff0000}{size=200}GAME OVER{/size}{/color}" at game_over_pos
    n "ppppfffttttt"
    n "telat langsung disuruh pulang ya? kasian amat manusia satu ini"
    n "logika kids, yakali satpam bolehin lu masuk wkwkwk"
    n "jadiin pelajaran juga ya, disiplin itu penting, apalagi di sekolah mangkanya jangan begadang main game"
    n "jadiin pelajaran biar gak telat, NT"
    menu:
        "Memulai Ulang (Restart)":
            jump start
        "Kembali ke Lobby (Main Menu)":
            return
    with fade

label good_ending1:

    scene bg tanggakelas
    with fade
    show taishiro schoolwinter happy at zoom_taishiro

    t "gw harus buru buru nih sebelum ketuan guru/penjaga"

    hide taishiro schoolwinter happy

    "setelah melewati tembok belakang lu jalan pelan pelan agar tidak ketauan guru/penjaga yang sedang keliling dan setelah merasa aman di lorong sekolah lo lari sekuat tenaga menuju kelas"

    "dan lopun berhasil"

    show taishiro schoolwinter happy at zoom_taishiro

    t "yes, kayaknya gak ketuan deh"

    hide taishiro schoolwinter happy

    "lu berlari sekuat tenaga menuju kelas lu"

    "setibanya di depan kelas lu"

    scene bg gerbangkelas
    with fade

    play sound "audio/door_bang.wav"

    scene bg gerbangkelas at bg_shake

    show text "{size=80}{b}BRAKK!!{/b}{/size}" at text_shake
    with dissolve

    pause 0.4

    hide text

    "Pintu kelas dibuka dengan sedikit kencang."

    "murid-murid di kelas menoleh ke arah lu yang baru masuk"

    "lu ngos ngosan mencoba ngambil nafas"

    "lu mencoba melihat kedepan setelah tadi lu stabilin nafas"

    "dan yang terjadi....."

    "ya gurunya sudah datang dan melihat lu dengan tatapan seekor pemburu yang ingin menerkam mangsanya"
    
    show taishiro schoolwinter surprised at zoom_taishiro
    with dissolve

    t "(mati gw....)"
    t "a-a-nu pak... maaf pak saya telat"

    show taishiro schoolwinter happy at zoom_taishiro
    with dissolve

    show mod frown at zoom_guru
    hide taishiro schoolsummer happy at zoom_taishiro

    g "kamu telat lagi Kenzo, ini sudah yang ketiga kalinya"

    show taishiro schoolwinter sad at zoom_taishiro
    hide mod frown at zoom_guru

    t "maaf banget pak"

    hide taishiro schoolwinter at zoom_taishiro

    "akhirnya lu memutuskan untuk mengangkat kepala"

    "secara otomatis mata lu melihat kedepan"

    "setelah melihat kedepan ternyata lu ngeliat gadis yang berdiri di depan menghadap murid kelas"

    "jelasss, lu sedikit terkejut karena melihat gadis itu"
    
    show taishiro schoolwinter surprised at zoom_taishiro

    t "(kok gw gak liat tadi ada cewek disamping pak agus dah. Eh bentar.....)"

    t "loh , lukan cewek yang kemarin"

    "lo melihat gadis itu dengan tatapan terkejut"

    show alice_worried at zoom_alice
    hide taishiro schoolwinter surprised at zoom_taishiro

    l "loh lu cowok yang kemarin bantuin gw nyari kucing"

    hide alice_worried at zoom_alice 

    "diapun sama terkejutnya melihat shiro"

    show mod frown at zoom_guru

    g "loh kalian udah pernah ketemu?"

    hide mod frown 

    "mereka berdua serentak jawab iya"

    show mod frown at zoom_guru

    g "oke bagus dan cukup kenalannya, Ken kali ini saya maafkan, tapi kalau kamu ngulang lagi kamu akan diberikan surat peringatan"

    hide mod frown 
    show taishiro schoolwinter happy at zoom_taishiro

    t "wah makasih banyak pak, saya janji gak akan telat lagi"
    
    hide taishiro schoolwinter normal
    show mod frown at zoom_guru

    g "iya, silahkan kamu duduk. Untuk kamu lisa silahkan duduk dibelakang"
    
    hide mod frown
    show alice_happy at zoom_alice

    l "baik pak"
    
    hide Alice_Happy 

    scene bg kelas
    with fade

    "waktu istirahatpun tiba"

    "anak anak kelas terutama cowok langsung ngerumunin anak baru itu"

    show taishiro schoolwinter surprised at zoom_taishiro

    t "(buset cowok cowok langsung pada nerkam semua kek nemu mangsa aja jir, mentang mentang ada bidadari nyasar ke kelas ini)"

    t "(mana cogan cogan dari kelas lain banyak yang ngumpul lagi, hffttt orang kaya gw yang muka standar kalau ikut join yang ada kayak monyet penasaran"

    hide taishiro schoolwinter surprised
    "saat lu ingin pergi ke rooftop lu ngerasa kalau anak baru itu seperti merasa risih karena di kerumunin banyak orang terutama cowok buaya"

    menu :
        "ikut ngerumunin anak baru itu" :
            show taishiro schoolwinter happy at zoom_taishiro
            t "apa gua ikut ngumpul ya?" 
            t "ikut ajalah, siapa tau bisa lebih deket"
            jump game_over2

        "langsung menuju rooftop sekolah dan ninggalin tuh cewek" :
            show taishiro schoolwinter pout at zoom_taishiro
            t "ahh bodoamatlah, mending ke rooftop gw"
            jump game_over3

        "bantu ngeluarin dia dari kerumunan"  :
            show taishiro schoolwinter happy at zoom_taishiro           
            t "(hmmmm, kalau ditinggal kasian juga)"
            hide taishiro schoolwinter happy
            "lu menuju ke arah kerumunan tersebut"
            show taishiro schoolwinter happy at zoom_taishiro
            t "misi...permisi, numpang lewat mas mbak"
            hide taishiro schoolwinter happy
            "orang orang jadi ngeliat termasuk anak baru itu"
            "dan ternyata salah satu cogan disitu ngatain lu cuman jadi pengganggu aja"
            "mungkin karena muka lu yang standar lu gak cocok ikut ngerumpi"
            show taishiro schoolwinter angry at zoom_taishiro
            t "(APASIH, nih orang ribet banget ya gw tau muka gw gak jauh kayak beruk tapi peka dong itu dia ngerasa risih)"
            hide taishiro schoolwinter angry
            "gumam lu dalam hati"
            show alice_worried at zoom_alice
            ".........."
            hide alice_worried
            show taishiro schoolwinter happy at zoom_taishiro
            t "eh mau ngasih info doang, lu tadi dipanggil pak agus"
            hide taishiro schoolwinter happy
            show alice_worried at zoom_alice
            l "gw dipanggil? ada apa?"
            hide alice_worried
            show taishiro schoolwinter happy at zoom_taishiro
            t "gak tau, sini gw anterin ke pak agus"
            "dan orang orang disekitarnya sedikit mengeluh terutama para BUAYA"
            jump good_ending2

label game_over2:
    scene bg BLACK
    with fade
    stop music
    play music "audio/marioGV.ogg" volume 1.0 noloop
    show text "{color=#ff0000}{size=200}GAME OVER{/size}{/color}" at game_over_pos
    n "yahhh si bro kepoan mana bilangnya mau lebih deket wkwwk, sadar diri bos muka lu aja pas pasan"
    n "btw punya kaca? ngaca dulu sana. Lu ikut malah bikin runyam bukannya deket"
    n "udah tau dia ngerasa risih di kerumunan, malah ngikut nimbrung"
    n "hadehhh peka dikit, NT dah"
    menu:
        "Memulai Ulang (Restart)":
            jump start
        "Kembali ke Lobby (Main Menu)":
            return
    with fade

label game_over3:
    scene bg BLACK
    with fade
    stop music
    play music "audio/marioGV.ogg" volume 1.0 noloop
    show text "{color=#ff0000}{size=200}GAME OVER{/size}{/color}" at game_over_pos
    "gila si bro anti sosial, pasti orang cool dan gak peduli apa yang terjadi disekitar"
    "peka dikitlah jadi cowok, aduh"
    "gak usah sok cuek pantes jomblo, lu aja orangnya gak peduli sekitar gimana mau dapet cewek"
    "makan tuh kata when yah setiap hari, NT"
    menu:
        "Memulai Ulang (Restart)":
            jump start
        "Kembali ke Lobby (Main Menu)":
            return
    with fade

label good_ending2 :
    scene bg gerbangkelas
    with fade
    "merekapun keluar dari kelas"

    scene bg lorongkelas
    with fade

    "mereka sedang jalan santai di lorong kelas"

    show alice_worried at zoom_alice
    
    l "emang pak agus tadi manggil gw?"

    hide alice_worried
    show taishiro schoolwinter happy at zoom_taishiro
    
    t "gak kok, gw cuman bohong tadi"

    hide taishiro schoolwinter happy
    show alice_worried at zoom_alice

    l "lah, berarti lu ngebohong tadi?"

    hide alice_worried
    show taishiro schoolwinter happy at zoom_taishiro
    
    t "ya"

    show alice_worried at zoom_alice
    hide taishiro schoolwinter happy

    l "kok gitu, kenapa?"

    hide alice_worried
    show taishiro schoolwinter happy at zoom_taishiro

    t "lu ngerasa risihkan dikerumunin banyak orang apalagi banyak cowok"

    show alice_worried at zoom_alice
    hide taishiro schoolwinter happy

    l "........."

    l "eh, kok lu bisa tau?"

    hide alice_worried
    show taishiro schoolwinter happy at zoom_taishiro

    t "cuman sekedar firasat doang"
    
    show alice_worried at zoom_alice
    hide taishiro schoolwinter happy

    l "........."

    hide alice_worried
    show alice_happy at zoom_alice

    l "........."

    hide alice_happy
    show taishiro schoolwinter blush at zoom_taishiro

    t "(jirlah....pantesan dikerumunin buaya lapar, emang sasaran segar nih orang)"

    hide taishiro schoolwinter blush
    "yaa lu secara gak langsung ngatain dia cantik"
    "tapi tanpa lu sadari banyak orang yang natap lu berdua"
    "lebih tepatnya sih natap cewek samping lu"
    "siapa juga yang mau natap lo"
    "dan lo ternyata denger obrolan mereka walaupun suarany kecil tapi itu menghinalu, karena orang sebiasa kek lu bisa jalan berdua sama primadona sekolah"
    "yang parahnya lagi lu sampe dikatain KODOK ZUMA"

    show taishiro schoolwinter angry at zoom_taishiro
    t "(sialan tuh orang, muka gw dikatain mirip KODOK ZUMA)"

    hide taishiro schoolwinter angry

    "lu mencoba untuk menghiraukan dan lanjut ngobrol dengan anak pindahan yang langsung jadi primadona sekolah"
    "dan lu baru inget, kalau niat lu tadinya ke rooftop sekolah buat istirahat dan nikmatin pemandangan"

    show taishiro schoolwinter happy at zoom_taishiro

    t "(lah iya, tadikan gw mau ke rooftop tapi apa ke kantin ya?)"

    menu :
        "ajak dia ke rooftop" :
            show taishiro schoolwinter happy at zoom_taishiro
            t "lu mau ikut gw rooftop sekolah gak?"
            t "disana enak kalau buat liat pemandangan dari atas sama tempatnya juga sejuk"
            hide taishiro schoolwinter happy
            show alice_worried at zoom_alice
            l "hmmm, boleh deh"
            hide alice_worried
            jump good_ending3

        "ke rooftop tanpa ajak dia" :
            show taishiro schoolwinter happy at zoom_taishiro
            t "eh gw lupa gw mau pergi ke rooftop dulu ya, lu ke kelas lagi aja dulu"
            hide taishiro schoolwinter happy
            show alice_worried at zoom_alice
            l "ehh, gw bol-"
            hide alice_worried
            show alice_doubt at zoom_alice
            l "......"
            hide alice_doubt
            "lu malah ngacir ninggalin dia"
            jump game_over4

        "ke kantin bareng dia" :
            show taishiro schoolwinter happy at zoom_taishiro
            t "mau ke kantin gak?"
            hide taishiro schoolwinter happy
            show alice_worried at zoom_alice
            l "boleh"
            hide alice_worried
            "saat dikantin"
            show taishiro schoolwinter happy at zoom_taishiro
            t "(woilah, rame banget nih kantin kek lagi demo aja)"
            t "(bentar... kok gak ada suaranya ya si primadona itu)"
            hide taishiro schoolwinter happy
            show taishiro schoolwinter surprised at zoom_taishiro
            t "........"
            hide taishiro schoolwinter surprised
            "saat lu nengok ke murid baru itu, ternyata dia udah dikepung sama anak anak kelas lain yang penasaran dengannya terutama cowok nakal yang sering bolos kelas"
            jump game_over5


label game_over4:
    scene bg BLACK
    with fade
    stop music
    play music "audio/marioGV.ogg" volume 1.0 noloop
    show text "{color=#ff0000}{size=200}GAME OVER{/size}{/color}" at game_over_pos
    n "kelazzz king malah ditinggalin wkwkwk"
    n "kalau lu lagi bareng cewek jangan langsung main ninggalin ya kids apalagi itu murid baru yang langsung jadi primadona sekolah"
    n "lu sebagai cowok mumpung bareng dia setidaknya lindungi dari keramaian agar gak dikepung buaya kelaparan lagi"
    n "kan lu tau dia aja tadi risih dideketin banyak cowok"
    n "lain kali jangan gitu ya kids kan ngambek jadinya dia ke lu malah berujung ilfeel, NT dah jones"
    menu:
        "Memulai Ulang (Restart)":
            jump start
        "Kembali ke Lobby (Main Menu)":
            return
    with fade

label game_over5:
    scene bg BLACK
    with fade
    stop music
    play music "audio/marioGV.ogg" volume 1.0 noloop
    show text "{color=#ff0000}{size=200}GAME OVER{/size}{/color}" at game_over_pos
    n "hmmm bagus sih ajak ke kantin sekalian study tour sekolah, tapi diakan murid baru yang langsung terkenal karena kecantikannya"
    n "dalam beberapa jam aja dia udah jadi bahan perbincangan satu sekolah"
    n "lu malah bawa ke kumpulan monyet monyet yang sering bolos kelas buat ke kantin"
    n "kali ini jawaban tidak terlalu salah tapi mikir kondisi kids, NT"
    menu:
        "Memulai Ulang (Restart)":
            jump start
        "Kembali ke Lobby (Main Menu)":
            return
    with fade

label good_ending3 :

    scene bg rooftop
    with fade

    show taishiro schoolwinter happy at zoom_taishiro
    t "nah disini tempat favorit gw, yaaa biasanya gw sering kesini nuat habisin waktu pas jam istirahat aja"
    
    hide taishiro schoolwinter happy
    show alice_worried at zoom_alice

    l "wah, bagus juga ya pemandangan dari atas sama sejuk juga kalau disini"

    show taishiro schoolwinter happy at zoom_taishiro
    hide alice_worried
    t "ya begitulah"

    hide taishiro schoolwinter happy
    show taishiro schoolwinter surprised at zoom_taishiro

    t "(eh bentar, gw baru inget kalau gw belum tau namanya)"

    t "oh iya kita belum kenalan ya?"

    hide taishiro schoolwinter surprised
    show alice_worried at zoom_alice

    l "eh iya namalu siapa?"

    show taishiro schoolwinter happy at zoom_taishiro
    hide alice_worried

    t "kenalin nama gw Kenzo panggil aja ken, namalu?"

    hide taishiro schoolwinter happy
    show alice_worried at zoom_alice

    l "oh, nama gw Alisa panggil aja Lisa, salken"
    
    show taishiro schoolwinter happy at zoom_taishiro
    hide alice_worried

    t "salken juga"

    t "btw lu pindahan darimana?"
    
    hide taishiro schoolwinter happy
    show alice_worried at zoom_alice

    l "oh gw pindahan dari sekolah SMA seirin di Jepang"

    show taishiro schoolwinter surprised at zoom_taishiro
    hide alice_worried

    t "hah? Jepang? lu tinggal di Jepang?"

    hide taishiro schoolwinter happy
    show alice_worried at zoom_alice

    l "ya dari lahir gw tinggal di Jepang soalnya ibu gw asli Jepang"

    show taishiro schoolwinter happy at zoom_taishiro
    hide alice_worried

    t "(hmmmm pantes, turunan orang jepang)"

    t "tapi lu kok mahir bahasa indonesia apalagi bahasa gaul di Jakarta?"

    hide taishiro schoolwinter happy
    show alice_worried at zoom_alice

    l "haha iya, soalnya gw pas SD kelas 1 sampai 6 tinggal di Indonesia sama gw juga diajarin sama ayah gw bahasa indo sama bahasa gaulnya juga diajarin jadi lancar deh"

    l "ayah gw juga lahir di Jakarta"

    show taishiro schoolwinter happy at zoom_taishiro
    hide alice_worried

    t "owalah, pantes lancar"
    
    hide taishiro schoolwinter happy

    "merekapun berbincang bincang sampe jam istirahat selesai"

    "setelah bel berbunyi mereka berdua menuju kelas lagi dan belajar sampai bel pulang"

    $ persistent.chapter_completed = max(persistent.chapter_completed, 2)
    jump chapter_menu
