from django.db import models

# CATEGORY
class GalleryCategory(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

# ALBUM
class Album(models.Model):

    category = models.ForeignKey(
        GalleryCategory,
        on_delete=models.CASCADE,
        related_name="albums"
    )

    title = models.CharField(max_length=200)

    cover_image = models.ImageField(
        upload_to='gallery/album_covers/',
        null=True,
        blank=True
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

# ALBUM IMAGES
class AlbumImage(models.Model):

    album = models.ForeignKey(
        Album,
        on_delete=models.CASCADE,
        related_name="images"
    )

    image = models.ImageField(upload_to='gallery/images/')

    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Image {self.id}"