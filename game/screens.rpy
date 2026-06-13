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

    ## Tentukan warna border dinamis berdasarkan nama karakter
    $ dynamic_color = "#cc3355"  # Default: Merah muda/pink
    if who == "kenzo":
        $ dynamic_color = "#f83e00"  # Oren
    elif who == "Lisa":
        $ dynamic_color = "#e0407a"  # Pink cerah
    elif who == "Satpam":
        $ dynamic_color = "#4a6ae6"  # Biru
    elif who == "Pak Agus":
        $ dynamic_color = "#33cc55"  # Hijau
    elif who == "narator":
        $ dynamic_color = "#cc3355"  # Merah default narator

    if who is not None:
        ## =====================================================
        ## DIALOG KARAKTER — speech bubble + panah ke kiri
        ## =====================================================
        vbox:
            xalign 0.5
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
            xalign 0.5
            yalign 0.45
            xsize 800
            yminimum 200
            ysize None
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
                yalign 0.0
                xalign 0.5
                xsize 680
                top_margin 18
                bottom_margin 25
                spacing 25

                text "◆    N  A  R  A  S  I    ◆":
                    color "#ffffff55"
                    size 12
                    bold True
                    xalign 0.5
                    kerning 2.0

                text what id "what":
                    style "say_narrator"
                    xsize 680
                    xalign 0.5

    ## =========================================================
    ## TOMBOL KE LOBBY — Pojok kanan atas layar
    ## =========================================================
    button:
        action MainMenu(confirm=True)
        align (0.98, 0.04)
        xysize (155, 45)
        background Frame(Transform(Solid("#ffffff33")), 15, 15)
        hover_background Frame(Transform(Solid("#fb6e9ba8")), 15, 15)
        text _("🏠 Ke Lobby") size 20 color "#ffffff" hover_color "#ffffff" align (0.5, 0.5)


## Buat namebox tersedia untuk mengatur gaya melalui objek karakter.
init python:
    config.character_id_prefixes.append('namebox')

style window is default
style say_label is default
style say_dialogue is default
style say_thought is default
style say_narrator is default

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


## Layar Menu utama ############################################################
##
## Digunakan untuk menampilkan menu utama ketika Ren'Py dimulai.
##
## https://www.renpy.org/doc/html/screen_special.html#main-menu

transform menu_btn_anim:
    on idle:
        easein 0.15 xoffset 0 alpha 0.8 zoom 1.0
    on hover:
        easein 0.15 xoffset 15 alpha 1.0 zoom 1.05

