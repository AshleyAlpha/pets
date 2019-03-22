from django.shortcuts import render
from django.http  import HttpResponse

# Create your views here.

class Image(models.Model):
    image = models.ImageField(upload_to='media/Images/')
    name = models.CharField(max_length=30)
    caption = models.TextField()
    profile = models.ForeignKey(Profile)
    likes = models.DateTimeField(auto_now_add=True)
    comments = models.TextField()

    class Meta:
        ordering = ('-id',)

    def save_image(self):
        self.save()
    
    def delete_image(self):
        self.delete()
    
    def __str__(self):
        return self.name

    @classmethod
    def search_image(cls,search_category):
        images_category = Image.objects.filter(category__photo_category__icontains=search_category)
        return images_category
    
