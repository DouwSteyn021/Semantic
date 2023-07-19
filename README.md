# Semantic

This repository contains an example code for computing semantic similarity using the SpaCy library. The code demonstrates how to compare the similarity between words, tokens, and sentences.

# Prerequisites

To run the code, you need to have the following installed on your system:

    Python (version 3.x)
    Docker

# Installation

    Clone this repository to your local machine or download the source code as a ZIP file.
    Navigate to the project directory.

#  Usage

    Open the semantic.py file.
    Modify the code if needed or run it as is.
    Save the changes.
    Open a terminal or command prompt.
    Navigate to the project directory.
    Run the following command to build the Docker image:

docker build -t semantic-similarity .

Once the Docker image is built, run the following command to execute the code:

arduino

    docker run semantic-similarity

    Observe the output in the terminal, which shows the semantic similarity scores between various words, tokens, and sentences.

# Notes

    The requirements.txt file specifies the required dependencies. If you want to install the dependencies manually, refer to        the file for the package versions.
    Make sure to replace <version> in the Dockerfile with the appropriate Python version you have installed on your system.
    Feel free to modify the code and experiment with different inputs to explore semantic similarities further.

