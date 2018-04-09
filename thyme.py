import mqtt_app as app
import mqtt_adn as adn
import values
import conf


def waitResponse(rqi):
    while not values.response.__contains__(rqi):
        pass


if __name__ == '__main__':
    import time
    values.mqttc = app.initMQTT()

    time.sleep(1)  # wait for mqtt initializing

    print("create AE")
    rqi = adn.createAE()
    waitResponse(rqi)

    monitor_target = '/' + conf.cse.id
    while True:
        rqi = adn.discovery(target=monitor_target, ty=conf.type.cnt)
        waitResponse(rqi)
        for cnt in values.response[rqi]['pc']['m2m:uril']:
            print(cnt)
        time.sleep(5)
