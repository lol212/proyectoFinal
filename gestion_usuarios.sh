read -p "Nombre del nuevo usuario: " usuario

sudo useradd $usuario
sudo passwd $usuario
sudo usermod -aG docker $usuario

echo "Usuario $usuario creado y agregado al grupo docker"
