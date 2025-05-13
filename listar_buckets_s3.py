import boto3

def listar_buckets_y_objetos():
    s3 = boto3.client('s3')
    respuesta = s3.list_buckets()

    if not respuesta['Buckets']:
        print("No se encontraron buckets")
        return

    for bucket in respuesta['Buckets']:
        nombre = bucket['Name']
        print(f"\nBucket: {nombre}")
        print("-" * 40)

        try:
            objetos = s3.list_objects_v2(Bucket=nombre)
            if 'Contents' in objetos:
                for objeto in objetos['Contents']:
                    print(f"  - {objeto['Key']} ({objeto['Size']} bytes)")
            else:
                print("  (Vacío)")
        except Exception as e:
            print(f"  Error al acceder al bucket: {e}")

if __name__ == "__main__":
    listar_buckets_y_objetos()

