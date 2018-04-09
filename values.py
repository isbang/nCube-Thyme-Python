import conf
"""
This code is for global variable
"""

req_topic = '/oneM2M/req/' + conf.ae.id + '/' + conf.cse.id + '/' + conf.ae.bodytype
mqttc = None  # mqtt client
conreq = {}  # noti request
response = {}  # response data
