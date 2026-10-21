# xrwvm-fullstack_developer_capstone

## Project name

**fullstack_developer_capstone**

Repository name: `xrwvm-fullstack_developer_capstone`

A capstone Django and React application for browsing car dealers, viewing dealer details and reviews, registering users, and submitting sentiment-analyzed reviews.

## Run locally

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

The API is available under `/api/`, and the static frontend pages are under `/static/`.
