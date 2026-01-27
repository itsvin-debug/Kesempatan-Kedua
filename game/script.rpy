# Data chapter: list of dicts dengan title, description, dan image untuk setiap chapter
define chapters = [
    {
        "title": "Chapter 1: Pertemuan Pertama",
        "description": "tahun kemarin tahun yang membosankan. Namun, tahun ini ada sesuatu yang merubah hidup lo dan pertemuan pertama yang akan mengubah nasib lo yang membosankan.",
        "image": "images/bg/apartment a exterior day.png"
    },
    {
        "title": "Chapter 2: kesialan yang mengejutkan",
        "description": "di hari ini lu ngalamin sial yaitu telat bangun, lu bergegas berangkat sekolah namun ada hal yang tak terduga",
        "image": "images/chapter2.png"
    },
    {
        "title": "Chapter 3: the first step in yor life",
        "description": "langkah awal yang akan mengubah hidup lo kedepannya",
        "image": "images/chapter3.png"
    },
    {
        "title": "Chapter 4: the last day",
        "description": "setelah lu nganterin dia, lu bergegas untuk berangkat ekskul dan menghabiskan hari ini. Apakah besok hari lo berubah?",
        "image": "images/chapter4.png"
    },
    {
        "title": "Chapter 5: coming soon",
        "description": "-",
    },
    {
        "title": "Chapter 6: coming soon",
        "description": "-",
    },
    {
        "title": "Chapter 7: coming soon",
        "description": "-",
    },
    {
        "title": "Chapter 8: coming soon",
        "description": "-",   
    },
    {
    
        "title": "Chapter 9: coming soon",
        "description": "-",
    },
]

    # Tambahkan chapter lainnya sesuai kebutuhan cerita, dengan image masing-masing

# Variabel persistent untuk melacak chapter yang telah selesai (0 = belum ada, 1 = chapter 1 selesai, dst.)
default persistent.chapter_completed = 0

# Label baru untuk menu chapter, agar bisa di-jump dari akhir chapter
label chapter_menu:
    call screen chapter_slots(_("Chapter"))
    return

# Sekarang, modifikasi layar load untuk menampilkan sebagai chapter
screen load():
    tag menu
    use chapter_slots(_("Chapter"))

# Layar baru untuk chapter slots, berdasarkan file_slots tapi disesuaikan
screen chapter_slots(title):
    default page_name_value = FilePageNameInputValue(pattern=_("Halaman {}"), auto=_("Otomatis save"), quick=_("Save cepat"))

    use game_menu(title):
        fixed:
            order_reverse True

            # Nama halaman (opsional, bisa dihapus jika tidak perlu)
            button:
                style "page_label"
                key_events True
                xalign 0.5
                action page_name_value.Toggle()
                input:
                    style "page_label_text"
                    value page_name_value

            # Grid untuk chapter slots
            grid gui.file_slot_cols gui.file_slot_rows:
                style_prefix "slot"
                xalign 0.5
                yalign 0.5
                spacing gui.slot_spacing

                for i in range(gui.file_slot_cols * gui.file_slot_rows):
                    $ slot = i + 1
                    $ chapter_index = slot - 1  # Index dimulai dari 0
                    $ is_unlocked = chapter_index <= persistent.chapter_completed
                    $ chapter_data = chapters[chapter_index] if chapter_index < len(chapters) else {"title": "Chapter {}".format(slot), "description": "Belum tersedia.", "image": "default_chapter.png"}

                    button:
                        # Jika unlocked, action jump ke label chapter; jika locked, tidak ada action
                        if is_unlocked:
                            action Jump("chapter{}_start".format(slot))
                        else:
                            action None

                        has vbox

                        # Jika unlocked, tampilkan gambar chapter statis; jika locked, tampilkan gambar kunci
                        if is_unlocked:
                            add chapter_data["image"] xalign 0.5 yalign 0.5
                        else:
                            add "gui/lock_icon.png" xalign 0.5 yalign 0.5  # Pastikan ada gambar lock_icon.png di folder gui

                        # Judul chapter
                        text chapter_data["title"]:
                            style "slot_name_text"
                            if not is_unlocked:
                                color "#666666"  # Warna abu-abu jika locked

                        # Deskripsi singkat
                        text chapter_data["description"]:
                            style "slot_time_text"
                            if not is_unlocked:
                                color "#666666"

                        # Jika locked, tambahkan overlay hitam transparan
                        if not is_unlocked:
                            add Solid("#00000080")  # Hitam dengan alpha 50%

                        key "save_delete" action FileDelete(slot)

            # Tombol navigasi halaman (opsional, jika ada banyak chapter)
            vbox:
                style_prefix "page"
                xalign 0.5
                yalign 1.0

                hbox:
                    xalign 0.5
                    spacing gui.page_spacing

                    textbutton _("<") action FilePagePrevious()
                    if config.has_autosave:
                        textbutton _("{#auto_page}O") action FilePage("auto")
                    if config.has_quicksave:
                        textbutton _("{#quick_page}C") action FilePage("quick")
                    for page in range(1, 10):
                        textbutton "[page]" action FilePage(page)
                    textbutton _(">") action FilePageNext()

