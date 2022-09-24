# 🚀 Similar Images Search 📷 [![Project Status: Active](https://www.repostatus.org/badges/latest/active.svg)](https://www.repostatus.org/#active) [![](https://img.shields.io/badge/Prateek-Ralhan-brightgreen.svg?colorB=ff0000)](https://prateekralhan.github.io/)
A streamlit based webapp to search for similar images as per the user's input (textual info, image URLs, uploaded image anything!! ). This work has been inspired by [getsimilar](https://github.com/ternaus/getsimilar) built by [ternaus](https://github.com/ternaus) 😯!


## Installation:
* Simply run the command ***pip install -r requirements.txt*** to install the necessary dependencies.

## Usage:
1. Head over to [this link](https://github.com/ternaus/getsimilar) and follow the steps to generate/save the API Token. 
2. Simply run the command: 
```
streamlit run app.py
```
3. Navigate to http://localhost:8501 in your web-browser.
4. By default, streamlit allows us to upload files of **max. 200MB**. If you want to have more size for uploading images, execute the command :
```
streamlit run app.py --server.maxUploadSize=1028
```


------------
## Results 
------------

### Running the Dockerized App
1. Ensure you have Docker Installed and Setup in your OS (Windows/Mac/Linux). For detailed Instructions, please refer [this.](https://docs.docker.com/engine/install/)
2. Navigate to the folder where you have cloned this repository ( where the ***Dockerfile*** is present ).
3. Build the Docker Image (don't forget the dot!! :smile: ): 
```
docker build -f Dockerfile -t app:latest .
```
4. Run the docker:
```
docker run -p 8501:8501 app:latest
```

This will launch the dockerized app. Navigate to ***http://localhost:8501/*** in your browser to have a look at your application. You can check the status of your all available running dockers by:
```
docker ps
```
