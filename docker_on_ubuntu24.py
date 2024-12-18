# installing docker on ubuntu 22.04

# update software repository
sudo apt-get update

# install docker  
sudo apt-get install -y docker-ce docker-ce-cli containerd.io 
# OR
sudo apt install -y docker.io

# enable and start the docker service
sudo systemctl enable docker --now

# check docker version
docker --version

# to execute the docker command without sudo, add the current user to the docker group
sudo usermod -aG $USER

# to verify if the current user was added to the docker group run
getent group docker

# refresh the group permissions to use the updated one
newgrp docker

# restart docker service 
systemctl restart docker
