import paho.mqtt.client as mqtt
import shortid
import json
import conf
import values


def createAE(acpi=None):
    req_message = {}
    req_message['m2m:rqp'] = {}
    req_message['m2m:rqp']['op'] = 1  # create
    req_message['m2m:rqp']['to'] = conf.ae.parent
    req_message['m2m:rqp']['fr'] = conf.ae.id
    req_message['m2m:rqp']['rqi'] = shortid.generate()
    req_message['m2m:rqp']['ty'] = 2  # ae
    req_message['m2m:rqp']['pc'] = {}
    req_message['m2m:rqp']['pc']['m2m:ae'] = {}
    req_message['m2m:rqp']['pc']['m2m:ae']['rn'] = conf.ae.name
    req_message['m2m:rqp']['pc']['m2m:ae']['api'] = conf.ae.appid
    req_message['m2m:rqp']['pc']['m2m:ae']['rr'] = True
    if acpi != None:
        req_message['m2m:rqp']['pc']['m2m:ae']['acpi'] = [acpi]

    values.mqttc.publish(values.req_topic, json.dumps(req_message['m2m:rqp']))
    print(values.req_topic + ' (json) ' + json.dumps(req_message['m2m:rqp']) + ' ---->', end='\n\n')

    return req_message['m2m:rqp']['rqi']


def retrieveAE():
    req_message = {}
    req_message['m2m:rqp'] = {}
    req_message['m2m:rqp']['op'] = 2  # retrieve
    req_message['m2m:rqp']['to'] = conf.ae.parent + '/' + conf.ae.name
    req_message['m2m:rqp']['fr'] = conf.ae.id
    req_message['m2m:rqp']['rqi'] = shortid.generate()
    req_message['m2m:rqp']['pc'] = {}

    values.mqttc.publish(values.req_topic, json.dumps(req_message['m2m:rqp']))
    print(values.req_topic + ' (json) ' + json.dumps(req_message['m2m:rqp']) + ' ---->', end='\n\n')

    return req_message['m2m:rqp']['rqi']


def deleteAE():
    req_message = {}
    req_message['m2m:rqp'] = {}
    req_message['m2m:rqp']['op'] = 4  # delete
    req_message['m2m:rqp']['to'] = conf.ae.parent + '/' + conf.ae.name
    req_message['m2m:rqp']['fr'] = conf.ae.id
    req_message['m2m:rqp']['rqi'] = shortid.generate()
    req_message['m2m:rqp']['pc'] = {}

    values.mqttc.publish(values.req_topic, json.dumps(req_message['m2m:rqp']))
    print(values.req_topic + ' (json) ' + json.dumps(req_message['m2m:rqp']) + ' ---->', end='\n\n')

    return req_message['m2m:rqp']['rqi']


def createCNT(count):
    req_message = {}
    req_message['m2m:rqp'] = {}
    req_message['m2m:rqp']['op'] = 1  # create
    req_message['m2m:rqp']['to'] = conf.cnt[count]['parent']
    req_message['m2m:rqp']['fr'] = conf.ae.id
    req_message['m2m:rqp']['rqi'] = shortid.generate()
    req_message['m2m:rqp']['ty'] = 3  # cnt
    req_message['m2m:rqp']['pc'] = {}
    req_message['m2m:rqp']['pc']['m2m:cnt'] = {}
    req_message['m2m:rqp']['pc']['m2m:cnt']['rn'] = conf.cnt[count]['name']
    req_message['m2m:rqp']['pc']['m2m:cnt']['lbl'] = []
    req_message['m2m:rqp']['pc']['m2m:cnt']['lbl'].append(conf.cnt[count]['name'])

    values.mqttc.publish(values.req_topic, json.dumps(req_message['m2m:rqp']))
    print(values.req_topic + ' (json) ' + json.dumps(req_message['m2m:rqp']) + ' ---->', end='\n\n')

    return req_message['m2m:rqp']['rqi']


def retrieveCNT(count):
    req_message = {}
    req_message['m2m:rqp'] = {}
    req_message['m2m:rqp']['op'] = 2  # retrieve
    req_message['m2m:rqp']['to'] = conf.cnt[count]['parent'] + '/' + conf.cnt[count]['name']
    req_message['m2m:rqp']['fr'] = conf.ae.id
    req_message['m2m:rqp']['rqi'] = shortid.generate()
    req_message['m2m:rqp']['pc'] = {}

    values.mqttc.publish(values.req_topic, json.dumps(req_message['m2m:rqp']))
    print(values.req_topic + ' (json) ' + json.dumps(req_message['m2m:rqp']) + ' ---->', end='\n\n')

    return req_message['m2m:rqp']['rqi']


