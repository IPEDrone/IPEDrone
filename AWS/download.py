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

file_name = './design2.jpg' # 다운로드 받을 파일의 상대 경로, 파일이름 그리고 확장자
bucket = 'illegal-parking-enforcement-drone-system' # 우리가 사용하는 버킷의 이름
key = 'image/design.jpg' # 버킷에 저장된 파일의 위치, 파일 이름 그리고 확장자

s3.download_file(bucket, key, file_name)
