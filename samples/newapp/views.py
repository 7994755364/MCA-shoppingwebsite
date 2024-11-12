import base64
import datetime
import random
import time

from django.core.files.storage import FileSystemStorage
from django.db.models import Q
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from geopy.distance import geodesic

from .models import shops, login, category, delivery_boy, rating, product, orders, order_sub, order_assign, payment, \
    buyer, cart, feedback, bank, location,offer

media_path="E:\\New folder\\sample\\samples\\media\\"


def login_load(request):
    return render(request,"Login.html")
def login_post(request):
    username=request.POST['textfield']
    password=request.POST['textfield2']

    log_obj=login.objects.filter(username=username ,password=password)
    if log_obj.exists():
        log_obj=log_obj[0]
        type=log_obj.usertype
        print(type)
        if type=="admin":

            request.session['lg']="yes"
            if request.session['lg'] == "yes":
                return admin_home_load(request)
            else:
                return render(request, "login.html")

        elif type=="shop":
            request.session["logout"] = "0"
            request.session['lg'] = "yes"
            if request.session['lg'] == "yes":
                shop_obj=shops.objects.filter(LOGIN_ID=log_obj)
                if shop_obj.exists():
                    shop_obj=shop_obj[0]
                    request.session['shop_id']=shop_obj.id
                    return seller_home_load(request)
                else:
                    return HttpResponse("Not Exist")
            else:
                return render(request, "login.html")
        else:
            return HttpResponse("invalid user")
    else:
       return HttpResponse("invalid details")

def logout(request):
    request.session['lg'] = "no"
    return render(request,"login.html")

def forgot_password_load(request):
    return render(request,"forget_password.html")

def forgot_password_post(request):
    email=request.POST['textfield']
    log_obj=login.objects.filter(username=email)
    if log_obj.exists():
        log_obj=log_obj[0]
        import smtplib
        s = smtplib.SMTP(host='smtp.gmail.com', port=587)
        s.starttls()
        s.login("shopping.app.2k21@gmail.com", "7994755364")
        msg = MIMEMultipart()  # create a message...... ...."
        msg['From'] = "shopping.app.2k21@gmail.com"
        msg['To'] = email
        msg['Subject'] = "Password for SHOPPING APP"
        body = "Your password for  SHOPPING APP is " + log_obj.password
        msg.attach(MIMEText(body, 'plain'))
        s.send_message(msg)
        return HttpResponse("Password send to email")
    else:
        return HttpResponse("Email doesnot exist")


def shopreg_load(request):
    return render(request,"shop_registration.html")
def shopreg_post(request):
    name=request.POST['textfield']
    gst_in=request.POST['textfield2']
    place=request.POST['textfield3']
    post=request.POST['textfield4']
    pincode=request.POST['textfield5']
    email=request.POST['textfield11']
    phone=request.POST['textfield6']
    category=request.POST['select']
    image=request.FILES['fileField']
    latitude=request.POST['textfield7']
    longitude=request.POST['textfield8']
    password=request.POST['textfield9']
    log_obj=login()
    log_obj.username=email
    log_obj.password=password
    log_obj.usertype='pending'
    log_obj.save()
    fs=FileSystemStorage()
    fname=time.strftime("%Y%m%d-%H%M%S")+".jpg"
    file_name=fs.save(fname,image)
    path=fs.url(file_name)
    shop_obj=shops()
    shop_obj.shop_name=name
    shop_obj.gst_in=gst_in
    shop_obj.place=place
    shop_obj.post=post
    shop_obj.pincode=pincode
    shop_obj.email=email
    shop_obj.phone=phone
    shop_obj.category=category
    shop_obj.image=path
    shop_obj.latitude=latitude
    shop_obj.longitude=longitude
    shop_obj.LOGIN_ID=log_obj
    shop_obj.save()
    return HttpResponse("ok")

#####################admin portion start

def admin_add_category_load(request):
    if request.session['lg']=="yes":
        return render(request,"Admin/Add_category.html")
    else:
        return render(request, "login.html")
def admin_add_category_post(request):
    name= request.POST['textfield']
    img= request.FILES['filefield']
    fs = FileSystemStorage()
    fname = time.strftime("%Y%m%d-%H%M%S") + ".jpg"
    file_name = fs.save(fname, img)
    path = fs.url(file_name)

    cat_obj=category()
    cat_obj.cat_name=name
    cat_obj.image=path
    cat_obj.save()
    return admin_add_category_load(request)

def admin_edit_category_load(request,c_id):
    if request.session['lg'] == "yes":
        cat_obj=category.objects.get(id=c_id)
        request.session['c_id']=c_id
        return render(request,"Admin/Edit_category.html",{'data': cat_obj})
    else:
        return render(request, "login.html")
def admin_edit_category_post(request):
    name = request.POST['textfield']
    c_id=request.session['c_id']
    cat_obj=category.objects.get(id=c_id)
    cat_obj.cat_name=name
    if 'filefield' in request.FILES:
        img = request.FILES['filefield']
        fs = FileSystemStorage()
        fname = time.strftime("%Y%m%d-%H%M%S") + ".jpg"
        file_name = fs.save(fname, img)
        path = fs.url(file_name)
        cat_obj.image = path

    cat_obj.save()
    return admin_view_category_load(request)

def admin_view_category_load(request):
    if request.session['lg'] == "yes":
        cat_obj=category.objects.all()
        return render(request,"Admin/View_category.html",{'data':cat_obj})
    else:
        return render(request, "login.html")
def admin_view_category_post(request):
    name = request.POST['textfield']
    cat_obj=category.objects.filter(cat_name__contains=name)
    return render(request, "Admin/View_category.html", {'data': cat_obj})


def delete_category(request,c_id):
    cat_obj=category.objects.get(id=c_id)
    cat_obj.delete()
    return redirect("/newapp/admin_view_category_load/#content")
def admin_view_shopreg_load(request):
    if request.session['lg'] == "yes":
        shop_obj=shops.objects.filter(LOGIN_ID__usertype='pending')
        return render(request,"Admin/View_regshop.html", {'data':shop_obj})
    else:
        return render(request, "login.html")
def admin_view_shopreg_post(request):
     
    shop_obj = shops.objects.filter(LOGIN_ID__usertype='pending',shop_name__contains=shop_name)
    return render(request, "Admin/View_regshop.html", {'data': shop_obj})

def approve_shopreg(request,log_id):
    if request.session['lg'] == "yes":
        log_obj=login.objects.get(id=log_id)
        log_obj.usertype="shop"
        log_obj.save()
        return admin_view_shopreg_load(request)
    else:
        return render(request, "login.html")

def reject_shopreg(request,log_id):
    if request.session['lg'] == "yes":
        log_obj=login.objects.get(id=log_id)
        log_obj.usertype="rejected"
        log_obj.save()
        return admin_view_shopreg_load(request)
    else:
        return render(request, "login.html")


def admin_Approvedshops_load(request):
    if request.session['lg'] == "yes":
        shop_obj=shops.objects.filter(LOGIN_ID__usertype='shop')
        return render(request,"Admin/Approvedshops.html", {'data':shop_obj})
    else:
        return render(request, "login.html")
def admin_Approvedshops_post(request):
    shop_name = request.POST['textfield']
    shop_obj = shops.objects.filter(LOGIN_ID__usertype='shop',shop_name__contains=shop_name)
    return render(request, "Admin/Approvedshops.html", {'data': shop_obj})

def admin_Rejectedshops_load(request):
    if request.session['lg'] == "yes":
        shop_obj = shops.objects.filter(LOGIN_ID__usertype='rejected')
        return render(request,"Admin/Rejectedshops.html", {'data':shop_obj})
    else:
        return render(request, "login.html")
