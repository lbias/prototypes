import sys

from django.conf import settings

settings.configure(
    DEBUG=True,
    SECRET_KEY='f#&o4)9ibe=k1ofu696+4rt8#5e73fsf9leuj5@-&$nf4%(#jn',
    ROOT_URLCONF='sitebuilder.urls',
    MIDDLEWARE_CLASSES=(),
    INSTALLED_APPS=(
        'django.contrib.staticfiles',
        'sitebuilder',
    ),
    STATIC_URL='/static/',
)

if __name__ == "__main__":
    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
