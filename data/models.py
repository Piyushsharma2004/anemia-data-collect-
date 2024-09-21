from django.db import models
import base64
from django.core.files.base import ContentFile

# Create your models here.
class Allimage(models.Model):
    patient_id = models.CharField(max_length=200)
    nails = models.ImageField(upload_to="data/nails", null=True)
    palm = models.ImageField(upload_to="data/palm", null=True)
    full = models.ImageField(upload_to="data/full", null=True)
    eye = models.ImageField(upload_to="data/eye", null=True)

    def save_image_from_data(self, data, imgtype):
        # Decode the base64 image data
        format, imgstr = data.split(';base64,')
        ext = format.split('/')[-1]
        img_data = ContentFile(base64.b64decode(imgstr), name=f"{self.patient_id}.{ext}")

        # Save the image to the model field
        if imgtype == "nails":
            self.nails.save(f"{self.patient_id}.{ext}", img_data, save=True)
        elif imgtype == "palm":
            self.palm.save(f"{self.patient_id}.{ext}", img_data, save=True)
        elif imgtype == "full":
            self.full.save(f"{self.patient_id}.{ext}", img_data, save=True)
        elif imgtype == "eye":
            self.eye.save(f"{self.patient_id}.{ext}", img_data, save=True)

    def __str__(self) -> str:
        return self.patient_id