def admin_Rejectedshops_post(request):
    shop_name = request.POST['textfield']
    shop_obj = shops.objects.filter(LOGIN_ID__usertype='rejected', shop_name__contains=shop_name)
    return render(request, "Admin/Rejectedshops.html", {'data': shop_obj})

def admin_Add_deliveryboy_load(request):
    if request.session['lg'] == "yes":
        return render(request,"Admin/Add_deliveryboy.html")
    else:
        return render(request, "login.html")
def admin_Add_deliveryboy_post(request):
    delboy_name = request.POST['textfield']
    house_name_no= request.POST['textfield2']
    place= request.POST['textfield3']
    post= request.POST['textfield4']
    pincode= request.POST['textfield5']
    email = request.POST['textfield11']
    phone = request.POST['textfield6']
    image=request.FILES['fileField']
    password=str(random.randint(1000,9999))
    fs = FileSystemStorage()
    fname=time.strftime("%Y%m%d-%H%M%S")+".jpg"
    file_name = fs.save(fname, image)
    path=fs.url(file_name)
    log_obj=login()
    log_obj.username=email
    log_obj.password=password
    log_obj.usertype='deliveryboy'
    log_obj.save()
    del_obj=delivery_boy()
    del_obj.delboy_name=delboy_name
    del_obj.house_no_name=house_name_no
    del_obj.place=place
    del_obj.post=post
    del_obj.pincode=pincode
    del_obj.email=email
    del_obj.phone=phone
    del_obj.image=path
    del_obj.LOGIN_ID=log_obj
    del_obj.save()
    loc_obj = location()
    curdate=datetime.datetime.now().date()
    curtime=datetime.datetime.now().time()
    loc_obj.latitude = "0"
    loc_obj.longitude = "0"
    loc_obj.DELIVERY_ID = del_obj
    loc_obj.date = curdate
    loc_obj.time = curtime
    loc_obj.save()
    return admin_Add_deliveryboy_load(request)


def admin_Edit_deliveryboy_load(request,d_id):
    if request.session['lg'] == "yes":
        delboy_obj=delivery_boy.objects.get(id=d_id)
        request.session['d_id'] = d_id
        return render(request,"Admin/Edit_deliveryboy.html",{'data':delboy_obj})
    else:
        return render(request, "login.html")
def admin_Edit_deliveryboy_post(request):
    d_id=request.session['d_id']
    delboy_name = request.POST['textfield']
    house_name_no = request.POST['textfield2']
    place = request.POST['textfield3']
    post = request.POST['textfield4']
    pincode = request.POST['textfield5']
    email = request.POST['textfield11']
    phone = request.POST['textfield6']
    image = request.FILES['fileField']
    delboy_obj=delivery_boy.objects.get(id=d_id)
    delboy_obj.delboy_name=delboy_name
    delboy_obj.house_no_name=house_name_no
    delboy_obj.place=place
    delboy_obj.post=post
    delboy_obj.pincode=pincode
    delboy_obj.email=email
    delboy_obj.phone=phone
    if 'fileField' in request.FILES:
        fs = FileSystemStorage()
        fname = time.strftime("%Y%m%d-%H%M%S") + ".jpg"
        file_name = fs.save(fname,image)
        path = fs.url(file_name)
        delboy_obj.image=path
    delboy_obj.save()
    return admin_view_deliveryboy_load(request)


def admin_view_deliveryboy_load(request):
    if request.session['lg'] == "yes":
        delb_obj=delivery_boy.objects.all()
        return render(request,"Admin/view_deliveryboy.html",{'data':delb_obj})
    else:
        return render(request, "login.html")
def admin_view_deliveryboy_post(request):
    name=request.POST['textfield']
    delb_obj=delivery_boy.objects.filter(delboy_name__contains=name)
    return render(request,"Admin/view_deliveryboy.html",{'data':delb_obj})

def delete_delboy(request,d_id):
    delboy_obj=delivery_boy.objects.get(id=d_id)
    log_obj=login.objects.get(id=delboy_obj.LOGIN_ID_id)
    delboy_obj.delete()
    log_obj.delete()
    return admin_view_deliveryboy_load(request)

def admin_rating_load(request,shop_id):
    if request.session['lg'] == "yes":
        shop_obj=shops.objects.get(id=shop_id)
        rating_obj=rating.objects.filter(SHOP_ID_id=shop_id)
        return render(request,"Admin/Rating.html", {"data": shop_obj,"rating":rating_obj})
    else:
        return render(request, "login.html")




#####################admin portion end


####################seller portion start

def seller_viewprofile_load(request):
    if request.session['lg'] == "yes":
        s_id=request.session['shop_id']
        print(s_id)
        prof_obj=shops.objects.get(id=s_id)
        return render(request, "Seller/view_profile.html",{'data':prof_obj})
    else:
        return render(request, "login.html")

def seller_editprofile_load(request):
    if request.session['lg'] == "yes":
        s_id = request.session['shop_id']
        print(s_id)
        shop_obj = shops.objects.get(id=s_id)
        return render(request, "Seller/Edit_profile.html",{'data':shop_obj})
    else:
        return render(request, "login.html")
def seller_editprofile_post(request):
    name = request.POST['textfield']
    gst_in = request.POST['textfield2']
    place = request.POST['textfield3']
    post = request.POST['textfield4']
    pincode = request.POST['textfield5']
    phone = request.POST['textfield6']
    category = request.POST['select']
    latitude = request.POST['textfield7']
    longitude = request.POST['textfield8']
    s_id = request.session['shop_id']
    shop_obj = shops.objects.get(id=s_id)
    shop_obj.shop_name=name
    shop_obj.gst_in=gst_in
    shop_obj.place=place
    shop_obj.post=post
    shop_obj.pincode=pincode
    shop_obj.phone=phone
    shop_obj.category=category
    shop_obj.latitude=latitude
    shop_obj.longitude=longitude
    if 'fileField' in request.FILES:
        image = request.FILES['fileField']
        fs = FileSystemStorage()
        fname = time.strftime("%Y%m%d-%H%M%S") + ".jpg"
        file_name = fs.save(fname,image)
        path = fs.url(file_name)
        shop_obj.image=path
    shop_obj.save()
    return seller_viewprofile_load(request)


def seller_addproduct_load(request):
    if request.session['lg'] == "yes":
        cat_obj=category.objects.all()
        return render(request, "Seller/Add_product.html",{'data': cat_obj})
    else:
        return render(request, "login.html")
def seller_addproduct_post(request):
    name = request.POST['textfield']
    cat_id= request.POST['select']
    shop_id=request.session['shop_id']
    rate = request.POST['textfield7']
    image = request.FILES['fileField']
    fs=FileSystemStorage()
    fname=time.strftime("%Y%m%d-%H%M%S")+".jpg"
    file_name=fs.save(fname,image)
    path=fs.url(file_name)
    prod_obj=product()
    prod_obj.product_name=name
    prod_obj.product_rate=rate
    prod_obj.image=path
    prod_obj.PRODUCT_CATEGORY=category.objects.get(id=cat_id)
    prod_obj.SHOP_ID=shops.objects.get(id=shop_id)
    prod_obj.save()
    return seller_addproduct_load(request)

def seller_editproduct_load(request,p_id):
    if request.session['lg'] == "yes":
        prod_obj=product.objects.get(id=p_id)
        print(prod_obj)
        cat_obj=category.objects.all()
        return render(request, "Seller/Edit_product.html",{'data': prod_obj, 'category': cat_obj})
    else:
        return render(request, "login.html")
