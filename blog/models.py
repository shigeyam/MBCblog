from django.db import models

class Category(models.Model):
    category = models.CharField(max_length=100)

    def __str__(self):
        return self.category


class PostQuerySet(models.QuerySet):

    def logical_thinking(self):
        return self.filter(category=1)

    def mba_class(self):
        return self.filter(category=2)

    def excel_class(self):
        return self.filter(category=3)


class Post(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField()
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    intro = models.TextField()
    body = models.TextField()
    posted_date = models.DateTimeField(auto_now_add=True)

    objects = PostQuerySet.as_manager()

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(Post, related_name="comments", on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    body = models.TextField()
    posted_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name 
    

class ImageUpload(models.Model):
    title = models.CharField(max_length=255, unique=True)
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title 


class Meeting(models.Model):
    name = models.CharField(verbose_name='お名前', max_length=255)
    email = models.EmailField(verbose_name='Email')
    contents = models.TextField(verbose_name='内容')
    posted_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name 
