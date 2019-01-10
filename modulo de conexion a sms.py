import boto3


client = boto3.client(
	"sns",
	aws_access_key_id="AKIAI6SAHCKJXU6FFZ7A",
	aws_secret_access_key="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",
	region_name="us-east-1"
)

def send_sms(phone, msg):
    client.publish(
        PhoneNumber="+51{}".format(phone),
        Message=msg
    )

