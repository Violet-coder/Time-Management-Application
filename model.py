class User:
    def __init__(self, name=None, password=None, salt=None, taskid = None):
        self.name = name
        self.password = password
        self.salt = salt
        self.taskid = taskid

    def toList(self):
        return [self.name, self.email, self.password, self.photo_id]

    def fromList(self, user_info):
        self.name = user_info[0]
        self.password = user_info[1]
        self.salt = user_info[2]


    def getAttrs(self):
        return ('name, email, password','photo_id')

class User_photo:
    def __init__(self, name=None, org_photo=None, thumbnail=None, det_photo=None):
        self.name = name
        self.org_photo = org_photo
        self.thumbnail = thumbnail
        self.det_photo = det_photo