init python:
    def typewriter_callback(event, **kwargs):
        if event == "show":
            renpy.music.play("audio/dialog.ogg", channel="sound", loop=True) 
            renpy.music.set_volume(1, channel="sound")
        elif event == "slow_done" or event == "end":
            renpy.music.stop(channel="sound")

# === SHAKE KHUSUS BACKGROUND ===
transform bg_shake:
    xoffset 0
    linear 0.03 xoffset -20
    linear 0.03 xoffset 20
    linear 0.03 xoffset -15
    linear 0.03 xoffset 15
    linear 0.03 xoffset 0

# === SHAKE TEKS ===
transform text_shake:
    xoffset 0
    linear 0.02 xoffset -10
    linear 0.02 xoffset 10
    repeat 4

# === ZOOM KHUSUS KARAKTER ===
transform zoom_taishiro:
    zoom 1.15
    yalign 1.0



#buat kebutuhan digame biar ga susah
define t = Character("kenzo", color="#f83e00", what_slow_cps=20, callback=typewriter_callback)
define n = Character("narator", color="#f5e101f9", what_slow_cps=20, callback=typewriter_callback)
define l = Character("Lisa", color="#ffb6c1", what_slow_cps=20, callback=typewriter_callback)
define s = Character("Satpam", color="#0e26fa", what_slow_cps=20, callback=typewriter_callback) 
define g = Character("Pak Agus", color="#00ff1aff", what_slow_cps=20, callback=typewriter_callback)

screen typewriter_dialog(who, what):
    window:
        id "window"
        has vbox
        if who:
            text who id "who"
        text what id "what"
    if renpy.get_say_who() and renpy.get_say_what():
        text "|" at blink(0.5) xalign 1.0 yalign 1.0

transform blink(delay):
    alpha 1.0
    pause delay
    alpha 0.0
    pause delay
    repeat


# Background images
image bg BLACK = Solid("#00000000")
image bg kelas = "bg/smp_classroom1_day1.png"
image bg kelas_sore = "bg/smp_classroom1_evening1.png"
image bg taman_sore = "bg/park_s1_evening.png"
image bg opening = "bg/smp_classroom1_evening1.png"
image bg kamartidurkarakteru = "bg/personal room c day.png"
image bg sekolahgrtutup = "bg/smp_front_day3c.png"
image bg gerbangkelas = "bg/smp_classroom4_day2.png"
image bg tanggakelas = "bg/school a stairs st2 day.png"
image bg lorongkelas = "bg/school a hallway st2 day.png"
image bg rooftop = "bg/school a s2st2 day.png"
image bg jalan = "bg/city a s3st2 day.png"
image bg rumahlisa = "bg/house a day.png"

# Character transforms
transform zoom_taishiro:
    zoom 1.6
    xalign 1
    yalign 0.3

transform zoom_satpam:
    zoom 2.6
    xalign -0.1
    yalign 0.1

transform zoom_guru:
    zoom 2.6
    xalign -0.1
    yalign 0.1

transform zoom_alice:
    zoom 0.6
    xalign 0
    yalign 1.0

# Game start
label start:
    if persistent.chapter_completed == 0:
        jump chapter1_start
    else:
        call screen chapter_menu


