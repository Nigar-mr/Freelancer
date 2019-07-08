from django.db import models
# Create your models here.

class MenuModel(models.Model):
    num = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=20)
    url = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.name}"



class PortfolioModel(models.Model):
    caption = models.CharField(max_length=100, null=True, blank=True)
    images = models.ImageField(upload_to='media/')
    text = models.TextField(blank=True, null=True)


class AboutModel(models.Model):
    left_text = models.CharField(max_length=255,null=True, blank=True)
    right_text = models.CharField(max_length=255,null=True, blank=True)



class ContactFormModel(models.Model):
    name = models.CharField(max_length=20,blank=True, null=True)  # name
    phone = models.CharField(max_length=20,blank=True, null=True)  # phone
    email = models.EmailField(blank=True, null=True)
    message = models.TextField(blank=True, null=True)

    create_date = models.DateTimeField(auto_now_add=True, null=True, blank= True)

class InfoModel(models.Model):
    title = models.CharField(max_length=20)
    text = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.title}"

class IconModel(models.Model):
    icon = models.CharField(max_length=30)
    link = models.URLField()
    section = models.ForeignKey("InfoModel", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.icon}"


class UniqeModel(models.Model):
    pagename = models.CharField(max_length=50, blank=True, null=True)
    menu_bg = models.CharField(max_length=50, blank=True, null=True)
    header_bg = models.CharField(max_length=50, blank=True, null=True)
    header_avatar = models.ImageField(upload_to='media/')
    header_title = models.CharField(max_length=200)
    header_subtitle = models.CharField(max_length=200)
    portfolio_name = models.CharField(max_length=50)
    about_name = models.CharField(max_length=20, null=True, blank=True)
    about_btn_link = models.CharField(max_length=500, null=True, blank=True)    #https://startbootstrap.com/themes/freelancer/
    about_btn = models.CharField(max_length=20, null=True, blank=True)
    about_bg = models.CharField(max_length=50,null=True, blank=True)
    contact_name = models.CharField(max_length=20,blank=True, null=True)
    contact_btn = models.CharField(max_length=10, blank=True, null=True)
    contact_btn_color = models.CharField(max_length=50, null=True, blank=True)
    footer_bg = models.TextField(blank=True, null=True)
    copyright = models.CharField(max_length=50)