screen main_menu():

    tag menu

    add Transform(gui.main_menu_background, xysize=(1920, 1080))

    frame:
        xpos 120
        ypos 280
        xsize 380
        ysize 540
        # Glassmorphism panel background
        background Transform(Solid("#ffffff0c"))
        padding (30, 40)
        
        vbox:
            align (0.5, 0.5)
            spacing 30
            
            button at menu_btn_anim:
                action Start()
                hover_background Frame(Transform(Solid("#ffffff1a"), zoom=1.05))
                xsize 300
                padding (15, 10)
                hbox:
                    spacing 20
                    text "▶" font gui.text_font color "#00dfa4" size 24 yalign 0.5
                    text _("Mulai") font gui.text_font color "#8fa2b4" hover_color "#ffffff" size 28 yalign 0.5

            button at menu_btn_anim:
                action ShowMenu("chapter_menu")
                hover_background Frame(Transform(Solid("#ffffff1a"), zoom=1.05))
                xsize 300
                padding (15, 10)
                hbox:
                    spacing 20
                    text "📖" font gui.text_font color "#00dfa4" size 24 yalign 0.5
                    text _("Chapter") font gui.text_font color "#8fa2b4" hover_color "#ffffff" size 28 yalign 0.5

            button at menu_btn_anim:
                action ShowMenu("preferences")
                hover_background Frame(Transform(Solid("#ffffff1a"), zoom=1.05))
                xsize 300
                padding (15, 10)
                hbox:
                    spacing 20
                    text "⚙" font gui.text_font color "#00dfa4" size 24 yalign 0.5
                    text _("Setting") font gui.text_font color "#8fa2b4" hover_color "#ffffff" size 28 yalign 0.5

            button at menu_btn_anim:
                action ShowMenu("about")
                hover_background Frame(Transform(Solid("#ffffff1a"), zoom=1.05))
                xsize 300
                padding (15, 10)
                hbox:
                    spacing 20
                    text "ℹ" font gui.text_font color "#00dfa4" size 24 yalign 0.5
                    text _("Tentang") font gui.text_font color "#8fa2b4" hover_color "#ffffff" size 28 yalign 0.5

            button at menu_btn_anim:
                action ShowMenu("help")
                hover_background Frame(Transform(Solid("#ffffff1a"), zoom=1.05))
                xsize 300
                padding (15, 10)
                hbox:
                    spacing 20
                    text "❓" font gui.text_font color "#00dfa4" size 24 yalign 0.5
                    text _("Bantuan") font gui.text_font color "#8fa2b4" hover_color "#ffffff" size 28 yalign 0.5

            button at menu_btn_anim:
                action Quit(confirm=not main_menu)
                hover_background Frame(Transform(Solid("#ffffff1a"), zoom=1.05))
                xsize 300
                padding (15, 10)
                hbox:
                    spacing 20
                    text "🚪" font gui.text_font color "#ff7676" size 24 yalign 0.5
                    text _("Keluar") font gui.text_font color "#8fa2b4" hover_color "#ffffff" size 28 yalign 0.5

    ## Language Selector / Ikon Negara di Lobby
    vbox:
        align (0.95, 0.05)
        spacing 10
        text _("Pilih Bahasa / Language:") size 15 color "#a0d8cc" bold True kerning 1.5 xalign 0.5
        hbox:
            xalign 0.5
            spacing 15
            
            button:
                action Language(None)  ## Bahasa Indonesia (Default)
                xysize (60, 45)
                background Frame(Solid("#ffffff22" if _preferences.language != None else "#cc3355ee"), 10, 10)
                hover_background Frame(Solid("#cc3355aa"), 10, 10)
                text "🇮🇩" size 26 align (0.5, 0.5)

            button:
                action Language("english")  ## Bahasa Inggris
                xysize (60, 45)
                background Frame(Solid("#ffffff22" if _preferences.language != "english" else "#3355ccee"), 10, 10)
                hover_background Frame(Solid("#3355ccaa"), 10, 10)
                text "🇬🇧" size 26 align (0.5, 0.5)

    vbox:
        xalign 0.68
        yalign 0.48
        spacing 5
        text "Dream" font gui.text_font size 180 color "#5df7d9" italic True align (0.5, 0.5)
        text "WHERE MEMORIES FADE INTO STARLIGHT" font gui.text_font size 22 kerning 6.0 color "#97a2ad" align (0.5, 0.5)

    vbox:
        xpos 1660
        ypos 940
        text "DREAM" font gui.text_font size 48 color "#00dfa4" kerning 8.0 align (1.0, 1.0)
        text "VER [config.version]" font gui.text_font size 18 kerning 3.0 color "#97a2ad" align (1.0, 1.0)

    button:
        action NullAction()
        xpos 1750
        ypos 60
        background Transform(Solid("#ffffff1a"))
        padding (10, 10)
        xysize (65, 65)
        text "🌙" size 30 color "#ffffff" align (0.5, 0.5)


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

