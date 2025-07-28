# Wagtail Comments (Updated for Wagtail 6.x)

This module allows you to manage [django-comments-xtd](https://github.com/danirus/django-comments-xtd) comments into the Wagtail admin UI.

**Updated for Wagtail 6.x and Django 5.x compatibility by strafrecht-admin.**

![Screenshot 1](images/pages_list.png)

![Screenshot 2](images/comments_list.png)

## Installation

This is a forked and updated version for modern Wagtail/Django compatibility.

### Requirements
- Wagtail >= 6.0
- Django >= 5.0
- django-comments-xtd >= 2.10.0

### Installation Instructions

1. Install as editable package from this fork:
```bash
pip install -e git+https://github.com/strafrecht-admin/strafrecht-wagtailcomments_xtd.git#egg=wagtailcomments_xtd
```

2. Add `'wagtailcomments_xtd'` to your INSTALLED_APPS

3. No FontAwesome dependency required - uses built-in Wagtail icons

## Changes Made for Wagtail 6.x Compatibility

- Updated imports: `wagtail.wagtailcore` → `wagtail`
- Updated imports: `wagtail.wagtailadmin` → `wagtail.admin`
- Updated imports: `wagtail.wagtailcore.models` → `wagtail.models`
- Updated URL patterns: `django.conf.urls.url` → `django.urls.path`
- Updated URL resolver: `django.core.urlresolvers` → `django.urls`
- Updated translation: `ugettext_lazy` → `gettext_lazy`
- Updated icon: `icon-fa-comments-o` → `icon-comment` (built-in Wagtail icon)
- Removed wagtailfontawesome dependency
- Updated setup.py for modern Python/Django/Wagtail versions

## Original Project

This is a fork of the original [wagtailcomments_xtd](https://github.com/adrienlachaize/wagtailcomments_xtd) by Adrien Lachaize, updated for compatibility with modern Wagtail and Django versions.

