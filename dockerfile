# Imagen sacada de la documentación de fastAPI en docker.
FROM tiangolo/uvicorn-gunicorn-fastapi:python3.9

WORKDIR /app

# Credenciales para la base en mongoDB, una vez generado el contenedor nunca se ven.
ENV operator sade
ENV operator_pwd smoothoperator

COPY ./requirements.txt /app/requirements.txt
 
COPY . /app

RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

# Comando de ejecución de la API, 0.0.0.0 no discrimina la IP del host para funcionar. 
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]