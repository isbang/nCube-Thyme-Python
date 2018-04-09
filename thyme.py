import mqtt_app as app
import mqtt_adn as adn
import values
import conf

import flask_app.app as flask_app


def myNotiAction(key):
    import hashlib
    data = values.conreq[key]
    # adn.createACP()
    cnt = {}
    cnt['parent'] = '/' + conf.cse.name + '/' + conf.ae.name
    cnt['name'] = data['cr']
    conf.cnt.append(cnt)
    adn.createCNT(-1)
    suburl = hashlib.md5(data['con'].encode('utf8')).hexdigest()
    flask_app.addroute(suburl)
    url = 'http://' + conf.ae.host + '/' + suburl
    adn.createCIN(-1, url)


def waitResponse(rqi):
    while not values.response.__contains__(rqi):
        pass


if __name__ == '__main__':
    import threading
    import time
    values.mqttc = app.initMQTT()

    time.sleep(1)

    # adn.retrieveACP()
    # if None:
    #     adn.createACP()

    print("Delete AE")
    rqi = adn.deleteAE()
    waitResponse(rqi)

    print("create AE")
    rqi = adn.createAE()
    waitResponse(rqi)

    print("Delete CNT")
    rqis = []
    for i in range(len(conf.cnt)):
        rqis.append((adn.deleteCNT(i), i))

    print("Create CNT")
    while rqis != []:
        for rqi, idx in rqis:
            if values.response.__contains__(rqi):
                adn.createCNT(idx)
                rqis.remove((rqi, idx))

    rqis = []
    print("Delete SUB")
    for i in range(len(conf.sub)):
        rqis.append((adn.deleteSUB(i), i))

    print("Create SUB")
    while rqis != []:
        for rqi, idx in rqis:
            if values.response.__contains__(rqi):
                adn.createSUB(idx)
                rqis.remove((rqi, idx))

    flag = True

    thread_flask = threading.Thread(
        target=flask_app.app.run, kwargs={
            'host': '0.0.0.0',
            'port': '80',
            'threaded': True
        })
    thread_flask.daemon = True
    thread_flask.start()

    while True:
        for key in list(values.conreq):
            myNotiAction(key)
            values.conreq.__delitem__(key)
