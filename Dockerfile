FROM python:3.10
EXPOSE 5005
WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip3 install --upgrade setuptools \
    && pip3 install gunicorn
RUN pip3 install -r requirements.txt
RUN chmod 755 .
COPY . .
RUN python manage.py collectstatic --no-input
CMD ["gunicorn", "-w", "3", "-b", "0.0.0.0:5005", "object_detection_app.wsgi"]