label chapter1_start:

    play music "audio/BACKSOUNDKKC.mp3"
    $ renpy.music.set_volume(0.3, channel="music") 

    scene bg black

    n "selamat datang di game saya yang berjudul DREAM, saya buat game ini hanya modal nekat tapi saya akan berusaha untuk menyelesaikan game ini"

    n "mohon maaf jika game ini masih ada bug dan masih jauh diatas syarat untuk menjadi game Visual Novel"

    n "jika ada kritikan beserta saran saya akan dengar tapi jika hanya kritikan tanpa saran lu cuman sampah pemalas yang bisanya nge-judge karya orang lain"

    n "oh ya, anggap aja pemeran utama ini adalah dirilu sendiri"

    n "gak usah basa basi lagi, langsung aja masuk cerita"

    scene bg opening

    n "bercerita tentang seorang anak SMA yang tinggal di Jakarta dan bersekolah di sekolahan yang lumayan terkenal, anak itu bernama Kenzo Algahra"

    n "dia adalah seorang anak yang biasa saja, tidak terlalu pintar, tidak terlalu bodoh. Namun dia lumayan mahir dalam olahraga basket"

    n "walaupun mahir dalam basket, ia lebih menghabiskan waktu dikamar untuk bermain game"
    
    scene bg kelas
    with fade
    
    show taishiro schoolwinter normal  at zoom_taishiro

    t "perkenalkan, gw Kenzo Algahra sering dipanggil kenzo atau ken. gw berusia 17 tahun"

    t "gw cuman sekedar murid SMA biasa yang tidak mencolok, tidak tampan, tidak  terkenal, dan sering menghabiskan waktu di rooftop sekolah seperti tambahan pada umumnya"

    t "gw biasanya suka ke rooftop sekolah karena disitu tempat yang nyaman, sepi, dan orang jarang yang kesitu jadi cocok untuk tempat istirahat"

    t "oh ya, gw bersekolah di SMA kiyoga, gw sudah kelas 11 sekarang"
     
    t "setiap hari gw pulang sekolah langsung ke rumah untuk bermain game itupun kalau ekskul basket lagi libur"

    t "hidup gw yaaaa gini gini ajalah seperti hidup yang membosankan, tidak ada yang spesial dari gw"

    t "intinya adalah gw orang yang paling ngebosenin"

    t "dah segitu aja perkenalannya soalnya jam masuk mau mulai ini"

    hide taishiro schoolwinter normal

    scene bg kelas_sore
    with fade
    show taishiro schoolwinter happy at zoom_taishiro

    t "akhirnya beres juga pelajaran hari ini"

    t "sekarang gw bisa pulang ke rumah dan bermain game"

    scene bg taman_sore
    with fade
    "lu berjalan pulang dan seperti biasa melewati taman"
    "saat di jalan di area taman shiro melihat ada seorang cewek yang seperti mencari sesuatu"

    scene bg taman_sore
    with fade
    show taishiro schoolwinter happy at zoom_taishiro
    with dissolve
    t "loh, itu cewek kek nyari sesuatu dah"
    t "kayaknya dia butuh bantuan sih, hmmmm samperin gak ya?"
    menu :
        "menuju gadis itu":
            t "halo, lu butuh bantuan?"
            show alice_worried at zoom_alice
            hide taishiro schoolwinter happy at zoom_taishiro
            with dissolve
            l "...."
            l "boleh, soalnya gw lagi nyariin kucing gw yang hilang"
            show taishiro schoolwinter happy at zoom_taishiro
            hide alice_worried at zoom_alice
            t "kucing? dimana terakhir emang lu liat?"
            show alice_worried at zoom_alice
            hide taishiro schoolwinter happy at zoom_taishiro
            l "di taman ini tadi gw liat dia main-main disini"
            show taishiro schoolwinter happy at zoom_taishiro
            hide alice_worried at zoom_alice
            t "oh oke, gw bantuin ya cari kucinglu"
            show alice_worried at zoom_alice
            hide taishiro schoolwinter happy at zoom_taishiro
            l "eh, yakin nih? makasih ya maaf kalau ngerepotin"
            show taishiro schoolwinter happy at zoom_taishiro
            hide alice_worried at zoom_alice
            t "nggak masalah  santai aja, ayo kita cari" 
            jump good_ending

        "tidak peduli dan langsung pulang":
            t "ah, gw enggak mau repot-repot mending pulang terus main game atau tidur lebih enak"
            jump game_over
            
label game_over:
    stop music
    play sound "audio/marioGV.ogg"

    scene bg black
    with fade


    show text "{color=#ff0000}{size=200}GAME OVER{/size}{/color}" at truecenter
    n "............"
    n "wkwkwk mikir kids"
    n "lu masih punya perikemanusiaan?"
    n "kalau masih ada bantuin bukan lu cuekin"
    n "Ingat, setiap tindakan kecil bisa membuat perbedaan besar"
    n "Kebaikan dimulai dari keputusan untuk peduli terhadap sesama"
    n "bukan karena hal kecil dan tidak saling mengenal jadi kita gak mau nolong, bukan gitu ya"
    n "motivasi buat lu saat orang lain kesusahan lu tolong bukannya cuekin"
    n "ingat itu ya!, btw NT"

    with fade
    return

