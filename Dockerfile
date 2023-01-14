FROM python:3.10
EXPOSE 5005
WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip3 install --upgrade setuptools
RUN pip3 install -r requirements.txt
RUN chmod 755 .
COPY . .
CMD ["gunicorn", "-w", "3", "-b", "0.0.0.0:5005", "manage:app"]




