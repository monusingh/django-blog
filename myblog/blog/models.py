from django.db import models
 
class Author(models.Model):
    name = models.CharField(max_length=64)
    email = models.CharField(max_length=64)
 
    def __str__(self):
        return "%s (%s)" % (self.name, self.email)
 
class Post(models.Model):
    title = models.CharField(max_length=64)
    date = models.DateTimeField()
    author = models.ForeignKey(Author)
    body = models.TextField()
 
    def __str__(self):
        return "%s (%s)" % (self.title, self.author.name)

class Comment(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    author = models.CharField(max_length=60)
    body = models.TextField()
    post = models.ForeignKey(Post)

    def __str__(self):
        return unicode("%s: %s" % (self.post, self.body[:60]))





