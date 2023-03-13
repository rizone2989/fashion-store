from django.urls import path
from .import views
urlpatterns=[
    path('index/',views.indexpage),
    path('st/',views.student,name='student'),
    path('display/',views.display,name='display'),
    path('img/',views.imagesave,name='imagesave'),
    path('edit/<int:dataid>/',views.editpage, name="editpage"),
    path('update/<int:dataid>/',views.update, name="update"),
    path('deletedata/<int:dataid>/',views.deletedata,name="deletedata"),
    path('addcategory/',views.addcategorypage,name='addcategorypage'),
    path('cat/',views.addcategory,name='addcategory'),
    path('displaycat/',views.displaycategory,name="displaycategory"),
    path('updatecat/<int:dataid>/',views.updatecat,name="updatecategory"),
    path('editcat/<int:dataid>/',views.editcat,name="editcategory"),
    path('deletecat/<int:dataid>/',views.deletecategory,name="deletecategory"),
    path('addproduct/',views.addproduct,name='addproduct'),
    path('displaypro/',views.displayproduct,name='displayproduct'),
    path('savepro/',views.saveproduct,name='saveproduct'),
    path('editpro/<int:dataid>/',views.editpro,name="editproduct"),
    path('updateproduct/<int:dataid>/',views.updatepro, name="updateproduct"),
    path('deletepro/<int:dataid>/',views.deleteproduct,name="deleteproduct")
]