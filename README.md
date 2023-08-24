# qa-webapp
a front end that answer you questions about a pdf formated book. 

## how to run it
```
git clone https://github.com/EmanuelRiquelme/qa-webapp
wget https://github.com/sophiamyang/tutorials-LangChain/blob/main/materials/example.pdf -P app/back-end
sudo docker build -t qa-app --build-arg API_KEY_SECRET='PLACE-YOUR-OPEN-AI-API-KEY-HERE' .
sudo docker run -p 8000:8000 -p 8501:8501 qa-app
http://localhost:8000
```
