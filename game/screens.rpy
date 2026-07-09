################################################################################
## Inisialisasi
################################################################################

init offset = -1

## Pastikan variabel persistent chapter sudah terdefinisi




################################################################################
## Gaya
################################################################################

style default:
    properties gui.text_properties()
    language gui.language

style input:
    properties gui.text_properties("input", accent=True)
    adjust_spacing False

style hyperlink_text:
    properties gui.text_properties("hyperlink", accent=True)
    hover_underline True

style gui_text:
    properties gui.text_properties("interface")


style button:
    properties gui.button_properties("button")

style button_text is gui_text:
    properties gui.text_properties("button")
    yalign 0.5


style label_text is gui_text:
    properties gui.text_properties("label", accent=True)

style prompt_text is gui_text:
    properties gui.text_properties("prompt")


style bar:
    ysize gui.bar_size
    left_bar Frame("gui/bar/left.png", gui.bar_borders, tile=gui.bar_tile)
    right_bar Frame("gui/bar/right.png", gui.bar_borders, tile=gui.bar_tile)

style vbar:
    xsize gui.bar_size
    top_bar Frame("gui/bar/top.png", gui.vbar_borders, tile=gui.bar_tile)
    bottom_bar Frame("gui/bar/bottom.png", gui.vbar_borders, tile=gui.bar_tile)

