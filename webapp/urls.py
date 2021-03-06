from django.conf.urls.defaults import *
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = patterns('',
    # Login and Logout urls
    url(r'^accounts/login/$', 'django_cas.views.login', name='login'),
    url(r'^accounts/logout/$', 'django_cas.views.logout', name='logout'),
    
    # App Urls
    url(r'^$', 'core.views.index', name='index'),
    url(r'^current$', 'core.views.current_loans', name='current_loans'),
    url(r'^past$', 'core.views.past_loans', name='past_loans'),
    url(r'^user_admin$', 'core.views.user_admin', name='user_admin'),
    url(r'^remove_user/(\d+)$', 'core.views.remove_user', name='remove_user'),
    url(r'^loans/add$', 'core.views.add_loan', name='add_loan'),
    url(r'^loans/(\d+)$', 'core.views.view_loan', name='view_loan'),
    url(r'^person/find$', 'core.views.find_person', name='find_person'),
    url(r'^person/add$', 'core.views.add_person', name='add_person'),
    url(r'^person/(\d+)$', 'core.views.view_person', name='view_person'),
    url(r'^items/description$', 'core.views.item_description', name='item_description'),
    url(r'^loans/(\d+)/return$', 'core.views.return_loan', name='return_loan'),
    url(r'^loans/(\d+)/edit$', 'core.views.edit_loan', name='edit_loan'),
    url(r'^loans/(\d+)/comment$', 'core.views.comment_loan', name='comment_loan'),
    url(r'^loans/(\d+)/print$', 'core.views.print_loan', name='print_loan'),
    url(r'^loans/(\d+)/receipt$', 'core.views.receipt', name='receipt'),
) + staticfiles_urlpatterns()
