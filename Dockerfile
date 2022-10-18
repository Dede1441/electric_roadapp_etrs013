FROM python:3.9
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
EXPOSE 5000
CMD flask --app electric_roadapp_interface run --host=0.0.0.0