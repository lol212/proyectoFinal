import boto3
from datetime import datetime, timedelta

ec2 = boto3.client('ec2')
s3 = boto3.client('s3')
cloudwatch = boto3.client('cloudwatch')

with open("reporte_aws.txt", "w") as file:
    file.write("Listado de instancias EC2:\n")
    response = ec2.describe_instances()
    for reservation in response['Reservations']:
        for instance in reservation['Instances']:
            file.write(f"- ID: {instance['InstanceId']}, Estado: {instance['State']['Name']}, Tipo: {instance['InstanceType']}, Zona: {instance['Placement']['AvailabilityZone']}\n")

    file.write("\nBuckets en S3:\n")
    buckets = s3.list_buckets()
    for bucket in buckets['Buckets']:
        file.write(f"- {bucket['Name']}\n")
        try:
            objects = s3.list_objects_v2(Bucket=bucket['Name'])
            for obj in objects.get('Contents', []):
                file.write(f"   - {obj['Key']}\n")
        except Exception as e:
            file.write("   (sin acceso o vacío)\n")

    file.write("\nUso de CPU de instancias EC2 (última hora):\n")
    for reservation in response['Reservations']:
        for instance in reservation['Instances']:
            metrics = cloudwatch.get_metric_statistics(
                Namespace='AWS/EC2',
                MetricName='CPUUtilization',
                Dimensions=[{'Name': 'InstanceId', 'Value': instance['InstanceId']}],
                StartTime=datetime.utcnow() - timedelta(hours=1),
                EndTime=datetime.utcnow(),
                Period=300,
                Statistics=['Average']
            )
            datapoints = metrics['Datapoints']
            if datapoints:
                avg = datapoints[-1]['Average']
                file.write(f"- {instance['InstanceId']}: {avg:.2f}% CPU\n")
            else:
                file.write(f"- {instance['InstanceId']}: No data\n")

