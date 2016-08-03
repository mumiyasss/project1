from django.db import models
from django.utils import timezone


class Post(models.Model):
    # Main part
    author = models.ForeignKey('auth.User')
    title  = models.CharField(max_length=200)
    text   = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)
    comment_block = []

    def get_post_title(self):
        return self.title;

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def delete_post(self):
        self.delete()

    def __str__(self):
        return self.title

    # Comments for the post
    class Comments(models.Model):
        author = models.ForeignKey('auth.User')
        text = models.TextField()
        created_date = models.DateTimeField(default=timezone.now)
        published_date = models.DateTimeField(blank=True, null=True)

        def set_author(self, commentAuthor):
            self.author = commentAuthor

        def set_comment_text(self, commentText):
            self.text = commentText;

    def add_new_comment_to_block(self, text, author):
        newComment = self.Comments()
        newComment.set_author(author)
        newComment.set_comment_text(text)

        self.comment_block.append(newComment)