def seller_editproduct_post(request):
    name = request.POST['textfield']
    cat_id = request.POST['select']
    rate = request.POST['textfield7']
    # image = request.FILES['fileField']
    pid=request.POST['pid']
    # prod_obj.product_name=name
    # prod_obj.product_rate=rate
    # prod_obj.PRODUCT_CATEGORY=cat_id
    if 'fileField' in request.FILES:
        image = request.FILES['fileField']
        fs = FileSystemStorage()
        fname = time.strftime("%Y%m%d-%H%M%S") + ".jpg"
        file_name = fs.save(fname,image)
        path = fs.url(file_name)
        product.objects.filter(id=pid).update(product_name=name,product_rate=rate,PRODUCT_CATEGORY_id=cat_id,image=path)

    else:
        product.objects.filter(id=pid).update(product_name=name, product_rate=rate, PRODUCT_CATEGORY_id=cat_id)
        # prod_obj.save()

    return seller_viewproduct_load(request)

def seller_viewproduct_load(request):
    if request.session['lg'] == "yes":
        s_id = request.session['shop_id']
        prod_obj=product.objects.filter(SHOP_ID_id=s_id)
        return render(request, "Seller/View_product.html",{'data': prod_obj})
    else:
        return render(request, "login.html")
def seller_viewproduct_post(request):
    name= request.POST['textfield']
    prod_obj =product.objects.filter(product_name__contains=name)
    return render(request, "Seller/View_product.html", {'data': prod_obj})
def remove_product(request,p_id):
    prod_obj=product.objects.get(id=p_id)
    prod_obj.delete()
    return seller_viewproduct_load(request)

def seller_view_productorder_load(request):
    if request.session['lg'] == "yes":
        s_id = request.session['shop_id']
        order_obj=orders.objects.filter(SHOP_ID_id=s_id,status='pending')
        return render(request, "Seller/View_product_orders.html",{'data': order_obj})
    else:
        return render(request, "login.html")
def seller_view_productorder_post(request):
    btn=request.POST['button']
    s_id = request.session['shop_id']
    if btn == "Search":
        p_name = request.POST['textfield']
        order_obj=orders.objects.filter(SHOP_ID_id=s_id,status='pending' ,BUYER_ID__buyer_name__contains =p_name)
    else:
        f_date = request.POST['textfield2']
        to_date = request.POST['textfield3']
        order_obj=orders.objects.filter(SHOP_ID_id=s_id,date__range=(f_date,to_date),status='pending')
    return render(request, "Seller/View_product_orders.html",{'data': order_obj})

def seller_more_productoreders_load(request,o_id):
    if request.session['lg'] == "yes":
        ordersub_obj=order_sub.objects.filter(ORDER_ID_id=o_id)
        res=[]
        total=0
        payable=0
        for i in ordersub_obj:
            amount=float(i.PRODUCT_ID.product_rate)*float(i.quantity)
            lobj = offer.objects.filter(PRODUCT_ID=i.PRODUCT_ID_id)

            disc = 0
            for j in lobj:
                qt1 = j.quantity_1
                qt2 = j.quantity_2
                qw = i.quantity

                if int(qw) >= int(qt1) and int(qw) <= int(qt2):
                    disc = j.discount
                    break
            total = total + float(amount)

            tot_disc = amount * float(disc) / 100
            # print("hhhh  ",amount, tot_disc)
            t_amount = amount - tot_disc
            print(t_amount)
            payable = payable + t_amount
            print("pppp", payable)

            d={
                "product_name":i.PRODUCT_ID.product_name,
                "product_price":i.PRODUCT_ID.product_rate,
                "product_quantity":i.quantity,
                "amount":amount,
                "disc":tot_disc,
                "offer_amount":t_amount
            }
            res.append(d)
        data2={}
        order_obj=orders.objects.get(id=o_id)
        data2['total']=total
        data2['payable']=payable
        data2['order_id']=o_id
        data2['email']= order_obj.BUYER_ID.email
        data2['phone']= order_obj.BUYER_ID.phone
        data2['name']= order_obj.BUYER_ID.buyer_name
        data2['date']= order_obj.date
        return render(request, "Seller/More_product_orders.html",{'data':res, 'data2':data2 })
    else:
        return render(request, "login.html")


def seller_billpreview(request,o_id):
    if request.session['lg'] == "yes":
        ordersub_obj = order_sub.objects.filter(ORDER_ID_id=o_id)
        res = []
        total = 0
        payable = 0
        for i in ordersub_obj:
            amount = float(i.PRODUCT_ID.product_rate) * float(i.quantity)
            lobj = offer.objects.filter(PRODUCT_ID=i.PRODUCT_ID_id)

            disc = 0
            for j in lobj:
                qt1 = j.quantity_1
                qt2 = j.quantity_2
                qw = i.quantity

                if int(qw) >= int(qt1) and int(qw) <= int(qt2):
                    disc = j.discount
                    break
            total = total + float(amount)

            tot_disc = amount * float(disc) / 100
            # print("hhhh  ",amount, tot_disc)
            t_amount = amount - tot_disc
            print(t_amount)
            payable = payable + t_amount
            print("pppp", payable)

            d = {
                "product_name": i.PRODUCT_ID.product_name,
                "product_price": i.PRODUCT_ID.product_rate,
                "product_quantity": i.quantity,
                "amount": amount,
                "disc": tot_disc,
                "offer_amount": t_amount
            }
            res.append(d)
        data2 = {}
        order_obj = orders.objects.get(id=o_id)
        data2['total'] = total
        data2['payable'] = payable
        data2['order_id'] = o_id
        data2['email'] = order_obj.BUYER_ID.email
        data2['phone'] = order_obj.BUYER_ID.phone
        data2['name'] = order_obj.BUYER_ID.buyer_name
        data2['date'] = order_obj.date
        return render(request, "Seller/print_billreport.html",{'data':res, 'data2':data2 })
    else:
        return render(request, "login.html")

def seller_assignorder_delboy_load(request,o_id):
    if request.session['lg'] == "yes":
        del_obj=delivery_boy.objects.all()
        return render(request, "Seller/Assignorder_delboy.html",{'data':del_obj,'o_id': o_id})
    else:
        return render(request, "login.html")
def seller_assignorder_delboy_post(request):
    ord_id = request.POST['hide']
    delivery_boyid = request.POST['select']

    asnorder_obj=order_assign()
    asnorder_obj.DELBOY_ID_id=delivery_boyid
    asnorder_obj.ORDER_ID_id=ord_id
    asnorder_obj.date=time.strftime("%Y%m%d-%H%M%S")
    asnorder_obj.status="pending"
    asnorder_obj.save()

    orders.objects.filter(id=ord_id).update(status='assigned')



    return seller_view_productorder_load(request)

def seller_view_deliverystatus_load(request):
    if request.session['lg'] == "yes":
        shop_id=request.session['shop_id']
        res=order_assign.objects.filter(ORDER_ID__SHOP_ID_id=shop_id)
        return render(request, "Seller/view_delivery_status.html",{'data':res})
    else:
        return render(request, "login.html")

def seller_view_deliverystatus_post(request):
    btn=request.POST['button']
    shop_id = request.session['shop_id']

    if btn== "Search":
        name = request.POST['textfield']
        obj = order_assign.objects.filter(ORDER_ID__BUYER_ID__buyer_name__contains=name,ORDER_ID__SHOP_ID_id=shop_id)
    elif btn=="Filter":
        f_date = request.POST['date1']
        to_date = request.POST['date2']
        obj = order_assign.objects.filter(ORDER_ID__date__range={f_date,to_date},ORDER_ID__SHOP_ID_id=shop_id)
    return render(request, "Seller/view_delivery_status.html", {'data': obj})