label good_ending:
    scene bg taman_sore
    with fade

    show taishiro schoolwinter happy at zoom_taishiro
    hide alice_worried at zoom_alice
    t "mungkin kucinglu suka main di area yang gelap"

    show alice_worried at zoom_alice
    hide taishiro schoolwinter happy at zoom_taishiro
    l "ah iya, dia memang suka tempat yang ada bayangan pohon"

    hide alice_worried
    hide taishiro schoolwinter happy
    "saat sedang mencari, shiro melihat kucing abu abu di dekat pohon"
    
    show taishiro schoolwinter happy at zoom_taishiro
    hide alice_worried at zoom_alice
    t "loh, itu kah? ada kucing abu-abu di dekat pohon itu"

    show alice_blush at zoom_alice 
    hide taishiro schoolwinter happy at zoom_taishiro
    l "iya! itu dia! miky!"
    l "terima kasih banyak, gw senang banget lu bantu gw"

    show taishiro schoolwinter happy at zoom_taishiro
    hide alice_blush at zoom_alice
    t "nggak usah berterima kasih, wajar kok kalau orang saling ngebantu"

    show alice_blush at zoom_alice
    hide taishiro schoolwinter happy at zoom_taishiro
    l "tapi lu udah membantu gw, sekali lagi maaf ya kalau ngerepotin"

    show taishiro schoolwinter happy at zoom_taishiro
    hide alice_blush at zoom_alice
    t "haha santai, gw juga senang kalau kucingnya udah ketemu"
    t "kalau gitu gw balik dulu ya, dah"

    hide taishiro schoolwinter happy
    hide alice_worried
    "lu memutuskan untuk balik"

    "tapi lu melupakan satu hal"

    show taishiro schoolwinter happy at zoom_taishiro

    t "lah iya, lupa nanya namanya lagi, hmmm lagian juga gak bakal ketemu lagi. muka kayak gw orang nginget aja gak sudi"

    hide taishiro schoolwinter happy

    "lanjut cerita di chapter 2"

    stop music

    $ persistent.chapter_completed = max(persistent.chapter_completed, 1)
    return

label chapter2_start:

    play music "audio/BACKSOUNDKKC.mp3"
    $ renpy.music.set_volume(0.1, channel="music")

    scene bg BLACK
    show text "{color=#ff0000}{size=200}KEESOKAN HARINYA{/size}{/color}" at truecenter

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

    show taishiro outing surprised at zoom_taishiro

    t "astaga, gw telat bangun! udah jam 06:50 mana sekolah masuk jam 07:00 belum diperjalanan 15 menit, gw harus buru-buru siap-siap ke sekolah bisa dihukun yang ada!"

    scene bg BLACK
    show text "{color=#ff0000}{size=200}SESAMPAINYA DISEKOLAH{/size}{/color}" at truecenter

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
    play sound "marioGV.mp3"
    show text "{color=#ff0000}{size=200}GAME OVER{/size}{/color}" at truecenter
    n "ppppfffttttt"
    n "telat langsung disuruh pulang ya? kasian amat manusia satu ini"
    n "logika kids, yakali satpam bolehin lu masuk wkwkwk"
    n "jadiin pelajaran juga ya, disiplin itu penting, apalagi di sekolah mangkanya jangan begadang main game"
    n "jadiin pelajaran biar gak telat, NT"
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
            "(APASIH, nih orang ribet banget ya gw tau muka gw gak jauh kayak beruk tapi peka dong itu dia ngerasa risih)"
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
    play sound "marioGV.mp3"
    show text "{color=#ff0000}{size=200}GAME OVER{/size}{/color}" at truecenter
    n "yahhh si bro kepoan mana bilangnya mau lebih deket wkwwk, sadar diri bos muka lu aja pas pasan"
    n "btw punya kaca? ngaca dulu sana. Lu ikut malah bikin runyam bukannya deket"
    n "udah tau dia ngerasa risih di kerumunan, malah ngikut nimbrung"
    n "hadehhh peka dikit, NT dah"
    return
    with fade

label game_over3:
    scene bg BLACK
    with fade
    play sound "marioGV.mp3"
    show text "{color=#ff0000}{size=200}GAME OVER{/size}{/color}" at truecenter
    "gila si bro anti sosial, pasti orang cool dan gak peduli apa yang terjadi disekitar"
    "peka dikitlah jadi cowok, aduh"
    "gak usah sok cuek pantes jomblo, lu aja orangnya gak peduli sekitar gimana mau dapet cewek"
    "makan tuh kata when yah setiap hari, NT"
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
            hide taishiro schoolwinter suprised
            "saat lu nengok ke murid baru itu, ternyata dia udah dikepung sama anak anak kelas lain yang penasaran dengannya terutama cowok nakal yang sering bolos kelas"
            jump game_over5


label game_over4:
    scene bg BLACK
    with fade
    play sound "marioGV.mp3"
    show text "{color=#ff0000}{size=200}GAME OVER{/size}{/color}" at truecenter
    n "kelazzz king malah ditinggalin wkwkwk"
    n "kalau lu lagi bareng cewek jangan langsung main ninggalin ya kids apalagi itu murid baru yang langsung jadi primadona sekolah"
    n "lu sebagai cowok mumpung bareng dia setidaknya lindungi dari keramaian agar gak dikepung buaya kelaparan lagi"
    n "kan lu tau dia aja tadi risih dideketin banyak cowok"
    n "lain kali jangan gitu ya kids kan ngambek jadinya dia ke lu malah berujung ilfeel, NT dah jones"
    return
    with fade

