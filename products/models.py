from django.db import models
from django.contrib.auth.models import User
class Product(models.Model):

    titles=models.CharField(max_length=200)
    pub_date=models.DateTimeField()
    body=models.TextField()
    url=models.TextField()
    image=models.ImageField(upload_to='image/')
    icon = models.ImageField(upload_to='image/')
    votes_total= models.IntegerField(default=1)
    hunter=models.ForeignKey(User,on_delete=models.CASCADE) #If user deleted product also deleted

    def __str__(self):
        return self.titles

    def summary(self):
        return self.body[:1000]
    def pub_date_modified(self):
        return self.pub_date.strftime(' %b %e %Y')
