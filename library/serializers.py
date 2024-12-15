from rest_framework import serializers
from .models import Author, Book

class BookSerializer(serializers.ModelSerializer):
    author_id = serializers.PrimaryKeyRelatedField(
        queryset=Author.objects.all(),
        source='author',
        write_only=True
    )
    author = serializers.StringRelatedField(read_only=True)
    url = serializers.HyperlinkedIdentityField(
        view_name='book-detail',
        lookup_field='pk'
    )

    class Meta:
        model = Book
        fields = [
            'id', 'title', 'author', 'author_id', 'publication_year',
            'genre', 'category', 'publisher', 'cover_image', 'file', 'is_textbook', 'url'
        ]

    def validate(self, data):
        title = data.get('title')
        author = data.get('author')
        publication_year = data.get('publication_year')
        publisher = data.get('publisher')

        if Book.objects.filter(title=title, author=author,
                               publication_year=publication_year, publisher=publisher).exists():
            raise serializers.ValidationError("Книга с таким названием, автором, годом выпуска и издательством уже существует.")

        return data


class AuthorSerializer(serializers.ModelSerializer):
    books = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = ['id', 'name', 'biography', 'books']