def deleteCNT(count):
    req_message = {}
    req_message['m2m:rqp'] = {}
    req_message['m2m:rqp']['op'] = 4  # retrieve
    req_message['m2m:rqp']['to'] = conf.cnt[count]['parent'] + '/' + conf.cnt[count]['name']
    req_message['m2m:rqp']['fr'] = conf.ae.id
    req_message['m2m:rqp']['rqi'] = shortid.generate()
    req_message['m2m:rqp']['pc'] = {}

    values.mqttc.publish(values.req_topic, json.dumps(req_message['m2m:rqp']))
    print(values.req_topic + ' (json) ' + json.dumps(req_message['m2m:rqp']) + ' ---->', end='\n\n')

    return req_message['m2m:rqp']['rqi']


def createCIN(count, content):
    req_message = {}
    req_message['m2m:rqp'] = {}
    req_message['m2m:rqp']['op'] = 1  # create
    req_message['m2m:rqp']['to'] = conf.cnt[count]['parent'] + '/' + conf.cnt[count]['name']
    req_message['m2m:rqp']['fr'] = conf.ae.id
    req_message['m2m:rqp']['rqi'] = shortid.generate()
    req_message['m2m:rqp']['ty'] = '4'  # cin
    req_message['m2m:rqp']['pc'] = {}
    req_message['m2m:rqp']['pc']['m2m:cin'] = {}
    req_message['m2m:rqp']['pc']['m2m:cin']['con'] = content

    values.mqttc.publish(values.req_topic, json.dumps(req_message['m2m:rqp']))
    print(values.req_topic + ' (json) ' + json.dumps(req_message['m2m:rqp']) + ' ---->', end='\n\n')

    return req_message['m2m:rqp']['rqi']


def retrieveCIN(count):
    req_message = {}
    req_message['m2m:rqp'] = {}
    req_message['m2m:rqp']['op'] = 2  # retrieve
    req_message['m2m:rqp']['to'] = conf.cnt[count]['parent'] + '/' + conf.cnt[count]['name'] + '/latest'
    req_message['m2m:rqp']['fr'] = conf.ae.id
    req_message['m2m:rqp']['rqi'] = shortid.generate()
    req_message['m2m:rqp']['pc'] = {}

    values.mqttc.publish(values.req_topic, json.dumps(req_message['m2m:rqp']))
    print(values.req_topic + ' (json) ' + json.dumps(req_message['m2m:rqp']) + ' ---->', end='\n\n')

    return req_message['m2m:rqp']['rqi']


def createSUB(count):
    req_message = {}
    req_message['m2m:rqp'] = {}
    req_message['m2m:rqp']['op'] = 1  # create
    req_message['m2m:rqp']['to'] = conf.sub[count]['parent']
    req_message['m2m:rqp']['fr'] = conf.ae.id
    req_message['m2m:rqp']['rqi'] = shortid.generate()
    req_message['m2m:rqp']['ty'] = 23  # sub
    req_message['m2m:rqp']['pc'] = {}
    req_message['m2m:rqp']['pc']['m2m:sub'] = {}
    req_message['m2m:rqp']['pc']['m2m:sub']['rn'] = conf.sub[count]['name']
    req_message['m2m:rqp']['pc']['m2m:sub']['enc'] = {}
    req_message['m2m:rqp']['pc']['m2m:sub']['enc']['net'] = []
    req_message['m2m:rqp']['pc']['m2m:sub']['enc']['net'].append(3)
    req_message['m2m:rqp']['pc']['m2m:sub']['nu'] = []
    req_message['m2m:rqp']['pc']['m2m:sub']['nu'].append(conf.sub[count]['nu'])
    req_message['m2m:rqp']['pc']['m2m:sub']['nct'] = 2

    values.mqttc.publish(values.req_topic, json.dumps(req_message['m2m:rqp']))
    print(values.req_topic + ' (json) ' + json.dumps(req_message['m2m:rqp']) + ' ---->', end='\n\n')

    return req_message['m2m:rqp']['rqi']


