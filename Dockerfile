FROM python:3.8 as common
WORKDIR /app
RUN pip install pipenv

ADD Pipfile /app
ADD Pipfile.lock /app
RUN pipenv install --system


FROM common as dev
RUN  pipenv install --dev --system
COPY skeleton/ /app/skeleton

FROM common as prod
COPY skeleton/ /app/skeleton
ENV FLASK_APP=skeleton/app.py
CMD [ "flask", "run", "--host=0.0.0.0" ]