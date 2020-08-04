# Image having basic core os requirements

FROM python:3.7.4-stretch

WORKDIR /app/

# Django app
ADD restorant_proj/ /app/

# 1. Basic python development setup
# 2. Postgresql support
# 3. Install pip requirements
# 4. Clean apt


RUN apt-get update \
    && ls /app \
    && apt-get install vim less python3-dev musl-dev -y \
    && apt-get install libpq-dev -y \
    && pip install -r requirements.txt \
    && rm -rf /var/lib/apt/lists/* \
    && rm -rf /libs


CMD [ "gunicorn", "-c", "/app/gunicorn.conf.py", "restorant_proj.wsgi:application"]