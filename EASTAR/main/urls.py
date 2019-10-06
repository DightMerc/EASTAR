from django.urls import path, re_path, include
from .views import Base, About, Values, Technology, Contacts, TechnologiesView
# from .views import temp_order, getTempOrder, removeProduct, changeAmount, CartShow
# from .views import discounts_view, vacancy_view, blog_view, blog_view_detailed, contact_view, about_view, newOrderView, AdminPanelView, AdminPanelViewSingle, orderCountView, getOrderView,url_redirect, toggleOrder_view, closeOrder_view, archievedordersView, AdminPanelViewArchievedSingle, setOrderState, getOrderState

urlpatterns = [
    path('', Base, name='base_view'),
    path('about/', About, name='about_view'),
    path('values/', Values, name='values_view'),
    path('technology/', Technology, name='tech_view'),
    path('technology/<int:pk>/', TechnologiesView, name='techs_view'),
    path('contacts/', Contacts, name='contact_view'),



    # path('temp/<int:pk>/', temp_order, name='tmp_view'),
    # path('getmytemp/', getTempOrder, name='tmp_get'),
    # path('remove/', removeProduct, name='rm_prod'),
    # path('change_amount/', changeAmount, name='rm_prod'),
    # path('cart/', CartShow, name='show_cart'),
    # path('cart/getmytemp/', getTempOrder, name='tmp_get'),
    # path('cart/remove/', removeProduct, name='rm_prod'),
    # path('cart/change_amount/', changeAmount, name='rm_prod'),
    # path('cart/temp/<int:pk>/', temp_order, name='tmp_view'),

    # path('discounts/', discounts_view, name='dsc_view'),
    # path('vacancy/<int:pk>/', vacancy_view, name='vcn_view'),
    # path('vacancy/', url_redirect, name='blg_view'),

    
    # path('blog/', url_redirect, name='blg_view'),
    # path('blog/<int:pk>/', blog_view, name='blg_view'),
    # path('blog/<int:pk>/detail/', blog_view_detailed, name='blg_view'),

    # path('contact/', contact_view, name='dsc_view'),
    # path('about/', about_view, name='dsc_view'),

    # re_path('panel/', include('trivial_dummy_admin.urls')),

    # path('cart/new_order/', newOrderView, name='newOrderView'),

    # path('admin_panel/<int:pk>/', AdminPanelView, name='admin_panel'),
    # path('admin_panel/', url_redirect, name='admin_panel'),

    # path('admin_panel/<int:pk>/detail/', AdminPanelViewSingle, name='admin_panel2'),
    # path('admin_panel/count/', orderCountView, name='admin_panel3'),
    # path('admin_panel/archieved/<int:pk>/', archievedordersView, name='admin_panel7'),
    # path('admin_panel/archieved/<int:pk>/detail/', AdminPanelViewArchievedSingle, name='admin_panel8'),



    # path('get_order/<int:pk>/', getOrderView, name='admin_panel4'),

    # path('order_toggle/<int:pk>/', toggleOrder_view, name='admin_panel5'),
    # path('order_set_state/<int:pk>/', setOrderState, name='admin_panel7'),
    # path('get_state/<int:pk>/', getOrderState, name='admin_panel8'),


    # path('close_order/<int:pk>/', closeOrder_view, name='admin_panel6'),


    
]