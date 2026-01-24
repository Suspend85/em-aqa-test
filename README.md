# SauceDemo Login Autotests (Playwright + Pytest + Allure)

Автотесты для проверки сценариев авторизации на сайте SauceDemo: https://www.saucedemo.com/

## Проверяем 5 сценариев
1. Успешный логин (standard_user / secret_sauce)
2. Логин с неверным паролем
3. Логин заблокированного пользователя (locked_out_user)
4. Логин с пустыми полями
5. Логин пользователем performance_glitch_user (проверка перехода и загрузки страницы при возможных задержках)

## Структура проекта
- `tests/` — тесты
- `pages/` — Page Object
- `fixtures/` — фикстуры
- `allure-results/` — результаты Allure (генерируются после запуска)
- `.github/workflows/` — CI/CD workflow


---

# Предварительные требования
- Python **3.10**
- Установленный Allure CLI (нужен только если хотите смотреть отчёт локально)
- (Опционально) Docker Desktop — для запуска тестов в контейнере


---
# Запуск локально (без Docker)
## 1) Клонировать репозиторий:  
`git clone https://github.com/Suspend85/em-aqa-test.git`    
`cd em-aqa-test`

## 2) Создать и активировать виртуальное окружение

### Windows (PowerShell):
`python -m venv venv`   
`.\venv\Scripts\Activate`

### macOS / Linux:
`python3 -m venv venv`  
`source venv/bin/activate`

## 3) Установить зависимости
`pip install -r requirements.txt`

## 4) Установить браузеры Playwright
`python -m playwright install`

## 5) Запустить все тесты
`python -m pytest -s -v --alluredir=./allure-results`

### Или запуск конкретного теста по имени
`python -m pytest -k "test_successful_authorization" -s -v --alluredir=./allure-results`

--- 
# Allure отчёт локально
### Вариант 1: Запустить сервер Allure (если установлен Allure CLI)
`allure serve allure-results`   
Запустится сайт с Allure-отчетом в браузере

### Вариант 2: Сгенерировать статический отчёт
`allure generate allure-results -o allure-report --clean`


---
# Запуск в Docker

## 1) Сборка образа
`docker build -t effective-mobile-aqa .`

## 2) Запуск тестов в контейнере и сохранение Allure results на хост
Windows PowerShell:  
`docker run --rm --env-file .env -v "${PWD}\allure-results:/app/allure-results" effective-mobile-aqa`

macOS / Linux:   
`docker run --rm --env-file .env -v "$(pwd)/allure-results:/app/allure-results" effective-mobile-aqa`

После выполнения результаты Allure будут доступны в папке `allure-results/.`


---
# CI/CD (GitHub Actions + GitHub Pages)

### Проект содержит workflow в .github/workflows/, который автоматически запускает тесты при push и pull_request.

Пайплайн запускается при условии изменений в файлах проекта:   
      - `tests/**`  
      - `pages/**`  
      - `elements/**`   
      - `fixtures/**`   
      - `tools/**`  
      - `conftest.py`   
      - `pytest.ini`    
      - `requirements.txt`  
      - `.github/workflows/**`  

**Типовой пайплайн:**   
- Checkout репозитория    
- Установка Python 3.10   
- Установка зависимостей из файла `requirements.txt`  
- Установка браузеров Playwright  
- Запуск pytest с генерацией allure-results   
- Генерация allure-report
- Публикация отчёта в GitHub Pages (если включено)

**Где смотреть результаты:**    
GitHub Actions → вкладка Actions → последний запуск workflow    
Allure отчет (GitHub Pages): публикуется как статическая страница (https://suspend85.github.io/em-aqa-test)