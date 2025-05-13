#!/bin/bash

INSTANCIA_ID="i-0993ae6d0e89fdc93"

aws ssm send-command \
  --document-name "AWS-RunShellScript" \
  --targets "Key=instanceIds,Values=$INSTANCIA_ID" \
  --comment "Descargar y ejecutar script desde GitHub" \
  --parameters 'commands=["cd /home/ec2-user", "rm -f instalar_agente_logs.sh", "wget https://raw.githubusercontent.com/lol212/proyectoFinal/develop/instalar_agente_logs.sh", "chmod +x instalar_agente_logs.sh", "./instalar_agente_logs.sh"]' \
  --region us-east-1

