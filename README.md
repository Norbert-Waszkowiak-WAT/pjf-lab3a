# pjf-lab3a

# Zadanie
Zadanie znajdują się w pliku _zad1.py_ i _zad2.py_.
Aby uruchomić testy jednostkowe, należy uruchomić polecenie:
```bash
python -m unittest test_zad1.py
python -m unittest test_zad2.py
```
### Punktacja:
- Zadanie 1: 15 pkt
- Zadanie 2: 35 pkt

# Programowanie funkcyjne w Pythonie

Programowanie funkcyjne to paradygmat programowania, który traktuje obliczenia jako ewaluację funkcji matematycznych i unika zmiany stanu i danych mutowalnych. Python, mimo że jest językiem wieloparadygmatowym, obsługuje programowanie funkcyjne. Oto kilka kluczowych aspektów programowania funkcyjnego w Pythonie:

1. **Funkcje jako obiekty pierwszej klasy**: W Pythonie funkcje są obiektami pierwszej klasy. Oznacza to, że funkcje można przypisywać do zmiennych, przechowywać w strukturach danych, przekazywać jako argumenty do innych funkcji i zwracać jako wartości z innych funkcji.

```python
def greet(name):
    return f"Hello, {name}"

say_hello = greet
print(say_hello("World"))
```

2. **Funkcje wyższego rzędu**: Funkcje, które przyjmują inne funkcje jako argumenty lub zwracają inne funkcje, nazywane są funkcjami wyższego rzędu. Przykładem może być funkcja `map`, która przyjmuje funkcję i listę jako argumenty i zwraca nową listę, która zawiera wynik zastosowania funkcji do każdego elementu listy.

```python
def square(n):
    return n * n

numbers = [1, 2, 3, 4]
squared = map(square, numbers)
print(list(squared))
```

3. **Funkcje anonimowe (lambda)**: Python obsługuje funkcje anonimowe, zwane również funkcjami lambda. Są to funkcje, które są zdefiniowane bez nazwy. Chociaż są one technicznie ograniczone do pojedynczego wyrażenia, mogą być używane w wielu miejscach, gdzie wymagane są krótkie, małe funkcje.

```python
numbers = [1, 2, 3, 4]
squared = map(lambda n: n * n, numbers)
print(list(squared))
```

4. **Czyste funkcje**: W programowaniu funkcyjnym, funkcje powinny być "czyste", co oznacza, że dla danego zestawu argumentów, funkcja zawsze powinna zwracać ten sam wynik, i nie powinna mieć żadnych efektów ubocznych.

5. **Niezmienność**: W programowaniu funkcyjnym, dane są niezmienne. Oznacza to, że zamiast modyfikować istniejące dane, tworzymy i pracujemy na nowych skopiowanych danych.

6. **Rekurencja**: W programowaniu funkcyjnym, zamiast pętli, często używa się rekurencji, gdzie funkcja wywołuje samą siebie.

Pamiętaj, że Python nie jest czystym językiem funkcyjnym i nie wszystkie te zasady są ścisłe. Python pozwala na mieszanie różnych paradygmatów programowania, co pozwala na wybór najbardziej odpowiedniego stylu dla danego problemu.

# Dekoratory

Dekoratory to potężne narzędzie w Pythonie, które pozwala na modyfikowanie zachowania funkcji lub klasy. Są to funkcje wyższego rzędu, które przyjmują funkcję lub klasę jako argument i zwracają nową funkcję lub klasę, która zazwyczaj rozszerza lub modyfikuje zachowanie oryginalnej funkcji lub klasy.

Dekoratory są używane do opakowywania innej funkcji, co pozwala na wykonanie kodu przed i po wykonaniu dekorowanej funkcji, bez modyfikowania samej funkcji. To jest szczególnie użyteczne, gdy chcesz dodać tę samą funkcjonalność do wielu różnych funkcji lub klas.

Dekoratory są zazwyczaj zdefiniowane jako funkcje, ale mogą być również zdefiniowane jako klasy. Dekoratory funkcji są najczęściej używane, ale dekoratory klas są również użyteczne w niektórych przypadkach.

Oto przykład dekoratora, który mierzy czas wykonania dekorowanej funkcji:

```python
import time

def timer_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"{func.__name__} took {end_time - start_time} seconds to run.")
        return result
    return wrapper

@timer_decorator
def slow_function():
    time.sleep(2)

slow_function()
```

W tym przykładzie, `timer_decorator` jest dekoratorem, który przyjmuje funkcję `func` jako argument. Dekorator zwraca nową funkcję `wrapper`, która wykonuje `func` i mierzy czas, jaki to zajmuje. Dekorator jest następnie używany do dekorowania `slow_function` za pomocą składni `@timer_decorator`.

Pamiętaj, że dekoratory są wykonywane od dołu do góry, a więc kolejność dekoratorów ma znaczenie.