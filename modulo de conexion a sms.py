import boto3


client = boto3.client(
	"sns",
	aws_access_key_id="",
	aws_secret_access_key="",
	region_name="us-east-1"
)

def send_sms(phone, msg):
    client.publish(
        PhoneNumber="+51{}".format(phone),
        Message=msg
    )

