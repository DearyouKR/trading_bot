FROM python:latest
EXPOSE 80
USER root
RUN ./main.py
ENTRYPOINT [ "./main.py" ]