def seller_view_buyer_rating_load(request):
    if request.session['lg'] == "yes":
        s_id = request.session['shop_id']
        rate_obj = rating.objects.filter(SHOP_ID_id=s_id).order_by('-id')
        res_rate = []
        for i in rate_obj:
            rate = int(i.rating)
            rate_list = []
            for j in range(rate):
                rate_list.append(j)
            no_rate = 5 - rate
            no_rate_list = []
            for j in range(no_rate):
                no_rate_list.append(j)
            print(rate_list, no_rate_list)
            res_rate.append({'rating': rate_list, 'no_rating': no_rate_list, 'date': i.date, 'review': i.review,
                             'name': i.USER_ID.buyer_name, 'image': i.USER_ID.image})
        return render(request, "Seller/view_buyer_rating.html",{"rating": res_rate})
    else:
        return render(request, "login.html")

def seller_view_paymentreports_load(request):
    if request.session['lg'] == "yes":
        shop_id = request.session['shop_id']
        p_obj=payment.objects.filter(ORDER_ID__SHOP_ID_id=shop_id)
        return render(request, "Seller/view_paymentreports.html",{'data':p_obj})
    else:
        return render(request, "login.html")
def seller_view_paymentreports_post(request):
    shop_id = request.session['shop_id']
    f_date = request.POST['textfield2']
    to_date = request.POST['textfield3']
    p_obj = payment.objects.filter(ORDER_ID__date__range={f_date, to_date},ORDER_ID__SHOP_ID_id=shop_id)
    return render(request, "Seller/view_paymentreports.html",{'data':p_obj})

def seller_add_offers_load(request,id):
    if request.session['lg'] == "yes":
        return render(request, "Seller/add_offer.html",{'product_id':id})
    else:
        return render(request, "login.html")
def seller_add_product_post(request):
    p_id= request.POST['pid']
    quantity_1= request.POST['textfield']
    quantity_2= request.POST['textfield1']
    discount= request.POST['textfield2']
    offer_obj=offer()
    offer_obj.quantity_1=quantity_1
    offer_obj.quantity_2=quantity_2
    offer_obj.discount=discount
    offer_obj.PRODUCT_ID_id=p_id
    offer_obj.save()
    return redirect('/newapp/seller_view_offers_load/'+p_id)


def seller_view_offers_load(request,id):
    if request.session['lg'] == "yes":
        offer_obj=offer.objects.filter(PRODUCT_ID_id=id)
        request.session['pid']=id
        return render(request, "Seller/view_offer.html",{'data':offer_obj,'product_id':id})
    else:
        return render(request, "login.html")

def seller_edit_offers(request, oid):
    if request.session['lg'] == "yes":
        offer_obj = offer.objects.get(id=oid)
        request.session['oid']=oid
        return render(request, "Seller/edit_offer.html", {'data':offer_obj})
    else:
        return render(request, "login.html")

def seller_edit_offers_post(request):
    p_id = request.session['pid']
    oid = request.session['oid']
    quantity_1 = request.POST['textfield']
    quantity_2 = request.POST['textfield1']
    discount = request.POST['textfield2']
    offer_obj = offer.objects.get(id=oid)
    offer_obj.quantity_1 = quantity_1
    offer_obj.quantity_2 = quantity_2
    offer_obj.discount = discount
    offer_obj.save()
    return redirect('/newapp/seller_view_offers_load/' + p_id)


def seller_delete_offers(request, oid):
    p_id = request.session['pid']
    offer_obj = offer.objects.get(id=oid)
    offer_obj.delete()
    return redirect('/newapp/seller_view_offers_load/' + p_id)
############################### seller portion end

def admin_home_load(request):
    if request.session['lg'] == "yes":
        return render(request, "Admin/home_admin.html")
    else:
        return render(request, "login.html")
def admin_home_post(request):
    return render(request, "Admin/home_admin.html")

def seller_home_load(request):
    if request.session['lg'] == "yes":
        s_id = request.session['shop_id']
        cat_obj=category.objects.all()
        res_cat=[]
        for i in cat_obj:
            res_cat.append({'cat_name':i.cat_name, 'image':i.image})
        rate_obj = rating.objects.filter(SHOP_ID_id=s_id).order_by('-id')[:3]
        res_rate = []
        cnt=1
        for i in rate_obj:
            rate=int(i.rating)
            rate_list=[]
            for j in range(rate):
                rate_list.append(j)
            no_rate=5-rate
            no_rate_list=[]
            for j in range(no_rate):
                no_rate_list.append(j)
            print(rate_list, no_rate_list)
            res_rate.append({'rating': rate_list, 'no_rating': no_rate_list,'date': i.date, 'review': i.review, 'name': i.USER_ID.buyer_name, 'image':i.USER_ID.image })
            # cnt+=1
            # if cnt==3:
            #     break
        print(res_rate)
        return render(request, "Seller/home_seller.html",{'data_cat':res_cat, 'data_rate':res_rate})
    else:
        return render(request, "login.html")


#######################3            android
def and_login_post(request):
    username=request.POST['username']
    password=request.POST['password']
    log_obj=login.objects.filter(username=username ,password=password)
    if log_obj.exists():
        log_obj=log_obj[0]
        type=log_obj.usertype
        print(type)
        if type=="user":
            user_obj=buyer.objects.filter(LOGIN_ID=log_obj)
            if user_obj.exists():
                user_obj=user_obj[0]
                return JsonResponse({'status':'ok','id':user_obj.id, 'type':log_obj.usertype})

        elif type=="deliveryboy":
            delboy_obj=delivery_boy.objects.filter(LOGIN_ID=log_obj)
            if delboy_obj.exists():
                delboy_obj=delboy_obj[0]
                return JsonResponse({'status': 'ok', 'id': delboy_obj.id,  'type':log_obj.usertype})
        else:
            return JsonResponse({'status':'invalid user'})
    else:
       return JsonResponse({'status':'invalid details'})


def and_verify_email(request):
    email=request.POST['email']
    log_obj=login.objects.filter(username=email)
    if log_obj.exists():
        return JsonResponse({'status':'no'})
    else:
        otp=random.randint(10000,99999)
        import smtplib
        s = smtplib.SMTP(host='smtp.gmail.com', port=587)
        s.starttls()
        s.login("shopping.app.2k21@gmail.com", "7994755364")
        msg = MIMEMultipart()  # create a message.........."
        msg['From'] = "shopping.app.2k21@gmail.com"
        msg['To'] = email
        msg['Subject'] = "VERIFICATION CODE"
        body = "Verify your mail id using this code : \n" + str(otp)
        msg.attach(MIMEText(body, 'plain'))
        s.send_message(msg)
        return JsonResponse({'status':'ok', 'otp':str(otp)})


def and_buyerreg_post(request):
    name=request.POST['name']
    phone=request.POST['phone']
    email=request.POST['email']
    house_no_name=request.POST['house']
    place=request.POST['place']
    pincode=request.POST['pincode']
    post=request.POST['post']
    district=request.POST['district']
    password=request.POST['password']
    image=request.POST['image']
    timestr = time.strftime("%Y%m%d-%H%M%S")
    print(timestr)
    a = base64.b64decode(image)
    fh = open(media_path + timestr + ".jpg", "wb")
    path = "/media/" + timestr + ".jpg"
    fh.write(a)
    fh.close()

    log_obj=login()
    log_obj.username=email
    log_obj.password=password
    log_obj.usertype='user'
    log_obj.save()
    user_obj=buyer()
    user_obj.buyer_name=name
    user_obj.phone=phone
    user_obj.email=email
    user_obj.house_no_name=house_no_name
    user_obj.place=place
    user_obj.pin=pincode
    user_obj.post=post
    user_obj.district=district
    user_obj.image=path
    user_obj.LOGIN_ID=log_obj
    user_obj.save()
    return JsonResponse({'status':'ok'})

