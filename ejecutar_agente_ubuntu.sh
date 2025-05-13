#!/bin/bash

aws ssm send-command \
  --document-name "AWS-RunShellScript" \
  --targets "Key=instanceIds,Values=i-0993ae6d0e89fdc93" \
  --comment "Instalar y configurar CloudWatch Agent en Ubuntu" \
  --parameters 'commands=[
    "cd /home/ubuntu",
    "rm -f instalar_agente_logs_ubuntu.sh",
    "wget https://raw.githubusercontent.com/lol212/proyectoFinal/develop/scripts/instalar_agente_logs_ubuntu.sh",
    "chmod +x instalar_agente_logs_ubuntu.sh",
    "sudo ./instalar_agente_logs_ubuntu.sh"
  ]' \
  --region us-east-1

