from datetime import datetime, timedelta
import boto3

ec2 = boto3.client('ec2')
s3 = boto3.client('s3')
cloudwatch = boto3.client('cloudwatch')

print(" Listado de instancias EC2:")
response = ec2.describe_instances()
for reservation in response['Reservations']:
    for instance in reservation['Instances']:
        print(f"- ID: {instance['InstanceId']}, Estado: {instance['State']['Name']}, Tipo: {instance['InstanceType']}, Zona: {instance['Placement']['AvailabilityZone']}")

print("\n Buckets en S3:")
buckets = s3.list_buckets()
for bucket in buckets['Buckets']:
    print(f"- {bucket['Name']}")
    try:
        objects = s3.list_objects_v2(Bucket=bucket['Name'])
        for obj in objects.get('Contents', []):
            print(f"   - {obj['Key']}")
    except Exception as e:
        print("   (sin acceso o vacío)")

print("\n Uso de CPU de instancias EC2 (última hora):")
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
            print(f"- {instance['InstanceId']}: {avg:.2f}% CPU")
        else:
            print(f"- {instance['InstanceId']}: No data")

