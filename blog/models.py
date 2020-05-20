from django.db import models


class Blog(models.Model):
    title = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now_add=True)
    description = models.TextField()
    main_image = models.ImageField(upload_to='blog/main_images/')
    image1 = models.ImageField(upload_to='blog/optional_images', blank=True)
    image2 = models.ImageField(upload_to='blog/optional_images', blank=True)
    image3 = models.ImageField(upload_to='blog/optional_images', blank=True)
    image4 = models.ImageField(upload_to='blog/optional_images', blank=True)
    url = models.URLField(blank=True)

    def __str__(self):
        return self.title
