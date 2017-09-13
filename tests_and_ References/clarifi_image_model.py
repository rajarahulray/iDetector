from clarifai.rest import ClarifaiApp
from clarifai.rest import Image as ClImage

app = ClarifaiApp(api_key='{dceaac99f1af4f9495fcefc95747354a}')

model = app.models.get('general-v1.3');
image = ClImage(file_obj=open('/home/raja/Pictures/ACM_ICPC_pics/IMG_20161022_170020.jpg', 'rb'))
model.predict([image]);
