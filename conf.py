class type:
    ae = "2"
    cnt = "3"
    ci = "4"
    sub = "23"


class cse:
    host = "127.0.0.1"  # YOUR_CSE_IP_OR_URL
    port = '7579'  # YOUR_CSE_PORT
    name = 'Mobius'  # YOUR_CSE_NAME
    id = 'Mobius'  # YOUR_CSE_ID
    mqttport = 1883  # BROKER_IP


class ae:
    host = "127.0.0.1"  # YOUR AE IP
    id = 'MY-AE'  # YOUR AE ID
    parent = '/' + cse.id
    name = 'MY-AE'  # YOUR AE NAME
    appid = 'MY-AE'  # YOUR AE APPID
    port = '3376'  # YOUR AE PORT
    bodytype = 'json'


cnt = []

data = {}
data['parent'] = '/' + cse.name + '/' + ae.name
data['name'] = 'CNT-NAME'  # YOUR CONTAINER NAME
cnt.append(data)

sub = []

data = {}
data['parent'] = '/' + cse.name + '/' + ae.name + '/' + cnt[0]['name']
data['name'] = "SUB-NAME"  # YOUR SUBSCRIBER NAME FOR NOTIFICATION
data['nu'] = "mqtt://" + cse.host + '/' + ae.id + '?ct=' + ae.bodytype
sub.append(data)
