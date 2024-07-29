FROM python:3.10
LABEL maintainer="vinogradova.lisaveta@gmail.com"
WORKDIR /the-blog
COPY . /the-blog
RUN pip install --no-cache-dir -r requirements.txt
CMD ["python", "manage.py"]
