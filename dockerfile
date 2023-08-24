# Use a suitable base image
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install dependencies
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code into the container
COPY app/ app/

#api key
ARG API_KEY_SECRET
ENV OPENAI_API_KEY=$API_KEY_SECRET

# Expose ports for FastAPI and Streamlit
EXPOSE 8000 8501

#showfile
RUN ls app/back-end

# Command to run both applications using uvicorn for FastAPI and streamlit for Streamlit
CMD ["sh", "-c", "uvicorn app.back-end.main:app --host 0.0.0.0 --port 8000 & streamlit run app/front-end/app.py --server.port 8501 --server.address 0.0.0.0"]
