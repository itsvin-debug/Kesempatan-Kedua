label chapter2_start:

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
    show text "{color=#ff0000}{size=200}GAME OVER{/size}{/color}" at game_over_pos
    n "si bro pemalas banget udah gak ikut basket balik lagi kerumah"
    n "lu balik juga mau ngapain? main HP? kagak guna"
    n "lebih baik tubuhlu digerakkin, udah mah nolak tawaran lagi. gak respect emang"
    n "udah sono coba lagi gak usah maless"
    menu:
        "Memulai Ulang (Restart)":
            jump start
        "Kembali ke Lobby (Main Menu)":
            return
    with fade

label game_over7:
    scene bg BLACK
    with fade
    play sound "marioGV.mp3"
    show text "{color=#ff0000}{size=200}GAME OVER{/size}{/color}" at game_over_pos
    n "waduh NT banget, walaupun lagi buru buru minimal tawarin jalan bareng ke gerbang bukannya ninggalin"
    n "gak peka emang nih orang"
    n "coba lagi biar peka jadi orang"
    menu:
        "Memulai Ulang (Restart)":
            jump start
        "Kembali ke Lobby (Main Menu)":
            return
    with fade

label game_over8:
    scene bg BLACK
    with fade
    play sound "marioGV.mp3"
    show text "{color=#ff0000}{size=200}GAME OVER{/size}{/color}" at game_over_pos
    n "kebangetan nih orang udah ngebohong, bolos basket, ninggalin temen lu lagi"
    n "itu temen lu nungguin lu, parah sih di PHP gak respect banget"
    n "mikir kids, coba belajar respect ama jangan bohong sana"
    menu:
        "Memulai Ulang (Restart)":
            jump start
        "Kembali ke Lobby (Main Menu)":
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
            show taishiro schoolwinter happy at zoom_taishiro

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
    show text "{color=#ff0000}{size=200}GAME OVER{/size}{/color}" at game_over_pos
    n "aduh, pikir pikir dulu dong udah tau macet panjang yakali lu lewat jalan pintas yang ujungnya lewat jalan yang sama"
    n "ya jelas masih macetlah, kan lu liat sendiri macetnya kayak kereta"
    n "dan parahnya lagi lu gak bisa putar balik"
    menu:
        "Memulai Ulang (Restart)":
            jump start
        "Kembali ke Lobby (Main Menu)":
            return
    with fade

label game_over10:
    scene bg BLACK
    with fade
    play sound "marioGV.mp3"
    show text "{color=#ff0000}{size=200}GAME OVER{/size}{/color}" at game_over_pos
    n "wkwkwk si bro masih sabar dalam menghadapi macet"
    n "lu mau nunggu kapan kalau macet panjang "
    n "sinetron tukang bubur naik haji aja keburu tamat daripada nungguin macet panjang gitu"
    n "coba lagi tuan penyabar"
    menu:
        "Memulai Ulang (Restart)":
            jump start
        "Kembali ke Lobby (Main Menu)":
            return
    with fade

label game_over11:
    scene bg BLACK
    with fade
    play sound "marioGV.mp3"
    show text "{color=#ff0000}{size=200}GAME OVER{/size}{/color}" at game_over_pos
    n "bagus sih ke warung makan dulu daripada nunggu macet"
    n "tapi yang gak bagusnya lu ngobrol sampe lupa waktu. Apalagi ada temen lu nungguin di tempat ekskul"
    n "coba lagi"
    menu:
        "Memulai Ulang (Restart)":
            jump start
        "Kembali ke Lobby (Main Menu)":
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
