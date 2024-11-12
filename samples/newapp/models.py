from django.db import models

# Create your models here.
class login(models.Model):
    username=models.CharField(max_length=50)
    password=models.CharField(max_length=50)
    usertype=models.CharField(max_length=50)
    class Meta:
        db_table="login"

class category(models.Model):
    cat_name=models.CharField(max_length=50)
    image=models.CharField(max_length=200, default="")
    class Meta:
        db_table="category"

class shops(models.Model):
    gst_in=models.CharField(max_length=50)
    shop_name=models.CharField(max_length=50)
    place=models.CharField(max_length=50)
    post=models.CharField(max_length=50)
    pincode=models.CharField(max_length=50)
    phone=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    image=models.CharField(max_length=100)
    latitude=models.CharField(max_length=100)
    longitude=models.CharField(max_length=100)
    LOGIN_ID=models.ForeignKey(login,on_delete=models.CASCADE)
    category=models.CharField(max_length=50,default="")
    class Meta:
        db_table="shops"

class delivery_boy(models.Model):
    delboy_name=models.CharField(max_length=50)
    house_no_name=models.CharField(max_length=50)
    place = models.CharField(max_length=50)
    post = models.CharField(max_length=50)
    pincode = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    image = models.CharField(max_length=100)
    LOGIN_ID = models.ForeignKey(login, on_delete=models.CASCADE)
    class Meta:
        db_table="delivery_boy"

class product(models.Model):
    product_name=models.CharField(max_length=50)
    product_rate =models.CharField(max_length=50)
    image = models.CharField(max_length=100)
    PRODUCT_CATEGORY = models.ForeignKey(category, on_delete=models.CASCADE)
    SHOP_ID = models.ForeignKey(shops, on_delete=models.CASCADE, default=1)
    class Meta:
        db_table="product"

class buyer(models.Model):
    buyer_name=models.CharField(max_length=50)
    phone=models.CharField(max_length=50)
    email= models.CharField(max_length=50)
    house_no_name= models.CharField(max_length=50)
    place= models.CharField(max_length=50)
    post= models.CharField(max_length=50,default="")
    district= models.CharField(max_length=50,default="")
    pin= models.CharField(max_length=50)
    image= models.CharField(max_length=100)
    LOGIN_ID = models.ForeignKey(login, on_delete=models.CASCADE)
    class Meta:
        db_table="buyer"

class orders(models.Model):
    date=models.CharField(max_length=50)
    amount=models.CharField(max_length=50)
    status=models.CharField(max_length=50)
    BUYER_ID = models.ForeignKey(buyer, on_delete=models.CASCADE)
    SHOP_ID = models.ForeignKey(shops, on_delete=models.CASCADE)
    class Meta:
        db_table="orders"

class order_sub(models.Model):
    quantity=models.CharField(max_length=50)
    ORDER_ID = models.ForeignKey(orders, on_delete=models.CASCADE)
    PRODUCT_ID = models.ForeignKey(product, on_delete=models.CASCADE)
    class Meta:
        db_table="order_sub"

class payment(models.Model):
    amount=models.CharField(max_length=50)
    account_no=models.CharField(max_length=50)
    ORDER_ID = models.ForeignKey(orders, on_delete=models.CASCADE)
    class Meta:
        db_table="payment"

class feedback(models.Model):
    feedback=models.CharField(max_length=50)
    date=models.CharField(max_length=50)
    BUYER_ID = models.ForeignKey(buyer, on_delete=models.CASCADE)
    PRODUCT_ID = models.ForeignKey(product, on_delete=models.CASCADE)
    class Meta:
        db_table="feedback"

class rating(models.Model):
    rating=models.CharField(max_length=50)
    date=models.CharField(max_length=50)
    review=models.CharField(max_length=200,default="")
    USER_ID = models.ForeignKey(buyer, on_delete=models.CASCADE)
    SHOP_ID = models.ForeignKey(shops, on_delete=models.CASCADE)
    class Meta:
        db_table="rating"

class cart(models.Model):
    quantity=models.CharField(max_length=50)
    PRODUCT_ID = models.ForeignKey(product, on_delete=models.CASCADE)
    BUYER_ID = models.ForeignKey(buyer, on_delete=models.CASCADE)
    class Meta:
        db_table="cart"

class location(models.Model):
    date=models.CharField(max_length=50)
    time=models.CharField(max_length=50)
    latitude=models.CharField(max_length=50)
    longitude=models.CharField(max_length=50)
    DELIVERY_ID = models.ForeignKey(delivery_boy, on_delete=models.CASCADE)
    class Meta:
        db_table="location"

class order_assign(models.Model):
    ORDER_ID=models.ForeignKey(orders,on_delete=models.CASCADE)
    DELBOY_ID=models.ForeignKey(delivery_boy,on_delete=models.CASCADE)
    status=models.CharField(max_length=50)
    date=models.CharField(max_length=50)

    class Meta:
        db_table = "order_assign"

class bank(models.Model):
    bank_name=models.CharField(max_length=50)
    account_no=models.CharField(max_length=50)
    pin_no=models.CharField(max_length=50)
    balance=models.CharField(max_length=50)

    class Meta:
        db_table = "bank"

class offer(models.Model):
    quantity_1=models.CharField(max_length=50)
    quantity_2=models.CharField(max_length=50)
    discount=models.CharField(max_length=50)
    PRODUCT_ID=models.ForeignKey(product,on_delete=models.CASCADE)

    class Meta:
        db_table = "offer"
