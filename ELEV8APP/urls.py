from django.urls import path
from .import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('',views.home,name='home'),
    path('content/<int:post_id>', views.content,name='content'),
    path('edit/',views.edit,name='edit'),
    path('email/',views.email,name='email'),
    path('profile/',views.profile,name='profile'),
    path('edit_task/',views.edit_task,name='edit_task'),
    path('signup/',views.signup,name='signup')

]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)