import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "backend.settings")
django.setup()

from django.conf import settings
from django.core.files import File
from store.models import Product

media_products = os.path.join(settings.MEDIA_ROOT, "products")

for product in Product.objects.all():
    if product.image:
        filename = os.path.basename(product.image.name)
        local_path = os.path.join(media_products, filename)

        if os.path.exists(local_path):
            with open(local_path, "rb") as f:
                product.image.save(filename, File(f), save=True)

            print(f"Uploaded: {filename}")
        else:
            print(f"Not found: {filename}")

print("Migration completed!")