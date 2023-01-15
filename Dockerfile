FROM python:3.10
EXPOSE 5005
WORKDIR /app

COPY requirements.txt requirements.txt
ENV PYTHONUNBUFFERED 1
RUN python -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

RUN pip3 install --upgrade setuptools \
    && pip3 install gunicorn
RUN pip3 install -r requirements.txt --no-cache-dir
RUN chmod 755 .
COPY . .
RUN python manage.py collectstatic
CMD ["gunicorn", "-w", "3", "-b", "0.0.0.0:5005", "object_detection_app.wsgi"]

