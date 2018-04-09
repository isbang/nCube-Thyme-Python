import mqtt_app as app
import mqtt_adn as adn
import values
import conf


def myNotiAction(rqi):
    print("\nNoti <----")
    print(rqi, ':', values.conreq[rqi])


def waitResponse(rqi):
    while not values.response.__contains__(rqi):
        pass


if __name__ == '__main__':
    import time
    values.mqttc = app.initMQTT()

    time.sleep(1)  # wait for mqtt initializing

    # adn.retrieveACP()
    # if None:
    #     adn.createACP()

    # print("Delete AE")
    # rqi = adn.deleteAE()
    # waitResponse(rqi)

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

    print("Delete SUB")
    rqis = []
    for i in range(len(conf.sub)):
        rqis.append((adn.deleteSUB(i), i))

    print("Create SUB")
    while rqis != []:
        for rqi, idx in rqis:
            if values.response.__contains__(rqi):
                adn.createSUB(idx)
                rqis.remove((rqi, idx))

    # Do your job below here
    while True:
        # # Example1: noti Action handling
        # for key in list(values.conreq):
        #     myNotiAction(key)
        #     values.conreq.__delitem__(key)

        # # Example2: update data each 5 seconds
        # adn.createCIN(1, "SOME_DATA")
        # time.sleep(5)

        pass
