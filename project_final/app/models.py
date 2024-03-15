from datetime import date, datetime
from django.db import models
from PIL import Image
from django.contrib.auth.models import User
from django.utils import timezone


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_image = models.ImageField(upload_to='images_profile', null=True, blank=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15, null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    pass1 = models.CharField(max_length=100, null=True, blank=True)
    
    def __str__(self):
        return self.user.username
    

class Food(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField(default=0)
    unit = models.CharField(max_length=100,default='บาท')
    score = models.FloatField(default=0,blank=True,null=True)
    quantity_review = models.IntegerField(default=0,blank=True,null=True)
    image = models.ImageField(upload_to='media/image/',blank=True,null=True)
    options = models.CharField(max_length=20, choices=(
        ('notchoose', 'ไม่ได้เลือก'),
        ('onsale', 'วางขาย'),
        ('soldout', 'ขายหมดแล้ว'),
    ), default='notchoose')

    def __str__(self) -> str:
        return f'เมนู {self.name} ราคา {self.price} บาท status : {self.options}'
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if self.image:
            img = Image.open(self.image.path)
            if img.height >300 or img.width >300:
                output_size = (300,300)
                img.thumbnail(output_size)
                img.save(self.image.path)
            
        
    
class Historysale(models.Model):
    date_field = models.DateField()
    food = models.ForeignKey(Food,on_delete=models.DO_NOTHING,null=True,blank=True)

    def __str__(self) -> str:
        return f'{self.date_field} {self.food}'
    

class Cart(models.Model):
    cart = models.ForeignKey(UserProfile, on_delete=models.CASCADE)


class Detailcart(models.Model):
    itemImages = models.ImageField(upload_to='media/image/',blank=True,null=True)
    carts = models.ForeignKey(Cart, on_delete=models.CASCADE)
    amount = models.IntegerField()


class Order(models.Model):
    user_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    price = models.IntegerField(default=0)
    name = models.CharField(max_length=100)
    food = models.ForeignKey(Food, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    date_ordered = models.DateTimeField(auto_now_add=True)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50, choices=[('รอดำเนินการ', 'รอดำเนินการ'), ('กำลังดำเนินการ', 'กำลังดำเนินการ'), ('จัดส่งแล้ว', 'จัดส่งแล้ว'), ('จัดส่งเรียบร้อย', 'จัดส่งเรียบร้อย')])


    def __str__(self):
        return f"Order {self.id}: {self.name} ({self.get_status_display()})"
    