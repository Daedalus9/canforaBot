import yaml
from var.text import NO_ROLE, USER_ALREADY_IN_USER, ADD_USER_USER_CONFIRM

def adduser(update, context):
    chat_id=update.effective_chat.id
    message=update.message.text
    confirm = 0
    already_in = 0
    with open(r'var/admin.yaml') as file1:
        data_admin = yaml.full_load(file1)
        for admin in data_admin['admin']:
            if admin.split(" ", 1)[1] == str(chat_id):
                confirm = 1
                break
        if confirm==1:
            with open(r'var/user.yaml') as file2:
                data_user = yaml.full_load(file2)
                if data_user['user']:
                    for user in data_user['user']:
                        if user.split(" ", 1)[1] == str(message.split(" ", 2)[2]):
                            context.bot.send_message(chat_id, USER_ALREADY_IN_USER)
                            already_in=1
                            break
                if(already_in==0):
                    with open(r'var/user.yaml', 'a') as file3:
                        user=[message.split(" ",1)[1]]
                        yaml.dump(user, file3)
                        file3.close()
                        context.bot.send_message(chat_id, ADD_USER_USER_CONFIRM)
        else:
            context.bot.send_message(chat_id, NO_ROLE)
