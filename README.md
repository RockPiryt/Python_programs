# Python_programs
With tests

## Write programs for studies at the University of Gdańsk

## Zadanie 1 [2 pkt]
Napisz program, który wypisze na ekranie wszystkie liczby pierwsze z zadanego zakresu.

## Zadanie 2 [2 pkt]
Liczby zaprzyjaźnione to dwie liczby naturalne, gdzie każda z nich jest równa sumie dzielników właściwych drugiej liczby. Napisz program wypisujący liczby zaprzyjaźnione z zadanego zakresu.

## Zadanie 3 [3 pkt]
Problem Józefa Flawiusza.

Wyobraź sobie następującą sytuację: jesteś powstańcem żydowskim podczas oblężenia Jotopaty w 67 roku n.e. Zostałeś otoczony wraz z 40 innymi żołnierzami przez legiony rzymskie, ale nie chcecie zostać pojmani. Po krótkiej naradzie wymyśliliście rozwiązanie: ustawicie się w kole i pierwsza osoba zabije tą znajdującą się bezpośrednio po lewej, kolejny żołnierz zabije kompana po swojej lewej, aż do momentu gdy zostanie tylko jeden powstaniec, który popełni samobójstwo. Ty jednak nie chcesz zginąć z ręki innego powstańca ani popełniać samobójstwa. Gdzie w takim razie ustawić się w tym kręgu, aby uniknąć śmerci? Jak opracować uniwersalny sposób na obliczenie bezpiecznego miejsca w kole dla dowolnej liczby znajdujących się w nim osób? W opisanej wyżej sytuacji znalazł się Józef Flawiusz, rzymsko-żydowski historyk, od którego wzięła się nazwa problemu.

Napisz program rozwiązujący ten problen dla dowolnej liczby żołnierzy.

## Zadanie 4 [3 pkt]
Napisz program, który posortuje n dat. Zdefiniuj i wykorzystaj słownik, która będzie posiadał klucze zawierające informacje na temat dnia, miesiąca i roku. Następnie posortuje dowolnym algorytmem daty rosnąco.

Uwaga: Napisz algorytm sortujący od podstaw. Nie korzystaj z gotowych rozwiązań dostępnych w Pythonie.

### Uwaga
Napisz wszystkie algorytmy bez wykorzystywania funkcji. Napisz use cases do prezentowanych algorytmów i przetestuj czy zwracają dobre wyniki - najlepiej automatycznie.

## Zadanie 5 [10 pkt]
Zadanie: Hetmani i Pionek

### Generowanie mapy [3 pkt]
Pierwszy etapem zadania będzie wygenerowanie planszy 8x8. W skład mapy wychodzą:

- k hetmanów rozmieszczonych losowa na mapie,
- jeden pionek rozmieszczony losowa na mapie.
- Każdy z elementów zostaje ustawiony na różnej pozycji. Po włączeniu programu schemat planszy powinien się wyświetlać użytkownikowi.

### Weryfikacja bicia [4 pkt]
Program powinien odpowiadać na pytania: Czy pionek zostanie zbity przez któregoś z hetmanów?

Dodakowo: wyświetlić pozycje wszystkich hetmanów, którzy mają możliwość zbicia pionka (o ile tacy istnieją).

### Dodakowe funkcje [3 pkt]
Po wyświeleniu komunikatu z informacją o biciu, użytkownik programu, powinien mieć możliwość:

- wylosowania nowej pozycji dla pionka z pozostawieniem pierwotnego układu hetmanów;
- usunięcia dowolnego hetmana (wskazanie jego pozycji);
- ponowną weryfikację bicia po ustaleniu zmian.

### Uwagi
- Hetman może poruszać się pionowo, poziomo lub ukośnie.
- Maksymalna liczba hetmanów (k) to 5.
- Napisz testy jednostkowe tam, gdzie to możliwe.
