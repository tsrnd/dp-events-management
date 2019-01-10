from rest_framework import serializers
from .models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES, Post


class SnippetSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(
        required=False, allow_blank=True, max_length=100)
    code = serializers.CharField(style={'base_template': 'textarea.html'})
    linenos = serializers.BooleanField(required=False)
    language = serializers.ChoiceField(
        choices=LANGUAGE_CHOICES, default='python')
    style = serializers.ChoiceField(choices=STYLE_CHOICES, default='friendly')

    # If it link to other table (Many-to-One).
    # fk_Snippet_Post = serializers.PrimaryKeyRelatedField(
    #    queryset=Post.objects.all(), many=True)

    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        return Snippet.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        instance.title = validated_data.get('title', instance.title)
        instance.code = validated_data.get('code', instance.code)
        instance.linenos = validated_data.get('linenos', instance.linenos)
        instance.language = validated_data.get('language', instance.language)
        instance.style = validated_data.get('style', instance.style)
        instance.save()
        return instance

    class Meta:
        model = Snippet
        fields = ('id', 'title', 'code', 'linenos', 'language', 'style')


# you're not serializing a model and since you want to display that count I guess, I'd suggest changing the serializer to this.
class CustomeSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(
        required=False, allow_blank=True, max_length=100)

    class Meta:
        fields = ('id', 'title')


class JoinColumnSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(
        required=False, allow_blank=True, max_length=100)
    content = serializers.CharField(required=False, allow_blank=True)

    class Meta:
        fields = ('id', 'title', 'content')


class PostSerializer(serializers.Serializer):

    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(
        required=False, allow_blank=True, max_length=200)
    content = serializers.CharField(required=False, allow_blank=True)
    # field name FK with other table.
    snipid = serializers.PrimaryKeyRelatedField(queryset=Snippet.objects.all())

    class Meta:
        model = Post
        fields = ('id', 'title', 'content', 'snipid')