def and_user_viewprofile(request):
    u_id = request.POST['u_id']
    user_obj = buyer.objects.get(id=u_id)
    return JsonResponse({'status': 'ok', 'name':user_obj.buyer_name, 'phone':user_obj.phone, 'email':user_obj.email, 'house':user_obj.house_no_name,
                         'place':user_obj.place, 'post':user_obj.post, 'district':user_obj.district, 'pin':user_obj.pin, 'image':user_obj.image})


def and_user_editprofile_post(request):
    u_id=request.POST['u_id']
    name=request.POST['name']
    phone = request.POST['phone']
    email = request.POST['email']
    house_no_name = request.POST['house']
    place = request.POST['place']
    pincode = request.POST['pincode']
    post = request.POST['post']
    district = request.POST['district']
    image = request.POST['image']
    user_obj=buyer.objects.get(id=u_id)
    user_obj.buyer_name=name
    user_obj.phone=phone
    user_obj.email=email
    user_obj.house_no_name=house_no_name
    user_obj.place=place
    user_obj.pin=pincode
    user_obj.post=post
    user_obj.district=district
    if image!=" ":
        timestr = time.strftime("%Y%m%d-%H%M%S")
        print(timestr)
        a = base64.b64decode(image)
        fh = open(media_path + timestr + ".jpg", "wb")
        path = "/media/" + timestr + ".jpg"
        fh.write(a)
        fh.close()
        user_obj.image=path
    user_obj.save()
    log_obj=user_obj.LOGIN_ID
    log_obj.username=email
    log_obj.save()
    return JsonResponse({'status':'ok'})

def and_nearestshop_post(request):
    category=request.POST['cat']
    lati=request.POST['lat']
    logi=request.POST['long']
    print("kkk",lati,logi)
    lat=lati.strip()
    log=logi.strip()
    if category=="All":
        shop_obj = shops.objects.all()
    else:
        shop_obj=shops.objects.filter(category=category)
    res = []
    ids=[]
    dist=[]
    for i in shop_obj:
        my_coord=(float(lat),float(log))
        shop_coord=(float(i.latitude),float(i.longitude))
        distannce_in_km = geodesic(my_coord, shop_coord).km
        dist.append(distannce_in_km)
        ids.append(i.id)
    n=len(ids)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if dist[j] > dist[j + 1]:
                dist[j], dist[j + 1] = dist[j + 1], dist[j]
                ids[j], ids[j + 1] = ids[j + 1], ids[j]

    for j in range(len(ids)):
        i=shops.objects.get(id=ids[j])
        d = {'image': i.image, 'name': i.shop_name, 'phone': i.phone, 'city': i.place, 'latitude': i.latitude,
             'longitude': i.longitude, 'distance' : dist[j], 'id': i.id}
        res.append(d)
    print(res)
    return JsonResponse({'status': 'ok', 'data': res})

def and_viewshop_rating_post(request):
    shop_id=request.POST['shop_id']
    rating_obj=rating.objects.filter(SHOP_ID_id=shop_id)
    res = []
    for i in rating_obj:
        d = {'image': i.USER_ID.image, 'name': i.USER_ID.buyer_name, 'date':i.date, 'rating':i.rating, 'review':i.review}
        res.append(d)
    return JsonResponse({'status': 'ok', 'data': res})

def view_shopmore_post(request):
    s_id = request.POST['s_id']
    shop_obj = shops.objects.get(id=s_id)
    p_obj=product.objects.filter(SHOP_ID_id=s_id)
    res = []
    for i in p_obj:
        d = {'image': i.image, 'name': i.product_name, 'category': i.PRODUCT_CATEGORY.cat_name, 'rate': i.product_rate, 'id':i.id}
        res.append(d)
    return JsonResponse({'status': 'ok', 'name': shop_obj.shop_name, 'phone': shop_obj.phone, 'email': shop_obj.email,
                         'place': shop_obj.place, 'post': shop_obj.post,
                         'pin': shop_obj.pincode, 'image': shop_obj.image, 'data':res})

def and_addtocart_post(request):
    p_id=request.POST['p_id']
    u_id=request.POST['u_id']
    quantity=request.POST['quantity']
    cart_obj=cart()
    cart_obj.quantity=quantity
    cart_obj.PRODUCT_ID_id=p_id
    cart_obj.BUYER_ID_id=u_id
    cart_obj.save()
    return JsonResponse({'status': 'ok'})

def and_viewfeedback_post(request):
    p_id = request.POST['p_id']
    f_obj = feedback.objects.filter(PRODUCT_ID_id=p_id)
    res = []
    for i in f_obj:
        d = {'image': i.BUYER_ID.image, 'name': i.BUYER_ID.buyer_name, 'date': i.date, 'feedback': i.feedback}
        res.append(d)
    return JsonResponse({'status': 'ok', 'data': res})

def and_viewcart_post(request):
    u_id=request.POST['u_id']
    cart_obj=cart.objects.filter(BUYER_ID_id=u_id)
    res = []
    total=0
    payable=0
    for i in cart_obj:
        amount=float(i.PRODUCT_ID.product_rate)*float(i.quantity)
        print(amount)
        lobj=offer.objects.filter(PRODUCT_ID=i.PRODUCT_ID_id)

        disc=0
        for j in lobj:
            qt1=j.quantity_1
            qt2=j.quantity_2
            qw=i.quantity

            if int(qw)>=int(qt1) and int(qw)<=int(qt2):
                disc=j.discount

                break
                # discount= total+ float(j.discount)
        # print("jjjjjjj", disc)
        total=total+float(amount)

        tot_disc = amount * float(disc) / 100
        # print("hhhh  ",amount, tot_disc)
        t_amount = amount - tot_disc
        print(t_amount)
        payable=payable+t_amount
        print("pppp",payable)

        d = {'image': i.PRODUCT_ID.image, 'name': i.PRODUCT_ID.product_name, 'category': i.PRODUCT_ID.PRODUCT_CATEGORY.cat_name,
                 'rate': i.PRODUCT_ID.product_rate, 'quantity':i.quantity, 'id':i.id,
                 'shop_info':i.PRODUCT_ID.SHOP_ID.shop_name+"\n"+i.PRODUCT_ID.SHOP_ID.place+"\n"+i.PRODUCT_ID.SHOP_ID.phone+"\n"+
                             i.PRODUCT_ID.SHOP_ID.email, 'amount': amount, 'p_payable':t_amount}
        res.append(d)

        print(amount)
    print(res)
    print(total,"aaaaa")
    savings=total-payable
    return JsonResponse({'status': 'ok', 'savings':savings, 'data': res, 'data2':total,'payable':payable})

def and_removefromcart_post(request):
    cart_id=request.POST['cart_id']
    cart_obj=cart.objects.get(id=cart_id)
    cart_obj.delete()
    return JsonResponse({'status': 'ok'})