label game_over5:
    scene bg BLACK
    with fade
    play sound "marioGV.mp3"
    show text "{color=#ff0000}{size=200}GAME OVER{/size}{/color}" at truecenter
    n "hmmm bagus sih ajak ke kantin sekalian study tour sekolah, tapi diakan murid baru yang langsung terkenal karena kecantikannya"
    n "dalam beberapa jam aja dia udah jadi bahan perbincangan satu sekolah"
    n "lu malah bawa ke kumpulan monyet monyet yang sering bolos kelas buat ke kantin"
    n "kali ini jawaban tidak terlalu salah tapi mikir kondisi kids, NT"
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

label chapter3_start:

    play music "audio/BACKSOUNDKKC.mp3"
    $ renpy.music.set_volume(0.1, channel="music")

    scene bg kelas_sore
    with fade

    show taishiro schoolwinter happy at zoom_taishiro

    t "finally, selesai juga pelajaran hari ini"

    t "seperti biasa gw balik terus tidur atau main game"
    
    hide taishiro schoolwinter happy

    "tiba tiba dapet notif dari teman dekat lo kalau ada latihan basket dan dia izin berangkat duluan"

    "temen dekatlu pun bilang kalau dia akan nunggu lu disana"

    show taishiro schoolwinter happy at zoom_taishiro

    t "oh iya gw ada latihan basket hari ini"

    hide taishiro schoolwinter happy

    "lo bergegas merapihkan buku buku"

    "setelah selesai merapihkan. lu siap siap untuk berangkat"

    "namun......"

    show taishiro schoolwinter happy at zoom_taishiro
    hide alice_worried

    t "........"


    hide taishiro schoolwinter happy
    show alice_worried at zoom_alice

    l "........"

    l "Ken"

    show taishiro schoolwinter happy at zoom_taishiro
    hide alice_worried

    t "ya?"

    hide taishiro schoolwinter happy
    show alice_worried at zoom_alice

    l "rumahlu deket taman kemarin bukan?"

    show taishiro schoolwinter happy at zoom_taishiro
    hide alice_worried

    t "ya rumah gw luumayan deket sih ama taman kemarin, kenapa? rumahlu deket situ juga?"

    t "(haha asal ceplos aja, gak mungkin rumah dia deket situ toh kemarin paling cuman main doang bareng kucingnya)"

    hide taishiro schoolwinter happy
    show alice_worried at zoom_alice

    l "ya, rumah gw deket situ"

    show taishiro schoolwinter happy at zoom_taishiro
    hide alice_worried

    t "eh..."

    t "(lah padahal gw asbun doang)"

    t "wah dekat dong berarti, btw disitu juga ada cafe enak loh kopi ama makanannya, nanti mau kesana buat nyoba?"

    hide taishiro schoolwinter happy
    show alice_worried at zoom_alice
 
    l "wah boleh tuh, mau kesana kapan? sekarang?"
 
    hide alice_worried
    show taishiro schoolwinter surprised at zoom_taishiro

    t "(aduh gw ada ekskul basket lagi, gimana ya...)"

    hide taishiro schoolwinter surprised

    menu :
        "nolak tawarannya dan ngajak pulang bareng saja, gak jadi ikut ekskul basket" :
            
            show taishiro schoolwinter happy at zoom_taishiro

            t "aduh lain kali aja ya, gw mau langsung balik, capek banget soalnya"

            t "lu mau ikut bareng gw naik motor ga?"

            hide taishiro schoolwinter happy
            show alice_worried at zoom_alice

            l "hmm.. boleh deh"

            l "berarti lain kali aja kalau lu gak capek atau sibuk"

            hide taishiro schoolwinter happy

            "dan lu pun malah balik dan bolos ekskul basket"
            jump game_over6

        "nolak tawarannya karena lu ada ekskul basket dan ninggalin dia di kelas" :

            show taishiro schoolwinter happy at zoom_taishiro

            t "aduh sorry banget, gw ada ekskul basket sekarang"

            hide taishiro schoolwinter happy
            show alice_worried at zoom_alice

            l "loh ekskul basket?"

            show taishiro schoolwinter happy at zoom_taishiro
            hide alice_worried

            t "iya nih gw lagi buru buru, sorry banget ya"

            hide taishiro schoolwinter happy

            "lupun berangkat buru buru dan ninggalin dia di kelas"
            jump game_over7

        "nolak tawarannya karena ada ekskul dan anterin dia balik" :

            show taishiro schoolwinter happy at zoom_taishiro

            t "aduh sorry banget gw gak bisa hari ini soalnya ada ekskul"

            hide taishiro schoolwinter happy
            show alice_worried at zoom_alice

            l "oh lu ekskul basket ya?"

            show taishiro schoolwinter happy at zoom_taishiro
            hide alice_worried

            t "iya nih sorry banget"

            hide taishiro schoolwinter happy
            show alice_worried at zoom_alice

            l "iya gapapa"

            show taishiro schoolwinter happy at zoom_taishiro
            hide alice_worried

            t "btw lu balik make apa? dijemput ortulu kah?"

            hide taishiro schoolwinter happy
            show alice_worried at zoom_alice

            l "gw naik transportasi umum, soalnya ayah gw lagi sibuk kerja"

            show taishiro schoolwinter happy at zoom_taishiro
            hide alice_worried

            t "(hmmm kasian juga kalau pulang sendiri naik angkutan umum)"

            t "mau gw anterin naik motor gw gak?"

            hide taishiro schoolwinter happy
            show alice_worried at zoom_alice

            l "eh gak usah. Nanti ngerepotin sama nanti lu telat ekskul basket"

            show taishiro schoolwinter happy at zoom_taishiro
            hide alice_worried

            t "udah santai aja"

            hide taishiro schoolwinter happy
            show alice_worried at zoom_alice

            l "aduh, nanti lu dimarahin pelatih lu kalau telat. Gw pulang sendiri aja"

            show taishiro schoolwinter happy at zoom_taishiro
            hide alice_worried

            t "udah ikut aja soalnya gw sekalian mau ngambil barang ketinggalan di rumah"

            hide taishiro schoolwinter happy
            show alice_worried at zoom_alice

            l "hmmm, bener nih? lu gak ngeboongkan kalau ada barang ketinggalan?"
            
            show taishiro schoolwinter happy at zoom_taishiro
            hide alice_worried

            t "gak kok santai aja"
            t "(tajem banget di cewek instingnya)"

            hide taishiro schoolwinter happy
            show alice_worried at zoom_alice

            l "yaudah gw bareng lu ya"
            
            show taishiro schoolwinter happy at zoom_taishiro
            hide alice_worried

            t "sip lu tunggu aja di depan gerbang sekolah entar gw kesana, mau ke parkiran ngambil motor"

            hide taishiro schoolwinter happy
            show alice_worried at zoom_alice

            l "oke, gw kesana ya"

            show taishiro schoolwinter happy at zoom_taishiro
            hide alice_worried

            t "ya"

            hide taishiro schoolwinter happy

            "lu ngambil motor terlebih dahulu dan dilanjut jemput lisa didepan gerbang sekolah. setelah itu, lu langsung gas anter ke rumahnya"
            jump good_ending4

        "terima tawarannya pergi ke cafe dan bolos ekskul basket" :

            show taishiro schoolwinter happy at zoom_taishiro

            t "hmm.. boleh deh, mau bareng naik motor?"

            hide taishiro schoolwinter happy
            show alice_worried at zoom_alice

            l "emang lu gak sibuk?"

            show taishiro schoolwinter happy at zoom_taishiro
            hide alice_worried

            t "enggak santai aja"

            hide taishiro schoolwinter happy
            show alice_worried at zoom_alice

            l "oh boleh deh kalau lagi gak sibuk lunya"

            show taishiro schoolwinter happy at zoom_taishiro
            hide alice_worried

            t "oke"

            hide taishiro schoolwinter happy

            "lu berangkat ke cafe dan bolos ekskul basket. Parahnya lagi lu gak ngabarin temenlu"
            jump game_over8


