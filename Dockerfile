
FROM python:3.7

RUN useradd -m app

USER app

COPY --chown=app:app sources /home/app/project

WORKDIR /home/app/project

RUN pip install --user -r requirements.txt

CMD ["/home/app/project/run.sh"]