screen preferences():

    tag menu

    use game_menu(_("Setting"), scroll="viewport"):

        vbox:
            xfill True
            spacing 28

            ## ─── BARIS 1: Tampilan + Skip + Otomatis Maju ───────────────────
            hbox:
                xfill True
                spacing 24

                ## === Kartu: Tampilan ===
                if renpy.variant("pc") or renpy.variant("web"):
                    frame:
                        xsize 300
                        ysize 160
                        padding (20, 16, 20, 16)
                        background Frame(Solid("#071520"), 14, 14)

                        vbox:
                            spacing 12

                            hbox:
                                spacing 8
                                text "🖥" size 17 yalign 0.5
                                text _("TAMPILAN"):
                                    size 15
                                    color "#00dfa4"
                                    bold True
                                    kerning 2.0
                                    yalign 0.5

                            frame:
                                xfill True
                                ysize 1
                                background Solid("#00dfa430")

                            hbox:
                                spacing 10

                                textbutton _("Jendela"):
                                    action Preference("display", "window")
                                    xsize 116
                                    ysize 42
                                    background Frame(Solid("#0d2030"), 8, 8)
                                    hover_background Frame(Solid("#003d2a"), 8, 8)
                                    selected_background Frame(Solid("#00dfa440"), 8, 8)
                                    text_color "#7ab8cc"
                                    text_hover_color "#00dfa4"
                                    text_selected_color "#00dfa4"
                                    text_size 16
                                    text_yalign 0.5
                                    text_xalign 0.5

                                textbutton _("Layar Penuh"):
                                    action Preference("display", "fullscreen")
                                    xsize 116
                                    ysize 42
                                    background Frame(Solid("#0d2030"), 8, 8)
                                    hover_background Frame(Solid("#003d2a"), 8, 8)
                                    selected_background Frame(Solid("#00dfa440"), 8, 8)
                                    text_color "#7ab8cc"
                                    text_hover_color "#00dfa4"
                                    text_selected_color "#00dfa4"
                                    text_size 16
                                    text_yalign 0.5
                                    text_xalign 0.5

                ## === Kartu: Lompati Dialog ===
                frame:
                    xsize 420
                    ysize 160
                    padding (20, 16, 20, 16)
                    background Frame(Solid("#071520"), 14, 14)

                    vbox:
                        spacing 12

                        hbox:
                            spacing 8
                            text "⏩" size 17 yalign 0.5
                            text _("LOMPATI DIALOG"):
                                size 15
                                color "#00dfa4"
                                bold True
                                kerning 2.0
                                yalign 0.5

                        frame:
                            xfill True
                            ysize 1
                            background Solid("#00dfa430")

                        hbox:
                            spacing 10

                            textbutton _("Belum Terlihat"):
                                action Preference("skip", "toggle")
                                xsize 170
                                ysize 42
                                background Frame(Solid("#0d2030"), 8, 8)
                                hover_background Frame(Solid("#003d2a"), 8, 8)
                                selected_background Frame(Solid("#00dfa440"), 8, 8)
                                text_color "#7ab8cc"
                                text_hover_color "#00dfa4"
                                text_selected_color "#00dfa4"
                                text_size 15
                                text_yalign 0.5
                                text_xalign 0.5

                            textbutton _("Setelah Pilihan"):
                                action Preference("after choices", "toggle")
                                xsize 170
                                ysize 42
                                background Frame(Solid("#0d2030"), 8, 8)
                                hover_background Frame(Solid("#003d2a"), 8, 8)
                                selected_background Frame(Solid("#00dfa440"), 8, 8)
                                text_color "#7ab8cc"
                                text_hover_color "#00dfa4"
                                text_selected_color "#00dfa4"
                                text_size 15
                                text_yalign 0.5
                                text_xalign 0.5

                ## === Kartu: Otomatis Maju ===
                frame:
                    xsize 280
                    ysize 160
                    padding (20, 16, 20, 16)
                    background Frame(Solid("#071520"), 14, 14)

                    vbox:
                        spacing 12

                        hbox:
                            spacing 8
                            text "▶▶" size 15 color "#00dfa4" yalign 0.5
                            text _("OTOMATIS MAJU"):
                                size 15
                                color "#00dfa4"
                                bold True
                                kerning 2.0
                                yalign 0.5

                        frame:
                            xfill True
                            ysize 1
                            background Solid("#00dfa430")

                        textbutton _("Aktifkan / Nonaktifkan"):
                            action Preference("auto-forward", "toggle")
                            xsize 234
                            ysize 42
                            background Frame(Solid("#0d2030"), 8, 8)
                            hover_background Frame(Solid("#003d2a"), 8, 8)
                            selected_background Frame(Solid("#00dfa440"), 8, 8)
                            text_color "#7ab8cc"
                            text_hover_color "#00dfa4"
                            text_selected_color "#00dfa4"
                            text_size 14
                            text_yalign 0.5
                            text_xalign 0.5

            ## ─── BARIS 2: Kecepatan Text + Waktu Auto-Forward ───────────────
            hbox:
                xfill True
                spacing 24

                ## === Kartu: Kecepatan Text ===
                frame:
                    xsize 490
                    ysize 112
                    padding (20, 14, 20, 14)
                    background Frame(Solid("#071520"), 14, 14)

                    vbox:
                        spacing 10

                        hbox:
                            spacing 8
                            text "✏" size 16 yalign 0.5
                            text _("KECEPATAN TEXT"):
                                size 15
                                color "#00dfa4"
                                bold True
                                kerning 2.0
                                yalign 0.5

                        frame:
                            xfill True
                            ysize 1
                            background Solid("#00dfa430")

                        bar:
                            value Preference("text speed")
                            xsize 448
                            ysize 24

                ## === Kartu: Waktu Otomatis-Maju ===
                frame:
                    xsize 490
                    ysize 112
                    padding (20, 14, 20, 14)
                    background Frame(Solid("#071520"), 14, 14)

                    vbox:
                        spacing 10

                        hbox:
                            spacing 8
                            text "⏱" size 16 yalign 0.5
                            text _("WAKTU OTOMATIS-MAJU"):
                                size 15
                                color "#00dfa4"
                                bold True
                                kerning 2.0
                                yalign 0.5

                        frame:
                            xfill True
                            ysize 1
                            background Solid("#00dfa430")

                        bar:
                            value Preference("auto-forward time")
                            xsize 448
                            ysize 24

            ## ─── BARIS 3: Panel Audio ───────────────────────────────────────
            frame:
                xfill True
                ysize 216
                padding (24, 18, 24, 18)
                background Frame(Solid("#071520"), 14, 14)

                vbox:
                    xfill True
                    spacing 14

                    hbox:
                        spacing 8
                        text "🎵" size 17 yalign 0.5
                        text _("PENGATURAN AUDIO"):
                            size 15
                            color "#00dfa4"
                            bold True
                            kerning 2.0
                            yalign 0.5

                    frame:
                        xfill True
                        ysize 1
                        background Solid("#00dfa430")

                    hbox:
                        xfill True
                        spacing 32

                        ## Volume Musik
                        if config.has_music:
                            vbox:
                                xsize 290
                                spacing 8

                                hbox:
                                    spacing 6
                                    text "🎶" size 15 yalign 0.5
                                    text _("Volume Musik"):
                                        size 16
                                        color "#a0d8cc"
                                        yalign 0.5

                                bar:
                                    value Preference("music volume")
                                    xsize 290
                                    ysize 24

                        ## Volume Suara (SFX)
                        if config.has_sound:
                            vbox:
                                xsize 290
                                spacing 8

                                hbox:
                                    spacing 6
                                    text "🔊" size 15 yalign 0.5
                                    text _("Volume Suara"):
                                        size 16
                                        color "#a0d8cc"
                                        yalign 0.5

                                bar:
                                    value Preference("sound volume")
                                    xsize 290
                                    ysize 24

                        ## Volume Vokal (hanya jika game punya voice acting)
                        if config.has_voice:
                            vbox:
                                xsize 290
                                spacing 8

                                hbox:
                                    spacing 6
                                    text "🎙" size 15 yalign 0.5
                                    text _("Volume Vokal"):
                                        size 16
                                        color "#a0d8cc"
                                        yalign 0.5

                                bar:
                                    value Preference("voice volume")
                                    xsize 290
                                    ysize 24

                    if config.has_music or config.has_sound or config.has_voice:
                        hbox:
                            xalign 1.0

                            textbutton _("🔇  Senyapkan Semua"):
                                action Preference("all mute", "toggle")
                                xsize 236
                                ysize 40
                                background Frame(Solid("#0d2030"), 8, 8)
                                hover_background Frame(Solid("#003d2a"), 8, 8)
                                selected_background Frame(Solid("#00dfa440"), 8, 8)
                                text_color "#7ab8cc"
                                text_hover_color "#00dfa4"
                                text_selected_color "#00dfa4"
                                text_size 15
                                text_yalign 0.5
                                text_xalign 0.5


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

