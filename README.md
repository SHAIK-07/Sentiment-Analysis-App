
# Sentiment Analysis App with Streamlit and Hugging Face Transformers

This project is a web-based application for performing sentiment analysis on text using the Hugging Face Transformers library. The app is built with Streamlit and leverages a pre-trained model to classify text as either positive or negative sentiment.

## Features

- **Interactive Web Interface**: User-friendly input and output for sentiment analysis.
- **Pre-trained Model**: Uses the distilbert-base-uncased-finetuned-sst-2-english model from Hugging Face for reliable sentiment predictions.
 - **Confidence Scores**: Provides a confidence score for the predicted sentiment.

## Installation

 **Prerequisites**:

 Python 3.7 to 3.11

 Pip (Python package manager)

**Clone the Repository** :
```bash
git clone https://github.com/SHAIK-07/Sentiment-Analysis-App/sentiment-analysis-app.git
cd sentiment-analysis-app
```
**Install Required Libraries** :

Run the following command to install all dependencies:
```bash
pip install -r requirements.txt
```
**Ensure either PyTorch or TensorFlow is installed**:
```bash
pip install torch torchvision  # Recommen
```

## Usage

**Run the Application**

Start the Streamlit server:

```bash
streamlit run app.py
```

## File Structure
```bash
sentiment-analysis-app/
│
├── app.py                 # Main Streamlit application script
├── requirements.txt       # Required Python libraries
└── README.md              # Project documentation
```
## Requirements File (requirements.txt)
```bash
streamlit
transformers
torch
```

## License

This project is licensed under the [MIT License](LICENSE). See the `LICENSE` file for more details on terms and conditions.

Feel free to use and contribute to the project under these terms!

## Acknowledgement Codes
- Hugging Face for their robust Transformers library.
- Streamlit for making data apps simple and intuitive.
- The distilbert-base-uncased-finetuned-sst-2-english model used for sentiment analysis

## Live Demo

[Sentiment-Analysis-App](https://huggingface.co/spaces/SHAIKT07/Sentiment-Analysis-App)
