from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now

class BlogPost(models.Model):
    postId = models.AutoField(primary_key= True)
    title = models.CharField(max_length=100)
    shortSummary = models.CharField(max_length=100, default="Click below link to read the article.")
    heading1 = models.CharField(max_length=500, default="")
    body1 = models.CharField(max_length=5000, default="")
    heading2 = models.CharField(max_length=500, default="")
    body2 = models.CharField(max_length=5000, default="")
    heading3 = models.CharField(max_length=500, default="")
    body3 = models.CharField(max_length=5000, default="")
    publishDate = models.DateField()
    thumbnail = models.ImageField( default="https://images.unsplash.com/photo-1513342791620-b106dc487c94?ixlib=rb-1.2.1&amp;q=85&amp;fm=jpg&amp;crop=entropy&amp;cs=srgb&amp;h=1000")
    author = models.CharField(max_length=50, default="petzocare")

    def __str__(self):
        return self.title + ' by ' + self.author
    
class BlogComment(models.Model):
    serialNumber= models.AutoField(primary_key=True)
    comment=models.TextField()
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    post=models.ForeignKey(BlogPost, on_delete=models.CASCADE)
    parent=models.ForeignKey('self',on_delete=models.CASCADE, null=True )
    timestamp= models.DateTimeField(default=now)

    def __str__(self):
        return self.comment[0:13] + "..." + "by" + " " + self.user.username