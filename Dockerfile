FROM python:latest
EXPOSE 80
USER root
RUN chmod a+x ./main.py
# ENTRYPOINT [ "./main.py" ]
