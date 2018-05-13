FROM python:3.6.5-alpine3.7

LABEL maintainer="Kyle O'Brien, kdobrien@ucsc.edu"

# The requirements file is copied first so that it's installation is cached.
# This reduces container build time since Docker will only reinstall requirments if the file is changed.

COPY requirements.txt cruzhacks/api/requirements.txt
RUN pip install -r cruzhacks/api/requirements.txt

COPY . cruzhacks/api/

WORKDIR cruzhacks/api/

EXPOSE 300

RUN python -u seed.py

CMD ["python", "app.py"]