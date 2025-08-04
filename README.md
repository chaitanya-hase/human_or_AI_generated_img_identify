# AI Image Classification

## Project Description

This project uses a pre-trained image classification model from Hugging Face to determine if a given image is likely to be AI-generated or human-made. The model is specifically trained on images from Midjourney V6 and SDXL.

## Prerequisites

Before running the code, you need to have a Python environment set up with the following libraries:

* `transformers`
* `torch`
* `Pillow`
* `google.colab.files` (if you are running the code in Google Colab or Jupyter notebooks)

You can install these libraries using `pip`:

```bash
pip install transformers torch Pillow

```
## Usage
This script is designed to be run in an interactive environment like Google Colab or Jupyter, as it uses google.colab.files to handle image uploads.

Run the script: Copy and paste the code into a Google Colab cell and run it.

Upload an image: A file dialog will appear, prompting you to upload an image file. Select the image you want to classify.

View the result: The script will process the image and print the predicted label (ai_gen or human) to the console.
