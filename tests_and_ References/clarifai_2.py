from clarifai.rest import ClarifaiApp, Image as ClImage, Video as vid
##from clarifai.rest import Image as ClImage
##from clarifai.rest import Video as vid


app = ClarifaiApp()
model = app.models.get('general-v1.3')
##response = model.predict_by_url(url='https://samples.clarifai.com/metro-north.jpg')
##
##concepts = response['outputs'][0]['data']['concepts']
##for concept in concepts:
##    print(concept['name'], concept['value'])

# Note: Store the API_key in the config file via terminal using coomand clarifai config...

image = ClImage(file_obj=open('/home/raja/Pictures/#fest_pics/DSC01174.JPG', 'rb'))
pre = model.predict([image]);

print(pre);

#Video siize should notexceed 10 MB...for morw than 10 MB just slice videos in patrs of 10 MB each.... 

##video = vid(filename = "/home/raja/Videos/Jerry's_face_expression_chat_no.4_Screencast 2017-08-13 23:41:11.mp4");
##pre_vid = model.predict([video]);

##print(pre_vid);
