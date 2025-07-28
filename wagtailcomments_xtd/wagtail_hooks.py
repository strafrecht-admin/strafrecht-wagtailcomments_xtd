from django.urls import reverse
from wagtailcomments_xtd import urls
from wagtail import hooks
from django.urls import include, path
from wagtail.admin.menu import MenuItem
from django.utils.translation import gettext_lazy as _


@hooks.register('register_admin_urls')
def register_admin_urls():
    return [
        path('comments/', include(urls)),
    ]


@hooks.register('register_admin_menu_item')
def register_styleguide_menu_item():
    return MenuItem(
        _('Comments'),
        reverse('wagtailcomments_xtd_pages'),
        classnames='icon icon-comment',
        order=1000
    )
