FROM python:3.6

ENV INSTALLDIR /apps/covid-stats

RUN mkdir -p $INSTALLDIR

COPY . $INSTALLDIR

WORKDIR $INSTALLDIR

RUN pip install -r requirements.txt

CMD ["python","./run.py"]