label game_over6:
    scene bg BLACK
    with fade
    play sound "marioGV.mp3"
    show text "{color=#ff0000}{size=200}GAME OVER{/size}{/color}" at truecenter
    n "si bro pemalas banget udah gak ikut basket balik lagi kerumah"
    n "lu balik juga mau ngapain? main HP? kagak guna"
    n "lebih baik tubuhlu digerakkin, udah mah nolak tawaran lagi. gak respect emang"
    n "udah sono coba lagi gak usah maless"
    return
    with fade

label game_over7:
    scene bg BLACK
    with fade
    play sound "marioGV.mp3"
    show text "{color=#ff0000}{size=200}GAME OVER{/size}{/color}" at truecenter
    n "waduh NT banget, walaupun lagi buru buru minimal tawarin jalan bareng ke gerbang bukannya ninggalin"
    n "gak peka emang nih orang"
    n "coba lagi biar peka jadi orang"
    return
    with fade

label game_over8:
    scene bg BLACK
    with fade
    play sound "marioGV.mp3"
    show text "{color=#ff0000}{size=200}GAME OVER{/size}{/color}" at truecenter
    n "kebangetan nih orang udah ngebohong, bolos basket, ninggalin temen lu lagi"
    n "itu temen lu nungguin lu, parah sih di PHP gak respect banget"
    n "mikir kids, coba belajar respect ama jangan bohong sana"
    return
    with fade

