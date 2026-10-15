# aap-example-django

A minimal **Python Django** app, kept as a deploy example for [AI Admin Panel](https://aiadminpanel.com).

AI Admin Panel deploys it from this repository with **Git Deploy** (and **AI Deploy**) and checks
the result regularly: the page at `/` must contain the marker `aap-example:django`. Use it to see how
your own Python Django project is built, or as a starting point.

A standard Django layout (`manage.py`, `mysite/`) served by Gunicorn, which binds to `$PORT`. Set `DJANGO_SECRET_KEY` and `DJANGO_ALLOWED_HOSTS` for real use.

- The app listens on `$PORT` (default 8080).
- No secrets in this repository.
- License: MIT.