def deleteSUB(count):
    req_message = {}
    req_message['m2m:rqp'] = {}
    req_message['m2m:rqp']['op'] = 4  # delete
    req_message['m2m:rqp']['to'] = conf.sub[count]['parent'] + '/' + conf.sub[count]['name']
    req_message['m2m:rqp']['fr'] = conf.ae.id
    req_message['m2m:rqp']['rqi'] = shortid.generate()
    req_message['m2m:rqp']['pc'] = {}

    values.mqttc.publish(values.req_topic, json.dumps(req_message['m2m:rqp']))
    print(values.req_topic + ' (json) ' + json.dumps(req_message['m2m:rqp']) + ' ---->', end='\n\n')

    return req_message['m2m:rqp']['rqi']


# TODO: Add acp method
def createACP(count):
    req_message = {}
    req_message['m2m:rqp'] = {}
    req_message['m2m:rqp']['op'] = 1
    req_message['m2m:rqp']['to'] = '/' + conf.cse.id
    req_message['m2m:rqp']['fr'] = conf.ae.id
    req_message['m2m:rqp']['rqi'] = shortid.generate()
    req_message['m2m:rqp']['ty'] = 1  #acp
    req_message['m2m:rqp']['pc'] = {}
    req_message['m2m:rqp']['pc']['m2m:acp'] = {}
    req_message['m2m:rqp']['pc']['m2m:acp']['rn'] = conf.acp[count]['name']
    req_message['m2m:rqp']['pc']['m2m:acp']['pv'] = {}
    req_message['m2m:rqp']['pc']['m2m:acp']['pv']['acr'] = [{
        'acor': conf.acp[count]['target'],
        'acop': conf.acp[count]['policy']
    }]
    # req_message['m2m:rqp']['pc']['m2m:acp']['pv']['acr']['acor'] = conf.acp[count]['target']
    # req_message['m2m:rqp']['pc']['m2m:acp']['pv']['acr']['acop'] = conf.acp[count]['policy']
    req_message['m2m:rqp']['pc']['m2m:acp']['pvs'] = {}
    req_message['m2m:rqp']['pc']['m2m:acp']['pvs']['acr'] = [{
        'acor': conf.acp[count]['selfTarget'],
        'acop': conf.acp[count]['selfPolicy']
    }]
    # req_message['m2m:rqp']['pc']['m2m:acp']['pvs']['acr']['acor'] = conf.acp[count]['selfTarget']
    # req_message['m2m:rqp']['pc']['m2m:acp']['pvs']['acr']['acop'] = conf.acp[count]['selfPolicy']

    values.mqttc.publish(values.req_topic, json.dumps(req_message['m2m:rqp']))
    print(values.req_topic + ' (json) ' + json.dumps(req_message['m2m:rqp']) + ' ---->', end='\n\n')

    return req_message['m2m:rqp']['rqi']


def retrieveACP(count):
    req_message = {}
    req_message['m2m:rqp'] = {}
    req_message['m2m:rqp']['op'] = 2  # retrieve
    req_message['m2m:rqp']['to'] = conf.acp[count]['location']
    req_message['m2m:rqp']['fr'] = conf.ae.id
    req_message['m2m:rqp']['rqi'] = shortid.generate()
    req_message['m2m:rqp']['pc'] = {}

    values.mqttc.publish(values.req_topic, json.dumps(req_message['m2m:rqp']))
    print(values.req_topic + ' (json) ' + json.dumps(req_message['m2m:rqp']) + ' ---->', end='\n\n')

    return req_message['m2m:rqp']['rqi']


def updateACP():
    pass


def discovery(target, ty):
    req_message = {}
    req_message['m2m:rqp'] = {}
    req_message['m2m:rqp']['op'] = 2  # retrieve
    req_message['m2m:rqp']['to'] = target + '?fu=1&ty=' + str(ty)
    req_message['m2m:rqp']['fr'] = conf.ae.id
    req_message['m2m:rqp']['rqi'] = shortid.generate()
    req_message['m2m:rqp']['pc'] = {}

    values.mqttc.publish(values.req_topic, json.dumps(req_message['m2m:rqp']))
    print(values.req_topic + ' (json) ' + json.dumps(req_message['m2m:rqp']) + ' ---->', end='\n\n')

    return req_message['m2m:rqp']['rqi']
