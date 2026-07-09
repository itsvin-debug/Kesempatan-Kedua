# Data chapter: list of dicts dengan title, description, dan image untuk setiap chapter
default chapters = [
    {
        "title": _("Buku: Awal Mula"),
        "description": _("Lu dulu bekerja di perusahaan gelap yang menjual barang ilegal dan lu berhenti dari pekerjaan itu. Namun keberhentian lu malah membuat masalah besar"),
        "image": "images/bg/apartment a exterior day.png",
        "label": "prolog_start"
    },
    {
        "title": _("Buku 1: Awal Perubahan"),
        "description": _("Entah kenapa lu balik ke masa - masa SMA lu, lu masih belum mengerti apa yang terjadi namun ini adalah kesempatan lu untuk merubah kehidupan menjadi lebih baik"),
        "image": "images/bg/apartment a exterior day.png",
        "label": "chapter1_start"
    },
    {
        "title": _("Buku 3: "),
        "description": _("kejadian yang tidak terduga, lu pikir akan mati tapi malah balik ke masa lalu, apakah ini keajaiban untuk lu merubah diri dan kembali ke jalan yang lurus?"),
        "image": "images/chapter2.png",
        "label": "chapter2_start"
    },
    {
        "title": _("Chapter 3: the first step in yor life"),
        "description": _("langkah awal yang akan mengubah hidup lo kedepannya"),
        "image": "images/chapter3.png",
        "label": "chapter2_start"
    },
    {
        "title": _("Chapter 4: the last day"),
        "description": _("setelah lu nganterin dia, lu bergegas untuk berangkat ekskul dan menghabiskan hari ini. Apakah besok hari lo berubah?"),
        "image": "images/chapter4.png",
        "label": "chapter4_start"
    },
    {
        "title": _("Chapter 5: coming soon"),
        "description": _("-"),
    },
    {
        "title": _("Chapter 6: coming soon"),
        "description": _("-"),
    },
    {
        "title": _("Chapter 7: coming soon"),
        "description": _("-"),
    },
    {
        "title": _("Chapter 8: coming soon"),
        "description": _("-"),   
    },
    {
    
        "title": _("Chapter 9: coming soon"),
        "description": _("-"),
    },
]

# Variabel persistent untuk melacak chapter yang telah selesai (0 = belum ada, 1 = chapter 1 selesai, dst.)
default persistent.chapter_completed = 0
default persistent.chapter = 0

init python:
    def typewriter_callback(event, **kwargs):
        if event == "show":
            renpy.music.play("audio/dialog.ogg", channel="sound", loop=True) 
            renpy.music.set_volume(1, channel="sound")
        elif event == "slow_done" or event == "end":
            renpy.music.stop(channel="sound")

# === GAME OVER TEXT POS ===
transform game_over_pos:
    xalign 0.5
    yalign 0.38

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
    zoom 0.75
    xpos 0
    xanchor 0.0
    yalign 1.0

# === WARNA PER KARAKTER ===
# Setiap karakter memiliki warna khas masing-masing pada dialog box.
# Kenzo: Oranye (#f83e00) | Rio: Biru (#1fa0e0) | Kael: Merah-pink (#cc3355)
# Lisa: Pink (#e0407a) | Satpam: Biru tua (#4a6ae6) | Pak Agus: Hijau (#33cc55)
# Osis: Ungu (#9b59b6) | Elina: Kuning emas (#f5b800) | narator: Merah-pink (#cc3355)

# Karakter
define t = Character("Kenzo", color="#ffffff", what_slow_cps=20, callback=typewriter_callback)
define r = Character("Rio", color="#ffffff", what_slow_cps=20, callback=typewriter_callback)
define e = Character("Elina", color="#ffffff", what_slow_cps=20, callback=typewriter_callback)
define o = Character("Osis", color="#ffffff", what_slow_cps=20, callback=typewriter_callback)
define k = Character("Kael", color="#ffffff", what_slow_cps=20, callback=typewriter_callback)
define n = Character("narator", color="#ffffff", what_slow_cps=20, callback=typewriter_callback)
define l = Character("Lisa", color="#ffffff", what_slow_cps=20, callback=typewriter_callback)
define s = Character("Satpam", color="#ffffff", what_slow_cps=20, callback=typewriter_callback) 
define g = Character("Pak Agus", color="#ffffff", what_slow_cps=20, callback=typewriter_callback)

# Efek Baris Dialog
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


image bg kelas_siang = "bg/kelas siang.png"
image bg kelas_sore = "bg/kelas sore.png"
image bg kelas_malam = "bg/kelas malam.png"

image cutscene balkon = im.Scale("images/cutscene/balkon.png", 1920, 1080)
image bg balkon = im.Scale("images/bg/balkon.png", 1920, 1080)

# Character transforms (Zoom/Pos)
transform zoom_satpam:
    zoom 2.6
    xalign -0.1
    yalign 0.1

transform zoom_guru:
    zoom 2.6
    xalign -0.1
    yalign 0.1

transform zoom_alice:
    zoom 0.75
    xpos 0
    xanchor 0.0
    yalign 1.0

transform cila_left:
    zoom 0.75
    xpos 0
    xanchor 0.0
    yalign 1.0

transform kael_left:
    zoom 0.75
    xpos 0
    xanchor 0.0
    yalign 1.0

transform kael_left1:
    zoom 1
    xanchor 0.0
    yalign 1.0

transform rio_left:
    zoom 0.75
    xpos 0
    xanchor 0.0
    yalign 1.0
