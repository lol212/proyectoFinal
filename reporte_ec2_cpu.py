import boto3
from datetime import datetime, timedelta

def obtener_uso_cpu(instancia_id, region="us-east-1"):
    cloudwatch = boto3.client('cloudwatch', region_name=region)

    fin = datetime.utcnow()
    inicio = fin - timedelta(minutes=60)

    respuesta = cloudwatch.get_metric_statistics(
        Namespace='AWS/EC2',
        MetricName='CPUUtilization',
        Dimensions=[{'Name': 'InstanceId', 'Value': instancia_id}],
        StartTime=inicio,
        EndTime=fin,
        Period=300,
        Statistics=['Average']
    )

    puntos = respuesta['Datapoints']
    if puntos:
        promedio = round(puntos[-1]['Average'], 2)
        print(f"Instancia: {instancia_id} - Uso promedio de CPU: {promedio}%")
    else:
        print(f"Instancia: {instancia_id} - Sin datos de CPU disponibles")

def obtener_instancias():
    ec2 = boto3.client('ec2', region_name='us-east-1')
    respuesta = ec2.describe_instances()

    instancias = []
    for reserva in respuesta['Reservations']:
        for instancia in reserva['Instances']:
            instancias.append(instancia['InstanceId'])

    return instancias

if __name__ == "__main__":
    instancias = obtener_instancias()
    if not instancias:
        print("No hay instancias EC2 activas")
    else:
        for id in instancias:
            obtener_uso_cpu(id)

