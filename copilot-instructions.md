# GitHub Copilot Instructions - Mailer Project

## 1. Python i Zależności
- Python 3.9+
- PEP 8, linting: flake8, black
- Type hints obowiązkowe dla każdej nowej funkcji
- `requirements.txt` zawsze aktualny

## 2. Struktura kodu
- Moduły: max 500 linii
- Funkcje: max 50 linii
- Klasy: odpowiadają pojedynczej odpowiedzialności
- Separacja logiki biznesowej od widoków Flask
- `mailer/` zawiera logikę aplikacji
- `templates/` zawiera HTML Flask
- `static/` zawiera CSS i JS
- `tests/` zawiera testy jednostkowe

## 3. Testy
- 80% code coverage
- pytest + pytest-cov
- Mock email i bazy danych
- Testy izolowane bez zewnętrznych usług
- Wszystkie krytyczne funkcje muszą mieć testy

## 4. Bezpieczeństwo
- Brak credentials w kodzie
- Environment variables dla secrets
- Waliduj dane wejściowe, w szczególności adresy email
- Unikaj SQL injection, jeśli pojawi się baza danych

## 5. Git
- Commity: conventional commits
- Branch naming: feature/*, bugfix/*, docs/*
- PRs: opisane, z testami

## 6. HTML/CSS/JS
- Szablony Flask w `templates/`
- Statyczne zasoby w `static/`
- Unikaj inline CSS/JS
