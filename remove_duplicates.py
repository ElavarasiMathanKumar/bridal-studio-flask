# remove_duplicates.py

from app import create_app, db
from app.models import GalleryImage

# Create the Flask app using your factory
app = create_app()

# Activate the application context
with app.app_context():

    print("Checking for duplicate gallery images...")

    seen = set()
    duplicates = []

    # Loop through all gallery images
    for img in GalleryImage.query.all():
        if img.image_filename in seen:
            duplicates.append(img)
        else:
            seen.add(img.image_filename)

    # Delete duplicates
    for d in duplicates:
        print(f"Deleting duplicate: {d.image_filename} (ID: {d.id})")
        db.session.delete(d)

    db.session.commit()

    print("✅ Duplicate gallery images removed successfully!")
    print(f"✅ Total duplicates deleted: {len(duplicates)}")