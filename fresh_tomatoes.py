import webbrowser
import os
import re
print("Content-type:text/html\n")

main_page_head = '''
<html>
   <head>
    <meta http-equiv = "content-type" content = "text/html">
    <link rel = "stylesheet" href = "mt.css">

    <title>
        movie trailers
    </title>
    <div>
        <div>
            <!-- The Modal -->
            <div id = "myModal" class = "modal">

                <!-- Modal content -->
                <div class="modal-content">
                    <span class="close">&times;</span>
                    <iframe id="f" width="100%" height="315" src=""
                    frameborder="0" allow="autoplay;
                    encrypted-media" allowfullscreen></iframe>
                </div>
            </div>
        </div>
        <script>
            // Get the modal
            var modal = document.getElementById('myModal');

            // Get the <span> element that closes the modal
            var span = document.getElementsByClassName("close")[0];
            // When the user clicks on the button, open the modal
            onc = function (c) {
                modal.style.display = "block";
                c = 'https://www.youtube.com/embed/' + c;
                console.log(c);
                document.getElementById("f").setAttribute("src", c);
            }
            // When the user clicks on <span> (x), close the modal
            span.onclick = function () {
                modal.style.display = "none";
            }
            span.onclick = function(){
            console.log("hello");
            var iframe = document.getElementById("f");
            iframe.src = iframe.src;
            modal.style.display = "none";
            }


            // When the user clicks anywhere outside of the modal, close it
            window.onclick = function (event) {
                if (event.target == modal) {
                    modal.style.display = "none";
                }
            }
        </script>

</head>

'''

main_page_content = '''
<body>
        <header>
            <center>
                    <b>Movie Trailers</b>
            </center>
        </header>
        <div class="main">
            <div class="m1" onclick="onc('97h9fBWltBM')">
                <img src="https://bit.ly/2KGQgXe">
                <center><b><p>Agnyaathavaasi</p></b></center>
                </div>
            <div class="m2" onclick="onc('UwYfxVlwy64')">
                <img src="https://bit.ly/2wWphEU" >
                                <center><b>
                            <p>Khaidi no 150</p>
                    </b></center>
            </div>
                    <div class="m3" onclick="onc('sueMmTm-M4Y')">
                        <img src="https://bit.ly/2kdiEoN">
                        <center><b><p>Rangasthalam</p></b></center>
                        </div>
                        <div class="m4" onclick="onc('ZnVIUr_BQSs')">
                            <img src="https://bit.ly/2Leklyi">
                            <center><b><p>Naa Peru Surya</p></b></center>
            </div>
            <div class="m5" onclick="onc('-kFvrsAgp3M')">
                                <img src="https://bit.ly/2IWlrAp">
                                <center>
                                    <b><p>Tholiprema</p></b>
                                </center>
            </div>
        </div>
</body>
</html>
'''
movie_tile_content = '''
<div class="col-md-6 col-lg-4 movie-title text-center" data-trailer-youtbe-id=
           "{trailer_youtube_id}" data-toggle="modal" data-target="#trailer">
     <img src="{poster_image_url}" width="220" height="342">
     <h2 style="color:white;">{movie_title}</h2>
    </div>
'''


def create_movie_tiles_content(movies):
    content = ''
    for movie in movies:
        youtube_id_match = re.search(
            r'(?<=v=)[^&#]+', movie.trailer_youtube_url)
        youtube_id_match = youtube_id_match or re.search(
            r'(?<=v=)[^&#]+', movie.trailer_youtube_url)
        trailer_youtube_id = (youtube_id_match.group(0) if youtube_id_match
                              else None)
        content += movie_tile_content.format(
            movie_title=movie.title,
            poster_image_url=movie.poster_image_url,
            trailer_youtube_id=trailer_youtube_id
         )
        return content


def open_movies_page(movies):
    output_file = open('fresh_tomatoes.html', 'w')
    rendered_content = main_page_content.format(
        movie_tiles=create_movie_tiles_content(movies))
    output_file.write(main_page_head+rendered_content)
    output_file.close()

    url = os.path.abspath(output_file.name)
    webbrowser.open('file://'+url, new=2)
