
from django.urls import path
from . import views

urlpatterns = [
    path('login_load/', views.login_load),
    path('logout/', views.logout),
    path('admin_add_category_load/', views.admin_add_category_load),
    path('admin_edit_category_load/<c_id>', views.admin_edit_category_load),
    path('admin_view_category_load/', views.admin_view_category_load),
    path('delete_category/<c_id>', views.delete_category),
    path('shopreg_load/', views.shopreg_load),
    path('admin_view_shopreg_load/', views.admin_view_shopreg_load),
    path('approve_shopreg/<log_id>', views.approve_shopreg),
    path('reject_shopreg/<log_id>', views.reject_shopreg),
    path('admin_Approvedshops_load/', views.admin_Approvedshops_load),
    path('admin_Rejectedshops_load/', views.admin_Rejectedshops_load),
    path('admin_Add_deliveryboy_load/', views.admin_Add_deliveryboy_load),
    path('admin_Edit_deliveryboy_load/<d_id>', views.admin_Edit_deliveryboy_load),
    path('admin_view_deliveryboy_load/',views.admin_view_deliveryboy_load),
    path('delete_delboy/<d_id>',views.delete_delboy),
    path('forgot_password_load/',views.forgot_password_load),
    path('admin_rating_load/<shop_id>',views.admin_rating_load),

    ###########admin post
    path('login_post/',views.login_post),
    path('forgot_password_post/',views.forgot_password_post),
    path('shopreg_post/', views.shopreg_post),
    path('admin_add_category_post/',views.admin_add_category_post),
    path('admin_edit_category_post/',views.admin_edit_category_post),
    path('admin_view_category_post/',views.admin_view_category_post),
    path('admin_Approvedshops_post/',views.admin_Approvedshops_post),
    path('admin_Rejectedshops_post/',views.admin_Rejectedshops_post),
    path('admin_Add_deliveryboy_post/',views.admin_Add_deliveryboy_post),
    path('admin_Edit_deliveryboy_post/',views.admin_Edit_deliveryboy_post),
    path('admin_view_shopreg_post/',views.admin_view_shopreg_post),
    path('admin_view_deliveryboy_post/', views.admin_view_deliveryboy_post),


    ##### Seller load

    path('seller_viewprofile_load/',views.seller_viewprofile_load),
    path('seller_editprofile_load/', views.seller_editprofile_load),
    path('seller_addproduct_load/', views.seller_addproduct_load),
    path('seller_editproduct_load/<p_id>', views.seller_editproduct_load),
    path('seller_viewproduct_load/', views.seller_viewproduct_load),
    path('seller_viewproduct_post/', views.seller_viewproduct_post),
    path('remove_product/<p_id>', views.remove_product),
    path('seller_view_productorder_load/', views.seller_view_productorder_load),
    path('seller_more_productoreders_load/<o_id>', views.seller_more_productoreders_load),
    path('seller_assignorder_delboy_load/<o_id>', views.seller_assignorder_delboy_load),
    path('seller_view_deliverystatus_load/', views.seller_view_deliverystatus_load),
    # path('more_deliverystatus/<o_id>', views.seller_view_deliverystatus_load),
    path('seller_view_buyer_rating_load/', views.seller_view_buyer_rating_load),
    path('seller_view_paymentreports_load/', views.seller_view_paymentreports_load),
    path('seller_view_paymentreports_post/', views.seller_view_paymentreports_post),
    path('seller_add_offers_load/<id>', views.seller_add_offers_load),
    path('seller_view_offers_load/<id>', views.seller_view_offers_load),
    path('seller_edit_offers/<oid>', views.seller_edit_offers),
    path('seller_delete_offers/<oid>', views.seller_delete_offers),
    path('seller_billpreview/<o_id>', views.seller_billpreview),

    ########seler post

    path('seller_editprofile_post/', views.seller_editprofile_post),
    path('seller_addproduct_post/', views.seller_addproduct_post),
    path('seller_editproduct_post/', views.seller_editproduct_post),
    path('seller_view_productorder_post/', views.seller_view_productorder_post),
    path('seller_assignorder_delboy_post/', views.seller_assignorder_delboy_post),
    path('seller_view_deliverystatus_post/', views.seller_view_deliverystatus_post),
    path('seller_add_product_post/', views.seller_add_product_post),
    path('seller_edit_offers_post/', views.seller_edit_offers_post),
    path('and_buyer_bill/', views.and_buyer_bill),

    ####home

    path('admin_home_load/', views.admin_home_load),
    path('seller_home_load/', views.seller_home_load),

    ######### android

    path('and_login_post/', views.and_login_post),
    path('and_verify_email/', views.and_verify_email),
    path('and_buyerreg_post/', views.and_buyerreg_post),
    path('and_user_editprofile_post/', views.and_user_editprofile_post),
    path('and_user_viewprofile/', views.and_user_viewprofile),
    path('and_nearestshop_post/', views.and_nearestshop_post),
    path('and_viewshop_rating_post/', views.and_viewshop_rating_post),
    path('view_shopmore_post/', views.view_shopmore_post),
    path('and_addtocart_post/', views.and_addtocart_post),
    path('and_viewfeedback_post/', views.and_viewfeedback_post),
    path('and_viewcart_post/', views.and_viewcart_post),
    path('and_removefromcart_post/', views.and_removefromcart_post),
    path('and_payment_post/', views.and_payment_post),

    # path('and_payment_postby_offer/', views.and_payment_postby_offer),

    path('and_viewandtrack_orders_post/', views.and_viewandtrack_orders_post),
    path('and_vieworder_items_post/', views.and_vieworder_items_post),
    path('and_sendfeedback_post/', views.and_sendfeedback_post),
    path('and_sendrating_post/', views.and_sendrating_post),
    path('and_userhome_post/', views.and_userhome_post),
    path('and_view_productmore_post/', views.and_view_productmore_post),
    path('and_view_productdetails_post/', views.and_view_productdetails_post),
    path('and_calc_discount/', views.and_calc_discount),
    path('product_view/', views.product_view),
    path('and_product_search/', views.and_product_search),
    path('and_viewoffers_post/', views.and_viewoffers_post),

    ########### android delvery boy
    path('and_delb_viewassignedorders_post/', views.and_delb_viewassignedorders_post),
    path('and_delb_more_viewassignedorders_post/', views.and_delb_more_viewassignedorders_post),
    path('and_updatedelivery_post/', views.and_updatedelivery_post),
    path('and_deliveryboy_profile/', views.and_deliveryboy_profile),
    path('update_location/', views.update_location),
    path('and_delboy_ordernotification/', views.and_delboy_ordernotification),


    path('and_forgot_password/', views.and_forgot_password),

    path('ab/', views.ab),



]