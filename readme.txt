Projekt z przedmiotu AAL

Autor: Mateusz Śledź

Stabilne geny misia
Genom człowieka jest reprezentowany jako ciąg znaków o długości n (gdzie n jest podzielne przez 4), zbudowany za pomocą 4 liter A,C,G i T. Taki gen nazywamy stabilnym jeżeli każda z 4 liter wystąpiła dokładnie n/4 liczbę razy.
Dr Limak jest światowej sławy ekspertem do spraw modyfikacji genów niedźwiedzi. Aktualnie zamuje się problemem stabilizacji genetycznie modyfikowanych genomów. Po pierwsze sprawdza czy analizowany gen n jest stabilny. Jeżeli nie, dr Limak potrafi za pomocą metody CRISBEAR podmienić jeden fragment (podciąg) genu tak żeby ustabilizować cały gen. Jak wiadomo modyfikowanie długich fragmentów genów może być niebezpieczne, dlatego Twoim zadaniem jest znalezienie najmniejszego podciągu genu (w szczególności pustego), który można zastąpić dowolynm innym podciągiem tej samej długości, tak żeby ustabilizować gen niedźwiedzia.
Przykładowo, analizując gen ACTGAAAG, podciąg AA (po pierwszym G lub przed kolejnym G) można zastąpić ciągiem CT lub TC. Wówczas gen ACTGCTAG jest już stabilnym przykładem. Przykładowe rozwiązanie:
Wejście: GAAATAAA
Wyjście: AAATA -> TTCCG dłgugość: 5


Uruchomienie programu
Przed uruchomieniem programu należy zainstalować dodatkowe biblioteki pythona poleceniem:
	pip install PrettyTable matplotlib

Następnie program uruchamiamy w konsoli komendą
	python3 geny.py

W zależności od wybranego trybu wykonania programu:
	1) wprowadzamy własny ciąg znaków do przetworzenia, program wyświetla wynik
	2) program generuje ciąg o podanej długości, przetwarza go następnie wyświetla wyniki
	3) program pyta o wielkość ciągu początkowego, liczbę iteracji oraz liczbę liter o którą ciąg początkowy ma być powiększany co iterację. Następnie program przetwarza dane i prezentuje wyniki czasowe w postaci tabelki.

Metoda rozwiązania
Liczymy, których liter jest za dużo, i o ile za dużo w danym ciągu. Liczymy również analogicznie, których liter jest za mało i o ile za mało.
Wyznaczamy długość najkrótszego możliwego ciągu do zastąpienia dodając ilość wszystkich nadmiarowych liter.
Sprawdzamy wszystkie ciągi o danej długości, w przypadku braku wyniki długość zwiększamy.
Przez „sprawdzenie” rozumiemy policzenie i sprawdzenie czy ilość każdej z osobna nadmiarowej litery w danym ciągu jest większa bądź równa ilości nadmiarowej tej litery wyznaczonej na początku.
Tworzymy nowy ciąg składający się z liter w odpowiednich ilościach, którym zastępujemy znaleziony ciąg.

Struktury danych (python): List, Dictionary, int, string


Generowanie danych testowych

Korzystam z funkcji randint
	value = randint(0, 99999)
        value = value % 4
        genome += letters[value]

Lista "letters" zawiera 4 litery genomu: A, C, T, G