label good_ending4 :

    scene bg sekolahgrtutup
    with fade

    "saat menjemput lisa digerbang lu jadi pusat perhatian"

    show taishiro schoolwinter angry  at zoom_taishiro

    t "(LAGI LAGI GINI SIALAN, nih orang orang punya masalah apa dah sampe liatin gw segitunya)"

    hide taishiro schoolwinter angry

    "karena lu orangnya cuek, lupun berusaha tidak peduli sama sekitar lu"

    show taishiro schoolwinter happy at zoom_taishiro

    t "lis, dah siap?"

    hide taishiro schoolwinter happy
    show alice_worried at zoom_alice

    l "udah"

    hide alice_worried 
    show taishiro schoolwinter happy at zoom_taishiro

    t "oke sip, gass meluncur"

    hide taishiro schoolwinter happy

    scene bg jalan
    with fade

    "mereka berduapun akhirnya meluncur"

    "saat diperjalanan mereka berbincang bincang santai"

    "tapi saat sudah setengah jalan tiba tiba jalan didepan macet"

    show taishiro schoolwinter angry  at zoom_taishiro

    t "(sial, napa harus macet sih. Hobi banget nih kota kalau soal macet, mana macetnya kayak nungguin bansos)"

    t "(tapi ada sih beberapa jalan)"

    menu :
        "lewat jalan pintas" :

            hide alice_worried 
            show taishiro schoolwinter happy at zoom_taishiro

            t "eh lis, gw lewat jalan pintas aja ya biar cepet"

            hide taishiro schoolwinter happy
            show alice_worried at zoom_alice

            l "ya, emang lewat mana?"

            hide alice_worried 
            show taishiro schoolwinter happy at zoom_taishiro

            t "tuh lewat gang yang khusus buat motor didepan"

            hide taishiro schoolwinter happy
            show alice_worried at zoom_alice

            l "oh, emang nanti nembus mana kalau lewat situ?"

            hide alice_worried 
            show taishiro schoolwinter happy at zoom_taishiro

            t "gak jauh sini, tetep masuk jalan ini. Cuman semoga aja gak macet didepan"

            hide taishiro schoolwinter happy
            show alice_worried at zoom_alice

            l "oh, kalau gitu lewat situ aja"

            hide alice_worried 
            show taishiro schoolwinter happy at zoom_taishiro

            t "sip"

            hide taishiro schoolwinter happy

            "lupun akhirnya lewat jalan situ"

            "setelah masuk, lu mengikuti jalan dan menghabiskan waktu 5 menit untuk menyusuri itu jalan"

            "setelah menyusuri jalan akhirnya didepan lu udah ada pintu keluarnya"

            "namun......."

            hide alice_worried 
            show taishiro schoolwinter happy at zoom_taishiro

            t "(loh.....)"

            "lupun kaget karena saaat keluar gang macetnya tetap ada dan malah lebih parah karena lu sekarang gak bisa putar balik. Motor lu sekarang ada di tengah tengah kemacetan, mau gak mau lu harus nunggu"
            jump game_over9

        "tetap sabar nunggu, siapa tau nanti didepan gak macet" :

            hide alice_worried 
            show taishiro schoolwinter happy at zoom_taishiro

            t "(nunggu aja kali ya siapa tau nanti gak macet)"

            t "eh lis, lu nunggu rada lama gapapa? soalnya macet"

            hide taishiro schoolwinter happy
            show alice_worried at zoom_alice

            l "oh ya, gapapa"

            hide alice_worried 

            "lu akhirnya memutuskan buat nunggu macet"

            "lu nunggu sampe 5 menit tapi lom juga gerak"

            show taishiro beachwear normal

            t "(jirlah udah 5 menit masih lom gerak, hmmm tunggu aja kali)"

            hide alice_worried 
            show taishiro schoolwinter happy at zoom_taishiro

            "15 menit berlalu, tapi  belum juga gerak"

            "lu nunggu dengan sabar"

            "30 menit berlalu, akhirnya gerak walaupun cuman beberapa cm"

            hide alice_worried 
            show taishiro schoolwinter angry at zoom_taishiro

            t "(AKHHH APES BANGET DAH CUMAN NUNGGU MAJU SECUIL SAMPE 30 MENIT)"

            "lu masih sabar walaupun sedikit emosi dan lu ngajak ngobrol lisa biar gak bosen menghadapi macet jakarta"

            "dan ya"

            "lu sampe sampe malem karena harus sabar nungguin macet"
            jump game_over10

        "muter jalan walaupun rada jauh" :

            hide alice_worried 
            show taishiro schoolwinter happy at zoom_taishiro
            
            t "( muter jalan aja kali ya, tapi ngabisin waktu 1 jam lebih buat bolak balik, mana sekarang udah jam 3 sedangkan latihan basket mulai jam 4 sore )"

            t "(hmmm yaudahlah muter aja daripada harus nunggu macet)"

            t "lis, mau muter jalan aja gak? tapi lumayan jauh"

            hide taishiro schoolwinter happy
            show alice_worried at zoom_alice

            l "boleh, tapi lu capek gak muter jalan jauh?"

            hide alice_worried 
            show taishiro schoolwinter happy at zoom_taishiro

            t "gak kok, yaudah ya muter jalan aja"

            hide taishiro schoolwinter happy

            "akhirnya lu mutusin buat muter jalan walaupun jaraknya nambah jauh"
            jump good_ending5

        "istirahat di tempat seperti tempat makan di pinggir jalan" :

            hide alice_worried 
            show taishiro schoolwinter happy at zoom_taishiro

            t "hmmm lis, mau istirahat dulu gak? soalnya ini macet"

            hide taishiro schoolwinter happy
            show alice_worried at zoom_alice

            l "boleh deh, mau istirahat dimana emangnya?"

            hide alice_worried 
            show taishiro schoolwinter happy at zoom_taishiro

            t "itu dipinggir jalan ada warung makan"

            hide taishiro schoolwinter happy
            show alice_worried at zoom_alice

            l "boleh deh, takut lunya capek kalau lanjut ngendarain motor"

            hide alice_worried 
            show taishiro schoolwinter happy at zoom_taishiro

            t "hehe, yaudah gw kesana ya"

            hide taishiro schoolwinter happy

            "lu akhirnya menuju ke warung itu"

            "dan lu berdua mesan makanan dan es sambil mengobrol"

            "sangking asiknya ngobrol lu gak nyadar kalau hari udah mulai sore"

            hide alice_worried 
            show taishiro schoolwinter happy at zoom_taishiro

            
            hide taishiro schoolwinter happy

            "lu cek jam dan ternyata jarum jam sudah menunjukkan bawa sekarang pukul 17:30"

            hide alice_worried 
            show taishiro schoolwinter surprised at zoom_taishiro

            t "(anjirlah udah jam segini)"

            t "eh lis, udah jam segini balik yok, udah mau malem"

            hide taishiro schoolwinter surprised
            show alice_worried at zoom_alice

            l "yaudah yok pulang"

            hide alice_worried

            "akhirnya lu berdua pulang dan lu bolos ekskul"
            jump game_over11

