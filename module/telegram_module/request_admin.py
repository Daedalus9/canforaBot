import yaml
from var.text import ERROR_ADMIN_MESSAGE, CONFIRM_SEND_REQUEST

def request_admin(update, context):
    chat_id=update.effective_chat.id
    user = update.message.from_user.username
    with open(r'var/admin.yaml') as file1:
        data = yaml.full_load(file1)
        for admin in data['admin']:
            if admin.split(" ", 1)[1] == str(chat_id):
                context.bot.send_message(chat_id, ERROR_ADMIN_MESSAGE)
                break
        else:
            for admin in data['admin']:
                context.bot.send_message(admin.split(" ",1)[1], "L'utente " + user + " vuole essere aggiunto al gruppo admin. Per aggiungerlo copia ed incolla il comando che segue")
                context.bot.send_message(admin.split(" ",1)[1], "/addadmin " + user + " " + str(chat_id))
            context.bot.send_message(chat_id, CONFIRM_SEND_REQUEST)