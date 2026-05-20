"""
Autograder – P1: Proměnné a datové typy
Spouštění:
  python .github/autograder/run_tests.py
"""

import subprocess
import sys
import os

# ── Konfigurace testů ────────────────────────────────────────
# (název testu, volá se funkce, vstup, expected soubor, body, popis)
TESTS = [
    (
        "ukol1",
        "ukol1",
        "ukol1_input.txt",
        "ukol1_expected.txt",
        1,
        "Úkol 1 – jméno a věk (Jana, 15 → věta)",
    ),
    (
        "ukol2",
        "ukol2",
        "ukol2_input.txt",
        "ukol2_expected.txt",
        1,
        "Úkol 2 – výpis operátorů (10/3, 10//3, 10%3)",
    ),
    (
        "ukol3a",
        "ukol3",
        "ukol3a_input.txt",
        "ukol3a_expected.txt",
        1,
        "Úkol 3a – kalkulačka (10 a 4)",
    ),
    (
        "ukol3b",
        "ukol3",
        "ukol3b_input.txt",
        "ukol3b_expected.txt",
        1,
        "Úkol 3b – kalkulačka – dělení nulou (5 a 0)",
    ),
]

BASE_DIR  = os.path.dirname(os.path.abspath(__file__))
TESTS_DIR = os.path.join(BASE_DIR, "tests")
SOLUTION  = os.path.join(BASE_DIR, "..", "..", "solution.py")


def spust_funkci(nazev_funkce: str, vstup: str) -> tuple[str, str]:
    """Importuje solution.py a zavolá jednu funkci se zadaným vstupem."""
    kod = f"""
import sys, os
sys.path.insert(0, os.path.dirname(r"{SOLUTION}"))

# Importuj funkci ze solution.py
import importlib.util
spec = importlib.util.spec_from_file_location("solution", r"{SOLUTION}")
mod  = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)

getattr(mod, "{nazev_funkce}")()
"""
    result = subprocess.run(
        [sys.executable, "-c", kod],
        input=vstup,
        capture_output=True,
        text=True,
        timeout=10,
    )
    return result.stdout, result.stderr


def nacti(soubor: str) -> str:
    cesta = os.path.join(TESTS_DIR, soubor)
    with open(cesta, "r", encoding="utf-8") as f:
        return f.read()


def normalizuj(text: str) -> str:
    radky = [r.rstrip() for r in text.splitlines()]
    while radky and radky[-1] == "":
        radky.pop()
    return "\n".join(radky)


def main():
    print("=" * 55)
    print("  AUTOGRADER – P1: Proměnné a datové typy")
    print("=" * 55)

    celkem_bodu = 0
    max_bodu    = sum(t[4] for t in TESTS)
    uspesnych   = 0

    for nazev, funkce, vstup_soubor, ocekavany_soubor, body, popis in TESTS:
        print(f"\n[TEST] {popis}")
        try:
            vstup     = nacti(vstup_soubor)
            ocekavany = nacti(ocekavany_soubor)
            skutecny, stderr = spust_funkci(funkce, vstup)

            if normalizuj(skutecny) == normalizuj(ocekavany):
                print(f"  ✅  PASSED  (+{body} bod)")
                celkem_bodu += body
                uspesnych   += 1
            else:
                print(f"  ❌  FAILED")
                print(f"\n  Očekávaný výstup:")
                for r in normalizuj(ocekavany).splitlines():
                    print(f"    {r}")
                print(f"\n  Skutečný výstup:")
                for r in normalizuj(skutecny).splitlines():
                    print(f"    {r}")
                if stderr.strip():
                    print(f"\n  Chyba:")
                    for r in stderr.strip().splitlines():
                        print(f"    {r}")

        except subprocess.TimeoutExpired:
            print("  ❌  FAILED – překročen časový limit (10 s)")
        except Exception as e:
            print(f"  ❌  FAILED – chyba: {e}")

    print()
    print("=" * 55)
    print(f"  Výsledek: {uspesnych}/{len(TESTS)} testů  |  {celkem_bodu}/{max_bodu} bodů")
    print("=" * 55)

    sys.exit(0 if celkem_bodu == max_bodu else 1)


if __name__ == "__main__":
    main()
