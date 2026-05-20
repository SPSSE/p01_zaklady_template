# P1 – Proměnné a datové typy

**Předmět:** Informatika / Python &nbsp;|&nbsp; **Délka:** 45 min &nbsp;|&nbsp;

---

## Zadání

Otevři soubor `solution.py` a doplň kód na místo každého `# TODO` komentáře.

---

### Úkol 1 – Jméno a věk

Napiš program, který se zeptá uživatele na **jméno** a **věk** a vypíše:

```
Ahoj Jana, za 10 let ti bude 25 let.
```

> Čísla závisí na zadaném vstupu. Věk načti jako celé číslo (`int`).

---

### Úkol 2 – Operátory

Vypiš výsledky těchto tří výrazů, každý na nový řádek:

| Výraz    | Co dělá                    |
|----------|----------------------------|
| `10 / 3` | Dělení s desetinným výsledkem |
| `10 // 3`| Celočíselné dělení         |
| `10 % 3` | Zbytek po dělení           |

---

### Úkol 3 – Kalkulačka

Program načte **dvě čísla** (jako `float`) a vypíše:

```
Součet: 14.0
Rozdíl: 6.0
Součin: 40.0
Podíl: 2.5
```

Pokud je druhé číslo `0`, vypiš místo podílu:

```
Dělení nulou není možné.
```

---

## Jak odevzdat

1. Doplň kód do `solution.py`
2. Otestuj lokálně (viz níže)
3. **Commitni a pushni** – GitHub automaticky spustí testy

## Lokální testování

```bash
# Spusť autograder ručně
python .github/autograder/run_tests.py
```

## Hodnocení

| Test | Popis | Body |
|------|-------|------|
| `ukol1` | Výpis věty s jménem a věkem | 1 |
| `ukol2` | Výpis tří operátorů | 1 |
| `ukol3a` | Kalkulačka – normální dělení | 1 |
| `ukol3b` | Kalkulačka – dělení nulou | 1 |

**Celkem: 4 body**

---

## Tipy

- `input("text")` přečte řetězec od uživatele
- `int(...)` převede řetězec na celé číslo, `float(...)` na desetinné
- `f"Ahoj {jmeno}"` je f-string – proměnná se dosadí do textu
- `print(10 / 3)` vypíše `3.3333333333333335` (ne `3.33`)
