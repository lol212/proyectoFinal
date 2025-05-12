echo "Instalando recursos..."
sudo yum update -y
sudo yum install git vim python3 docker -y
sudo service docker start
echo "Instalacion completada"
