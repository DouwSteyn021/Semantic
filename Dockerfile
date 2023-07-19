# Use a base image with Python pre-installed
FROM python:3.11

# Set the working directory in the container
WORKDIR /app

# Copy the requirements.txt file to the container
COPY requirements.txt .

# Install the required dependencies
RUN pip install -r requirements.txt

# Copy the rest of the project files to the container
COPY . .

# Run the semantic.py script
CMD [ "python", "semantic.py" ]
