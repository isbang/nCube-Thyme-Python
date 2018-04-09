import paho.mqtt.client as mqtt
import json
import shortid
import conf
import values
import noti

req_topic = '/oneM2M/req/' + conf.ae.id + '/' + conf.cse.id + '/' + conf.ae.bodytype
reg_resp_topic = '/oneM2M/reg_resp/' + conf.ae.id + '/' + conf.cse.id + '/#'
resp_topic = '/oneM2M/resp/' + conf.ae.id + '/' + conf.cse.id + '/#'
noti_topic = '/oneM2M/req/' + conf.cse.id + '/' + conf.ae.id + '/#'


def mqtt_on_connect(client, userdata, flags, rc):
    print("MQTT connected with result code " + str(rc))

    client.subscribe(reg_resp_topic)
    client.subscribe(resp_topic)
    client.subscribe(noti_topic)

    print('subscribe reg_resp_topic as ' + reg_resp_topic)
    print('subscribe resp_topic as ' + resp_topic)
    print('subscribe noti_topic as ' + noti_topic)


def mqtt_on_message(client, userdata, msg):
    topic_arr = msg.topic.split("/")
    if len(topic_arr) >= 5 and topic_arr[5]:
        bodytype = topic_arr[5] if topic_arr[5] in ['xml', 'cbor', 'json'] else None

    payload = msg.payload.decode('UTF8')
    print("<--- ", msg.topic, "\n<--- ", payload)
    print("")

    if topic_arr[1] == 'oneM2M':
        if topic_arr[2] in ['resp', 'reg_resp'] and topic_arr[3].replace(':', '/') == conf.ae.id:
            if bodytype == 'xml':
                # TODO: add xml code in here
                pass

            elif bodytype == 'cbor':
                # TODO: add cbor code in here
                pass

            else:  # json
                jsonObj = json.loads(payload)
                values.response[jsonObj['rqi']] = jsonObj

        elif topic_arr[2] == 'req' and topic_arr[4] == conf.ae.id:
            if bodytype == 'xml':
                # TODO: add xml code in here
                pass

            elif bodytype == 'cbor':
                # TODO: add cbor code in here
                pass

            else:
                jsonObj = json.loads(payload)

                if not jsonObj.__contains__('m2m:rqp'):
                    jsonObj['m2m:rqp'] = jsonObj

                noti.mqtt_noti_action(topic_arr, jsonObj)
        else:
            print('topic is not supported')
    else:
        print('topic is not supported')


def initMQTT():
    client = mqtt.Client()
    client.on_connect = mqtt_on_connect
    client.on_message = mqtt_on_message
    client.connect(conf.cse.host, conf.cse.mqttport, 60)

    client.loop_start()

    return client
