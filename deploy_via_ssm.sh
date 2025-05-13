#!/bin/bash

INSTANCE_ID="i-03677feb081d68f80"

echo "Instancia EC2 válida para SSM: $INSTANCE_ID"
echo "Desplegando desde la rama develop..."

aws ssm send-command \
  --document-name "AWS-RunShellScript" \
  --targets "Key=instanceIds,Values=$INSTANCE_ID" \
  --comment "Clonar develop y desplegar contenedor" \
  --parameters '{
    "commands": [
      "sudo yum update -y",
      "sudo yum install -y git docker",
      "sudo service docker start",
      "sudo usermod -aG docker ec2-user",
      "cd /home/ec2-user",
      "rm -rf proyectoFinal",
      "git clone --single-branch --branch develop https://github.com/lol212/proyectoFinal.git",
      "if [ -d proyectoFinal/app_web ]; then cd proyectoFinal/app_web; docker build -t app-web-devops .; docker run -d -p 8080:80 --name contenedor-web app-web-devops; else echo Carpeta app_web no encontrada; exit 1; fi"
    ]
  }' \
  --region us-east-1