screen confirm(message, yes_action, no_action):

    ## Memastikan layar lain tidak mendapatkan input ketika layar ini di
    ## panggil.
    modal True

    zorder 200

    style_prefix "confirm"

    add "gui/overlay/confirm.png"

    frame:

        vbox:
            xalign .5
            yalign .5
            spacing 45

            label _(message):
                style "confirm_prompt"
                xalign 0.5

            hbox:
                xalign 0.5
                spacing 80

                button:
                    action yes_action
                    xysize (180, 60)
                    background Frame(Transform(Solid("#fb6e9b")), 10, 10)
                    hover_background Frame(Transform(Solid("#ff8fb2")), 10, 10)
                    text _("Ya"):
                        align (0.5, 0.5)
                        color "#ffffff"
                        hover_color "#ffffff"
                        size 28

                button:
                    action no_action
                    xysize (180, 60)
                    background Frame(Transform(Solid("#8a9cb5")), 10, 10)
                    hover_background Frame(Transform(Solid("#a0b2cc")), 10, 10)
                    text _("Tidak"):
                        align (0.5, 0.5)
                        color "#ffffff"
                        hover_color "#ffffff"
                        size 28

    ## Klik kanan dan jawaban escape "Tidak".
    key "game_menu" action no_action


style confirm_frame is gui_frame
style confirm_prompt is gui_prompt
style confirm_prompt_text is gui_prompt_text
style confirm_button is gui_medium_button
style confirm_button_text is gui_medium_button_text

