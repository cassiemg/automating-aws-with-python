import boto3
import click

session = boto3.Session(profile_name='pythonAutomation')
s3 = session.resource('s3')

@click.group()
def cli():
    "Webotron Deploy websites to AWS"
    pass

@cli.command('list-bucket-objects')
def list_bucket_objects():
    "List objects ins3 bucket"
    for obj in s3.Bucket('elasticbeanstalk-us-east-2-361753644252').objects.all():
        print (obj)

@cli.command('list-buckets')
def list_buckets():
    "List all s3 buckets"
    for bucket in s3.buckets.all():
        print(bucket.name)

if __name__ == '__main__':
    cli()
