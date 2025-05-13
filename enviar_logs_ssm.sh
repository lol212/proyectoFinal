#!/bin/bash

INSTANCIA_ID="i-0993ae6d0e89fdc93"

aws ssm send-command \
  --document-name "AWS-RunShellScript" \
  --targets "Key=instanceIds,Values=$INSTANCIA_ID" \
  --comment "Instalar agente y configurar logs" \
  --parameters commands=["$(< instalar_agente_logs.sh)"] \
  --region us-east-1

