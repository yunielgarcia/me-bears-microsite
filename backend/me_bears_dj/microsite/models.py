from django.db import models


class Page(models.Model):
    name = models.CharField(max_length=250, null=False, blank=False)
    slug = models.SlugField(max_length=250, null=False, blank=False)

    def __str__(self):
        return self.name


class Section(models.Model):
    name = models.CharField(max_length=250)
    page = models.ForeignKey(Page, related_name='sections',
                             null=False, blank=False)

    def __str__(self):
        return '{}-section'.format(self.name)


class Content(models.Model):
    IMAGE_CONTENT = 'image'
    VIDEO_CONTENT = 'video'

    CONTENT_TYPE_CHOICES = (
        (IMAGE_CONTENT, 'Image'),
        (VIDEO_CONTENT, 'Video'),
    )

    type = models.CharField('Content type',
                            choices=CONTENT_TYPE_CHOICES,
                            max_length=20,
                            null=False,
                            blank=False)
    display_url = models.ImageField('display image',
                                    max_length=255,)
    section = models.ForeignKey(Section,
                                related_name='contents',
                                null=True,
                                blank=False)
    description = models.TextField('description', null=True, blank=True)
    name = models.CharField('name', max_length=120, null=True, blank=True)
    order = models.PositiveIntegerField('order', null=True, blank=True)

    def __str__(self):
        return '{}-content'.format(self.name)

