import paho.mqtt.client as mqtt
import json

def on_connect(mqttc, obj, flags, rc):
    print("rc: " + str(rc))


def on_message(mqttc, obj, msg):
    from .models import tiket, pengguna
    from . import transformer

    payload = (json.loads(msg.payload))
    
    values = payload['values']
    message = payload['message']
    #print(values)

    if message == 'cek_kode':
        try:
            boardingpass = tiket.objects.get(kode_booking=values)
            boardingpass = transformer.singleTransform(boardingpass)

            isi = json.dumps({
                'values':boardingpass,
                'message':'resp_kode',
                })
            ret = mqttc.publish(topik,isi)
            print(ret)
        except:
            print('Tiket tidak valid!')

    elif message == 'daftar':
        daftar = tiket.objects.all().order_by('-updated_at')
        daftar = transformer.transform(daftar)
        isi = json.dumps({
            'values':daftar,
            'message':'resp_daftar',
            })
        ret = mqttc.publish(topik,isi)
        print(ret)
    
    elif message == 'wajah':
        daftar = tiket.objects.all().order_by('-updated_at')
        calon = daftar[0]
        nama = calon.nik.nama
        if calon.status != '0':
            if nama == values['wajah']:
                try:
                    calon.wajah = '1'
                    calon.masker = "1" if values['masker'] == 'ya' else "x"
                    calon.save()
                    print('Updated')
                except:
                    print('Gagal update')
                print('Benar')
            else:
                try:
                    calon.wajah = 'x'
                    #calon.masker = "1" if values['masker'] == 'ya' else "x"
                    calon.save()
                    print('Updated')
                except:
                    print('Gagal update')
                print('Salah')
            isi = json.dumps({
                'values': transformer.transform(daftar),
                'message': 'daftar'
                })
            ret = mqttc.publish(topik,isi)

    elif message == 'masuk':
        try:
            user = pengguna.objects.get(email=values['email'])
        except:
            user = None
            isi = json.dumps({
                'values': '',
                'message': 'resp_masuk'
                })
            ret = mqttc.publish(topik,isi)

        if user != None:
            if user.password == values['password']:
                isi = json.dumps({
                    'values': transformer.singleTransform(user),
                    'message': 'resp_masuk'
                    })
            else:
                isi = json.dumps({
                    'values': 'Password tidak sesuai!',
                    'message': 'resp_masuk'
                    })
            ret = mqttc.publish(topik,isi)
               

def on_publish(mqttc, obj, mid):
    print("mid: " + str(mid))
    print("data published \n")

def on_subscribe(mqttc, obj, mid, granted_qos):
    print("Subscribed: " + str(mid) + " " + str(granted_qos))

def on_log(mqttc, obj, level, string):
    print(string)

mqttc = mqtt.Client()

mqttc.on_message = on_message
mqttc.on_connect = on_connect
mqttc.on_publish = on_publish
mqttc.on_subscribe = on_subscribe

topik = "TugasAkhirAldiLugina"

mqttc.connect("broker.emqx.io", 1883, 60)
mqttc.subscribe(topik, 0)