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

### Opcja 1: Automatyczna (Windows)

Dwuklik na `setup.bat` w katalogu projektu. Skrypt utworzy środowisko wirtualne, zainstaluje wymagane pakiety i zaktualizuje pip.

### Opcja 2: Ręczna

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

Aplikacja domyślnie używa `localhost:1025` jako serwera SMTP. Jeśli ten serwer nie działa, wiadomości są zapisywane do pliku `demo_emails.log`.

### Opcja 1: Automatyczne (Windows)

Dwuklik na `start-smtp-server.bat` - uruchomi lokalny serwer SMTP do testów.

### Opcja 2: Ręczne

Plik `start-smtp-server.bat` używa polecenia `python -m smtpd`, które może nie działać w nowszych wersjach Pythona. Jeśli nie działa, użyj alternatywy z modułem `aiosmtpd` lub sprawdź plik `mock_smtp_server.py`.

### Uruchomienie mock SMTP z Pythona

Jeśli chcesz uruchomić serwer w Pythonie bez `smtpd`:

```bash
python mock_smtp_server.py
```

Uruchom to w osobnym oknie terminala/PowerShell. Maile będą drukowane w konsoli lub zapisywane do `demo_emails.log`.

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

Jeśli używasz Pythona 3.12+ i `python -m smtpd` nie działa, uruchom `mock_smtp_server.py` zamiast tego:

```bash
python mock_smtp_server.py
```

Wszystkie maile zostaną wydrukowane w konsoli serwera lub zapisane do `demo_emails.log`.
