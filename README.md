Opis projektu:
Aplikacja generuje sformatowany kod HTML na podstawie dostarczonego artykułu tekstowego oraz odpowiedniego promptu, korzystając z API OpenAI oraz tworzy plik podglądowy,
który umożliwia wizualizację artykułu z zastosowaniem odpowiedniego stylu i struktury. Projekt składa się z dwóch głównych części:

Generowanie kodu HTML na podstawie artykułu i prompta. - plik task.py

Dla chętnych: Tworzenie pliku podglądowego z pełnym widokiem artykułu na podstawie wygenerowanego kodu HTML. - plik podglad.py

Struktura plików
sample_article.txt: Plik wejściowy z artykułem w formacie tekstowym.
prompt.txt: Zawiera instrukcje dla modelu OpenAI do przekształcenia tekstu w HTML.
artykul.html: Wygenerowany plik HTML z artykułem.
szablon.html: Szablon HTML zawierający style CSS i miejsce na kod artykułu.
podglad.html: Pełny podgląd artykułu z zastosowanym stylem CSS, wygenerowany na podstawie szablon.html oraz artykul.html.

Instrukcja uruchomienia:
Ustaw zmienną środowiskową dla klucza OpenAI API:
Edytuj zmienne środowiskowe --> Zmienne środowiskowe --> Nowa --> Nazwa: OPENAI_API_KEY_RAFALM Wartość: klucz API OpenAI z maila

Upewnij się, że klucz OpenAI jest zapisany w zmiennej środowiskowej OPENAI_API_KEY_RAFALM:
Otwórz cmd i wpisz komendę echo %OPENAI_API_KEY_RAFALM%. Powinieneś w odpowiedzi otrzymać wartość klucza API OpenAI

Zmienna środowiskowa została ustawiona ze względów bezpieczeństwa, ponieważ hardkodowanie jej w kodzie niesie za sobą ryzyko!

Aby uruchomić program, który na podstawie wysłanego do api OpenAI promptu oraz artykułu zwraca plik artykul.html należy uruchomić Visual Studio Code i wpisać komendę w terminalu:
python .\task.py  oczywiście z poziomu katalogu, w którym znajduje się plik wpisując wcześniej: cd "Ścieżka do katalogu"
Analogicznie aby uruchomić program, który generuje wystylizowany podgląd artykułu należy wpisać komendę: python .\podglad.py 
