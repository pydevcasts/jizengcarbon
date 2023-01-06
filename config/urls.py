
from django.contrib import admin
from django.urls import re_path, include,path
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth import views as auth_views



urlpatterns = [
    # re_path(r'^', views.home),
    path(r'admin/', admin.site.urls),
    re_path(r'^accounts/', include('accounts.urls',namespace='accounts')),
    re_path(r'^about/', include('about.urls' ,namespace='about-us')),
    re_path(r'^', include('product.urls')),
    re_path(r'^category/', include('category.urls')),
    re_path(r'^contact/', include('contact.urls')),
    re_path(r'^feedback', include('feedback.urls')),
    re_path(r'^search/', include('search.urls')),
    re_path(r'^tag/', include('tag.urls')),
    re_path(r'^team/', include('team.urls')),
    re_path(r'^social-auth/', include('social_django.urls', namespace='social')),
    re_path(r'^accounts/login/$', auth_views.LoginView.as_view(template_name='frontend/accounts/login.html'), name='login'),
    re_path(r'^accounts/logout/$', auth_views.LogoutView.as_view(), name='logout'),
    re_path(r'^accounts/reset/$',
        auth_views.PasswordResetView.as_view(
            template_name='frontend/accounts/password_reset.html',
            html_email_template_name='frontend/accounts/password_reset_email.html',
            email_template_name='frontend/accounts/password_reset_email.html',
            subject_template_name='frontend/accounts/password_reset_subject.txt'
        ),
        name='password_reset'),
    re_path(r'^accounts/reset/done/$',
        auth_views.PasswordResetDoneView.as_view(template_name='frontend/accounts/password_reset_done.html'),
        name='password_reset_done'),
    re_path(r'^accounts/reset/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$',
        auth_views.PasswordResetConfirmView.as_view(template_name='frontend/accounts/password_reset_confirm.html'),
        name='password_reset_confirm'),
    re_path(r'^accounts/reset/complete/$',
        auth_views.PasswordResetCompleteView.as_view(template_name='frontend/accounts/password_reset_complete.html'),
        name='password_reset_complete'),
    re_path(r'^settings/password/done/$',
        auth_views.PasswordChangeDoneView.as_view(template_name='frontend/accounts/password_change_done.html'),
        name='password_change_done'),


    # re_path(r'^.*\.*', views.pages, name='pages'),   

]
if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
    urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
