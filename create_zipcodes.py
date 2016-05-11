from faker import Factory
import requests

fake = Factory.create("pt_BR")

for x in range(40):

    nro = fake.postcode().replace("-","")

    ret = requests.get("http://bob-berlotto.herokuapp.com/zipcode?number=%s" % nro)
    if ret.status_code == 200 :

        if not ret.json()['results']:

            dados = {
                'number': nro,
                'street': fake.street_name(),
                'city': fake.city(),
                'state': fake.estado_sigla()
            }

            ret = requests.post("http://bob-berlotto.herokuapp.com/zipcode/", data=dados)

            print("ZipCode added: %s" % nro)

        else:

            print("ZipCode already exists: %s" % nro)
