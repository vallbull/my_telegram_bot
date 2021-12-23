FROM python:3.8.10
WORKDIR /usr/src/app
COPY . .
RUN pip install --user pyTelegramBotAPI
CMD ["python3", "mybot.py"]
~                               
