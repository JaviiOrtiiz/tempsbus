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

#Copiar entrypoint.sh al contenedor
COPY entrypoint.sh .

# CHMOD the shell script to make it executable
RUN chmod +x run.sh

# Install the required packages
RUN pip install -r requirements.txt

# expose port 5000
EXPOSE 5000
# Run the shell script to execute the python script periodically
CMD ["sh", "entrypoint.sh"]