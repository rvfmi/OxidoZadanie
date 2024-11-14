import os

artykul_file = 'artykul.html'  
szablon_file = 'szablon.html'  
podglad_file = 'podglad.html'  

with open(artykul_file, 'r', encoding='utf-8') as f:
    artykul_content = f.read()

with open(szablon_file, 'r', encoding='utf-8') as f:
    szablon_content = f.read()

podglad_content = szablon_content.replace("<!-- ARTYKUL -->", artykul_content)

with open(podglad_file, 'w', encoding='utf-8') as f:
    f.write(podglad_content)

