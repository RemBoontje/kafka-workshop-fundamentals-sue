#!/bin/bash

echo "--- Workshop Setup Start ---"

# 1. Zorg dat alles up to date is
sudo dnf update -y

# 2. Installeer Docker en de Compose Plugin (voor Amazon Linux 2023)
sudo dnf install -y docker docker-compose-plugin

# 3. Start Docker service
sudo service docker start

# 4. Voeg de huidige user (ec2-user) toe aan de docker group
# Dit voorkomt dat je 'sudo' voor elk docker commando moet zetten
sudo usermod -a -G docker ec2-user

echo "--------------------------------------------------------"
echo "INSTALLATIE VOLTOOID!"
echo "--------------------------------------------------------"
echo "BELANGRIJK: Sluit deze terminal nu en open een nieuwe."
echo "(Dit is nodig om de nieuwe groepsrechten te activeren)"