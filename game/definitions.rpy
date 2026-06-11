# Data chapter: list of dicts dengan title, description, dan image untuk setiap chapter
default chapters = [
    {
        "title": _("Prolog: Pertemuan Pertama"),
        "description": _("tahun kemarin tahun yang membosankan. Namun, tahun ini ada sesuatu yang merubah hidup lo dan pertemuan pertama yang akan mengubah nasib lo yang membosankan."),
        "image": "images/bg/apartment a exterior day.png",
        "label": "prolog_start"
    },
    {
        "title": _("Chapter 2: kesialan yang mengejutkan"),
        "description": _("di hari ini lu ngalamin sial yaitu telat bangun, lu bergegas berangkat sekolah namun ada hal yang tak terduga"),
        "image": "images/chapter2.png",
        "label": "chapter1_start"
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
    zoom 1.15
    yalign 1.0

# Karakter
define t = Character("kenzo", color="#ffffff", what_slow_cps=20, callback=typewriter_callback)
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
    zoom 0.6
    xalign 0
    yalign 1.0
