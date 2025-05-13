import boto3
from datetime import datetime, timedelta

def obtener_metricas(instancia_id, region="us-east-1"):
    cloudwatch = boto3.client('cloudwatch', region_name=region)
    fin = datetime.utcnow()
    inicio = fin - timedelta(minutes=60)

    metricas = ["NetworkIn", "NetworkOut", "DiskReadBytes", "DiskWriteBytes"]

    for metrica in metricas:
        respuesta = cloudwatch.get_metric_statistics(
            Namespace='AWS/EC2',
            MetricName=metrica,
            Dimensions=[{'Name': 'InstanceId', 'Value': instancia_id}],
            StartTime=inicio,
            EndTime=fin,
            Period=300,
            Statistics=['Average']
        )

        puntos = respuesta['Datapoints']
        if puntos:
            promedio = round(puntos[-1]['Average'], 2)
            print(f"{metrica} promedio: {promedio}")
        else:
            print(f"{metrica}: No hay datos disponibles")

    print("-" * 50)

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
        print("No hay instancias EC2 activas.")
    else:
        for id in instancias:
            print(f"Métricas para la instancia: {id}")
            obtener_metricas(id)

