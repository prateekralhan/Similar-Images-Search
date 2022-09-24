# 🚀 Similar Images Search 📷 [![Project Status: Active](https://www.repostatus.org/badges/latest/active.svg)](https://www.repostatus.org/#active) [![](https://img.shields.io/badge/Prateek-Ralhan-brightgreen.svg?colorB=ff0000)](https://prateekralhan.github.io/)
A streamlit based webapp to search for similar images as per the user's input (textual info, image URLs, uploaded image anything!! ). This work has been inspired by [getsimilar](https://github.com/ternaus/getsimilar) built by [ternaus](https://github.com/ternaus) 😯!

![1](https://user-images.githubusercontent.com/29462447/192104038-b95e79f9-8ca3-46a1-9e23-01e5f99eedd0.gif)

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

* Based on user's text prompt

![1](https://user-images.githubusercontent.com/29462447/192104200-8f1de826-09f3-49e4-8aaf-6cb938fb93de.gif)

* Based on an Image URL

![2](https://user-images.githubusercontent.com/29462447/192104193-6805eee2-d402-473e-8b76-40b4c8682e4c.gif)

* Based on an Image uploaded by the user

![3](https://user-images.githubusercontent.com/29462447/192104376-d49468c0-880c-4f79-8deb-c21830845a1f.gif)


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
