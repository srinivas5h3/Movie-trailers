import media
import fresh_tomatoes
print("Content-type:text/html\n")

agv = media.Movie("Agnyaathavaasi", "sentiment", "https://bit.ly/2KGQgXe",
                  "https://www.youtube.com/embed/97h9fBWltBM")

kn = media.Movie("Khaidi no 150", "action", "https://bit.ly/2wWphEU",
                 "https://www.youtube.com/embed/UwYfxVlwy64")

rgm = media.Movie("Rangasthalam", "brother sentiment",
                  "https://bit.ly/2kdiEoN",
                  "https://www.youtube.com/embed/sueMmTm-M4Y")

nps = media.Movie("Naa Peru Surya", "action", "https://bit.ly/2Leklyi",
                  "https://www.youtube.com/embed/ZnVIUr_BQSs")

tp = media.Movie("Tholiprema", "love", "https://bit.ly/2IWlrAp",
                 "https://www.youtube.com/embed/-kFvrsAgp3M")
movies = [agv, kn, rgm, nps, tp]
fresh_tomatoes.open_movies_page(movies)
