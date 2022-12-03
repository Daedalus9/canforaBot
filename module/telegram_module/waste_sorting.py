import yaml
import telegram.ext

def waste_sorting(context: telegram.ext.CallbackContext):
    with open(r'var/waste_sorting.yaml') as file:
        data = yaml.full_load(file)
        file.close()
        current=data['CURRENT']

        if current!="Sabato":
            with open(r'var/admin.yaml') as file1:
                data_admin = yaml.full_load(file1)
                for admin in data_admin['admin']:
                    context.bot.send_message(admin.split(" ", 1)[1],"Ciao " + admin.split(" ", 1)[0] +"! Oggi è " + current + " e si butta " + data[current])
                    
        if current=="Domenica":
            data['CURRENT']="Lunedi'"
        elif current=="Lunedi'":
            data['CURRENT']="Martedi'"
        elif current=="Martedi'":
            data['CURRENT']="Mercoledi'"
        elif current=="Mercoledi'":
            data['CURRENT']="Giovedi'"
        elif current=="Giovedi'":
            data['CURRENT']="Venerdi'"
        elif current=="Venerdi'":
            data['CURRENT']="Sabato"
        elif current=="Sabato":
            data['CURRENT']="Domenica"

    with open('./var/waste_sorting.yaml', 'w') as f:
        yaml.dump(data, f)
        
