import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("PATH to Firebase generated Certificate key")
default_app = firebase_admin.initialize_app(cred, {
	'databaseURL': databaseURL
	})

ref = db.reference("/")

def TubeOnOff(status):
    """ Turn On/Off device using status '0'-> Off '1'-> On"""
    ref.update({'your device nameA':status})

def FanOnOff(status):
    """ Turn On/Off device using status '0'-> Off '1'-> On"""
    ref.update({'your device nameB':status})

def LightOnOff(status):
    """ Turn On/Off device using status '0'-> Off '1'-> On"""
    ref.update({'your device nameC':status})

def GyserOnOff(status):
    """ Turn On/Off device using status '0'-> Off '1'-> On"""
    ref.update({'your device nameD':status})

def AcOnOff(status):
    """ Turn On/Off device using status '0'-> Off '1'-> On"""
    ref.update({'your device nameE':status})

def TVOnOff(status):
    """ Turn On/Off device using status '0'-> Off '1'-> On"""
    ref.update({'your device nameF':status})

def AllOnOff(status):
    """ Turn On/Off all devices using status '0'-> Off '1'-> On"""
    ref.update({'your device nameA':status})
    ref.update({'your device nameB':status})
    ref.update({'your device nameC':status})
    ref.update({'your device nameD':status})
    ref.update({'your device nameE':status})
    ref.update({'your device nameF':status})
    
def ShowStatus():
    """Show running status of all devices"""
    stats = ref.get()
    for key,val in stats.items():
        print("{} -> {}".format(key,val))

