from django.db import models

# Create your models here.


class Tags(models.Model):
    tags_name = models.CharField(max_length=255)
    
    class Meta:
        db_table = "Tags"

    def __str__(self):
        return self.tags_name

class Category(models.Model):
    category = models.CharField(max_length=255)
    
    class Meta:
        db_table = "Category"

    def __str__(self):
        return self.category

class Blog(models.Model):
    BLOG_TYPES = (
        (u"tech", u'tech'),
        (u"health", u'health'),
        (u"social", u'social'),
    )

    title = models.CharField(max_length=50)
    category = models.CharField(choices=BLOG_TYPES,max_length=120)
    category = models.ForeignKey(Category,on_delete=models.DO_NOTHING,related_name="Category")
    tags = models.ManyToManyField(Tags,blank=True)
    content = models.TextField()
