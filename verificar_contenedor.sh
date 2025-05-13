#!/bin/bash

INSTANCE_ID="i-03677feb081d68f80"

echo "Verificando contenedores activos en la instancia EC2..."

aws ssm send-command \
  --document-name "AWS-RunShellScript" \
  --targets "Key=instanceIds,Values=$INSTANCE_ID" \
  --comment "Listar contenedores Docker en ejecución" \
  --parameters '{
    "commands": [
      "docker ps"
    ]
  }' \
  --region us-east-1

