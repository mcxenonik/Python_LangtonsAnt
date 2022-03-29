# Mrówka Langtona

Implementacja prostego automatu komórkowego, tzw. Mrówki Langtona
oraz interfejsu, za pomocą którego użytkownik mógłby modyfikować parametry tego automatu z 
wykorzystaniem języka Python.

# Instrukcja Obsługi

Program uruchamiany jest poleceniem "python RunApplication.py"

1. White image – gdy ta opcja jest wybrana po wciśnięciu przycisku Generate image zostanie
wygenerowany biały obraz.
2. Width – pole pozwalające wprowadzić szerokość generowanego obrazu w pikselach
(dostępne tylko po wybraniu opcji White image lub Random image; zakres od 2 do 1000 pikseli).
3. Height – pole pozwalające wprowadzić wysokość generowanego obrazu w pikselach
(dostępne tylko po wybraniu opcji White image lub Random image; zakres od 2 do 1000 pikseli).
4. Random image – opcja odpowiedzialna za wygenerowanie obrazu, na którym czarne piksele 
zostały losowo wygenerowane z zadanym prawdopodobieństwem.
5. Probability of black pixels – pole pozwalające wprowadzić prawdopodobieństwo z jakim 
będą pojawiać się czarne piksele na obrazie losowym (dostępne tylko po wybraniu opcji
Random image; zakres od 0 do 1 z dokładnością do 0.001).
6. Generate image – po wciśnięciu tego przycisku zostanie wygenerowany obraz zależny od 
wybranej opcji generowania obrazu (niedostępny gdy wybrana jest opcja Image from file, a 
plik zawierający obraz nie został jeszcze wybrany).
7. Image from file – po wybraniu tej opcji zostanie wygenerowany obraz z wybranego przez 
użytkownika pliku.
8. Path to image – pole pokazujące ścieżkę do aktualnie wybranego pliku z obrazem (aktywne 
tylko po wybraniu opcji Image from file; tylko do odczytu).
9. Select file – gdy ten przycisk zostanie wciśnięty pojawi się okno dialogowe pozwalające na 
wybór pliku z obrazem (aktywny tylko gdy wybrana jest opcja Image from file).
10. Save images to files – gdy to pole jest wybrane wynik poruszania się mrówki po planszy jest 
zapisywany do pliku.
11. All iterations – po zaznaczeniu tej opcji obraz z wynikiem ruchu mrówki zostanie zapisany 
po każdym jej kroku (aktywna tylko gdy opcja Save images to files jest wybrana).
12. Every N iterations – gdy ta opcja jest wybrana obrazy z wynikiem ruchu mrówki będą 
zapisywane co wybraną w polu 13 liczbę kroków (aktywna tylko gdy opcja Save images to 
files jest wybrana).
13. Iterations – pole z liczbą kroków, co którą będą zapisywane obrazy wynikowe (aktywne tylko 
gdy opcje Save images to files oraz Every N iterations są wybrane; gdy liczba jest większa od 
całkowite ilości kroków, zostanie zapisany obraz po pierwszym i ostatnim kroku; zakres od 1 
do 106).
14. Default file name – po odznaczeniu tej opcji aktywne staje się pole 14, pozwalające 
wprowadzić własną nazwę plików wynikowych, a po zaznaczeniu automatycznie ustawiana 
jest domyślna nazwa plików (aktywna tylko gdy opcja Save images to files jest wybrana).
15. W tym polu możliwe jest wpisanie własnej nazwy plików wynikowych (aktywne tylko gdy 
opcja Save images to files jest wybrana oraz opcja Default file name jest odznaczona; do 
wpisanej nazwy dodawany jest numer kroku mrówki; maksymalnie 10 znaków oraz tylko 
cyfry i litery).
16. Default save path – po odznaczeniu tej opcji możemy wybrać folder, do którego będą 
zapisywane pliki wynikowe za pomocą przycisku Select folder, a po jej wybraniu 
automatycznie zostanie przywrócona domyślna ścieżka (aktywna tylko gdy opcja Save 
images to files jest wybrana).
17. W tym polu wyświetlana jest ścieżka do folderu, w którym będą zapisywane pliki wynikowe 
(aktywne tylko gdy opcja Save images to files jest wybrana oraz opcja Default save path jest 
odznaczona; tylko do odczytu).
18. Select folder - gdy ten przycisk zostanie wciśnięty pojawi się okno dialogowe pozwalające 
na wybór folderu, w którym będą zapisywane pliki wynikowe (aktywny tylko gdy wybrana 
jest opcja Save images to files oraz opcja Default save path jest odznaczona).
19. Number of iterations – pole pozwalające wprowadzić liczbę kroków, które ma wykonać 
mrówka po planszy (zakres od 1 do 107).
20. RESET – przycisk przywracający obraz z przed wykonania wszystkich kroków mrówki na 
ostatnio wygenerowanej planszy (aktywny tylko gdy obraz został wygenerowany
przynajmniej raz).
21. RUN – przycisk po wciśnięciu którego zostanie wykonana zadana ilość kroków mrówki po 
ostatnio wygenerowanej planszy, wyświetlony obraz po wykonaniu wszystkich kroków oraz 
ewentualnie zapis obrazów do pliku (aktywny tylko gdy obraz został wygenerowany
przynajmniej raz).