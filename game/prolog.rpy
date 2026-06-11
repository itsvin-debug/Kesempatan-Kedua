label prolog_start:

    play music "audio/BACKSOUNDKKC.mp3" volume 0.3

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
    play music "audio/marioGV.ogg" volume 1.0 noloop

    scene bg black
    with fade


    show text "{color=#ff0000}{size=200}GAME OVER{/size}{/color}" at game_over_pos
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
    menu:
        "Memulai Ulang (Restart)":
            jump start
        "Kembali ke Lobby (Main Menu)":
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
