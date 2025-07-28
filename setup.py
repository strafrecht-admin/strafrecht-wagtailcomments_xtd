from setuptools import setup, find_packages


setup(
    name='wagtailcomments_xtd',
    author='Adrien Lachaize (Updated by strafrecht-admin)',
    author_email='adrien.lachaize@gmail.com',
    version='1.0.0',
    url='https://github.com/strafrecht-admin/strafrecht-wagtailcomments_xtd',
    classifiers=[
        "Environment :: Web Environment",
        "Framework :: Django",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        'Topic :: Internet :: WWW/HTTP',
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
    ],
    packages=find_packages(),
    install_requires=[
        "wagtail>=6.0",
        "Django>=5.0",
        "django-comments-xtd>=2.10.0"
    ],
)