label game_over9:
    scene bg BLACK
    with fade
    play sound "marioGV.mp3"
    show text "{color=#ff0000}{size=200}GAME OVER{/size}{/color}" at truecenter
    n "aduh, pikir pikir dulu dong udah tau macet panjang yakali lu lewat jalan pintas yang ujungnya lewat jalan yang sama"
    n "ya jelas masih macetlah, kan lu liat sendiri macetnya kayak kereta"
    n "dan parahnya lagi lu gak bisa putar balik"
    return
    with fade

label game_over10:
    scene bg BLACK
    with fade
    play sound "marioGV.mp3"
    show text "{color=#ff0000}{size=200}GAME OVER{/size}{/color}" at truecenter
    n "wkwkwk si bro masih sabar dalam menghadapi macet"
    n "lu mau nunggu kapan kalau macet panjang "
    n "sinetron tukang bubur naik haji aja keburu tamat daripada nungguin macet panjang gitu"
    n "coba lagi tuan penyabar"
    return
    with fade

label game_over11:
    scene bg BLACK
    with fade
    play sound "marioGV.mp3"
    show text "{color=#ff0000}{size=200}GAME OVER{/size}{/color}" at truecenter
    n "bagus sih ke warung makan dulu daripada nunggu macet"
    n "tapi yang gak bagusnya lu ngobrol sampe lupa waktu. Apalagi ada temen lu nungguin di tempat ekskul"
    n "coba lagi"
    return
    with fade

label good_ending5:

    scene bg rumahlisa
    with fade

    "setelah hampir 30 menitan akhirnya lu sampe ke rumah lisa"

    "saat liat rumahnya lu sedikit kaget"

    hide alice_worried 
    show taishiro schoolwinter happy at zoom_taishiro

    t "(buset nih rumah bagus banget anak orang kaya pasti)"

    t "hmm lis gw duluan ya"

    hide taishiro schoolwinter happy
    show alice_worried at zoom_alice

    l "eh, mampir dululah sini"

    hide alice_worried 
    show taishiro schoolwinter happy at zoom_taishiro

    t "waduh nanti aja deh, lagi buru buru gwnya lagian gak enak kalau mendadak mampir takutnya ganggu orang rumah"

    t "lain waktu aja ya, bye ketemu lagi besok"

    hide taishiro schoolwinter happy
    show alice_worried at zoom_alice

    l "ya, hati hati"

    hide taishiro schoolwinter happy

    scene bg jalan

    "lu ngendarain motor lu ngebut menuju tempat ekskul basket soalnya takut telat"

    $ persistent.chapter_completed = max(persistent.chapter_completed, 3)
    jump chapter_menu
    
    stop music

    label chapter4_start:

        "coming soon"

    return