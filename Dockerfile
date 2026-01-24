FROM mcr.microsoft.com/playwright/python:jammy

WORKDIR /app

ENV PIP_DISABLE_PIP_VERSION_CHECK=1 \
    PIP_NO_CACHE_DIR=1 \
    PYTHONUNBUFFERED=1

COPY requirements.txt /app/requirements.txt
RUN pip install --upgrade pip && pip install -r /app/requirements.txt

# Ставим браузеры под ТВОЮ версию playwright из requirements.txt
RUN python -m playwright install --with-deps

COPY . /app

RUN mkdir -p /app/allure-results /app/videos /app/tracing

CMD ["python", "-m", "pytest", "tests", "-s", "-v", "--alluredir=/app/allure-results"]
