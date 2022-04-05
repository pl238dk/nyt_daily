# Daily Newspaper (NY Times) Flask App

A Flask application that displays the front page of the current-day's New York Times in newspaper format.

Upon user request, the application grabs a PDF version of the newspaper for the current date with a fallback to the previous date's newspaper. After grabbing the PDF, a color JPG image is generated for display to a website. Page automatically refreshes every 900 seconds (15 minutes) and is suitable for always-on displays.

## Installation

### When using as a Docker application :
```
docker build -t nyt_daily Dockerfile
docker run -d -p 5002:80 --name=app nyt_daily
```
Then point your browser to http://localhost!




### When using as a standalone Flask application :
Requires downloading and installing Poppler (https://pdf2image.readthedocs.io/en/latest/installation.html)

##### Installing requirements automatically :
```
python3 -m pip install -r requirements.txt
```
##### Installing requirements manually :
```
python3 -m pip install pdf2image
```

After requirements are installed, start the Flask application :
```
python3 main.py
```

Then point your browser to http://localhost:5002!

## TODO
- Convert to HTTPS
- Allow historical view