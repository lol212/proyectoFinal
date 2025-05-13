#!/bin/bash
echo " Simulación de ejecución del pipeline CI/CD"
echo " Paso 1: Construcción de imagen Docker"
docker build -t app-web-devops ./app_web

echo " Imagen construida correctamente"

