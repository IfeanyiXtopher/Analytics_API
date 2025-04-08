# Django Analytics API

A simple Django REST API to track website visits.

## Features

- Authentication: Uses Django's built-in user model.
- Endpoints:
  - `POST /api/visits/` to record a visit.
  - `GET /api/visits/stats/` to retrieve aggregated stats.
- Management command: `python manage.py generate_visits` to create 10,000 fake visits.

## Setup

1. **Clone the repo**:
   ```bash
   git clone <repo-url>
   cd django_analytics_api
   ```

2. **Create a virtual environment & install dependencies**:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

3. **Apply migrations**:
   ```bash
   python manage.py migrate
   ```

4. **Create a superuser**:
   ```bash
   python manage.py createsuperuser
   ```

5. **Run the server**:
   ```bash
   python manage.py runserver
   ```

## Usage

- Obtain a session or basic auth credentials by logging in at `/admin/`.
- Send authenticated requests to the API endpoints.

## Generate Fake Data

```bash
python manage.py generate_visits
```

## License

MIT
