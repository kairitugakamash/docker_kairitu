# Install Docker: If you haven't already, download and install Docker from the official website.

sudo apt-get update
sudo apt-get install docker-ce docker-ce-cli containerd.io

# Pull OLLAMA Docker Image: Open your terminal and run the following command to pull the OLLAMA image.

docker pull ollama/ollama

# Run OLLAMA: To run OLLAMA, execute the following command in your terminal.

docker run -it ollama/ollama

