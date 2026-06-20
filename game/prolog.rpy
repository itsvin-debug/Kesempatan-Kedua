label prolog_start:

    # Nanti tambahkan scene video / cutscene di sini
    # Contoh play video:
    # $ renpy.movie_cutscene("movies/cutscene.webm")

    $ persistent.chapter_completed = max(persistent.chapter_completed, 1)

    jump chapter1_start
