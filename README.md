[![Format](https://github.com/nogibjj/IDS706_DataEngineering_BarbaraFlores_Project4/actions/workflows/format.yml/badge.svg)](https://github.com/nogibjj/IDS706_DataEngineering_BarbaraFlores_Project4/actions/workflows/format.yml)
[![Install](https://github.com/nogibjj/IDS706_DataEngineering_BarbaraFlores_Project4/actions/workflows/install.yml/badge.svg)](https://github.com/nogibjj/IDS706_DataEngineering_BarbaraFlores_Project4/actions/workflows/install.yml)
[![Test](https://github.com/nogibjj/IDS706_DataEngineering_BarbaraFlores_Project4/actions/workflows/test.yml/badge.svg)](https://github.com/nogibjj/IDS706_DataEngineering_BarbaraFlores_Project4/actions/workflows/test.yml)
[![Lint](https://github.com/nogibjj/IDS706_DataEngineering_BarbaraFlores_Project4/actions/workflows/lint.yml/badge.svg)](https://github.com/nogibjj/IDS706_DataEngineering_BarbaraFlores_Project4/actions/workflows/lint.yml)



IDS706_DataEngineering_BarbaraFlores_Project4
## 📂 Auto Scaling Flask App Using Any Platform As a Service


This project involves building a publicly accessible auto-scaling container using Azure App Services and Flask. 
The application translates English text to Spanish using the Helsinki-NLP Opus MT model.

### 🎥 Video Tutorial
The following [YouTube link](https://youtu.be/EFe9FRIGIUc) shows a clear, concise walkthrough and demonstration of the project


###🌲 Project Structure

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
- Build the Docker image: `docker build -t your-image-name .`
- Run the Docker container: `docker run -p 5000:5000 your-image-name`

### Azure Web App
1. Deploy the container to Azure App Services.
2. Access the public endpoint provided by Azure.




![000.png](https://raw.githubusercontent.com/nogibjj/IDS706_DataEngineering_BarbaraFlores_Project4/main/images/000.png)
![001.png](https://raw.githubusercontent.com/nogibjj/IDS706_DataEngineering_BarbaraFlores_Project4/main/images/001.png)
![002.png](https://raw.githubusercontent.com/nogibjj/IDS706_DataEngineering_BarbaraFlores_Project4/main/images/002.png)


## Conclusion
In conclusion, this project demonstrates the implementation of an auto-scaling Flask app using Azure App Services. The translation functionality is powered by the Helsinki-NLP Opus MT model. To further enhance scalability, consider optimizing containerization and deployment strategies.


