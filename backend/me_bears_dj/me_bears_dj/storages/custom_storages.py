from django.conf import settings
from storages.backends.s3boto3 import S3Boto3Storage


class MediaStorage(S3Boto3Storage):
    """Uploads to 'mybucket/media/'."""

    def path(self, name):
        pass

    location = settings.MEDIAFILES_LOCATION
    file_overwrite = False
