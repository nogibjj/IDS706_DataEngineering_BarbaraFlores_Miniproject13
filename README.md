[![Format](https://github.com/nogibjj/IDS706_DataEngineering_BarbaraFlores_Project4/actions/workflows/format.yml/badge.svg)](https://github.com/nogibjj/IDS706_DataEngineering_BarbaraFlores_Project4/actions/workflows/format.yml)
[![Install](https://github.com/nogibjj/IDS706_DataEngineering_BarbaraFlores_Project4/actions/workflows/install.yml/badge.svg)](https://github.com/nogibjj/IDS706_DataEngineering_BarbaraFlores_Project4/actions/workflows/install.yml)
[![Test](https://github.com/nogibjj/IDS706_DataEngineering_BarbaraFlores_Project4/actions/workflows/test.yml/badge.svg)](https://github.com/nogibjj/IDS706_DataEngineering_BarbaraFlores_Project4/actions/workflows/test.yml)
[![Lint](https://github.com/nogibjj/IDS706_DataEngineering_BarbaraFlores_Project4/actions/workflows/lint.yml/badge.svg)](https://github.com/nogibjj/IDS706_DataEngineering_BarbaraFlores_Project4/actions/workflows/lint.yml)



IDS706_DataEngineering_BarbaraFlores_Project4
## 📂 Auto Scaling Flask App Using Any Platform As a Service

### Project Overview
In this project, we have created a Translation App using Flask, allowing users to translate English text to Spanish seamlessly. The core functionality is powered by the Helsinki-NLP Opus MT model, showcasing the integration of advanced natural language processing capabilities into a Flask web application.

### Why Auto Scaling?
Auto scaling is a critical aspect of modern web applications, ensuring that the infrastructure adapts dynamically to varying workloads. This project not only demonstrates the translation capabilities of our app but also highlights the implementation of auto-scaling features using Azure App Services. By doing so, we address the need for efficiency, performance, and scalability in a real-world deployment scenario.

### How to Use This README
This README serves as a comprehensive guide for developers, reviewers, and anyone interested in understanding the structure, deployment process, and functionality of the Auto Scaling Flask App. Whether you're here to explore the codebase, run the application locally, or deploy it to the cloud, you'll find detailed instructions and insights to assist you on your journey.


## 🎥 Video Tutorial
The following [YouTube link](https://youtu.be/EFe9FRIGIUc) shows a clear, concise walkthrough and demonstration of the project.


## 🌲 Project Structure
The project structure is as follows:

```bash
.
├── Dockerfile
├── Makefile
├── README.md
├── app.py
├── requirements.txt
├── setup.sh
├── templates
│   └── index.html
└── test_main.py

```


## Setup and Running
1. Install dependencies: `pip install -r requirements.txt`
2. Run the application locally: `python app.py`
3. Open a web browser and go to [http://localhost:5000](http://localhost:5000)

## Deployment
### Docker Container
- Build the Docker image:
```bash
docker build -t barbarapfloresrios/translator_app .
```

- Run the Docker container:
```bash
docker run -p 5000:5000 barbarapfloresrios/translator_app 
```


## Dependencies
- Flask: 2.0.0
- transformers: 4.12.0


### Azure Web App
1. Deploy the container to Azure App Services.
2. Access the public endpoint provided by Azure.
![000.png](https://raw.githubusercontent.com/nogibjj/IDS706_DataEngineering_BarbaraFlores_Project4/main/images/000.png)


### 🎥 Esxample of use
![001.png](https://raw.githubusercontent.com/nogibjj/IDS706_DataEngineering_BarbaraFlores_Project4/main/images/001.png)
![002.png](https://raw.githubusercontent.com/nogibjj/IDS706_DataEngineering_BarbaraFlores_Project4/main/images/002.png)


## Conclusion
In conclusion, this project demonstrates the implementation of an auto-scaling Flask app using Azure App Services. The translation functionality is powered by the Helsinki-NLP Opus MT model. To further enhance scalability, consider optimizing containerization and deployment strategies.