def and_payment_post(request):
    u_id=request.POST['u_id']
    total_amnt=request.POST['total']
    bank_name=request.POST['bank']
    ac_no=request.POST['account_no']
    pin_no=request.POST['pin_no']
    pay_type=request.POST['pay_type']
    p_id=request.POST['p_id']
    qty=request.POST['qty']
    print(bank_name, ac_no, pin_no)
    bank_obj=bank.objects.filter(bank_name=bank_name, account_no=ac_no, pin_no=pin_no)
    if bank_obj.exists():
        bank_obj=bank_obj[0]
        balance=bank_obj.balance
        if float(balance)<float(total_amnt):
            return JsonResponse({'status': 'insufficient'})
        else:
            if pay_type=="cart":
                cart_obj_all=cart.objects.filter(BUYER_ID_id=u_id)
                shop_ids=[]
                for i in cart_obj_all:
                    if i.PRODUCT_ID.SHOP_ID_id not in shop_ids:
                        shp_id=i.PRODUCT_ID.SHOP_ID_id
                        shop_ids.append(shp_id)
                        cart_obj_by_shop=cart.objects.filter(PRODUCT_ID__SHOP_ID_id=shp_id)
                        bill_amt=0
                        for j in cart_obj_by_shop:
                            bill_amt+=float(j.quantity)*float(j.PRODUCT_ID.product_rate)
                        order_obj=orders()
                        order_obj.SHOP_ID_id=shp_id
                        order_obj.BUYER_ID_id=u_id
                        order_obj.date=datetime.datetime.now().date()
                        order_obj.amount=bill_amt
                        order_obj.status='pending'
                        order_obj.save()
                        pay_obj = payment()
                        pay_obj.amount = bill_amt
                        pay_obj.account_no = ac_no
                        pay_obj.ORDER_ID=order_obj
                        pay_obj.save()

                        ##  insert into ordersub
                        for j in cart_obj_by_shop:
                            ordsub_obj=order_sub()
                            ordsub_obj.ORDER_ID=order_obj
                            ordsub_obj.quantity=j.quantity
                            ordsub_obj.PRODUCT_ID=j.PRODUCT_ID
                            ordsub_obj.save()
                            j.delete()
            else:
                i=product.objects.get(id=p_id)
                shp_id = i.SHOP_ID_id
                cart_obj_by_shop = cart.objects.filter(PRODUCT_ID__SHOP_ID_id=shp_id)
                bill_amt = total_amnt
                order_obj = orders()
                order_obj.SHOP_ID_id = shp_id
                order_obj.BUYER_ID_id = u_id
                order_obj.date = datetime.datetime.now().date()
                order_obj.amount = bill_amt
                order_obj.status = 'pending'
                order_obj.save()
                pay_obj = payment()
                pay_obj.amount = bill_amt
                pay_obj.account_no = ac_no
                pay_obj.ORDER_ID = order_obj
                pay_obj.save()

                ##  insert into ordersub

                ordsub_obj = order_sub()
                ordsub_obj.ORDER_ID = order_obj
                ordsub_obj.quantity = qty
                ordsub_obj.PRODUCT_ID_id = p_id
                ordsub_obj.save()
            bank_obj.balance=float(balance)-float(total_amnt)
            bank_obj.save()

            return JsonResponse({'status': 'ok'})

    else:
        return JsonResponse({'status':'invalid'})










# def and_payment_postby_offer(request):
#     u_id=request.POST['u_id']
#     total_amnt=request.POST['total']
#     bank_name=request.POST['bank']
#     ac_no=request.POST['account_no']
#     pin_no=request.POST['pin_no']
#     pay_type=request.POST['pay_type']
#     p_id=request.POST['p_id']
#     qty=request.POST['qty']
#     print(bank_name, ac_no, pin_no)
#     bank_obj=bank.objects.filter(bank_name=bank_name, account_no=ac_no, pin_no=pin_no)
#     if bank_obj.exists():
#         bank_obj=bank_obj[0]
#         balance=bank_obj.balance
#         if float(balance)<float(total_amnt):
#             return JsonResponse({'status': 'insufficient'})
#         else:
#             if pay_type=="cart":
#                 cart_obj_all=cart.objects.filter(BUYER_ID_id=u_id)
#                 shop_ids=[]
#                 for i in cart_obj_all:
#                     if i.PRODUCT_ID.SHOP_ID_id not in shop_ids:
#                         shp_id=i.PRODUCT_ID.SHOP_ID_id
#                         shop_ids.append(shp_id)
#                         cart_obj_by_shop=cart.objects.filter(PRODUCT_ID__SHOP_ID_id=shp_id)
#                         bill_amt=0
#                         for j in cart_obj_by_shop:
#                             bill_amt+=float(j.quantity)*float(j.PRODUCT_ID.product_rate)
#                         order_obj=orders()
#                         order_obj.SHOP_ID_id=shp_id
#                         order_obj.BUYER_ID_id=u_id
#                         order_obj.date=datetime.datetime.now().date()
#                         order_obj.amount=bill_amt
#                         order_obj.status='pending'
#                         order_obj.save()
#                         pay_obj = payment()
#                         pay_obj.amount = bill_amt
#                         pay_obj.account_no = ac_no
#                         pay_obj.ORDER_ID=order_obj
#                         pay_obj.save()
#
#                         ##  insert into ordersub
#                         for j in cart_obj_by_shop:
#                             ordsub_obj=order_sub()
#                             ordsub_obj.ORDER_ID=order_obj
#                             ordsub_obj.quantity=j.quantity
#                             ordsub_obj.PRODUCT_ID=j.PRODUCT_ID
#                             ordsub_obj.save()
#                             j.delete()
#             else:
#                 i=product.objects.get(id=p_id)
#                 shp_id = i.SHOP_ID_id
#                 cart_obj_by_shop = cart.objects.filter(PRODUCT_ID__SHOP_ID_id=shp_id)
#                 bill_amt = total_amnt
#                 order_obj = orders()
#                 order_obj.SHOP_ID_id = shp_id
#                 order_obj.BUYER_ID_id = u_id
#                 order_obj.date = datetime.datetime.now().date()
#                 order_obj.amount = bill_amt
#                 order_obj.status = 'pending'
#                 order_obj.save()
#                 pay_obj = payment()
#                 pay_obj.amount = bill_amt
#                 pay_obj.account_no = ac_no
#                 pay_obj.ORDER_ID = order_obj
#                 pay_obj.save()
#
#                 ##  insert into ordersub
#
#                 ordsub_obj = order_sub()
#                 ordsub_obj.ORDER_ID = order_obj
#                 ordsub_obj.quantity = qty
#                 ordsub_obj.PRODUCT_ID_id = p_id
#                 ordsub_obj.save()
#             bank_obj.balance=float(balance)-float(total_amnt)
#             bank_obj.save()
#
#             return JsonResponse({'status': 'ok'})
#
#     else:
#         return JsonResponse({'status':'invalid'})

def and_viewandtrack_orders_post(request):
    u_id = request.POST['u_id']
    order_obj = orders.objects.filter(BUYER_ID_id=u_id)
    res = []
    for i in order_obj:
        d = {'date': i.date, 'image': i.SHOP_ID.image,
             'shop_info': i.SHOP_ID.shop_name + "\n" + i.SHOP_ID.place + "\n" + i.SHOP_ID.phone + "\n" +
                          i.SHOP_ID.email,'order_id':i.id, 'id':i.SHOP_ID_id,'amount':i.amount}
        assign_obj=order_assign.objects.filter(ORDER_ID=i)
        if assign_obj.exists():
            assign_obj=assign_obj[0]
            loc_obj=location.objects.filter(DELIVERY_ID=assign_obj.DELBOY_ID).order_by('-id')
            if loc_obj.exists():
                loc_obj=loc_obj[0]
                d['assign_status'] = "assigned"
                d['lat']=loc_obj.latitude
                d['log']=loc_obj.longitude
        else:
            d['assign_status']="not assigned"
        res.append(d)
    return JsonResponse({'status': 'ok', 'data': res})

