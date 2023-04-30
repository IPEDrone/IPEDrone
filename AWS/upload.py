from dotenv import load_dotenv
import boto3
import os

load_dotenv()

s3 = boto3.client(
    service_name="s3",
    region_name="ap-northeast-2",
    aws_access_key_id=os.environ.get('AWS_ACCESS_KEY_ID'),
    aws_secret_access_key=os.environ.get('AWS_SECRET_ACCESS_KEY')
)

file_name = './design.jpg' # 업로드 할 파일의 상대 경로, 파일 이름 그리고 확장자
bucket = 'illegal-parking-enforcement-drone-system' # 우리가 사용하는 버킷의 이름
key = 'image/design.jpg' # 버킷에 올라갈 장소 : image 폴더 내에 design.jpg가 생성됨

s3.upload_file(file_name, bucket, key)