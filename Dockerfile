FROM python:3.9

WORKDIR /app

RUN pip install streamlit

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

CMD ["streamlit", "run", "main.py"]