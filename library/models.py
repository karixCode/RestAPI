from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Author(models.Model):
    name = models.CharField(max_length=100, unique=True)
    biography = models.TextField(blank=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')
    publication_year = models.PositiveIntegerField(
        validators=[
            MinValueValidator(1000),
            MaxValueValidator(9999)
        ]
    )
    genre = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    publisher = models.CharField(max_length=100)
    cover_image = models.ImageField(upload_to='covers/', blank=True, null=True)
    file = models.FileField(upload_to='books/', blank=True, null=True)
    is_textbook = models.BooleanField(default=False)

    class Meta:
        unique_together = ('title', 'author', 'publication_year', 'publisher')

    def __str__(self):
        return f"{self.title} by {self.author.name} ({self.publication_year})"
