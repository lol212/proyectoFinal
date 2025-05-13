import boto3

def listar_instancias_ec2():
    ec2 = boto3.client('ec2', region_name='us-east-1')
    response = ec2.describe_instances()

    if len(response['Reservations']) == 0:
        print("No hay instancias EC2 activas en esta region")
        return

    for reservation in response['Reservations']:
        for instance in reservation['Instances']:
            print("ID:", instance['InstanceId'])
            print("Estado:", instance['State']['Name'])
            print("Tipo:", instance['InstanceType'])
            print("Zona:", instance['Placement']['AvailabilityZone'])
            print("-" * 40)

if __name__ == "__main__":
    listar_instancias_ec2()

