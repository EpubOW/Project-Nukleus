from config import *
from controllers.api_tools.wraplers import *
# from model.abstracts.updated_camera_tools.CameraPictureGetter import *
# from model.data.Camera import Camera
# from model.data.CamSector import CamSector
from model.data.Box import Box
# from tools.FileUtil import FileUtil
import json

@cross_origin
@app.route('/addBox', methods=['POST']) 
@exception_processing
def addBox():
    name = request.json['name']
    description = request.json['description']
    x1 = request.json['x1']
    y1 = request.json['y1']
    x2 = request.json['x2']
    y2 = request.json['y2']

    box = Box(name, description, x1, y1, x2, y2)

    if 'box_id' in request.json:
        box_id = request.json['box_id']
        if type(box_id) is int:
            box = Box.getByID(box_id)
            box.name = name
            box.description = description
            box.x1 = x1
            box.y1 = y1
            box.x2 = x2
            box.y2 = y2
            # print(box.id, box.name, box.description)
    try:
        box.save()
        return {'status': True}
    except Exception as e:
        print(e)
        return {'status': False, 'description': e}
    
@cross_origin
@app.route('/delBox', methods=['POST']) 
@exception_processing
def delBox():
    box_id = request.json['box_id']
    box = Box.getByID(box_id)
    try:
        box.delete()
        return {'status': True}
    except Exception as e:
        print(e)
        return {'status': False, 'description': e}
        