style scrollbar:
    ysize gui.scrollbar_size
    base_bar Frame("gui/scrollbar/horizontal_[prefix_]bar.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/scrollbar/horizontal_[prefix_]thumb.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)

style vscrollbar:
    xsize gui.scrollbar_size
    base_bar Frame("gui/scrollbar/vertical_[prefix_]bar.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/scrollbar/vertical_[prefix_]thumb.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)

style slider:
    ysize gui.slider_size
    base_bar Frame("gui/slider/horizontal_[prefix_]bar.png", gui.slider_borders, tile=gui.slider_tile)
    thumb "gui/slider/horizontal_[prefix_]thumb.png"

style vslider:
    xsize gui.slider_size
    base_bar Frame("gui/slider/vertical_[prefix_]bar.png", gui.vslider_borders, tile=gui.slider_tile)
    thumb "gui/slider/vertical_[prefix_]thumb.png"


style frame:
    padding gui.frame_borders.padding
    background Frame("gui/frame.png", gui.frame_borders, tile=gui.frame_tile)



################################################################################
## Layar In-game
################################################################################


## Layar Say ###################################################################
##
## Layar say di gunakan untuk menampilkan dialog kepada pemain. Ini menggunakan
## dua parameter, who dan what, yang merupakan nama karakter yang berbicara dan
## text yang akan di tampilkan, masing-masing. (Kedua parameter dapat berisi
## None jika tidak ada nama yang di berikan.
##
## Layar ini harus membuat text yang dapat di tampilkan dengan id "what", yang
## di mana Ren'Py menggunakan ini untuk mengatur tampilan text. Ini juga dapat
## membuat sesuatu yang dapat di tampilkan dengan id "who" dan id "window" untuk
## mengaplikasikan properti gaya.
##
## https://www.renpy.org/doc/html/screen_special.html#say

## Transform untuk panah speech bubble (kotak diputar 45 derajat)
transform say_arrow_rotate:
    rotate 45

screen say(who, what):

    ## Warna per karakter — setiap karakter punya warna khasnya masing-masing
    $ char_color = "#cc3355"  # Fallback
    if who == "Kenzo":
        $ char_color = "#f83e00"   # Oranye
    elif who == "Rio":
        $ char_color = "#1fa0e0"   # Biru
    elif who == "Kael":
        $ char_color = "#cc3355"   # Merah-pink
    elif who == "Lisa":
        $ char_color = "#e0407a"   # Pink cerah
    elif who == "Satpam":
        $ char_color = "#4a6ae6"   # Biru tua
    elif who == "Pak Agus":
        $ char_color = "#33cc55"   # Hijau
    elif who == "Osis":
        $ char_color = "#9b59b6"   # Ungu
    elif who == "Elina":
        $ char_color = "#f5b800"   # Kuning emas
    elif who == "narator":
        $ char_color = "#cc3355"

    ## Warna dialog = warna karakter (tetap, tidak berubah berdasarkan emosi)
    $ dynamic_color = char_color

    if who is not None:
        ## =====================================================
        ## DIALOG KARAKTER — speech bubble + panah ke kiri
        ## =====================================================
        vbox:
            xalign 0.65
            yalign 0.68
            xsize 960
            spacing 0

            ## Namebox di atas kotak dialog
            window:
                id "namebox"
                style "namebox"
                background Solid(dynamic_color)
                xalign 0.0
                text who id "who"

            ## Dialog + Arrow dalam fixed container
            fixed:
                xsize 960
                ysize 210

                ## Panah balon dialog (rotasi 45°, menonjol dari kiri)
                frame at say_arrow_rotate:
                    xpos -14
                    ypos 88
                    xysize (28, 28)
                    background Solid(dynamic_color)

                ## Window dialog utama
                window:
                    id "window"
                    xpos 0
                    xsize 940
                    ysize 210

                    has fixed

                    ## Layer 1: border berwarna
                    frame:
                        xfill True
                        yfill True
                        background Solid(dynamic_color)

                    ## Layer 2: area putih dalam
                    frame:
                        xfill True
                        yfill True
                        left_margin 12
                        right_margin 12
                        top_margin 12
                        bottom_margin 12
                        background Solid("#fffdf9")
                        padding (45, 28, 45, 28)

                        text what id "what"

                    ## Dekorasi tiga kotak pojok kanan atas
                    hbox:
                        xalign 1.0
                        yalign 0.0
                        xoffset -18
                        yoffset 18
                        spacing 8

                        frame:
                            xysize (22, 22)
                            background Solid("#fffdf9")
                        frame:
                            xysize (22, 22)
                            background Solid("#fffdf9")
                        frame:
                            xysize (22, 22)
                            background Solid("#fffdf9")

    elif what == "" or what == " ":
        ## =====================================================
        ## FIX BUG FLASH HITAM: Saat ganti scene (transisi)
        ## Ren'Py memanggil say screen kosong. Jangan render kotak apapun!
        ## =====================================================
        window:
            id "window"
            background None
            text "" id "what"

    else:
        ## =====================================================
        ## NARASI / TANPA KARAKTER — Desain Premium Kaca Gelap
        ## =====================================================
        window:
            id "window"
            style "say_narrator_window"
            xalign 0.5
            yalign 0.4
            xsize 1200
            ysize 300
            background Solid("#080814ee")
            padding (0, 0, 0, 0)

            # Top border line
            frame:
                xfill True
                ysize 1
                yalign 0.0
                background Solid("#ffffff30")

            # Bottom border line
            frame:
                xfill True
                ysize 1
                yalign 1.0
                background Solid("#ffffff30")

            # Left pink accent
            frame:
                xsize 4
                yfill True
                top_margin 25
                bottom_margin 25
                xpos 0
                background Solid("#ff4b6e")

            # Right pink accent
            frame:
                xsize 4
                yfill True
                top_margin 25
                bottom_margin 25
                xalign 1.0
                background Solid("#ff4b6e")

            # Content container (auto-resizes based on text height)
            vbox:
                yalign 0.5
                xalign 0.5
                xmaximum 1080
                spacing 20

                text what id "what":
                    style "say_narrator"
                    xmaximum 1080
                    xalign 0.5


    ## =========================================================
    ## TOMBOL KE LOBBY — Pojok kanan atas layar (gaya main menu)
    ## =========================================================
    button at main_menu_btn_transform:
        action Show("lobby_confirm")
        align (0.98, 0.04)
        xysize (200, 55)
        background "gui/menu_btn_idle.png"
        hover_background "gui/menu_btn_hover.png"
        text _("🏠 Lobby"):
            font "gui/font/PlayfairDisplay-Bold.ttf"
            color "#1c2833"
            hover_color "#000000"
            size 26
            bold True
            align (0.5, 0.5)


## Buat namebox tersedia untuk mengatur gaya melalui objek karakter.
init python:
    config.character_id_prefixes.append('namebox')

style window is default
style say_label is default
style say_dialogue is default
style say_thought is default
style say_narrator is default
style say_narrator_window is default

style namebox is default
style namebox_label is say_label


style window:
    xfill False
    xsize 940
    ysize 210
    padding (0, 0, 0, 0)
    background None  ## Transparan — mencegah gui/window.png flash saat ganti dialog

style namebox:
    xpos 0
    xanchor 0.0
    xsize None
    ysize None
    padding (30, 8, 30, 8)

style say_label:
    properties gui.text_properties("name", accent=True)
    xalign 0.0
    yalign 0.5
    color "#ffffff"
    bold True
    size 24

style say_dialogue:
    properties gui.text_properties("dialogue")
    color "#2a2a2a"
    size 26
    line_spacing 8
    xpos 0
    ypos 0
    xsize 850
    adjust_spacing False

## Gaya teks narasi — italic, warna terang, rata tengah
## Posisi dan padding dihandle oleh FRAME di layar, bukan style ini
style say_narrator:
    color "#d5ddf5"
    size 24
    italic True
    line_spacing 12
    text_align 0.5
    xalign 0.5
    adjust_spacing False

## Label watermark kecil pojok kanan bawah
style say_narrator_label is default:
    color "#ffffff18"
    size 11
    bold True
    kerning 4.0
    xalign 1.0
    yalign 1.0
    xoffset -16
    yoffset -10

## Layar masukkan/input ########################################################
##
## Layar ini di gunakan untuk menampilkan renpy.input. Parameter prompt
## digunakan untuk meneruskan text yang di prompt/minta.
##
## Layar ini harus membuat input yang dapat di tampilkan dengan id "input" untuk
## menerima berbagai parameter masukan.
##
## https://www.renpy.org/doc/html/screen_special.html#input

screen input(prompt):
    style_prefix "input"

    window:

        vbox:
            xanchor gui.dialogue_text_xalign
            xpos gui.dialogue_xpos
            xsize gui.dialogue_width
            ypos gui.dialogue_ypos

            text prompt style "input_prompt"
            input id "input"

style input_prompt is default

style input_prompt:
    xalign gui.dialogue_text_xalign
    properties gui.text_properties("input_prompt")

style input:
    xalign gui.dialogue_text_xalign
    xmaximum gui.dialogue_width


## Layar Pilihan ###############################################################
##
## Desain premium: kartu glassmorphism dengan efek glow bercahaya saat hover.
## Sesuai tema romance/drama SMA — warna pink-merah dengan border shimmer.
##
## https://www.renpy.org/doc/html/screen_special.html#choice

## Animasi transform: efek geser + glow saat hover
transform choice_idle_anim:
    on idle:
        easein 0.18 xoffset 0 alpha 0.82

transform choice_hover_anim:
    on idle:
        easein 0.18 xoffset 0 alpha 0.82
    on hover:
        easein 0.18 xoffset 10 alpha 1.0

screen choice(items):
    ## Overlay gelap semi-transparan di balik pilihan agar lebih fokus
    add Solid("#00000055")

    vbox:
        align (0.5, 0.5)
        spacing 0

        ## Header pilihan
        hbox:
            xalign 0.5
            spacing 16
            text "◆" color "#e07090" size 18 yalign 0.5
            text "P I L I H A N" color "#f5c0d0" size 20 bold True yalign 0.5 kerning 3.0
            text "◆" color "#e07090" size 18 yalign 0.5

        null height 22

        ## Kartu-kartu pilihan
        vbox:
            xalign 0.5
            spacing 16

            for i in items:
                ## Setiap pilihan = kartu dengan efek hover jika bisa diklik
                if i.action is not None:
                    button at choice_hover_anim:
                        action i.action
                        xsize 720
                        ysize 75

                        ## Latar default: kaca gelap semi-transparan
                        background Frame(
                            Solid("#1a0a1288"),
                            15, 15
                        )

                        ## Glow bercahaya saat hover
                        hover_background Frame(
                            Solid("#cc335544"),
                            15, 15
                        )

                        ## Foreground: border glow shimmer saat hover
                        foreground Frame(
                            Solid("#00000000"),
                            15, 15
                        )
                        hover_foreground Frame(
                            Solid("#ff408020"),
                            15, 15
                        )

                        padding (30, 0, 30, 0)

                        ## Isi kartu: ikon + teks
                        hbox:
                            yalign 0.5
                            spacing 18

                            ## Garis aksen kiri (selalu ada)
                            frame:
                                xysize (5, 44)
                                background Solid("#cc335599")
                                hover_background Solid("#ff6090")
                                yalign 0.5

                            ## Ikon berlian (muncul saat hover via alpha)
                            text "❯" color "#e0709088" hover_color "#ff8aaa" size 22 yalign 0.5

                            ## Teks pilihan
                            text i.caption:
                                color "#f0d0da"
                                hover_color "#ffffff"
                                size 26
                                bold False
                                yalign 0.5
                                font gui.text_font
                else:
                    ## Tampilan ketika pilihan terkunci / disabled
                    button:
                        action None
                        xsize 720
                        ysize 75
                        background Frame(
                            Solid("#22222288"),
                            15, 15
                        )
                        padding (30, 0, 30, 0)

                        hbox:
                            yalign 0.5
                            spacing 18

                            ## Garis aksen kiri abu-abu terkunci
                            frame:
                                xysize (5, 44)
                                background Solid("#555555")
                                yalign 0.5

                            ## Ikon gembok untuk menu terkunci
                            text "🔒" color "#777777" size 20 yalign 0.5

                            ## Teks pilihan terkunci (warna abu-abu redup)
                            text i.caption:
                                color "#777777"
                                size 26
                                bold False
                                yalign 0.5
                                font gui.text_font


## Style minimal — layout diatur manual di screen di atas
style choice_vbox is vbox
style choice_button is button
style choice_button_text is button_text

style choice_vbox:
    xalign 0.5
    yalign 0.5
    spacing 16

style choice_button is default:
    xsize 720
    ysize 75

style choice_button_text is default:
    color "#f0d0da"
    hover_color "#ffffff"
    size 26
    xalign 0.0
    yalign 0.5


## Layar Menu Cepat/Quick Menu #################################################
##
## Menu cepat ditampilkan dalam game untuk memudahkan akses ke menu di luar
## game.

screen quick_menu():

    ## Memastikan ini muncul di atas layar yang lain.
    zorder 100

    if _preferences.language == "english":
        key "t" action Language(None)
    else:
        key "t" action Language("english")

    if quick_menu:

        hbox:
            yoffset -50
            style_prefix "quick"

            xalign 0.5
            yalign 1.0


## Kode ini memastikan layar quick_menu di tampilkan di dalam permainan,
## kapanpun player tidak secaralangsung menyembunyikan antarmuka.
init python:
    config.overlay_screens.append("quick_menu")

default quick_menu = True

style quick_menu is hbox
style quick_button is default
style quick_button_text is button_text

style quick_menu:
    xalign 0.5
    yalign 1.0

style quick_button:
    properties gui.button_properties("quick_button")

style quick_button_text:
    properties gui.text_properties("quick_button")


################################################################################
## Layar Menu Utama dan Menu Permainan
################################################################################

## Layar navigasi ##############################################################
##
## Layar ini di ikutsertakan di menu utama dan permainan, dan menyediakan
## navigasi ke menu lainnya, dan untuk memulai permainan.

screen navigation():

    vbox:
        style_prefix "navigation"

        xpos gui.navigation_xpos
        yalign 0.5

        spacing gui.navigation_spacing

        if main_menu:

            textbutton _("Mulai") action Start()

        else:

            textbutton _("Chapter") action Show("chapter_menu")

        textbutton _("Setting") action ShowMenu("preferences")

        if _in_replay:

            textbutton _("Akhiri Replay") action EndReplay(confirm=True)

        elif not main_menu:

            textbutton _("Menu Utama") action MainMenu()

        textbutton _("Tentang") action ShowMenu("about")

        if renpy.variant("pc") or (renpy.variant("web") and not renpy.variant("mobile")):

            ## Bantuan tidak perlu atau relevan dengan perangkat mobile.
            textbutton _("Bantuan") action ShowMenu("help")

        if renpy.variant("pc"):

            ## Tombol keluar dilarang di iOS dan tidak diperlukan di Android dan
            ## Web.
            textbutton _("Keluar") action Quit(confirm=not main_menu)


style navigation_button is gui_button
style navigation_button_text is gui_button_text

style navigation_button:
    size_group "navigation"
    properties gui.button_properties("navigation_button")

style navigation_button_text:
    properties gui.text_properties("navigation_button")


## Layar Menu Utama
transform main_menu_btn_transform:
    subpixel True
    on idle:
        easein 0.18 zoom 1.0
    on hover:
        easein 0.18 zoom 1.04

screen main_menu():

    tag menu

    add Transform(gui.main_menu_background, xysize=(1920, 1080))

    vbox:
        xalign 0.5
        ypos 445
        spacing 16

        button at main_menu_btn_transform:
            action Start()
            xysize (400, 60)
            background "gui/menu_btn_idle.png"
            hover_background "gui/menu_btn_hover.png"
            text _("Mulai") font "gui/font/PlayfairDisplay-Bold.ttf" color "#1c2833" hover_color "#000000" size 28 bold True align (0.5, 0.5)

        button at main_menu_btn_transform:
            action ShowMenu("chapter_menu")
            xysize (400, 60)
            background "gui/menu_btn_idle.png"
            hover_background "gui/menu_btn_hover.png"
            text _("Buku") font "gui/font/PlayfairDisplay-Bold.ttf" color "#1c2833" hover_color "#000000" size 28 bold True align (0.5, 0.5)

        button at main_menu_btn_transform:
            action ShowMenu("preferences")
            xysize (400, 60)
            background "gui/menu_btn_idle.png"
            hover_background "gui/menu_btn_hover.png"
            text _("Pengaturan") font "gui/font/PlayfairDisplay-Bold.ttf" color "#1c2833" hover_color "#000000" size 28 bold True align (0.5, 0.5)

        button at main_menu_btn_transform:
            action ShowMenu("cerita_menu")
            xysize (400, 60)
            background "gui/menu_btn_idle.png"
            hover_background "gui/menu_btn_hover.png"
            text _("Cerita") font "gui/font/PlayfairDisplay-Bold.ttf" color "#1c2833" hover_color "#000000" size 28 bold True align (0.5, 0.5)

        button at main_menu_btn_transform:
            action ShowMenu("sosmed_menu")
            xysize (400, 60)
            background "gui/menu_btn_idle.png"
            hover_background "gui/menu_btn_hover.png"
            text _("Sosmed") font "gui/font/PlayfairDisplay-Bold.ttf" color "#1c2833" hover_color "#000000" size 28 bold True align (0.5, 0.5)

        button at main_menu_btn_transform:
            action Quit(confirm=not main_menu)
            xysize (400, 60)
            background "gui/menu_btn_idle.png"
            hover_background "gui/menu_btn_hover.png"
            text _("Keluar") font "gui/font/PlayfairDisplay-Bold.ttf" color "#1c2833" hover_color "#000000" size 28 bold True align (0.5, 0.5)




## Screen Sinopsis / Cerita Singkat Game
screen cerita_menu():
    tag menu
    default hovered_kembali_cerita = False

    # Latar belakang warm overlay
    add Transform(gui.game_menu_background, xysize=(1920, 1080))
    add Solid("#120c08ee")

    # Header judul
    vbox:
        xalign 0.5
        ypos 80
        spacing 10
        text _("SINOPSIS / CERITA"):
            font "gui/font/PlayfairDisplay-Bold.ttf"
            size 46
            kerning 8.0
            color "#dfc18c"
            xalign 0.5
            bold True
            outlines [(2, "#3e2715", 0, 0)]
            
        frame:
            xalign 0.5
            xsize 500
            ysize 2
            background Solid("#c3ab7d60")

    # Konten Sinopsis
    frame:
        xalign 0.5
        ypos 160
        xsize 1100
        background Frame(Solid("#1a130ccc"), 18, 18)
        padding (60, 50)

        vbox:
            spacing 20

            # --- Judul & Sinopsis ---
            text _("Kesempatan Kedua"):
                font "gui/font/PlayfairDisplay-Bold.ttf"
                size 36
                color "#dfc18c"
                bold True

            text _("Cerita dimulai dengan anak SMA bernama Shiro Kayaza yang hanya sekedar murid biasa yang tidak tampan, mencolok, dan pintar. Ekskul yang dia ikuti hanya basket dan jika tidak ada ekskul dia akan langsung pulang ke rumahnya lalu bermain game. Itulah kehidupan sehari-harinya yang membosankan.\n\nNamun, pada suatu hari ia bertemu dengan gadis bernama Alisa yang sering dipanggil Lisa. Itu adalah pertemuan yang akan mengubah kehidupan Shiro ke depannya. Itulah awal mula dari kisah yang berjudul DREAM. Penasaran dengan alur cerita? Mainkan sekarang juga!"):
                font gui.text_font
                size 22
                color "#ffffff"
                line_spacing 10
                justify True



    # Tombol KEMBALI (Capsule Gold)
    button:
        action Return()
        hovered SetScreenVariable("hovered_kembali_cerita", True)
        unhovered SetScreenVariable("hovered_kembali_cerita", False)
        xpos 40
        ypos 40
        xysize (180, 52)
        if hovered_kembali_cerita:
            background Frame(Solid("#ffd700"), 26, 26)
        else:
            background Frame(Solid("#c3ab7d"), 26, 26)
        padding (2, 2)
        frame:
            xfill True
            yfill True
            if hovered_kembali_cerita:
                background Frame(Solid("#2d1f12ee"), 24, 24)
            else:
                background Frame(Solid("#1c140cee"), 24, 24)
            hbox:
                align (0.5, 0.5)
                text _("KEMBALI") size 15 bold True kerning 2.0:
                    if hovered_kembali_cerita:
                        color "#ffffff"
                    else:
                        color "#dfc18c"
                    yalign 0.5


## Screen Sosial Media Kreator
screen sosmed_menu():
    tag menu
    default hovered_kembali_sosmed = False

    # Latar belakang warm overlay
    add Transform(gui.game_menu_background, xysize=(1920, 1080))
    add Solid("#120c08ee")

    # Header judul
    vbox:
        xalign 0.5
        ypos 80
        spacing 10
        text _("SOSIAL MEDIA KREATOR"):
            font "gui/font/PlayfairDisplay-Bold.ttf"
            size 44
            kerning 6.0
            color "#dfc18c"
            xalign 0.5
            bold True
            outlines [(2, "#3e2715", 0, 0)]
        frame:
            xalign 0.5
            xsize 550
            ysize 2
            background Solid("#c3ab7d60")

    # Daftar Kreator
    frame:
        xalign 0.5
        yalign 0.52
        xsize 900
        ysize 700
        background Frame(Solid("#1a130ccc"), 18, 18)
        padding (55, 50)

        vbox:
            spacing 30

            text _("Tim Kreator"):
                font "gui/font/PlayfairDisplay-Bold.ttf"
                size 30
                color "#dfc18c"
                bold True

            # --- Kreator 1 (ganti nama, peran, & username IG) ---
            hbox:
                spacing 25
                ysize 60
                frame:
                    yalign 0.5
                    xsize 550
                    background Solid("#ffffff08")
                    padding (16, 10)
                    vbox:
                        spacing 4
                        text _("Nama Kreator 1"):
                            font "gui/font/PlayfairDisplay-Bold.ttf"
                            size 22
                            color "#ffffff"
                        text _("Penulis Cerita"):
                            font gui.text_font
                            size 16
                            color "#dfc18cc0"
                button:
                    action OpenURL("https://www.instagram.com/username_ig_1/")
                    yalign 0.5
                    xysize (230, 44)
                    background Frame(Solid("#c13584"), 12, 12)
                    hover_background Frame(Solid("#e1306c"), 12, 12)
                    hbox:
                        align (0.5, 0.5)
                        spacing 10
                        text "📷" size 18 yalign 0.5
                        text "@username_ig_1":
                            font gui.text_font
                            size 16
                            color "#ffffff"
                            yalign 0.5

            # --- Kreator 2 ---
            hbox:
                spacing 25
                ysize 60
                frame:
                    yalign 0.5
                    xsize 550
                    background Solid("#ffffff08")
                    padding (16, 10)
                    vbox:
                        spacing 4
                        text _("Nama Kreator 2"):
                            font "gui/font/PlayfairDisplay-Bold.ttf"
                            size 22
                            color "#ffffff"
                        text _("Ilustrator / Artist"):
                            font gui.text_font
                            size 16
                            color "#dfc18cc0"
                button:
                    action OpenURL("https://www.instagram.com/username_ig_2/")
                    yalign 0.5
                    xysize (230, 44)
                    background Frame(Solid("#c13584"), 12, 12)
                    hover_background Frame(Solid("#e1306c"), 12, 12)
                    hbox:
                        align (0.5, 0.5)
                        spacing 10
                        text "📷" size 18 yalign 0.5
                        text "@username_ig_2":
                            font gui.text_font
                            size 16
                            color "#ffffff"
                            yalign 0.5

            # --- Kreator 3 ---
            hbox:
                spacing 25
                ysize 60
                frame:
                    yalign 0.5
                    xsize 550
                    background Solid("#ffffff08")
                    padding (16, 10)
                    vbox:
                        spacing 4
                        text _("Nama Kreator 3"):
                            font "gui/font/PlayfairDisplay-Bold.ttf"
                            size 22
                            color "#ffffff"
                        text _("Programmer / Developer"):
                            font gui.text_font
                            size 16
                            color "#dfc18cc0"
                button:
                    action OpenURL("https://www.instagram.com/username_ig_3/")
                    yalign 0.5
                    xysize (230, 44)
                    background Frame(Solid("#c13584"), 12, 12)
                    hover_background Frame(Solid("#e1306c"), 12, 12)
                    hbox:
                        align (0.5, 0.5)
                        spacing 10
                        text "📷" size 18 yalign 0.5
                        text "@username_ig_3":
                            font gui.text_font
                            size 16
                            color "#ffffff"
                            yalign 0.5

    # Tombol KEMBALI (Capsule Gold)
    button:
        action Return()
        hovered SetScreenVariable("hovered_kembali_sosmed", True)
        unhovered SetScreenVariable("hovered_kembali_sosmed", False)
        xpos 40
        ypos 40
        xysize (180, 52)
        if hovered_kembali_sosmed:
            background Frame(Solid("#ffd700"), 26, 26)
        else:
            background Frame(Solid("#c3ab7d"), 26, 26)
        padding (2, 2)
        frame:
            xfill True
            yfill True
            if hovered_kembali_sosmed:
                background Frame(Solid("#2d1f12ee"), 24, 24)
            else:
                background Frame(Solid("#1c140cee"), 24, 24)
            hbox:
                align (0.5, 0.5)
                text _("KEMBALI") size 15 bold True kerning 2.0:
                    if hovered_kembali_sosmed:
                        color "#ffffff"
                    else:
                        color "#dfc18c"
                    yalign 0.5


## layar Menu Permainan ########################################################
##
## Ini menjalaskan struktur dasar yang paling sering di gunakan di layar menu
## permainan, ini ditampilkan beserta layar judul, dan menampilkan latar
## belakang,judul,dan navigasi.
##
## Parameter scroll dapat berisi 'None', atau "viewport" dan "vpgrid". Layar
## ini di maksudkan untuk di gunakan dengan cabang satu atau lebih, yang di
## tempatkan di dalamnya.

screen game_menu(title, scroll=None, yinitial=0.0, spacing=0):

    style_prefix "game_menu"

    if main_menu:
        add Transform(gui.main_menu_background, xysize=(1920, 1080))
    else:
        add Transform(gui.game_menu_background, xysize=(1920, 1080))

    frame:
        style "game_menu_outer_frame"

        hbox:

            ## Memesan tempat untuk bagian navigasi.
            frame:
                style "game_menu_navigation_frame"

            frame:
                style "game_menu_content_frame"

                if scroll == "viewport":

                    viewport:
                        yinitial yinitial
                        scrollbars "vertical"
                        mousewheel True
                        draggable True
                        pagekeys True

                        side_yfill True

                        vbox:
                            spacing spacing

                            transclude

                elif scroll == "vpgrid":

                    vpgrid:
                        cols 1
                        yinitial yinitial

                        scrollbars "vertical"
                        mousewheel True
                        draggable True
                        pagekeys True

                        side_yfill True

                        spacing spacing

                        transclude

                else:

                    transclude

    # use navigation dihapus sesuai permintaan agar tidak ada double menu
    # use navigation

    textbutton _("Kembali"):
        style "return_button"

        action Return()

    label title

    if main_menu:
        key "game_menu" action ShowMenu("main_menu")


style game_menu_outer_frame is empty
style game_menu_navigation_frame is empty
style game_menu_content_frame is empty
style game_menu_viewport is gui_viewport
style game_menu_side is gui_side
style game_menu_scrollbar is gui_vscrollbar

style game_menu_label is gui_label
style game_menu_label_text is gui_label_text

style return_button is navigation_button
style return_button_text is navigation_button_text

style game_menu_outer_frame:
    bottom_padding 45
    top_padding 180

    background "gui/overlay/game_menu.png"

style game_menu_navigation_frame:
    xsize 420
    yfill True

style game_menu_content_frame:
    left_margin 60
    right_margin 30
    top_margin 15

style game_menu_viewport:
    xsize 1380

style game_menu_vscrollbar:
    unscrollable gui.unscrollable

style game_menu_side:
    spacing 15

style game_menu_label:
    xpos 75
    ysize 180

style game_menu_label_text:
    size 75
    color gui.accent_color
    yalign 0.5

style return_button:
    xpos gui.navigation_xpos
    yalign 1.0
    yoffset -45


## Layar About #################################################################
##
## Layar ini menampilkan credit dan informasi copyright tentang game dan Ren.Py.
##
## Tidak ada yang spesial dengan layar ini, semenjak ini juga berperan sebagai
## contoh bagaimana membuat layar custom.

screen about():

    tag menu

    ## Pernyataan 'use' ini mengikutsertakan layar game_menu ke dalam layar ini.
    ## Percabangan vbox lalu di ikutsertakan kedalam viewport di dalam layar
    ## game_menu.
    use game_menu(_("Tentang"), scroll="viewport"):

        style_prefix "about"

        vbox:

            label "[config.name!t]"
            text "{color=#00BFFF}SEASON 1\n{/color}"
            ## gui.about biasanya di set di options.rpy.
            if gui.about:
                text "[gui.about!t]\n"

            text _("cerita dimulai dengan anak SMA bernama shiro kayaza yang hanya sekedar murid biasa yang tidak tampan, mencolok, dan pintar. Ekskul yang dia ikuti hanya basket dan jika tidak ada ekskul dia akan langsung pulang kerumahnya lalu bermain game. Itulah kehidupan sehari harinya yang membosankan. Namun, pada sesuatu hari ia bertemu dengan gadis bernama Alisa yang sering dipanggil Lisa, itu adalah pertemuan yang akan mengubah kehidupan shiro kedepannya. Itulah awal mula dari kisah yang berjudul DREAM. Penasaran dengan alur cerita? mainkan sekarang juga ")
style about_label is gui_label
style about_label_text is gui_label_text
style about_text is gui_text

style about_label_text:
    size gui.label_text_size


## Layar Load and Save #########################################################
##
## Layar ini bertanggungjawab untuk mengijinkan pemain menyimpan dan
## meload lagi. Semenjak mereke hampir memiliki hal yang sama, keduanya di
## implementasinan di percabangan layar ketiga, file_slots.
##
## https://www.renpy.org/doc/html/screen_special.html#save https://
## www.renpy.org/doc/html/screen_special.html#load

screen save():
    tag menu
    use chapter_menu

screen load():

    tag menu

    use chapter_menu


style page_label is gui_label
style page_label_text is gui_label_text
style page_button is gui_button
style page_button_text is gui_button_text

style slot_button is gui_button
style slot_button_text is gui_button_text
style slot_time_text is slot_button_text
style slot_name_text is slot_button_text

style page_label:
    xpadding 75
    ypadding 5
    xalign 0.5

style page_label_text:
    textalign 0.5
    layout "subtitle"
    hover_color gui.hover_color

style page_button:
    properties gui.button_properties("page_button")

style page_button_text:
    properties gui.text_properties("page_button")

style slot_button:
    properties gui.button_properties("slot_button")

style slot_button_text:
    properties gui.text_properties("slot_button")


## Layar preferensi/opsi #######################################################
##
## Layar preferensi mengijinkan pemain untuk mengkonfigurasi permainan untuk
## menyesuaikan gaya bermain masing masing individu.
##
## https://www.renpy.org/doc/html/screen_special.html#preferences

## Warna tema emas untuk screen Pengaturan
define PREF_GOLD        = "#c8a84b"
define PREF_GOLD_DARK   = "#8a6e28"
define PREF_GOLD_BRIGHT = "#e8cc78"
define PREF_PANEL_BG    = "#1a120888"
define PREF_PANEL_BORDER= "#c8a84b"
define PREF_BTN_IDLE    = "#2a1e0ccc"
define PREF_BTN_HOV     = "#3d2d10dd"
define PREF_BTN_SEL     = "#5a3e0fee"
define PREF_TEXT_IDLE   = "#d4b87a"
define PREF_TEXT_HOV    = "#ffe8a0"
define PREF_TEXT_SEL    = "#ffe066"

screen preferences():

    tag menu

    ## Latar belakang game SMA
    if main_menu:
        add Transform(gui.main_menu_background, xysize=(1920, 1080))
    else:
        add Transform(gui.game_menu_background, xysize=(1920, 1080))

    ## Overlay hangat semi-transparan
    add Solid("#110900bb")

    ## ─── JUDUL "Pengaturan" kiri atas ─────────────────────────────────────
    text _("Pengaturan"):
        font "gui/font/PlayfairDisplay-Bold.ttf"
        size 72
        italic True
        color "#e8cc78"
        bold True
        outlines [(3, "#3e2000", 0, 0)]
        xpos 60
        ypos 30

    ## Dekorasi garis emas di bawah judul
    frame:
        xpos 60
        ypos 112
        xsize 380
        ysize 3
        background Solid("#c8a84b80")

    ## ─── KONTEN UTAMA ──────────────────────────────────────────────────────
    vbox:
        xpos 220
        ypos 138
        xsize 840
        spacing 18

        ## === BARIS 1: Tampilan | Lompat Dialog | Otomatis Maju ===============
        hbox:
            xfill True
            spacing 16

            ## --- Kartu TAMPILAN ---
            if renpy.variant("pc") or renpy.variant("web"):
                frame:
                    xsize 248
                    ysize 148
                    padding (2, 2, 2, 2)
                    background Frame(Solid("#c8a84b"), 12, 12)

                    frame:
                        xfill True
                        yfill True
                        background Frame(Solid("#1e1408e8"), 10, 10)
                        padding (14, 12, 14, 10)

                        vbox:
                            spacing 10

                            hbox:
                                spacing 6
                                text "🖥" size 14 yalign 0.5
                                text _("TAMPILAN"):
                                    size 13
                                    color "#e8cc78"
                                    bold True
                                    kerning 1.5
                                    yalign 0.5

                            frame:
                                xfill True
                                ysize 1
                                background Solid("#c8a84b50")

                            hbox:
                                spacing 8

                                textbutton _("Jendela"):
                                    action Preference("display", "window")
                                    xsize 98
                                    ysize 40
                                    background Frame(Solid("#2a1e0ccc"), 8, 8)
                                    hover_background Frame(Solid("#3d2d10dd"), 8, 8)
                                    selected_background Frame(Solid("#5a3e0fee"), 8, 8)
                                    foreground Frame(Solid("#c8a84b40"), 8, 8)
                                    selected_foreground Frame(Solid("#c8a84b90"), 8, 8)
                                    text_color "#c8a84b"
                                    text_hover_color "#ffe8a0"
                                    text_selected_color "#ffe066"
                                    text_size 14
                                    text_yalign 0.5
                                    text_xalign 0.5
                                    text_bold True

                                textbutton _("Layar Penuh"):
                                    action Preference("display", "fullscreen")
                                    xsize 98
                                    ysize 40
                                    background Frame(Solid("#2a1e0ccc"), 8, 8)
                                    hover_background Frame(Solid("#3d2d10dd"), 8, 8)
                                    selected_background Frame(Solid("#5a3e0fee"), 8, 8)
                                    foreground Frame(Solid("#c8a84b40"), 8, 8)
                                    selected_foreground Frame(Solid("#c8a84b90"), 8, 8)
                                    text_color "#c8a84b"
                                    text_hover_color "#ffe8a0"
                                    text_selected_color "#ffe066"
                                    text_size 14
                                    text_yalign 0.5
                                    text_xalign 0.5
                                    text_bold True

            ## --- Kartu LOMPAT DIALOG ---
            frame:
                xsize 300
                ysize 148
                padding (2, 2, 2, 2)
                background Frame(Solid("#c8a84b"), 12, 12)

                frame:
                    xfill True
                    yfill True
                    background Frame(Solid("#1e1408e8"), 10, 10)
                    padding (14, 12, 14, 10)

                    vbox:
                        spacing 10

                        hbox:
                            spacing 6
                            text "⏭" size 14 yalign 0.5
                            text _("LOMPAT DIALOG"):
                                size 13
                                color "#e8cc78"
                                bold True
                                kerning 1.5
                                yalign 0.5

                        frame:
                            xfill True
                            ysize 1
                            background Solid("#c8a84b50")

                        hbox:
                            spacing 8

                            textbutton _("Belum Terlihat"):
                                action Preference("skip", "toggle")
                                xsize 128
                                ysize 40
                                background Frame(Solid("#2a1e0ccc"), 8, 8)
                                hover_background Frame(Solid("#3d2d10dd"), 8, 8)
                                selected_background Frame(Solid("#5a3e0fee"), 8, 8)
                                foreground Frame(Solid("#c8a84b40"), 8, 8)
                                selected_foreground Frame(Solid("#c8a84b90"), 8, 8)
                                text_color "#c8a84b"
                                text_hover_color "#ffe8a0"
                                text_selected_color "#ffe066"
                                text_size 13
                                text_yalign 0.5
                                text_xalign 0.5
                                text_bold True

                            textbutton _("Setelah Pilihan"):
                                action Preference("after choices", "toggle")
                                xsize 128
                                ysize 40
                                background Frame(Solid("#2a1e0ccc"), 8, 8)
                                hover_background Frame(Solid("#3d2d10dd"), 8, 8)
                                selected_background Frame(Solid("#5a3e0fee"), 8, 8)
                                foreground Frame(Solid("#c8a84b40"), 8, 8)
                                selected_foreground Frame(Solid("#c8a84b90"), 8, 8)
                                text_color "#c8a84b"
                                text_hover_color "#ffe8a0"
                                text_selected_color "#ffe066"
                                text_size 13
                                text_yalign 0.5
                                text_xalign 0.5
                                text_bold True

            ## --- Kartu OTOMATIS MAJU ---
            frame:
                xsize 256
                ysize 148
                padding (2, 2, 2, 2)
                background Frame(Solid("#c8a84b"), 12, 12)

                frame:
                    xfill True
                    yfill True
                    background Frame(Solid("#1e1408e8"), 10, 10)
                    padding (14, 12, 14, 10)

                    vbox:
                        spacing 10

                        hbox:
                            spacing 6
                            text "▶▶" size 12 color "#e8cc78" yalign 0.5
                            text _("OTOMATIS MAJU"):
                                size 13
                                color "#e8cc78"
                                bold True
                                kerning 1.5
                                yalign 0.5

                        frame:
                            xfill True
                            ysize 1
                            background Solid("#c8a84b50")

                        textbutton _("Aktifkan/Nonaktifkan"):
                            action Preference("auto-forward", "toggle")
                            xsize 220
                            ysize 40
                            background Frame(Solid("#2a1e0ccc"), 8, 8)
                            hover_background Frame(Solid("#3d2d10dd"), 8, 8)
                            selected_background Frame(Solid("#5a3e0fee"), 8, 8)
                            foreground Frame(Solid("#c8a84b40"), 8, 8)
                            selected_foreground Frame(Solid("#c8a84b90"), 8, 8)
                            text_color "#c8a84b"
                            text_hover_color "#ffe8a0"
                            text_selected_color "#ffe066"
                            text_size 13
                            text_yalign 0.5
                            text_xalign 0.5
                            text_bold True

        ## === BARIS 2: Kecepatan Text + Waktu Otomatis-Maju ===================
        hbox:
            xfill True
            spacing 16

            ## --- Kartu KECEPATAN TEXT ---
            frame:
                xsize 410
                ysize 100
                padding (2, 2, 2, 2)
                background Frame(Solid("#c8a84b"), 12, 12)

                frame:
                    xfill True
                    yfill True
                    background Frame(Solid("#1e1408e8"), 10, 10)
                    padding (16, 10, 16, 10)

                    vbox:
                        spacing 8

                        hbox:
                            spacing 6
                            text "✏" size 14 yalign 0.5
                            text _("KECEPATAN TEXT"):
                                size 13
                                color "#e8cc78"
                                bold True
                                kerning 1.5
                                yalign 0.5

                        frame:
                            xfill True
                            ysize 1
                            background Solid("#c8a84b50")

                        bar:
                            value Preference("text speed")
                            xfill True
                            ysize 22
                            left_bar Frame(Solid("#c8a84b"), 4, 4)
                            right_bar Frame(Solid("#2a1a0880"), 4, 4)
                            thumb Frame(Solid("#ffe066"), 3, 3)
                            thumb_offset 11

            ## --- Kartu WAKTU OTOMATIS-MAJU ---
            frame:
                xsize 410
                ysize 100
                padding (2, 2, 2, 2)
                background Frame(Solid("#c8a84b"), 12, 12)

                frame:
                    xfill True
                    yfill True
                    background Frame(Solid("#1e1408e8"), 10, 10)
                    padding (16, 10, 16, 10)

                    vbox:
                        spacing 8

                        hbox:
                            spacing 6
                            text "⏱" size 14 yalign 0.5
                            text _("WAKTU OTOMATIS-MAJU"):
                                size 13
                                color "#e8cc78"
                                bold True
                                kerning 1.5
                                yalign 0.5

                        frame:
                            xfill True
                            ysize 1
                            background Solid("#c8a84b50")

                        bar:
                            value Preference("auto-forward time")
                            xfill True
                            ysize 22
                            left_bar Frame(Solid("#c8a84b"), 4, 4)
                            right_bar Frame(Solid("#2a1a0880"), 4, 4)
                            thumb Frame(Solid("#ffe066"), 3, 3)
                            thumb_offset 11

        ## === BARIS 3: Panel Audio ============================================
        frame:
            xfill True
            ysize 200
            padding (2, 2, 2, 2)
            background Frame(Solid("#c8a84b"), 14, 14)

            frame:
                xfill True
                yfill True
                background Frame(Solid("#1e1408e8"), 12, 12)
                padding (18, 14, 18, 14)

                vbox:
                    xfill True
                    spacing 12

                    ## Header Audio
                    hbox:
                        spacing 6
                        text "♪" size 16 color "#e8cc78" yalign 0.5
                        text _("PENGATURAN AUDIO"):
                            size 14
                            color "#e8cc78"
                            bold True
                            kerning 1.5
                            yalign 0.5

                    frame:
                        xfill True
                        ysize 1
                        background Solid("#c8a84b50")

                    ## Tiga slider volume dalam satu baris
                    hbox:
                        xfill True
                        spacing 20

                        ## Volume Musik
                        if config.has_music:
                            vbox:
                                xsize 240
                                spacing 5

                                hbox:
                                    xfill True
                                    spacing 4
                                    text "🎵" size 13 yalign 0.5
                                    text _("Music Volume"):
                                        size 13
                                        color "#d4b87a"
                                        yalign 0.5
                                    text _("[int(_preferences.get_volume('music') * 100)]%"):
                                        size 13
                                        color "#ffe066"
                                        yalign 0.5
                                        xalign 1.0

                                bar:
                                    value Preference("music volume")
                                    xfill True
                                    ysize 20
                                    left_bar Frame(Solid("#c8a84b"), 4, 4)
                                    right_bar Frame(Solid("#2a1a0880"), 4, 4)
                                    thumb Frame(Solid("#ffe066"), 3, 3)
                                    thumb_offset 10

                        ## Volume Suara
                        if config.has_sound:
                            vbox:
                                xsize 240
                                spacing 5

                                hbox:
                                    xfill True
                                    spacing 4
                                    text "🔊" size 13 yalign 0.5
                                    text _("Sound Volume"):
                                        size 13
                                        color "#d4b87a"
                                        yalign 0.5
                                    text _("[int(_preferences.get_volume('sound') * 100)]%"):
                                        size 13
                                        color "#ffe066"
                                        yalign 0.5
                                        xalign 1.0

                                bar:
                                    value Preference("sound volume")
                                    xfill True
                                    ysize 20
                                    left_bar Frame(Solid("#c8a84b"), 4, 4)
                                    right_bar Frame(Solid("#2a1a0880"), 4, 4)
                                    thumb Frame(Solid("#ffe066"), 3, 3)
                                    thumb_offset 10

                        ## Volume Vokal
                        if config.has_voice:
                            vbox:
                                xsize 240
                                spacing 5

                                hbox:
                                    xfill True
                                    spacing 4
                                    text "🎙" size 13 yalign 0.5
                                    text _("Vocal Volume"):
                                        size 13
                                        color "#d4b87a"
                                        yalign 0.5
                                    text _("[int(_preferences.get_volume('voice') * 100)]%"):
                                        size 13
                                        color "#ffe066"
                                        yalign 0.5
                                        xalign 1.0

                                bar:
                                    value Preference("voice volume")
                                    xfill True
                                    ysize 20
                                    left_bar Frame(Solid("#c8a84b"), 4, 4)
                                    right_bar Frame(Solid("#2a1a0880"), 4, 4)
                                    thumb Frame(Solid("#ffe066"), 3, 3)
                                    thumb_offset 10

                    ## Tombol Senyapkan Semua
                    if config.has_music or config.has_sound or config.has_voice:
                        hbox:
                            xalign 1.0

                            textbutton _("🔇 Senyapkan Semua"):
                                action Preference("all mute", "toggle")
                                xsize 220
                                ysize 36
                                background Frame(Solid("#2a1e0ccc"), 8, 8)
                                hover_background Frame(Solid("#3d2d10dd"), 8, 8)
                                selected_background Frame(Solid("#5a3e0fee"), 8, 8)
                                foreground Frame(Solid("#c8a84b40"), 8, 8)
                                selected_foreground Frame(Solid("#c8a84b90"), 8, 8)
                                text_color "#c8a84b"
                                text_hover_color "#ffe8a0"
                                text_selected_color "#ffe066"
                                text_size 13
                                text_yalign 0.5
                                text_xalign 0.5
                                text_bold True

    ## ─── Tombol KEMBALI pojok kiri bawah ─────────────────────────────────
    default hov_kembali_pref = False

    button:
        action Return()
        hovered SetScreenVariable("hov_kembali_pref", True)
        unhovered SetScreenVariable("hov_kembali_pref", False)
        xpos 40
        yalign 1.0
        yoffset -40
        xysize (200, 56)
        if hov_kembali_pref:
            background Frame(Solid("#e8cc78"), 28, 28)
        else:
            background Frame(Solid("#c8a84b"), 28, 28)
        padding (2, 2)
        frame:
            xfill True
            yfill True
            if hov_kembali_pref:
                background Frame(Solid("#2d1f12ee"), 26, 26)
            else:
                background Frame(Solid("#1c140cee"), 26, 26)
            hbox:
                align (0.5, 0.5)
                spacing 8
                text "◄" size 18 yalign 0.5:
                    if hov_kembali_pref:
                        color "#ffffff"
                    else:
                        color "#e8cc78"
                text _("Kembali") size 20 bold True yalign 0.5:
                    if hov_kembali_pref:
                        color "#ffffff"
                    else:
                        color "#e8cc78"

    if main_menu:
        key "game_menu" action ShowMenu("main_menu")


style pref_label is gui_label
style pref_label_text is gui_label_text
style pref_vbox is vbox

style radio_label is pref_label
style radio_label_text is pref_label_text
style radio_button is gui_button
style radio_button_text is gui_button_text
style radio_vbox is pref_vbox

style check_label is pref_label
style check_label_text is pref_label_text
style check_button is gui_button
style check_button_text is gui_button_text
style check_vbox is pref_vbox

style slider_label is pref_label
style slider_label_text is pref_label_text
style slider_slider is gui_slider
style slider_button is gui_button
style slider_button_text is gui_button_text
style slider_pref_vbox is pref_vbox

style mute_all_button is check_button
style mute_all_button_text is check_button_text

## Style bar emas untuk layar Pengaturan
style pref_gold_bar is bar:
    ysize 22
    left_bar Frame(Solid("#c8a84b"), 4, 4)
    right_bar Frame(Solid("#2a1a0880"), 4, 4)
    thumb Frame(Solid("#ffe066"), 3, 3)
    thumb_offset 11

style pref_label:
    top_margin gui.pref_spacing
    bottom_margin 3

style pref_label_text:
    yalign 1.0

style pref_vbox:
    xsize 338

style radio_vbox:
    spacing gui.pref_button_spacing

style radio_button:
    properties gui.button_properties("radio_button")
    foreground "gui/button/radio_[prefix_]foreground.png"

style radio_button_text:
    properties gui.text_properties("radio_button")

style check_vbox:
    spacing gui.pref_button_spacing

style check_button:
    properties gui.button_properties("check_button")
    foreground "gui/button/check_[prefix_]foreground.png"

style check_button_text:
    properties gui.text_properties("check_button")

style slider_slider:
    xsize 525

style slider_button:
    properties gui.button_properties("slider_button")
    yalign 0.5
    left_margin 15

style slider_button_text:
    properties gui.text_properties("slider_button")

style slider_vbox:
    xsize 675


## Layar Riwayat ###############################################################
##
## Layar yang menampilkan History dialog kepada pemain. Semenjak tidak ada yang
## spesial tentang layar ini, ini memiliki akses ke history dialog yang di
## simpan di _history_list.
##
## https://www.renpy.org/doc/html/history.html

screen history():

    tag menu

    ## Hindari mempredisi layar ini, ini dapat berukuran sangat besar.
    predict False

    use game_menu(_("Riwayat"), scroll=("vpgrid" if gui.history_height else "viewport"), yinitial=1.0, spacing=gui.history_spacing):

        style_prefix "history"

        for h in _history_list:

            window:

                ## Ini menampilkan layar secara semestinya jika history_height
                ## memiliki value None.
                has fixed:
                    yfit True

                if h.who:

                    label h.who:
                        style "history_name"
                        substitute False

                        ## Mengambil warna dari text 'who' dari karakter, jika
                        ## di set.
                        if "color" in h.who_args:
                            text_color h.who_args["color"]

                $ what = renpy.filter_text_tags(h.what, allow=gui.history_allow_tags)
                text what:
                    substitute False

        if not _history_list:
            label _("Riwayat dialog kosong.")


## Ini menentukan tag apa yang diizinkan ditampilkan di layar sejarah/catatan.

define gui.history_allow_tags = { "alt", "noalt", "rt", "rb", "art" }


style history_window is empty

style history_name is gui_label
style history_name_text is gui_label_text
style history_text is gui_text

style history_label is gui_label
style history_label_text is gui_label_text

style history_window:
    xfill True
    ysize gui.history_height

style history_name:
    xpos gui.history_name_xpos
    xanchor gui.history_name_xalign
    ypos gui.history_name_ypos
    xsize gui.history_name_width

style history_name_text:
    min_width gui.history_name_width
    textalign gui.history_name_xalign

style history_text:
    xpos gui.history_text_xpos
    ypos gui.history_text_ypos
    xanchor gui.history_text_xalign
    xsize gui.history_text_width
    min_width gui.history_text_width
    textalign gui.history_text_xalign
    layout ("subtitle" if gui.history_text_xalign else "tex")

style history_label:
    xfill True

style history_label_text:
    xalign 0.5


## Layar Bantuan ###############################################################
##
## Layar Bantuan yang didesain ulang dengan tema biru navy gelap premium.
## Menampilkan panduan kontrol keyboard, mouse, dan informasi chapter.

## Transisi tab bantuan
transform help_tab_show:
    on show:
        alpha 0.0
        linear 0.2 alpha 1.0
    on hide:
        linear 0.15 alpha 0.0

## Animasi kartu bantuan
transform help_card_hover:
    on idle:
        easein 0.2 yoffset 0 alpha 0.9
    on hover:
        easein 0.2 yoffset -4 alpha 1.0

screen help():

    tag menu

    default device = "keyboard"

    ## Latar belakang — full navy gelap gradient
    add Transform(gui.game_menu_background, xysize=(1920, 1080))
    add Solid("#020d1aee")

    ## Panel utama tengah
    frame:
        xalign 0.5
        yalign 0.5
        xysize (1180, 780)
        padding (0, 0)
        background Frame(Solid("#040f1f"), 20, 20)

        vbox:
            xfill True
            yfill True
            spacing 0

            ## ─── HEADER ───────────────────────────────────────────────────
            frame:
                xfill True
                ysize 90
                padding (40, 0)
                background Solid("#061629")

                hbox:
                    xfill True
                    yalign 0.5
                    spacing 0

                    ## Judul kiri
                    vbox:
                        yalign 0.5
                        spacing 4
                        hbox:
                            spacing 12
                            text "📘":
                                size 28
                                yalign 0.5
                            text _("P A N D U A N"):
                                size 28
                                color "#4fc3f7"
                                bold True
                                kerning 6.0
                                yalign 0.5
                        text _("Cara bermain & kontrol game DREAM"):
                            size 14
                            color "#4fc3f780"
                            kerning 1.0

                    ## Spacer dorong tab ke kanan
                    frame:
                        xsize 1
                        yfill True
                        background Solid("#00000000")

                    ## Tab navigasi (kanan header)
                    hbox:
                        yalign 0.5
                        spacing 8

                        ## Tab Keyboard
                        button:
                            action SetScreenVariable("device", "keyboard")
                            xysize (148, 52)
                            background Frame(
                                Solid("#0e2a4a" if device != "keyboard" else "#1565c0"),
                                10, 10
                            )
                            hover_background Frame(Solid("#1a4080"), 10, 10)
                            hbox:
                                align (0.5, 0.5)
                                spacing 8
                                text "⌨":
                                    size 18
                                    color ("#4fc3f7" if device == "keyboard" else "#4fc3f780")
                                    yalign 0.5
                                text _("Keyboard"):
                                    size 15
                                    color ("#ffffff" if device == "keyboard" else "#7ab8cc")
                                    bold (device == "keyboard")
                                    yalign 0.5

                        ## Tab Mouse
                        button:
                            action SetScreenVariable("device", "mouse")
                            xysize (120, 52)
                            background Frame(
                                Solid("#0e2a4a" if device != "mouse" else "#1565c0"),
                                10, 10
                            )
                            hover_background Frame(Solid("#1a4080"), 10, 10)
                            hbox:
                                align (0.5, 0.5)
                                spacing 8
                                text "🖱":
                                    size 18
                                    color ("#4fc3f7" if device == "mouse" else "#4fc3f780")
                                    yalign 0.5
                                text _("Mouse"):
                                    size 15
                                    color ("#ffffff" if device == "mouse" else "#7ab8cc")
                                    bold (device == "mouse")
                                    yalign 0.5

                        ## Tab Chapter
                        button:
                            action SetScreenVariable("device", "chapter")
                            xysize (140, 52)
                            background Frame(
                                Solid("#0e2a4a" if device != "chapter" else "#1565c0"),
                                10, 10
                            )
                            hover_background Frame(Solid("#1a4080"), 10, 10)
                            hbox:
                                align (0.5, 0.5)
                                spacing 8
                                text "📖":
                                    size 18
                                    color ("#4fc3f7" if device == "chapter" else "#4fc3f780")
                                    yalign 0.5
                                text _("Chapter"):
                                    size 15
                                    color ("#ffffff" if device == "chapter" else "#7ab8cc")
                                    bold (device == "chapter")
                                    yalign 0.5

            ## Garis pemisah bawah header
            frame:
                xfill True
                ysize 2
                background Solid("#1565c060")

            ## ─── KONTEN ────────────────────────────────────────────────────
            frame:
                xfill True
                yfill True
                padding (36, 28, 36, 28)
                background Solid("#040f1f")

                if device == "keyboard":
                    use keyboard_help_new
                elif device == "mouse":
                    use mouse_help_new
                elif device == "chapter":
                    use chapter_help_new

    ## Tombol Kembali
    button:
        action Return()
        xpos 40
        ypos 30
        xysize (160, 48)
        background Frame(Solid("#0e2a4a"), 12, 12)
        hover_background Frame(Solid("#1565c0"), 12, 12)
        hbox:
            align (0.5, 0.5)
            spacing 10
            text "◀":
                size 16
                color "#4fc3f7"
                yalign 0.5
            text _("KEMBALI"):
                size 15
                color "#ffffff"
                kerning 2.0
                yalign 0.5


## ─── KONFIGURASI KEYMAP: MENGHAPUS & MENAMBAH SHORTCUT ────────────────────────
init 1 python:
    ## Eksekusi ini di pass init yang lebih lambat agar menimpa config utama
    
    ## 1. Nonaktifkan fitur skip sepenuhnya (Ctrl dan Tab)
    config.keymap['skip'] = []
    config.keymap['toggle_skip'] = []
    
    ## 2. Nonaktifkan fitur sembunyikan UI (H)
    config.keymap['hide_windows'] = ['mouseup_2']  ## sisakan klik tengah mouse
    
    ## 3. Nonaktifkan rollback dan rollforward (Page Up / Page Down)
    config.keymap['rollback'] = ['mousedown_4', 'joy_rollback']
    config.keymap['rollforward'] = ['mousedown_5', 'joy_rollforward']
    
    ## 4. Matikan Buka Menu dari keyboard (M / Esc / Klik Kanan) -- DIHAPUS FULL
    config.keymap['game_menu'] = []

    ## 5. Matikan Arrow Keys (Panah) untuk navigasi UI
    config.keymap['focus_left'] = []
    config.keymap['focus_right'] = []
    config.keymap['focus_up'] = []
    config.keymap['focus_down'] = []

    ## 6. Matikan Quick Save (Q) & Quick Load (L)
    config.keymap['quicksave'] = []
    config.keymap['quickload'] = []

    ## 7. Matikan Enter (Lanjutkan teks pakai klik/spasi saja)
    config.keymap['dismiss'] = ['K_SPACE', 'mouseup_1', 'joy_dismiss']
    config.keymap['button_select'] = ['K_SPACE', 'mouseup_1', 'joy_select']

    ## 8. Matikan fitur suara narator otomatis (V)
    config.keymap['self_voicing'] = []


## ─── SUB LAYAR: Keyboard Help ─────────────────────────────────────────────────
screen keyboard_help_new():

    vbox:
        xfill True
        spacing 16

        ## Deskripsi singkat
        hbox:
            spacing 8
            text "⌨"  size 16 color "#4fc3f7" yalign 0.5
            text _("SHORTCUT KEYBOARD"):
                size 14
                color "#4fc3f7"
                bold True
                kerning 3.0
                yalign 0.5

        frame:
            xfill True
            ysize 1
            background Solid("#1565c050")

        null height 4

        ## Grid 2 kolom
        hbox:
            xfill True
            spacing 16

            ## Kolom kiri
            vbox:
                xsize 540
                spacing 12

                ## Baris tombol Kiri
                for key_label, key_desc in [
                    ("Space",         _("Lanjutkan dialog tanpa memilih pilihan")),
                    ("F",             _("Mode Layar Penuh (Fullscreen)")),
                    ("T",             _("Translate dialog ke Bahasa Inggris")),
                ]:
                    frame at help_card_hover:
                        xfill True
                        ysize 58
                        padding (18, 0)
                        background Frame(Solid("#071825"), 10, 10)
                        hover_background Frame(Solid("#0a2040"), 10, 10)

                        hbox:
                            xfill True
                            yalign 0.5
                            spacing 0

                            ## Key badge
                            frame:
                                xsize 148
                                yalign 0.5
                                padding (10, 6)
                                background Frame(Solid("#0e2a4a"), 8, 8)
                                text _(key_label):
                                    size 14
                                    color "#4fc3f7"
                                    bold True
                                    xalign 1.0
                                    textalign 1.0

                            null width 16

                            ## Deskripsi
                            text _(key_desc):
                                size 15
                                color "#c0d8ec"
                                yalign 0.5

            ## Kolom kanan
            vbox:
                xsize 540
                spacing 12

                for key_label, key_desc in [
                    ("A",             _("Jalankan mode cerita otomatis (Auto)")),
                    ("C",             _("Nyalakan Suara Pembaca dari Clipboard")),
                    ("S",             _("Ambil tangkapan layar (screenshot game)")),
                ]:
                    frame at help_card_hover:
                        xfill True
                        ysize 58
                        padding (18, 0)
                        background Frame(Solid("#071825"), 10, 10)
                        hover_background Frame(Solid("#0a2040"), 10, 10)

                        hbox:
                            xfill True
                            yalign 0.5
                            spacing 0

                            frame:
                                xsize 148
                                yalign 0.5
                                padding (10, 6)
                                background Frame(Solid("#0e2a4a"), 8, 8)
                                text key_label:
                                    size 14
                                    color "#4fc3f7"
                                    bold True
                                    xalign 1.0
                                    textalign 1.0

                            null width 16

                            text _(key_desc):
                                size 15
                                color "#c0d8ec"
                                yalign 0.5

        ## Tips bawah
        null height 8
        frame:
            xfill True
            padding (18, 14)
            background Frame(Solid("#061629"), 10, 10)
            hbox:
                spacing 10
                text "💡" size 16 yalign 0.5
                text _("Tips: Tekan tombol {b}A{/b} untuk menyalakan mode otomatis agar cerita berjalan tanpa perlu diklik manual."):
                    size 14
                    color "#7ab8cc"
                    yalign 0.5


## ─── SUB LAYAR: Mouse Help ────────────────────────────────────────────────────
screen mouse_help_new():

    vbox:
        xfill True
        spacing 16

        hbox:
            spacing 8
            text "🖱"  size 16 color "#4fc3f7" yalign 0.5
            text _("KONTROL MOUSE"):
                size 14
                color "#4fc3f7"
                bold True
                kerning 3.0
                yalign 0.5

        frame:
            xfill True
            ysize 1
            background Solid("#1565c050")

        null height 4

        ## Kartu mouse visual
        hbox:
            xalign 0.5
            spacing 24

            for icon, key_label, key_desc in [
                ("🖱️",  _("Klik Kiri"),         _("Lanjutkan dialog\n& aktifkan pilihan")),
                ("🖲️",  _("Klik Tengah"),       _("Sembunyikan\nantarmuka UI")),
            ]:
                frame at help_card_hover:
                    xsize 196
                    ysize 168
                    padding (16, 18)
                    background Frame(Solid("#071825"), 14, 14)
                    hover_background Frame(Solid("#0a2040"), 14, 14)

                    vbox:
                        xalign 0.5
                        spacing 10

                        text icon:
                            size 36
                            xalign 0.5

                        frame:
                            xalign 0.5
                            padding (12, 6)
                            background Frame(Solid("#0e2a4a"), 8, 8)
                            text _(key_label):
                                size 13
                                color "#4fc3f7"
                                bold True
                                xalign 0.5
                                textalign 0.5

                        text _(key_desc):
                            size 13
                            color "#a0c8e0"
                            xalign 0.5
                            textalign 0.5

        null height 8
        frame:
            xfill True
            padding (18, 14)
            background Frame(Solid("#061629"), 10, 10)
            hbox:
                spacing 10
                text "💡" size 16 yalign 0.5
                text _("Tips: Klik kanan kapan saja selama gameplay untuk membuka menu simpan / muat dengan cepat."):
                    size 14
                    color "#7ab8cc"
                    yalign 0.5


## ─── SUB LAYAR: Chapter Help ──────────────────────────────────────────────────
screen chapter_help_new():

    vbox:
        xfill True
        spacing 16

        hbox:
            spacing 8
            text "📖"  size 16 color "#4fc3f7" yalign 0.5
            text _("PANDUAN CHAPTER"):
                size 14
                color "#4fc3f7"
                bold True
                kerning 3.0
                yalign 0.5

        frame:
            xfill True
            ysize 1
            background Solid("#1565c050")

        null height 4

        ## Baris 1: 3 kartu info chapter
        hbox:
            xfill True
            spacing 16

            for ch_icon, ch_title, ch_desc in [("🔓", _("Chapter Terbuka"), _("Chapter yang sudah bisa\ndimainkan. Klik kartu\nuntuk mulai bermain.")), ("🔒", _("Chapter Terkunci"), _("Selesaikan chapter\nsebelumnya terlebih\ndahulu untuk membuka.")), ("✅", _("Chapter Selesai"), _("Chapter yang sudah\npernah kamu selesaikan.\nBisa dimainkan ulang."))]:
                frame at help_card_hover:
                    xsize 338
                    ysize 160
                    padding (22, 18)
                    background Frame(Solid("#071825"), 14, 14)
                    hover_background Frame(Solid("#0a2040"), 14, 14)

                    vbox:
                        spacing 12

                        hbox:
                            spacing 10
                            text ch_icon:
                                size 24
                                yalign 0.5
                            text ch_title:
                                size 16
                                color "#4fc3f7"
                                bold True
                                yalign 0.5

                        frame:
                            xfill True
                            ysize 1
                            background Solid("#1565c040")

                        text ch_desc:
                            size 14
                            color "#a0c8e0"
                            line_spacing 4

        null height 4

        ## Baris 2: Panduan navigasi chapter
        hbox:
            xfill True
            spacing 16

            for nav_icon, nav_title, nav_desc in [("◀ ▶", _("Navigasi Halaman"), _("Gunakan tombol Sebelum / Selanjutnya\ndi bawah layar chapter untuk pindah\nke halaman chapter berikutnya.")), ("📋", _("Informasi Chapter"), _("Setiap kartu menampilkan jumlah\nchapter, judul, dan deskripsi singkat\ntentang isi cerita di chapter tersebut.")), ("🏠", _("Kembali ke Lobby"), _("Tekan tombol Kembali di pojok\nkiri atas untuk kembali ke\nlayar utama (lobby) kapan saja."))]:
                frame at help_card_hover:
                    xsize 338
                    ysize 168
                    padding (22, 18)
                    background Frame(Solid("#071825"), 14, 14)
                    hover_background Frame(Solid("#0a2040"), 14, 14)

                    vbox:
                        spacing 12

                        hbox:
                            spacing 10
                            text nav_icon:
                                size 20
                                color "#4fc3f7"
                                yalign 0.5
                            text nav_title:
                                size 16
                                color "#4fc3f7"
                                bold True
                                yalign 0.5

                        frame:
                            xfill True
                            ysize 1
                            background Solid("#1565c040")

                        text nav_desc:
                            size 13
                            color "#a0c8e0"
                            line_spacing 4

        null height 4
        frame:
            xfill True
            padding (18, 14)
            background Frame(Solid("#061629"), 10, 10)
            hbox:
                spacing 10
                text "💡" size 16 yalign 0.5
                text _("Tips: Chapter akan terbuka otomatis setelah kamu menyelesaikan chapter sebelumnya. Progress tersimpan secara otomatis."):
                    size 14
                    color "#7ab8cc"
                    yalign 0.5


style help_button is gui_button
style help_button_text is gui_button_text
style help_label is gui_label
style help_label_text is gui_label_text
style help_text is gui_text

style help_button:
    properties gui.button_properties("help_button")
    xmargin 12

style help_button_text:
    properties gui.text_properties("help_button")

style help_label:
    xsize 375
    right_padding 30

style help_label_text:
    size gui.text_size
    xalign 1.0
    textalign 1.0



################################################################################
## Layar Tambahan
################################################################################


## Layar konfirmasi ############################################################
##
## Layar konfirmasi di panggil ketika Ren'Py mau menanyakan ke pemain pertanyaan
## ya atau tidak.
##
## https://www.renpy.org/doc/html/screen_special.html#confirm

## =========================================================
## SCREEN KONFIRMASI LOBBY — Desain frame kayu emas
## =========================================================
screen lobby_confirm():
    modal True
    zorder 200

    ## Overlay gelap semi-transparan di belakang dialog
    add Solid("#00000077")

    ## Container utama (frame kayu emas)
    frame:
        xalign 0.5
        yalign 0.5
        xsize 560
        ysize 260
        background None
        padding (0, 0, 0, 0)

        ## === LAPISAN 1: Border emas terluar ===
        fixed:
            xfill True
            yfill True

            ## Latar coklat kayu
            frame:
                xfill True
                yfill True
                background Frame(Solid("#c8a05a"), 18, 18)

            ## Latar krem dalam
            frame:
                xfill True
                yfill True
                left_margin 5
                right_margin 5
                top_margin 5
                bottom_margin 5
                background Frame(Solid("#f0dba8"), 14, 14)

            ## Border dalam (coklat tua)
            frame:
                xfill True
                yfill True
                left_margin 12
                right_margin 12
                top_margin 12
                bottom_margin 12
                background Frame(Solid("#7a5c2e"), 12, 12)

            ## Area putih/krem isi konten
            frame:
                xfill True
                yfill True
                left_margin 18
                right_margin 18
                top_margin 18
                bottom_margin 18
                background Frame(Solid("#fdf6e3"), 8, 8)
                padding (40, 30, 40, 28)

                vbox:
                    xalign 0.5
                    yalign 0.5
                    spacing 28

                    ## Teks pertanyaan
                    text _("Apakah yakin ingin kembali ke Lobby?"):
                        font "gui/font/PlayfairDisplay-Bold.ttf"
                        size 26
                        color "#3a2a10"
                        bold True
                        xalign 0.5
                        text_align 0.5

                    ## Tombol Ya dan Tidak
                    hbox:
                        xalign 0.5
                        spacing 32

                        ## Tombol Tidak
                        button:
                            action Hide("lobby_confirm")
                            xysize (160, 55)
                            background Frame(Solid("#f0dba8"), 8, 8)
                            hover_background Frame(Solid("#e0c890"), 8, 8)
                            text _("Tidak"):
                                font "gui/font/PlayfairDisplay-Bold.ttf"
                                size 24
                                color "#3a2a10"
                                bold True
                                align (0.5, 0.5)

                        ## Tombol Ya
                        button:
                            action [Hide("lobby_confirm"), Function(renpy.full_restart)]
                            xysize (160, 55)
                            background Frame(Solid("#f0dba8"), 8, 8)
                            hover_background Frame(Solid("#e0c890"), 8, 8)
                            text _("Ya"):
                                font "gui/font/PlayfairDisplay-Bold.ttf"
                                size 24
                                color "#3a2a10"
                                bold True
                                align (0.5, 0.5)

            ## Dekorasi diamond pojok kiri atas
            frame:
                xalign 0.0
                yalign 0.0
                xoffset 8
                yoffset 8
                xysize (16, 16)
                background Frame(Solid("#c8a05a"), 2, 2)
                text "+":
                    align (0.5, 0.5)
                    color "#7a5c2e"
                    size 14
                    bold True

            ## Dekorasi diamond pojok kanan atas
            frame:
                xalign 1.0
                yalign 0.0
                xoffset -8
                yoffset 8
                xysize (16, 16)
                background Frame(Solid("#c8a05a"), 2, 2)
                text "+":
                    align (0.5, 0.5)
                    color "#7a5c2e"
                    size 14
                    bold True

            ## Dekorasi diamond pojok kiri bawah
            frame:
                xalign 0.0
                yalign 1.0
                xoffset 8
                yoffset -8
                xysize (16, 16)
                background Frame(Solid("#c8a05a"), 2, 2)
                text "+":
                    align (0.5, 0.5)
                    color "#7a5c2e"
                    size 14
                    bold True

            ## Dekorasi diamond pojok kanan bawah
            frame:
                xalign 1.0
                yalign 1.0
                xoffset -8
                yoffset -8
                xysize (16, 16)
                background Frame(Solid("#c8a05a"), 2, 2)
                text "+":
                    align (0.5, 0.5)
                    color "#7a5c2e"
                    size 14
                    bold True

    key "game_menu" action Hide("lobby_confirm")


## =========================================================
## SCREEN KONFIRMASI BAWAAN REN'PY — Didesain ulang (kayu emas)
## =========================================================
screen confirm(message, yes_action, no_action):
    modal True
    zorder 200

    ## Overlay gelap semi-transparan
    add Solid("#00000077")

    frame:
        xalign 0.5
        yalign 0.5
        xsize 560
        ysize 260
        background None
        padding (0, 0, 0, 0)

        fixed:
            xfill True
            yfill True

            frame:
                xfill True
                yfill True
                background Frame(Solid("#c8a05a"), 18, 18)

            frame:
                xfill True
                yfill True
                left_margin 5
                right_margin 5
                top_margin 5
                bottom_margin 5
                background Frame(Solid("#f0dba8"), 14, 14)

            frame:
                xfill True
                yfill True
                left_margin 12
                right_margin 12
                top_margin 12
                bottom_margin 12
                background Frame(Solid("#7a5c2e"), 12, 12)

            frame:
                xfill True
                yfill True
                left_margin 18
                right_margin 18
                top_margin 18
                bottom_margin 18
                background Frame(Solid("#fdf6e3"), 8, 8)
                padding (40, 30, 40, 28)

                vbox:
                    xalign 0.5
                    yalign 0.5
                    spacing 28

                    text _(message):
                        font "gui/font/PlayfairDisplay-Bold.ttf"
                        size 26
                        color "#3a2a10"
                        bold True
                        xalign 0.5
                        text_align 0.5

                    hbox:
                        xalign 0.5
                        spacing 32

                        button:
                            action no_action
                            xysize (160, 55)
                            background Frame(Solid("#f0dba8"), 8, 8)
                            hover_background Frame(Solid("#e0c890"), 8, 8)
                            text _("Tidak"):
                                font "gui/font/PlayfairDisplay-Bold.ttf"
                                size 24
                                color "#3a2a10"
                                bold True
                                align (0.5, 0.5)

                        button:
                            if ("keluar game" in str(message).lower() or "quit" in str(message).lower()) and not main_menu:
                                action [Hide("confirm"), Function(renpy.full_restart)]
                            else:
                                action yes_action
                            xysize (160, 55)
                            background Frame(Solid("#f0dba8"), 8, 8)
                            hover_background Frame(Solid("#e0c890"), 8, 8)
                            text _("Ya"):
                                font "gui/font/PlayfairDisplay-Bold.ttf"
                                size 24
                                color "#3a2a10"
                                bold True
                                align (0.5, 0.5)

            ## Dekorasi + di empat sudut
            frame:
                xalign 0.0
                yalign 0.0
                xoffset 8
                yoffset 8
                xysize (16, 16)
                background Frame(Solid("#c8a05a"), 2, 2)
                text "+":
                    align (0.5, 0.5)
                    color "#7a5c2e"
                    size 14
                    bold True
            frame:
                xalign 1.0
                yalign 0.0
                xoffset -8
                yoffset 8
                xysize (16, 16)
                background Frame(Solid("#c8a05a"), 2, 2)
                text "+":
                    align (0.5, 0.5)
                    color "#7a5c2e"
                    size 14
                    bold True
            frame:
                xalign 0.0
                yalign 1.0
                xoffset 8
                yoffset -8
                xysize (16, 16)
                background Frame(Solid("#c8a05a"), 2, 2)
                text "+":
                    align (0.5, 0.5)
                    color "#7a5c2e"
                    size 14
                    bold True
            frame:
                xalign 1.0
                yalign 1.0
                xoffset -8
                yoffset -8
                xysize (16, 16)
                background Frame(Solid("#c8a05a"), 2, 2)
                text "+":
                    align (0.5, 0.5)
                    color "#7a5c2e"
                    size 14
                    bold True

    key "game_menu" action no_action


style confirm_frame is gui_frame
style confirm_prompt is gui_prompt
style confirm_prompt_text is gui_prompt_text
style confirm_button is gui_medium_button
style confirm_button_text is gui_medium_button_text

style confirm_frame:
    background Frame(Solid("#00000000"), 15, 15)
    padding (0, 0)
    xalign .5
    yalign .5

style confirm_prompt_text:
    textalign 0.5
    layout "subtitle"

style confirm_button:
    properties gui.button_properties("confirm_button")

style confirm_button_text:
    properties gui.text_properties("confirm_button")


## Lompati indikator layar #####################################################
##
## layar skip_indicator di tampilkan untuk mengindikasian proses skipping sedang
## dalam proses.
##
## https://www.renpy.org/doc/html/screen_special.html#skip-indicator

screen skip_indicator():

    zorder 100
    style_prefix "skip"

    frame:

        hbox:
            spacing 9

            text _("Melompati")

            text "▸" at delayed_blink(0.0, 1.0) style "skip_triangle"
            text "▸" at delayed_blink(0.2, 1.0) style "skip_triangle"
            text "▸" at delayed_blink(0.4, 1.0) style "skip_triangle"


## transform digunakan untuk mengkedipkan panah setelah yang lain.
transform delayed_blink(delay, cycle):
    alpha .5

    pause delay

    block:
        linear .2 alpha 1.0
        pause .2
        linear .2 alpha 0.5
        pause (cycle - .4)
        repeat


style skip_frame is empty
style skip_text is gui_text
style skip_triangle is skip_text

style skip_frame:
    ypos gui.skip_ypos
    background Frame("gui/skip.png", gui.skip_frame_borders, tile=gui.frame_tile)
    padding gui.skip_frame_borders.padding

style skip_text:
    size gui.notify_text_size

style skip_triangle:
    ## Kami harus menggunakan font yang mempunyai glyph BLACK RIGHT-POINTING
    ## SMALL TRIANGLE didalamnya.
    font "DejaVuSans.ttf"


## Layar pemberitahuan #########################################################
##
## layar notify digunakan untuk menampilkan pesan kepada pemain. (Seperti,
## ketika game di simpan cepat atau screenshot di ambil.)
##
## https://www.renpy.org/doc/html/screen_special.html#notify-screen

screen notify(message):

    zorder 100
    style_prefix "notify"

    frame at notify_appear:
        text "[message!tq]"

    timer 3.25 action Hide('notify')


transform notify_appear:
    on show:
        alpha 0
        linear .25 alpha 1.0
    on hide:
        linear .5 alpha 0.0


style notify_frame is empty
style notify_text is gui_text

style notify_frame:
    ypos gui.notify_ypos

    background Frame("gui/notify.png", gui.notify_frame_borders, tile=gui.frame_tile)
    padding gui.notify_frame_borders.padding

style notify_text:
    properties gui.text_properties("notify")


## Layar NVL ###################################################################
##
## Layar ini digunakan untuk dialog dan menu mode-NVL.
##
## https://www.renpy.org/doc/html/screen_special.html#nvl


screen nvl(dialogue, items=None):

    window:
        style "nvl_window"

        has vbox:
            spacing gui.nvl_spacing

        ## Menampilkan dialog pada vpgrid atau vbox.
        if gui.nvl_height:

            vpgrid:
                cols 1
                yinitial 1.0

                use nvl_dialogue(dialogue)

        else:

            use nvl_dialogue(dialogue)

        ## Menampilkan menu, jika diberikan. Menu dapat ditampilkan dengan tidak
        ## benar jika config.narrator_menu diatur ke True.
        for i in items:

            textbutton i.caption:
                action i.action
                style "nvl_button"

    add SideImage() xalign 0.0 yalign 1.0


screen nvl_dialogue(dialogue):

    for d in dialogue:

        window:
            id d.window_id

            fixed:
                yfit gui.nvl_height is None

                if d.who is not None:

                    text d.who:
                        id d.who_id

                text d.what:
                    id d.what_id


## Ini mengendalikan angka maksimum entri mode-NVL yang dapat di tampilkan
## sekaligus.
define config.nvl_list_length = gui.nvl_list_length

style nvl_window is default
style nvl_entry is default

style nvl_label is say_label
style nvl_dialogue is say_dialogue

style nvl_button is button
style nvl_button_text is button_text

style nvl_window:
    xfill True
    yfill True

    background "gui/nvl.png"
    padding gui.nvl_borders.padding

style nvl_entry:
    xfill True
    ysize gui.nvl_height

style nvl_label:
    xpos gui.nvl_name_xpos
    xanchor gui.nvl_name_xalign
    ypos gui.nvl_name_ypos
    yanchor 0.0
    xsize gui.nvl_name_width
    min_width gui.nvl_name_width
    textalign gui.nvl_name_xalign

style nvl_dialogue:
    xpos gui.nvl_text_xpos
    xanchor gui.nvl_text_xalign
    ypos gui.nvl_text_ypos
    xsize gui.nvl_text_width
    min_width gui.nvl_text_width
    textalign gui.nvl_text_xalign
    layout ("subtitle" if gui.nvl_text_xalign else "tex")

style nvl_thought:
    xpos gui.nvl_thought_xpos
    xanchor gui.nvl_thought_xalign
    ypos gui.nvl_thought_ypos
    xsize gui.nvl_thought_width
    min_width gui.nvl_thought_width
    textalign gui.nvl_thought_xalign
    layout ("subtitle" if gui.nvl_text_xalign else "tex")

style nvl_button:
    properties gui.button_properties("nvl_button")
    xpos gui.nvl_button_xpos
    xanchor gui.nvl_button_xalign

style nvl_button_text:
    properties gui.text_properties("nvl_button")


## Layar gelembung #############################################################
##
## Layar gelembung digunakan untuk menampilkan dialog kepada pemain saat
## menggunakan gelembung ucapan. Layar gelembung mengambil parameter yang sama
## dengan layar ucapkan, harus membuat tampilan dengan id "apa", dan dapat
## membuat tampilan dengan id "kotak nama", "siapa", dan "jendela".
##
## https://www.renpy.org/doc/html/bubble.html#bubble-screen

screen bubble(who, what):
    style_prefix "bubble"

    window:
        id "window"

        if who is not None:

            window:
                id "namebox"
                style "bubble_namebox"

                text who:
                    id "who"

        text what:
            id "what"

        default ctc = None
        showif ctc:
            add ctc

style bubble_window is empty
style bubble_namebox is empty
style bubble_who is default
style bubble_what is default

style bubble_window:
    xpadding 30
    top_padding 5
    bottom_padding 5

style bubble_namebox:
    xalign 0.5

style bubble_who:
    xalign 0.5
    textalign 0.5
    color "#000"

style bubble_what:
    align (0.5, 0.5)
    text_align 0.5
    layout "subtitle"
    color "#000"

define bubble.frame = Frame("gui/bubble.png", 55, 55, 55, 95)
define bubble.thoughtframe = Frame("gui/thoughtbubble.png", 55, 55, 55, 55)

define bubble.properties = {
    "bottom_left" : {
        "window_background" : Transform(bubble.frame, xzoom=1, yzoom=1),
        "window_bottom_padding" : 27,
    },

    "bottom_right" : {
        "window_background" : Transform(bubble.frame, xzoom=-1, yzoom=1),
        "window_bottom_padding" : 27,
    },

    "top_left" : {
        "window_background" : Transform(bubble.frame, xzoom=1, yzoom=-1),
        "window_top_padding" : 27,
    },

    "top_right" : {
        "window_background" : Transform(bubble.frame, xzoom=-1, yzoom=-1),
        "window_top_padding" : 27,
    },

    "thought" : {
        "window_background" : bubble.thoughtframe,
    }
}

define bubble.expand_area = {
    "bottom_left" : (0, 0, 0, 22),
    "bottom_right" : (0, 0, 0, 22),
    "top_left" : (0, 22, 0, 0),
    "top_right" : (0, 22, 0, 0),
    "thought" : (0, 0, 0, 0),
}



################################################################################
## Versi Mobile(HP/Handphone/Android)
################################################################################

style pref_vbox:
    variant "medium"
    xsize 675

## Semenjak mouse tidak ada, kami mengganti menu cepat dengan yang menggunakan
## tombol yang lebih besar dan sedikit, yang memudahkan untuk di sentuh.
screen quick_menu():
    variant "touch"

    zorder 100

    if quick_menu:

        hbox:
            style "quick_menu"
            style_prefix "quick"

            textbutton _("Kembali") action Rollback()
            textbutton _("Lompati") action Skip() alternate Skip(fast=True, confirm=True)
            textbutton _("Otomatis") action Preference("auto-forward", "toggle")
            textbutton _("Menu") action ShowMenu()


style window:
    variant "small"
    background "gui/phone/textbox.png"

style radio_button:
    variant "small"
    foreground "gui/phone/button/radio_[prefix_]foreground.png"

style check_button:
    variant "small"
    foreground "gui/phone/button/check_[prefix_]foreground.png"

style nvl_window:
    variant "small"
    background "gui/phone/nvl.png"

style main_menu_frame:
    variant "small"
    background "gui/phone/overlay/main_menu.png"

style game_menu_outer_frame:
    variant "small"
    background "gui/phone/overlay/game_menu.png"

style game_menu_navigation_frame:
    variant "small"
    xsize 510

style game_menu_content_frame:
    variant "small"
    top_margin 0

style game_menu_viewport:
    variant "small"
    xsize 1305

style pref_vbox:
    variant "small"
    xsize 600

style bar:
    variant "small"
    ysize gui.bar_size
    left_bar Frame("gui/phone/bar/left.png", gui.bar_borders, tile=gui.bar_tile)
    right_bar Frame("gui/phone/bar/right.png", gui.bar_borders, tile=gui.bar_tile)

style vbar:
    variant "small"
    xsize gui.bar_size
    top_bar Frame("gui/phone/bar/top.png", gui.vbar_borders, tile=gui.bar_tile)
    bottom_bar Frame("gui/phone/bar/bottom.png", gui.vbar_borders, tile=gui.bar_tile)

style scrollbar:
    variant "small"
    ysize gui.scrollbar_size
    base_bar Frame("gui/phone/scrollbar/horizontal_[prefix_]bar.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/phone/scrollbar/horizontal_[prefix_]thumb.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)

style vscrollbar:
    variant "small"
    xsize gui.scrollbar_size
    base_bar Frame("gui/phone/scrollbar/vertical_[prefix_]bar.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/phone/scrollbar/vertical_[prefix_]thumb.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)

style slider:
    variant "small"
    ysize gui.slider_size
    base_bar Frame("gui/phone/slider/horizontal_[prefix_]bar.png", gui.slider_borders, tile=gui.slider_tile)
    thumb "gui/phone/slider/horizontal_[prefix_]thumb.png"

style vslider:
    variant "small"
    xsize gui.slider_size
    base_bar Frame("gui/phone/slider/vertical_[prefix_]bar.png", gui.vslider_borders, tile=gui.slider_tile)
    thumb "gui/phone/slider/vertical_[prefix_]thumb.png"

style slider_vbox:
    variant "small"
    xsize None

style slider_slider:
    variant "small"
    xsize 900


## Animasi kunci kebuka — muncul smooth saat chapter tersedia
transform lock_unlock_anim:
    ## Mulai: kunci tertutup, kecil dan sedikit miring
    zoom 0.6
    rotate -20
    alpha 0.0
    ## Fase 1: muncul
    ease 0.25 zoom 1.1 rotate 5 alpha 1.0
    ## Fase 2: pantul sedikit
    ease 0.12 zoom 0.92 rotate -3
    ## Fase 3: idle stabil
    ease 0.12 zoom 1.0 rotate 0

## Pulse kecil saat idle agar terasa hidup
transform lock_idle_pulse:
    zoom 1.0
    pause 2.0
    ease 0.18 zoom 1.08
    ease 0.18 zoom 1.0
    repeat

## Animasi kartu chapter — tema biru navy
transform chapter_card_hover:
    on idle:
        easein 0.22 zoom 1.0 alpha 0.88 yoffset 0
    on hover:
        easein 0.22 zoom 1.02 alpha 1.0 yoffset -6

transform chapter_card_locked:
    on idle:
        easein 0.2 alpha 0.50
    on hover:
        easein 0.2 alpha 0.60

screen chapter_menu():
    tag menu

    default page = 0
    default hovered_card = None
    default hovered_kembali = False
    default hovered_sebelum = False
    default hovered_selanjutnya = False
    $ per_page = 3
    $ total_pages = max(1, (len(chapters) - 1) // per_page + 1)
    $ start = page * per_page
    $ end = start + per_page

    ## Latar belakang sekolah courtyard
    add Transform(gui.main_menu_background, xysize=(1920, 1080))
    add Solid("#120c0866") # Soft warm overlay

    ## Tombol KEMBALI (Capsule Gold dengan Hover Effect Sempurna)
    button:
        action Return()
        hovered SetScreenVariable("hovered_kembali", True)
        unhovered SetScreenVariable("hovered_kembali", False)
        xpos 40
        ypos 40
        xysize (180, 52)
        if hovered_kembali:
            background Frame(Solid("#ffd700"), 26, 26) # Glowing gold outer
        else:
            background Frame(Solid("#c3ab7d"), 26, 26) # Gold outer
        padding (2, 2)
        frame:
            xfill True
            yfill True
            if hovered_kembali:
                background Frame(Solid("#2d1f12ee"), 24, 24) # Lighter dark inner
            else:
                background Frame(Solid("#1c140cee"), 24, 24) # Dark inner
            hbox:
                align (0.5, 0.5)
                text _("KEMBALI") size 15 bold True kerning 2.0:
                    if hovered_kembali:
                        color "#ffffff"
                    else:
                        color "#dfc18c"
                    yalign 0.5

    ## Konten Utama
    vbox:
        xalign 0.5
        yalign 0.55
        spacing 30

        ## Header Title
        text _("Pilih Buku"):
            font "gui/font/PlayfairDisplay-BoldItalic.ttf"
            size 76
            color "#dfc18c"
            xalign 0.5
            outlines [(3, "#3e2715", 1, 1), (1, "#ffe2a033", 0, 0)]
            bold True

        ## Grid Kartu Buku (3 per halaman)
        hbox:
            xalign 0.5
            spacing 44

            if chapters:
                for i, chapter in enumerate(chapters[start:end]):
                    $ idx = start + i
                    $ lbl = chapter.get("label", "chapter{}_start".format(idx + 1))
                    $ unlocked = idx <= persistent.chapter_completed
                    $ badge = "Buku {}".format(idx + 1)
                    $ title = _(chapter["title"]) if unlocked else "???"
                    $ desc = _(chapter["description"]) if unlocked else "???"

                    if unlocked:
                        ## ===== Kartu Unlocked =====
                        button at chapter_card_hover:
                            action Jump(lbl)
                            hovered SetScreenVariable("hovered_card", idx)
                            unhovered SetScreenVariable("hovered_card", None)
                            xsize 400
                            ysize 560
                            padding (2, 2)
                            background Frame(Solid("#c3ab7d"), 14, 14) # Gold border
                            hover_background Frame(Solid("#ffd700"), 14, 14) # Hover glow

                            frame:
                                xfill True
                                yfill True
                                background Frame(Solid("#1a130cee"), 12, 12) # Dark interior
                                padding (24, 24)

                                vbox:
                                    xfill True
                                    spacing 0

                                    ## Area Visual Buku (Upper Half)
                                    frame:
                                        xfill True
                                        ysize 220
                                        background Solid("#00000000")

                                        ## Badge Buku 1/2/3 di Kiri Atas
                                        frame:
                                            xpos -12
                                            ypos -12
                                            xysize (100, 36)
                                            background Frame(Solid("#c3ab7d"), 6, 6)
                                            padding (1, 1)
                                            frame:
                                                xfill True
                                                yfill True
                                                background Solid("#3e2d1c")
                                                text badge size 13 color "#dfc18c" bold True align (0.5, 0.5)

                                        ## Buku 3D Vector Representation (Center)
                                        vbox:
                                            align (0.5, 0.5)
                                            # Book shadow / page base
                                            frame:
                                                xysize (114, 134)
                                                background Frame(Solid("#ffffffef"), 6, 6) # White page edges
                                                padding (0, 0, 4, 4) # offset for pages
                                                frame:
                                                    xfill True
                                                    yfill True
                                                    background Frame(Solid("#b39665"), 6, 6) # Main Cover
                                                    padding (8, 0, 0, 0)
                                                    # Spine accent
                                                    frame:
                                                        xpos 2
                                                        yfill True
                                                        xsize 4
                                                        background Solid("#ffd700")
                                                    # Label
                                                    frame:
                                                        align (0.5, 0.5)
                                                        xysize (64, 64)
                                                        background Frame(Solid("#3e2d1c"), 4, 4)
                                                        padding (2, 2)
                                                        frame:
                                                            xfill True
                                                            yfill True
                                                            background Frame(Solid("#ffd700"), 4, 4)
                                                            padding (1, 1)
                                                            frame:
                                                                xfill True
                                                                yfill True
                                                                background Solid("#3e2d1c")
                                                                text "BK{}".format(idx + 1) size 14 color "#dfc18c" bold True align (0.5, 0.5)

                                    ## Tombol MULAI (Capsule)
                                    frame:
                                        xsize 300
                                        ysize 50
                                        xalign 0.5
                                        if hovered_card == idx:
                                            background Frame(Solid("#ffd700"), 25, 25) # Glowing hover
                                        else:
                                            background Frame(Solid("#c3ab7d"), 25, 25)
                                        padding (2, 2)
                                        frame:
                                            xfill True
                                            yfill True
                                            background Frame(Solid("#1c140cee"), 23, 23)
                                            hbox:
                                                align (0.5, 0.5)
                                                spacing 12
                                                text "🔒" size 16 color "#dfc18c" yalign 0.5
                                                text _("M U L A I") size 15 color "#dfc18c" bold True kerning 3.0 yalign 0.5

                                    null height 30

                                    ## Judul Buku
                                    text title:
                                        size 22
                                        color "#ffffff"
                                        bold True
                                        xmaximum 352
                                        line_spacing 4

                                    null height 12

                                    ## Deskripsi Buku
                                    text desc:
                                        size 15
                                        color "#dfc18cc0"
                                        xmaximum 352
                                        line_spacing 6

                    else:
                        ## ===== Kartu Locked =====
                        frame:
                            xsize 400
                            ysize 560
                            padding (2, 2)
                            background Frame(Solid("#6b5b48"), 14, 14) # Muted border

                            frame:
                                xfill True
                                yfill True
                                background Frame(Solid("#110a06f0"), 12, 12) # Darker interior
                                padding (24, 24)

                                vbox:
                                    xfill True
                                    spacing 0

                                    ## Area Visual Buku Locked
                                    frame:
                                        xfill True
                                        ysize 220
                                        background Solid("#00000000")

                                        ## Badge locked
                                        frame:
                                            xpos -12
                                            ypos -12
                                            xysize (100, 36)
                                            background Frame(Solid("#6b5b48"), 6, 6)
                                            padding (1, 1)
                                            frame:
                                                xfill True
                                                yfill True
                                                background Solid("#251c12")
                                                text badge size 13 color "#6b5b48" bold True align (0.5, 0.5)

                                        ## Muted Lock Icon in Center
                                        text "🔒" size 60 color "#6b5b48" align (0.5, 0.5)

                                    ## Tombol MULAI Locked
                                    frame:
                                        xsize 300
                                        ysize 50
                                        xalign 0.5
                                        background Frame(Solid("#6b5b48"), 25, 25)
                                        padding (2, 2)
                                        frame:
                                            xfill True
                                            yfill True
                                            background Frame(Solid("#110a06"), 23, 23)
                                            hbox:
                                                align (0.5, 0.5)
                                                spacing 12
                                                text "🔒" size 16 color "#6b5b48" yalign 0.5
                                                text _("TERKUNCI") size 15 color "#6b5b48" bold True kerning 3.0 yalign 0.5

                                    null height 30

                                    ## Judul Locked
                                    text "???":
                                        size 22
                                        color "#6b5b48"
                                        bold True

                                    null height 12

                                    ## Deskripsi Locked
                                    text "???":
                                        size 15
                                        color "#6b5b48"
                                        line_spacing 6

            else:
                text _("Belum ada buku yang tersedia.") size 24 color "#dfc18c" align (0.5, 0.5)

        ## Navigasi Halaman (Capsule Gold)
        hbox:
            xalign 0.5
            spacing 26

            button:
                xysize (180, 50)
                hovered SetScreenVariable("hovered_sebelum", True)
                unhovered SetScreenVariable("hovered_sebelum", False)
                if hovered_sebelum and page > 0:
                    background Frame(Solid("#ffd700"), 25, 25)
                else:
                    background Frame(Solid("#c3ab7d"), 25, 25)
                sensitive page > 0
                action SetScreenVariable("page", page - 1)
                padding (2, 2)
                frame:
                    xfill True
                    yfill True
                    if hovered_sebelum and page > 0:
                        background Frame(Solid("#2d1f12ee"), 23, 23)
                    else:
                        background Frame(Solid("#1c140cee"), 23, 23)
                    hbox:
                        align (0.5, 0.5)
                        text _("SEBELUM") size 13 bold True kerning 1.5:
                            if hovered_sebelum and page > 0:
                                color "#ffffff"
                            else:
                                color "#dfc18c"
                            yalign 0.5

            frame:
                ysize 50
                padding (2, 2)
                background Frame(Solid("#c3ab7d"), 25, 25)
                frame:
                    yfill True
                    background Frame(Solid("#1c140cee"), 23, 23)
                    padding (24, 0)
                    text "{} / {}".format(page + 1, total_pages):
                        size 17
                        color "#dfc18c"
                        kerning 3.0
                        bold True
                        align (0.5, 0.5)

            button:
                xysize (200, 50)
                hovered SetScreenVariable("hovered_selanjutnya", True)
                unhovered SetScreenVariable("hovered_selanjutnya", False)
                if hovered_selanjutnya and page < total_pages - 1:
                    background Frame(Solid("#ffd700"), 25, 25)
                else:
                    background Frame(Solid("#c3ab7d"), 25, 25)
                sensitive page < total_pages - 1
                action SetScreenVariable("page", page + 1)
                padding (2, 2)
                frame:
                    xfill True
                    yfill True
                    if hovered_selanjutnya and page < total_pages - 1:
                        background Frame(Solid("#2d1f12ee"), 23, 23)
                    else:
                        background Frame(Solid("#1c140cee"), 23, 23)
                    hbox:
                        align (0.5, 0.5)
                        text _("SELANJUTNYA") size 13 bold True kerning 1.5:
                            if hovered_selanjutnya and page < total_pages - 1:
                                color "#ffffff"
                            else:
                                color "#dfc18c"
                            yalign 0.5