style confirm_frame:
    background Frame(Transform(Solid("#2b1e2eec")), 15, 15)
    padding (60, 60)
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
    $ per_page = 3
    $ total_pages = max(1, (len(chapters) - 1) // per_page + 1)
    $ start = page * per_page
    $ end = start + per_page

    ## Latar belakang
    add Transform(gui.game_menu_background, xysize=(1920, 1080))
    add Solid("#020c1aee")

    ## Header judul
    vbox:
        xalign 0.5
        ypos 42
        spacing 6
        hbox:
            xalign 0.5
            spacing 18
            text "✦":
                size 22
                color "#1565c0"
                yalign 0.5
            text _("CHAPTER SELECTION"):
                font gui.text_font
                size 46
                kerning 8.0
                color "#4fc3f7"
                yalign 0.5
                bold True
                outlines [(2, "#1565c055", 0, 0)]
            text "✦":
                size 22
                color "#1565c0"
                yalign 0.5
        text _("— PILIH CHAPTER YANG INGIN DIMAINKAN —"):
            font gui.text_font
            size 14
            kerning 5.0
            color "#4fc3f760"
            xalign 0.5

    ## Garis dekoratif bawah judul
    frame:
        xalign 0.5
        ypos 148
        xsize 500
        ysize 2
        background Solid("#1565c060")

    ## Kartu-kartu chapter
    hbox:
        xalign 0.5
        yalign 0.54
        spacing 40

        if chapters:
            for i, chapter in enumerate(chapters[start:end]):
                $ index = start + i
                $ label_name = chapter.get("label", "chapter{}_start".format(index + 1))
                $ is_unlocked = index <= persistent.chapter_completed
                $ ch_num = "CH {}".format(index + 1)
                $ ch_title = _(chapter["title"]) if is_unlocked else "???"
                $ ch_desc = _(chapter["description"]) if is_unlocked else _("Selesaikan chapter\nsebelumnya untuk\nmembuka chapter ini.")
                $ has_image = is_unlocked and "image" in chapter and renpy.loadable(chapter["image"])

                if is_unlocked:
                    button at chapter_card_hover:
                        action Jump(label_name)
                        xsize 380
                        ysize 580
                        padding (0, 0, 0, 0)
                        background Frame(Solid("#071a35"), 18, 18)
                        hover_background Frame(Solid("#0e3060"), 18, 18)

                        vbox:
                            xfill True

                            ## THUMBNAIL — 220px
                            frame:
                                xsize 380
                                ysize 220
                                padding (0, 0, 0, 0)
                                background Solid("#040e20")

                                if has_image:
                                    add Transform(chapter["image"], size=(380, 220)) align (0.5, 0.5)
                                else:
                                    add Solid("#061428")
                                    vbox:
                                        align (0.5, 0.5)
                                        spacing 6
                                        text "📖":
                                            size 44
                                            align (0.5, 0.5)
                                        text ch_num:
                                            size 16
                                            color "#4fc3f722"
                                            bold True
                                            xalign 0.5

                                ## Badge nomor chapter
                                frame:
                                    xpos 14
                                    ypos 14
                                    padding (10, 5, 10, 5)
                                    background Frame(Solid("#1565c099"), 10, 10)
                                    text ch_num:
                                        size 15
                                        color "#4fc3f7"
                                        bold True

                                ## Garis bawah thumbnail
                                frame:
                                    xfill True
                                    ysize 3
                                    ypos 217
                                    background Solid("#1565c0")

                            ## KONTEN — 360px
                            frame:
                                xsize 380
                                ysize 360
                                padding (22, 18, 22, 18)
                                background Solid("#050f20")

                                vbox:
                                    xfill True
                                    spacing 14

                                    ## Tombol Mulai — 58px
                                    frame:
                                        xfill True
                                        ysize 58
                                        padding (0, 0)
                                        background Frame(Solid("#1565c0"), 12, 12)
                                        hover_background Frame(Solid("#1976d2"), 12, 12)
                                        hbox:
                                            align (0.5, 0.5)
                                            spacing 12
                                            text "🔓":
                                                size 22
                                                yalign 0.5
                                            text _("M U L A I"):
                                                size 19
                                                color "#ffffff"
                                                kerning 3.0
                                                bold True
                                                yalign 0.5

                                    ## Divider
                                    frame:
                                        xfill True
                                        ysize 2
                                        background Solid("#4fc3f720")

                                    ## Judul chapter
                                    frame:
                                        xsize 336
                                        ysize 56
                                        padding (0, 0)
                                        background Solid("#00000000")
                                        text ch_title:
                                            size 22
                                            color "#4fc3f7"
                                            bold True
                                            xmaximum 336
                                            yalign 0.0

                                    null height 6

                                    ## Deskripsi
                                    frame:
                                        xsize 336
                                        ysize 106
                                        padding (0, 0)
                                        background Solid("#00000000")
                                        text ch_desc:
                                            size 17
                                            color "#7ab8cc"
                                            xmaximum 336
                                            line_spacing 6
                                            yalign 0.0

                else:
                    frame at chapter_card_locked:
                        xsize 380
                        ysize 580
                        padding (0, 0, 0, 0)
                        background Frame(Solid("#040d1a"), 18, 18)

                        vbox:
                            xfill True

                            ## THUMBNAIL TERKUNCI — 220px
                            frame:
                                xsize 380
                                ysize 220
                                padding (0, 0, 0, 0)
                                background Solid("#030a14")

                                vbox:
                                    align (0.5, 0.5)
                                    spacing 10
                                    text "🔒":
                                        size 50
                                        align (0.5, 0.5)
                                    text _("TERKUNCI"):
                                        size 15
                                        color "#1a3a5a"
                                        kerning 3.0
                                        align (0.5, 0.5)
                                        bold True

                                frame:
                                    xpos 14
                                    ypos 14
                                    padding (10, 5, 10, 5)
                                    background Frame(Solid("#0e2a4a55"), 10, 10)
                                    text ch_num:
                                        size 15
                                        color "#1a3a5a"
                                        bold True

                                frame:
                                    xfill True
                                    ysize 3
                                    ypos 217
                                    background Solid("#0e2a4a")

                            ## KONTEN TERKUNCI — 360px
                            frame:
                                xsize 380
                                ysize 360
                                padding (22, 18, 22, 18)
                                background Solid("#030c18")

                                vbox:
                                    xfill True
                                    spacing 14

                                    ## Tombol terkunci
                                    frame:
                                        xfill True
                                        ysize 58
                                        padding (0, 0)
                                        background Frame(Solid("#0c2035"), 12, 12)
                                        hbox:
                                            align (0.5, 0.5)
                                            spacing 12
                                            text "🔒":
                                                size 20
                                                yalign 0.5
                                            text _("TERKUNCI"):
                                                size 17
                                                color "#1a3a5a"
                                                kerning 2.0
                                                yalign 0.5

                                    frame:
                                        xfill True
                                        ysize 2
                                        background Solid("#0e2a4a30")

                                    frame:
                                        xsize 336
                                        ysize 56
                                        padding (0, 0)
                                        background Solid("#00000000")
                                        text "???":
                                            size 22
                                            color "#0e2a4a"
                                            bold True
                                            yalign 0.0

                                    null height 6

                                    frame:
                                        xsize 336
                                        ysize 106
                                        padding (0, 0)
                                        background Solid("#00000000")
                                        text _("Selesaikan chapter\nsebelumnya untuk\nmembuka chapter ini."):
                                            size 17
                                            color "#0e2a4a"
                                            italic True
                                            xmaximum 336
                                            line_spacing 6
                                            yalign 0.0

        else:
            text _("Belum ada chapter yang tersedia."):
                size 28
                color "#4fc3f7"
                align (0.5, 0.5)

    ## Navigasi halaman bawah
    hbox:
        xalign 0.5
        ypos 960
        spacing 40

        button:
            xysize (175, 50)
            background Frame(Solid("#071a35"), 12, 12)
            hover_background Frame(Solid("#1565c0"), 12, 12)
            sensitive page > 0
            action SetScreenVariable("page", page - 1)
            hbox:
                align (0.5, 0.5)
                spacing 10
                text "◀":
                    size 16
                    color "#4fc3f7"
                    yalign 0.5
                text _("SEBELUM"):
                    size 15
                    color "#ffffff"
                    kerning 2.0
                    yalign 0.5

        frame:
            ysize 50
            padding (24, 0)
            background Frame(Solid("#040e20"), 12, 12)
            text "{} / {}".format(page + 1, total_pages):
                size 18
                color "#4fc3f7"
                kerning 4.0
                align (0.5, 0.5)

        button:
            xysize (195, 50)
            background Frame(Solid("#071a35"), 12, 12)
            hover_background Frame(Solid("#1565c0"), 12, 12)
            sensitive page < total_pages - 1
            action SetScreenVariable("page", page + 1)
            hbox:
                align (0.5, 0.5)
                spacing 10
                text _("SELANJUTNYA"):
                    size 15
                    color "#ffffff"
                    kerning 2.0
                    yalign 0.5
                text "▶":
                    size 16
                    color "#4fc3f7"
                    yalign 0.5

    ## Tombol Kembali
    button:
        action Return()
        xpos 40
        ypos 40
        xysize (165, 50)
        background Frame(Solid("#071a35"), 12, 12)
        hover_background Frame(Solid("#1565c0"), 12, 12)
        hbox:
            align (0.5, 0.5)
            spacing 12
            text "◀":
                size 18
                color "#4fc3f7"
                yalign 0.5
            text _("KEMBALI"):
                size 17
                color "#ffffff"
                kerning 2.0
                yalign 0.5
