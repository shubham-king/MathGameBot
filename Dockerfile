FROM python:3.8.3-alpine

WORKDIR ./
ENV TZ=Europe/Moscow
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone
RUN apk --no-cache add gcc musl-dev
COPY . .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

ENTRYPOINT ["python", "bot.py"]