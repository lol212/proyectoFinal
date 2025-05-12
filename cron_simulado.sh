while true
do
  echo "Ejecutando limpieza de logs..."
  bash limpiar_logs.sh
  echo "Esperando 24 horas..."
  sleep 86400  # 86400 segundos = 24 horas
done