def and_vieworder_items_post(request):
    o_id = request.POST['order_id']
    ordsub_obj = order_sub.objects.filter(ORDER_ID_id=o_id)
    res = []

    for i in ordsub_obj:
        total_amnt = float(i.PRODUCT_ID.product_rate) * float(i.quantity)
        d = {'image': i.PRODUCT_ID.image, 'p_name': i.PRODUCT_ID.product_name,
             'rate': i.PRODUCT_ID.product_rate , 'quantity': i.quantity, 'price':total_amnt, 'id':i.PRODUCT_ID_id }
        res.append(d)
    return JsonResponse({'status': 'ok', 'data': res})

def and_sendrating_post(request):
    u_id=request.POST['u_id']
    s_id=request.POST['s_id']
    rate=request.POST['rate']
    rate=rate.split('.')[0]
    review=request.POST['review']
    rating_obj = rating.objects.filter(USER_ID_id=u_id, SHOP_ID_id=s_id)
    if rating_obj.exists():
        rating_obj=rating_obj[0]
        rating_obj.rating=int(rate)
        rating_obj.review=review
        rating_obj.date=datetime.datetime.now().date()
        rating_obj.save()
    else:
        rating_obj = rating()
        rating_obj.rating = int(rate)
        rating_obj.review = review
        rating_obj.date = datetime.datetime.now().date()
        rating_obj.USER_ID_id=u_id
        rating_obj.SHOP_ID_id=s_id
        rating_obj.save()
    return JsonResponse({'status': 'ok'})

def and_sendfeedback_post(request):
    u_id=request.POST['u_id']
    p_id=request.POST['p_id']
    feed=request.POST['feedback']
    feedback_obj=feedback.objects.filter(BUYER_ID_id=u_id,PRODUCT_ID_id=p_id)
    if feedback_obj.exists():
        feedback_obj=feedback_obj[0]
        feedback_obj.date=datetime.datetime.now().date()
        feedback_obj.feedback=feed
        feedback_obj.save()
    else:
        feedback_obj = feedback()
        feedback_obj.date = datetime.datetime.now().date()
        feedback_obj.feedback = feed
        feedback_obj.BUYER_ID_id=u_id
        feedback_obj.PRODUCT_ID_id=p_id
        feedback_obj.save()
    return JsonResponse({'status': 'ok'})

def and_userhome_post(request):
    cat_obj = category.objects.all()
    res = []
    for i in cat_obj:
        d = {'id': i.id, 'cat_name': i.cat_name, 'cat_img': i.image }
        res.append(d)
    return JsonResponse({'status': 'ok', 'data': res})

def and_view_productmore_post(request):
    cat_id=request.POST['cat_id']
    r=category.objects.get(pk=cat_id)
    p_obj=product.objects.filter(PRODUCT_CATEGORY_id=r.id)
    res = []
    for i in p_obj:
        d = {'id': i.id, 'p_name': i.product_name,'rate': i.product_rate,'image':i.image}
        res.append(d)
    return JsonResponse({'status': 'ok', 'data': res})

def and_view_productdetails_post(request):
    p_id=request.POST['p_id']
    i = product.objects.get(pk=p_id)
    offer_obj=offer.objects.filter(PRODUCT_ID=i)
    ar=[]
    if offer_obj.exists():
        off_stat="yes"
        for ff in offer_obj:
            d={'qty1':ff.quantity_1,'qty2':ff.quantity_2,'discount':ff.discount}
            ar.append(d)
    else:
        off_stat="no"
    print(off_stat)
    return JsonResponse({'status': 'ok','off_stat': off_stat,'data': ar, 'p_name': i.product_name, 'rate': i.product_rate, 'image': i.image,'shop_info':i.SHOP_ID.shop_name + "\n" + i.SHOP_ID.place})


def and_calc_discount(request):
    p_id=request.POST['p_id']
    qty=request.POST['qty']
    qty=int(qty)

    offer_obj=offer.objects.filter(PRODUCT_ID_id=p_id)
    for i in offer_obj:
        if int(i.quantity_1)<int(qty) and int(i.quantity_2)>int(qty):
            print(qty,i.discount)
            total=float(qty)*float(i.PRODUCT_ID.product_rate)
            tot_disc=total*float(i.discount)/100
            print(total,tot_disc)
            t_amount=total-tot_disc
            return JsonResponse({'status': 'ok','t_amount': t_amount})
    else:
        print("no")
        return JsonResponse({'status':'no'})

def product_view(request):
    p_obj=product.objects.all().order_by('-id')
    res = []
    for i in p_obj:
        d = {'id': i.id, 'p_name': i.product_name, 'rate': i.product_rate, 'image': i.image,'category':i.PRODUCT_CATEGORY.cat_name,'shop_id':i.SHOP_ID.id}
        res.append(d)

    return JsonResponse({'status': 'ok', 'data':res})

def and_product_search(request):
    p_name=request.POST['p_name']
    p_obj=product.objects.filter(product_name__contains=p_name)
    res = []
    for i in p_obj:
        d = {'id': i.id, 'p_name': i.product_name, 'rate': i.product_rate, 'image': i.image,'category':i.PRODUCT_CATEGORY.cat_name,'shop_id':i.SHOP_ID.id}
        res.append(d)

    return JsonResponse({'status': 'ok', 'data':res})

def and_viewoffers_post(request):
    o_obj=offer.objects.all().order_by('-id')
    res=[]
    for i in o_obj:
        d={'qty1':i.quantity_1,'qty2':i.quantity_2,'discount':i.discount,'shop_info':i.PRODUCT_ID.SHOP_ID.shop_name,
           'p_name':i.PRODUCT_ID.product_name,'pid':i.PRODUCT_ID_id}
        res.append(d)
    return JsonResponse({'status': 'ok', 'data': res})


def and_buyer_bill(request):
    o_id=request.POST['order_id']
    print("OOO ",o_id)
    ordersub_obj=order_sub.objects.filter(ORDER_ID_id=o_id)
    res=[]
    total=0
    payable=0
    savings=0
    for i in ordersub_obj:
        amount=float(i.PRODUCT_ID.product_rate)*float(i.quantity)
        lobj = offer.objects.filter(PRODUCT_ID=i.PRODUCT_ID_id)

        disc = 0
        for j in lobj:
            qt1 = j.quantity_1
            qt2 = j.quantity_2
            qw = i.quantity

            if int(qw) >= int(qt1) and int(qw) <= int(qt2):
                disc = j.discount
                break
        total = total + float(amount)

        tot_disc = amount * float(disc) / 100
        # print("hhhh  ",amount, tot_disc)
        t_amount = amount - tot_disc
        print(t_amount)
        payable = payable + t_amount
        print("pppp", payable)
        savings=savings+tot_disc

        d={
            "product_name":i.PRODUCT_ID.product_name,
            "product_price":i.PRODUCT_ID.product_rate,
            "product_quantity":i.quantity,
            "amount":amount,
            "disc":tot_disc,
            "offer_amount":t_amount
        }
        res.append(d)
    data2={}
    order_obj=orders.objects.get(id=o_id)
    data2['total']=total
    data2['payable']=payable
    data2['order_id']=o_id
    data2['email']= order_obj.SHOP_ID.email
    data2['phone']= order_obj.SHOP_ID.phone
    data2['name']= order_obj.SHOP_ID.shop_name
    data2['date']= order_obj.date
    data2['savings']= savings
    from .create_pdf import make_pdf
    mp=make_pdf(res, data2)
    mp.start_Create()

    return JsonResponse({'status': 'ok'})



