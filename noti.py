import conf
import json
import values


def response_mqtt(rsp_topic, rsc, to, fr, rqi, inpc, bodytype):
    rsp_message = {}
    rsp_message['m2m:rsp'] = {}
    rsp_message['m2m:rsp']['rsc'] = rsc
    rsp_message['m2m:rsp']['to'] = to
    rsp_message['m2m:rsp']['fr'] = fr
    rsp_message['m2m:rsp']['rqi'] = rqi
    rsp_message['m2m:rsp']['pc'] = inpc

    values.mqttc.publish(rsp_topic, json.dumps(rsp_message['m2m:rsp']))


def parse_sgn(rqi, pc, topic_arr):
    if pc['sgn']:
        nmtype = 'short' if pc['sgn'] else 'long'
        sgnObj = {}
        cinObj = {}
        sgnObj = pc['sgn'] if pc['sgn'] else pc['singleNotification']

        if nmtype == 'long':
            print('oneM2M spec. define only short name for resource')

        else:  # 'short'
            if sgnObj.__contains__('sur') and sgnObj['sur']:
                path_arr = sgnObj['sur'].split('/')

            if sgnObj.__contains__('nev') and sgnObj['nev']:
                if sgnObj['nev'].__contains__('rep') and sgnObj['nev']['rep']:
                    if sgnObj['nev']['rep'].__contains__('m2m:cin') and sgnObj['nev']['rep']['m2m:cin']:
                        sgnObj['nev']['rep']['cin'] = sgnObj['nev']['rep']['m2m:cin'].copy()
                        sgnObj['nev']['rep'].__delitem__('m2m:cin')

                    if sgnObj['nev']['rep'].__contains__('cin') and sgnObj['nev']['rep']['cin']:
                        cinObj = sgnObj['nev']['rep']['cin']

                    else:
                        print('[mqtt_noti_action] m2m:cin is none')
                        cinObj = None

                else:
                    print(
                        '[mqtt_noti_action] rep tag of m2m:sgn.nev is none. m2m:notification format mismatch with oneM2M spec.'
                    )
                    cinObj = None

            else:
                print(
                    '[mqtt_noti_action] nev tag of m2m:sgn is none. m2m:notification format mismatch with oneM2M spec.')
                cinObj = None

    else:
        print('[mqtt_noti_action] m2m:sgn tag is none. m2m:notification format mismatch with oneM2M spec.')
        print(pc)

    if cinObj:
        for i in range(len(conf.sub)):
            if conf.sub[i]['parent'].split('/')[-1] == path_arr[-2]:
                if conf.sub[i]['name'] == path_arr[-1]:
                    rsp_topic = '/oneM2M/resp/' + topic_arr[3] + '/' + topic_arr[4] + '/' + topic_arr[5]
                    response_mqtt(rsp_topic, 2001, '', conf.ae.id, rqi, '', topic_arr[5])

                    #print((cinObj.con != None ? cinObj.con : cinObj.content));
                    print('mqtt ' + topic_arr[5] + ' notification <----')
                    print('mqtt response - 2001 ---->')

                    values.conreq[rqi] = cinObj.copy()
                    break


def mqtt_noti_action(topic_arr, jsonObj):
    if jsonObj:
        bodytype = conf.ae.bodytype
        if len(topic_arr) >= 5:
            bodytype = topic_arr[5]

            op = jsonObj['m2m:rqp']['op'] if jsonObj['m2m:rqp']['op'] else ""
            to = jsonObj['m2m:rqp']['to'] if jsonObj['m2m:rqp'].__contains__('to') else ""
            fr = jsonObj['m2m:rqp']['fr'] if jsonObj['m2m:rqp']['fr'] else ""
            rqi = jsonObj['m2m:rqp']['rqi'] if jsonObj['m2m:rqp']['rqi'] else ""
            pc = jsonObj['m2m:rqp']['pc'].copy() if jsonObj['m2m:rqp']['pc'] else {}

            if pc.__contains__('m2m:sgn'):
                pc['sgn'] = {}
                pc['sgn'] = pc['m2m:sgn']
                pc.__delitem__('m2m:sgn')

                parse_sgn(rqi, pc, topic_arr)
            elif pc.__contains__('sgn'):
                parse_sgn(rqi, pc, topic_arr)
            else:
                print('[mqtt_noti_action] message is not noti')
