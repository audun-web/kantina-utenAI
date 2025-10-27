# Kantina Webapp

Dette er en enkel webapplikasjon for en kontorkantine, bygget med Python og Flask. Applikasjonen viser ukens meny, en liste over faste varer, og kontaktinformasjon for de ansatte.

## Funksjoner

- **Hjemmeside:** En velkomstside med generell informasjon og et bilde av kantinen.
- **Meny:** Viser en ukentlig meny i et rutenett. Dagens rett blir automatisk fremhevet basert på sanntids-dato.
- **Varer:** En oversikt over faste varer som er tilgjengelige for salg, som drikke og snacks.
- **Kontakt:** En liste over ansatte med bilde, stilling og telefonnummer.
- **Responsivt design (delvis):** Layouten tilpasser seg til en viss grad ulike skjermstørrelser.

## Teknologier

- **Backend:**
  - Python 3
  - Flask
- **Frontend:**
  - HTML5
  - CSS3 (med Flexbox og Grid)
- **Standardbiblioteker:**
  - `datetime` for å hente sanntids-dato.

## Oppsett og Kjøring

Følg disse stegene for å kjøre prosjektet lokalt.

1.  **Klone repositoriet:**
    ```bash
    git clone <din-repo-url>
    cd kantina-utenAI
    ```

2.  **Opprett og aktiver et virtuelt miljø (anbefalt):**
    ```bash
    # Opprett miljøet
    python -m venv venv

    # Aktiver på Windows
    .\venv\Scripts\activate

    # Aktiver på macOS/Linux
    source venv/bin/activate
    ```

3.  **Installer avhengigheter:**
    ```bash
    pip install Flask
    ```

4.  **Kjør applikasjonen:**
    ```bash
    python app.py
    ```

5.  **Åpne i nettleseren:**
    Naviger til `http://127.0.0.1:5000` i nettleseren din.

## Kilder
Nikolai Hauke Westergaard for å skrive lister i python filen

ChatGPT for datetime hjelp
