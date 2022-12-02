import yaml
from var.text import ERROR_ADMIN_MESSAGE, ERROR_USER_MESSAGE, CONFIRM_SEND_REQUEST

def requestuser(update, context):
    chat_id=update.effective_chat.id
    user = update.message.from_user.username
    already_in=0
    with open(r'var/admin.yaml') as file1:
        data_admin = yaml.full_load(file1)
        for admin in data_admin['admin']:
            if admin.split(" ", 1)[1] == str(chat_id):
                already_in=1
                context.bot.send_message(chat_id, ERROR_ADMIN_MESSAGE)
                break
        
    with open(r'var/user.yaml') as file2:
        data_user = yaml.full_load(file2)
        if data_user['user']:
            for user in data_user['user']:
                if user.split(" ", 1)[1] == str(chat_id):
                    already_in=1
                    context.bot.send_message(chat_id, ERROR_USER_MESSAGE)
                    break

    if already_in!=1:
        for admin in data_admin['admin']:
            context.bot.send_message(admin.split(" ",1)[1], "L'utente " + user + " vuole essere aggiunto al gruppo user. Per aggiungerlo copia ed incolla il comando che segue")
            context.bot.send_message(admin.split(" ",1)[1], "/adduser " + user + " " + str(chat_id))
        context.bot.send_message(chat_id, CONFIRM_SEND_REQUEST)
        