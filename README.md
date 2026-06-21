# Mailer

Prosty projekt Mailer w Pythonie z Flask, służący do zarządzania subskrybentami i wysyłania newsletterów.

## Struktura projektu

- `mailer/` - logika aplikacji i moduły
- `templates/` - szablony HTML Flask
- `static/` - CSS i zasoby statyczne
- `tests/` - testy jednostkowe
- `.agents/` - konfiguracje agentów AI
- `.copilot/skills/` - konfiguracje umiejętności Copilot
- `requirements.txt` - zależności Pythona

## Wymagania

- Python 3.9+
- Flask
- pytest

## Instalacja

1. Utwórz i aktywuj środowisko wirtualne:

```bash
python -m venv venv
venv\Scripts\activate
```

2. Zainstaluj zależności:

```bash
pip install -r requirements.txt
```

## Konfiguracja

Mailer używa zmiennych środowiskowych do ustawień SMTP i Flask.

Przykładowe wartości:

- `SMTP_SERVER` - adres serwera SMTP (domyślnie `localhost`)
- `SMTP_PORT` - port SMTP (domyślnie `1025`)
- `SMTP_USERNAME` - nazwa użytkownika SMTP
- `SMTP_PASSWORD` - hasło SMTP
- `FLASK_SECRET` - sekret Flask do sesji i flash messages
- `SUBSCRIBER_STORAGE_PATH` - ścieżka do pliku przechowującego subskrybentów

Możesz ustawić te zmienne w systemie lub pliku `.env`.

## Uruchamianie aplikacji

### Opcja 1: Automatyczne (Windows)

Dwuklik na `run.bat` - uruchomi Flask i otworzy przeglądarkę automatycznie.

### Opcja 2: Ręczne

1. Ustaw zmienną `FLASK_APP`:

```bash
set FLASK_APP=mailer
```

2. Uruchom serwer deweloperski Flask:

```bash
flask run
```

Aplikację otwórz w przeglądarce pod adresem: `http://127.0.0.1:5000`

## Testowanie wysyłania maili

Aby testować wysyłanie maili, musisz uruchomić testowy serwer SMTP:

### Opcja 1: Automatyczne (Windows)

Dwuklik na `start-smtp-server.bat` - uruchomi mock serwer SMTP, który drukuje wszystkie maile w konsoli.

### Opcja 2: Ręczne

```bash
python -m smtpd -c DebuggingServer -n localhost:1025
```

Uruchom to w osobnym oknie terminala/PowerShell. Maile będą drukowane w konsoli zamiast być wysyłane.

## Testy

Uruchom testy pytest:

```bash
pytest
```

## Jak działa aplikacja

- `mailer/web.py` - obsługuje trasy Flask:
  - `GET /` - strona główna z formularzami i listą subskrybentów
  - `POST /subscribe` - dodaje subskrybenta
  - `POST /send` - wysyła newsletter do wszystkich subskrybentów
- `mailer/subscribers.py` - zarządza listą subskrybentów w pliku JSON
- `mailer/email_sender.py` - wysyła wiadomości email
- `mailer/validators/email_validator.py` - waliduje format adresu email

## Uwaga

W środowisku deweloperskim możesz skorzystać z lokalnego serwera SMTP do testów, np.:

```bash
python -m smtpd -c DebuggingServer -n localhost:1025
```

Dzięki temu maile nie będą rzeczywiście wysyłane, tylko wyświetlone w konsoli.
