# qa-webapp
a front end that answer you questions about a pdf formated book. 
#### Please be mindful that there are grammar errors in this sentence. Also, note that it's a relatively large PDF file, and downloading it may contribute to your OpenAI billing.
## how to run it
```
git clone https://github.com/EmanuelRiquelme/qa-webapp
download this file directly https://github.com/sophiamyang/tutorials-LangChain/blob/main/materials/example.pdf and paste it here app/back-end
(neither the wget or the curl methods work)
sudo docker build -t qa-app --build-arg API_KEY_SECRET='PLACE-YOUR-OPEN-AI-API-KEY-HERE' .
sudo docker run -p 8000:8000 -p 8501:8501 qa-app
http://localhost:8000
```
