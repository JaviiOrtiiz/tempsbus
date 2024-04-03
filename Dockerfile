# Image: python:latest
FROM arm32v7/python:latest
# FROM python:latest
# Set the working directory
WORKDIR /app

# Copy the requirements.txt file to the working directory
COPY requirements.txt .

# Copy main.py to the working directory
COPY app.py .

# Copiar el script de shell al contenedor
COPY run.sh .

# Copiar el script de forwardear logs al contenedor
COPY log-event.sh .

# Pasar la variable de entorno al contenedor
ENV API_KEY=${API_KEY}

#Copiar entrypoint.sh al contenedor
COPY entrypoint.sh .

# Install the required packages
RUN pip install -r requirements.txt

# Run the shell script to execute the python script periodically
CMD ["sh", "entrypoint.sh"]