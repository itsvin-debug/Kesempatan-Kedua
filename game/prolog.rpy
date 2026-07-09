label prolog_start:

    # Menampilkan gambar/cutscene statis
    scene black
    with fade

    # Tambahkan dialog prolog di sini

    scene cutscene balkon
    with fade

    "Gua Rio seorang kriminal yang bergabung pada perusahaan gelap milik teman gua sendiri yang menjual barang terlarang, tugas gua memantau bisnis agar bisnis tersebut aman dari polisi dan sekarang gua udah berhenti. Namun keberhentian gua dalam bisnis gelap itu tidak menyelesaikan masalah tapi menambah malapetaka....... "
    hide cutscene balkon with fade

    scene bg balkon

    show rio ngobrol biasa at rio_left

    r "hhhh, jujur gua nyesel jadi seorang kriminal yang suka ngedarin barang terlarang dan gua nyesel pas masa SMA gua cuman jadi sampah masyarakat terus karena perbuatan itu gua jadi ninggalin orang orang berharga gua...."
    
    r "kalau gua dengerin orang tua gua gimana ya..... Mungkin kehidupan gua lebih baik sekarang, mungkin juga gua bisa ngejar orang yang gua suka dan masih kontakan sama sahabat gua"

    r "aaa mo gimana lagi, gua udah gak ada siapa siapa lagi, gua udah putus hubungan sama semua nya ( menghembuskan nafas berat )"
    hide rio ngobrol biasa

    show rio menghela nafas 
    # Contoh menampilkan cutscene foto:
    # scene nama_gambar_cutscene
    # with dissolve
    # "Dialog selama cutscene berlangsung..."

    scene black
    with fade

    $ persistent.chapter_completed = max(persistent.chapter_completed, 1)

    jump chapter_menu_return

label chapter_menu_return:
    return
