#!/bin/bash
echo "--- Setting up Environment ---"
sudo dnf update -y
sudo dnf install -y docker git python3-pip
sudo service docker start
sudo usermod -a -G docker ec2-user
pip3 install -r requirements.txt

# Aliases toevoegen voor 'binary feel'
echo "" >> ~/.bashrc
echo "alias k-topics='docker compose exec kafka kafka-topics --bootstrap-server kafka:9092'" >> ~/.bashrc
echo "alias k-console-producer='docker compose exec kafka kafka-console-producer --bootstrap-server kafka:9092'" >> ~/.bashrc
echo "alias k-console-consumer='docker compose exec kafka kafka-console-consumer --bootstrap-server kafka:9092'" >> ~/.bashrc
echo "alias dc='docker compose'" >> ~/.bashrc

echo "--- Setup Complete! Close this terminal and open a new one. ---"