FROM python:3
ADD chat chat
EXPOSE 8000
WORKDIR /chat
# Install any needed packages specified in requirements.txt
RUN pip install Flask==3.0.0
ENTRYPOINT ["python3", "server.py"]