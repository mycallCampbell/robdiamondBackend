from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields import AutoField

# Create your models here.


class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    category = models.CharField(max_length=200, null=True, blank=True)
    title = models.CharField(max_length=200, null=True, blank=True)
    strap = models.CharField(max_length=200, null=True, blank=True)
    dial = models.CharField(max_length=200, null=True, blank=True)
    model = models.CharField(max_length=200, null=True, blank=True)
    ref = models.CharField(max_length=200, null=True, blank=True)
    price1 = models.IntegerField(null=True, blank=True, default=0)
    year1 = models.CharField(max_length=200, null=True, blank=True)
    price2 = models.IntegerField(null=True, blank=True, default=0)
    year2 = models.CharField(max_length=200, null=True, blank=True)
    price3 = models.IntegerField(null=True, blank=True, default=0)
    year3 = models.CharField(max_length=200, null=True, blank=True)
    boxAndPapers = models.CharField(max_length=200, null=True, blank=True)
    condition = models.CharField(max_length=200, null=True, blank=True)
    warranty = models.CharField(max_length=200, null=True, blank=True)
    availble = models.CharField(max_length=200, null=True, blank=True)
    movement = models.CharField(max_length=200, null=True, blank=True)
    caliber = models.CharField(max_length=200, null=True, blank=True)
    caseMaterial = models.CharField(max_length=200, null=True, blank=True)
    braceletMaterial = models.CharField(max_length=200, null=True, blank=True)
    bezel = models.CharField(max_length=200, null=True, blank=True)
    powerReserve = models.CharField(max_length=200, null=True, blank=True)
    fullyStickered = models.CharField(max_length=200, null=True, blank=True)
    waterResistant = models.CharField(max_length=200, null=True, blank=True)
    gender = models.CharField(max_length=200, null=True, blank=True)
    imageAmount = models.CharField(max_length=200, null=True, blank=True)
    videoAmount = models.CharField(max_length=200, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    description1 = models.TextField(null=True, blank=True)
    descriptionSmall = models.TextField(null=True, blank=True)
    rating = models.DecimalField(
        max_digits=7, decimal_places=2, null=True, blank=True)
    numReviews = models.IntegerField(null=True, blank=True, default=0)
    createAt = models.DateTimeField(auto_now_add=True)
    _id = models.AutoField(primary_key=True, editable=False)

    def __str__(self):
        return str(self.title)


class Blog(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    imageRef1 = models.CharField(max_length=200, null=True, blank=True)
    imageRef2 = models.CharField(max_length=200, null=True, blank=True)
    imageRef3 = models.CharField(max_length=200, null=True, blank=True)
    imageRef4 = models.CharField(max_length=200, null=True, blank=True)
    imageRef5 = models.CharField(max_length=200, null=True, blank=True)
    imageRef6 = models.CharField(max_length=200, null=True, blank=True)
    imageRef7 = models.CharField(max_length=200, null=True, blank=True)
    minuteRead = models.IntegerField(null=True, blank=True, default=0)
    title = models.CharField(max_length=200, null=True, blank=True)
    subTitle1 = models.CharField(max_length=200, null=True, blank=True)
    subTitle2 = models.CharField(max_length=200, null=True, blank=True)
    subTitle3 = models.CharField(max_length=200, null=True, blank=True)
    subTitle4 = models.CharField(max_length=200, null=True, blank=True)
    subTitle5 = models.CharField(max_length=200, null=True, blank=True)
    subTitle6 = models.CharField(max_length=200, null=True, blank=True)
    subTitle7 = models.CharField(max_length=200, null=True, blank=True)
    subTitle8 = models.CharField(max_length=200, null=True, blank=True)
    subTitle9 = models.CharField(max_length=200, null=True, blank=True)
    caption1 = models.CharField(max_length=200, null=True, blank=True)
    caption2 = models.CharField(max_length=200, null=True, blank=True)
    captchaPhrase = models.TextField(null=True, blank=True)
    callToAction1 = models.TextField(null=True, blank=True)
    callToAction2 = models.TextField(null=True, blank=True)
    callToAction3 = models.TextField(null=True, blank=True)
    description1 = models.TextField(null=True, blank=True)
    description2 = models.TextField(null=True, blank=True)
    description3 = models.TextField(null=True, blank=True)
    description4 = models.TextField(null=True, blank=True)
    description5 = models.TextField(null=True, blank=True)
    description6 = models.TextField(null=True, blank=True)
    description7 = models.TextField(null=True, blank=True)
    description8 = models.TextField(null=True, blank=True)
    description9 = models.TextField(null=True, blank=True)
    description10 = models.TextField(null=True, blank=True)
    description11 = models.TextField(null=True, blank=True)
    category = models.CharField(max_length=200, null=True, blank=True)
    createAt = models.DateTimeField(auto_now_add=True)
    _id = AutoField(primary_key=True, editable=False)

    def __str__(self):
        return self.title


class Review(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=200, null=True, blank=True)
    rating = models.IntegerField(null=True, blank=True, default=0)
    comment = models.TextField(null=True, blank=True)
    _id = AutoField(primary_key=True, editable=False)

    def __str__(self):
        return str(self.rating)


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    paymentMethod = models.CharField(max_length=200, null=True, blank=True)
    taxPrice = models.DecimalField(
        max_digits=7, decimal_places=2, null=True, blank=True
    )
    shippingPrice = models.DecimalField(
        max_digits=7, decimal_places=2, null=True, blank=True
    )
    totalPrice = models.DecimalField(
        max_digits=7, decimal_places=2, null=True, blank=True
    )
    isPaid = models.BooleanField(default=False)
    paidAt = models.DateTimeField(auto_now_add=False, null=True, blank=True)
    isDelivered = models.BooleanField(default=False)
    deliveredAt = models.DateTimeField(
        auto_now_add=False, null=True, blank=True)
    createdAt = models.DateTimeField(auto_now_add=True)
    _id = AutoField(primary_key=True, editable=False)

    def __str__(self):
        return str(self.createdAt)


class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=200, null=True, blank=True)
    qty = models.IntegerField(null=True, blank=True, default=0)
    price = models.DecimalField(
        max_digits=7, decimal_places=2, null=True, blank=True)
    image = models.CharField(max_length=200, null=True, blank=True)
    size = models.CharField(max_length=100, default='M')
    halfSize = models.BooleanField(default=False)
    _id = AutoField(primary_key=True, editable=False)

    def __str__(self):
        return str(self.name)


class ShippingAddress(models.Model):
    order = models.OneToOneField(
        Order, on_delete=models.CASCADE, null=True, blank=True)
    addressLine1 = models.CharField(max_length=200, null=True, blank=True)
    addressLine2 = models.CharField(max_length=200, null=True, blank=True)
    city = models.CharField(max_length=200, null=True, blank=True)
    postcode = models.CharField(max_length=200, null=True, blank=True)
    country = models.CharField(max_length=200, null=True, blank=True)
    shippingPrice = models.DecimalField(
        max_digits=7, decimal_places=2, null=True, blank=True
    )
    phone = models.CharField(max_length=200, null=True, blank=True)
    _id = AutoField(primary_key=True, editable=False)

    def __str__(self):
        return str(self.addressLine1)


class SubscriberList(models.Model):
    email = models.CharField(max_length=200, null=True, blank=True)
    name = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return str(self.email)
