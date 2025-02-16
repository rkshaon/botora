import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'blog_site.settings')

import django
django.setup()

from django.utils import timezone

now = timezone.now()
print(now)
