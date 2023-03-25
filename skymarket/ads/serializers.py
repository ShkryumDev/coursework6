from rest_framework import serializers

from skymarket.ads.models import Ad, Comment


class CommentSerializer(serializers.ModelSerializer):
    author_id = serializers.ReadOnlyField(source="author.pk")
    author_first_name = serializers.ReadOnlyField(source="author_first_name")
    author_last_name = serializers.ReadOnlyField(source="author_last_name")
    ad_id = serializers.ReadOnlyField(source="ad.pk")

    class Meta:
        model = Comment
        fields = '__all__'


class AdSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ad
        fields = ['pk', 'image', 'title', 'price', 'description']


class AdDetailSerializer(serializers.ModelSerializer):
    author_first_name = serializers.SerializerMethodField()
    author_last_name = serializers.SerializerMethodField()

    def get_author_first_name(self, ad):
        return ad.author.first_name

    def get_author_last_name(self, ad):
        return ad.author.last_name

    class Meta:
        model = Ad
        fields = '__all__'
