
# A very simple Flask Hello World app for you to get started with...

from flask import Flask,request
from PIL import Image
from io import BytesIO
import base64

app = Flask(__name__)

@app.route('/',methods=['GET','POST'])
def hello_world():
    data = request.get_json()
    img1 =data["img1"].encode('UTF-8')
    img2=data["img2"].encode('UTF-8')
    def img_save(img,name):
        image = Image.open(BytesIO(base64.b64decode(img)))
        image.save("mysite/%s.png"%name, "PNG")
    img_save(img1,"img1")
    img_save(img2,"img2")

#    a=df.verify("img1.png","img1.png")

    return str(type(img1))