#######android deliveryboy

def and_delb_viewassignedorders_post(request):
   db_id=request.POST['db_id']
   print("dbid",db_id)
   ordasn_obj = order_assign.objects.filter( Q(status='pending')|Q(status='picked'),DELBOY_ID_id=db_id).order_by('id')
   res = []

   for i in ordasn_obj:
       d = {'date': i.date, 'id':i.id,
            'shop_info':i.ORDER_ID.SHOP_ID.shop_name+"\n"+i.ORDER_ID.SHOP_ID.place+"\n"+i.ORDER_ID.SHOP_ID.phone+"\n"+
                         i.ORDER_ID.SHOP_ID.email,'buyer_info':i.ORDER_ID.BUYER_ID.buyer_name+"\n"+i.ORDER_ID.BUYER_ID.house_no_name+
                         "\n"+i.ORDER_ID.BUYER_ID.place+", "+i.ORDER_ID.BUYER_ID.post+", "+i.ORDER_ID.BUYER_ID.pin+
                         "\n"+i.ORDER_ID.BUYER_ID.phone+"\n"+i.ORDER_ID.BUYER_ID.email}
       res.append(d)
   return JsonResponse({'status': 'ok','data': res})

def and_delb_more_viewassignedorders_post(request):
    oa_id = request.POST['oa_id']
    print(oa_id)
    i = order_assign.objects.get(id=oa_id)

    res=[]
    ordsub_obj=order_sub.objects.filter(ORDER_ID=i.ORDER_ID)
    for j in ordsub_obj:
        p={'product_name':j.PRODUCT_ID.product_name,'quantity':j.quantity, 'image':j.PRODUCT_ID.image}
        res.append(p)
    return JsonResponse({'status': 'ok', 'date': i.date, 'del_status':i.status,
         'shop_info': i.ORDER_ID.SHOP_ID.shop_name + "\n" + i.ORDER_ID.SHOP_ID.place + "\n" + i.ORDER_ID.SHOP_ID.phone + "\n" +
                      i.ORDER_ID.SHOP_ID.email,
         'buyer_info': i.ORDER_ID.BUYER_ID.buyer_name + "\n" + i.ORDER_ID.BUYER_ID.house_no_name +
                       "\n" + i.ORDER_ID.BUYER_ID.place + "\n" + i.ORDER_ID.BUYER_ID.post + "\n" + i.ORDER_ID.BUYER_ID.pin +
                       "\n" + i.ORDER_ID.BUYER_ID.phone + "\n" + i.ORDER_ID.BUYER_ID.email, 'data': res})



def and_updatedelivery_post(request):
    oa_id=request.POST['oa_id']
    status=request.POST['status']
    i=order_assign.objects.get(id=oa_id)
    i.status=status
    i.save()
    assign_obj=order_assign.objects.get(id=oa_id)
    ###
    email=i.ORDER_ID.BUYER_ID.email
    del_boy_name=i.DELBOY_ID.delboy_name
    del_boy_phn=i.DELBOY_ID.phone
    order_id=i.ORDER_ID
    order_sub_obj=order_sub.objects.filter(ORDER_ID=order_id)
    res=[]
    for i in order_sub_obj:
        res.append(i.PRODUCT_ID.product_name)
    p_names=", ".join(res)
    ###
    import smtplib
    s = smtplib.SMTP(host='smtp.gmail.com', port=587)
    s.starttls()
    s.login("shopping.app.2k21@gmail.com", "7994755364")
    msg = MIMEMultipart()  # create a message.........."
    msg['From'] = "shopping.app.2k21@gmail.com"
    msg['To'] = email
    msg['Subject'] = "ORDER STATUS"
    body = "Your order for "+p_names+" has been "+status+" by our delivery boy.\nStaff name :" + del_boy_name+"\nPhone : "+del_boy_phn
    msg.attach(MIMEText(body, 'plain'))
    s.send_message(msg)
    return JsonResponse({'status': 'ok'})

def and_deliveryboy_profile(request):
    db_id=request.POST['db_id']
    i=delivery_boy.objects.get(id=db_id)
    # d = {'id': i.id, 'delboy_name': i.delboy_name, 'house': i.house_no_name, 'place': i.place,'post': i.post,'pincode': i.pincode,
    #          'phone': i.phone,'email': i.email,'image': i.image,}
    # print(d)
    return JsonResponse({'status': 'ok','id': i.id, 'delboy_name': i.delboy_name, 'house': i.house_no_name, 'place': i.place,'post': i.post,'pincode': i.pincode,
             'phone': i.phone,'email': i.email,'image': i.image})

def update_location(request):
    db_id=request.POST['db_id']
    latitude=request.POST['latitude']
    longitude=request.POST['longitude']
    curdate=datetime.datetime.now().date()
    curtime=datetime.datetime.now().time()
    curtime=str(curtime).split(".")[0]
    loc_obj=location.objects.get(DELIVERY_ID_id=db_id)
    loc_obj.latitude=latitude
    loc_obj.longitude=longitude
    loc_obj.date=curdate
    loc_obj.time=curtime
    loc_obj.save()
    return JsonResponse({'status': 'ok'})

def and_delboy_ordernotification(request):
   db_id=request.POST['db_id']
   last_nid=request.POST['last_nid']    #last notification id
   print("dbid",db_id, last_nid)
   ordasn_obj = order_assign.objects.filter(DELBOY_ID_id=db_id,id__gt=last_nid)
   res=[]
   if ordasn_obj.exists():
       i=ordasn_obj[0]
       d = {'date': i.date, 'id':i.id,
            'shop_info':i.ORDER_ID.SHOP_ID.shop_name}
       res.append(d)
       return JsonResponse({'status': 'ok','data': res})
   else:
       return JsonResponse({'status': 'no'})



def and_forgot_password(request):
    email=request.POST['email']
    log_obj=login.objects.filter(username=email)
    if log_obj.exists():
        log_obj=log_obj[0]
        import smtplib
        s = smtplib.SMTP(host='smtp.gmail.com', port=587)
        s.starttls()
        s.login("shopping.app.2k21@gmail.com", "7994755364")
        msg = MIMEMultipart()  # create a message...... ...."
        msg['From'] = "shopping.app.2k21@gmail.com"
        msg['To'] = email
        msg['Subject'] = "Password for SHOPPING APP"
        body = "Your password for  SHOPPING APP is " + log_obj.password
        msg.attach(MIMEText(body, 'plain'))
        s.send_message(msg)
        return JsonResponse({'status': 'ok'})
    else:
        return JsonResponse({'status':'no'})
#
# #passin values through url
# def fun1(request, nm):
#     return HttpResponse("Good morning "+nm)
# def num(request, no):
#
#     return HttpResponse("cube of "+str(no)+"="+str(no*no*no))
# def largest(request, n1, n2):
#     if(n1>n2):
#         return  HttpResponse(str(n1) + " is greater")
#     else:
#         return HttpResponse(str(n2) + " is greater")
# def enter_no(request):
#     return render(request,"enter_no.html")
#
#
# def submit(request):
#     a=request.POST['txt']
#     print(a)
#     return render(request,"enter_no.html")
#
# def first_get(request):
#     return render(request,"first.html")
#
# def first_post(request):
#     f=request.POST['textfield']
#     l=request.POST['textfield2']
#     data={"fname":f,"lname":l}
#     return render(request,"second.html",{"data":data})
#_In

def ab(request):
    return render(request, "adminindex.html")

