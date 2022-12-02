import yaml
from var.text import NO_ROLE

def get_admin(update, context):
    chat_id=update.effective_chat.id
    confirm = 0
    with open(r'var/admin.yaml') as file1:
        data = yaml.full_load(file1)
        for admin in data['admin']:
            if admin.split(" ", 1)[1] == str(chat_id):
                confirm = 1
                break
    if confirm==1:
        with open(r"./var/admin.yaml") as file:
            data = yaml.full_load(file)
            for admin in data['admin']:
                context.bot.send_message(chat_id, admin)
    else:
        context.bot.send_message(chat_id, NO_ROLE)