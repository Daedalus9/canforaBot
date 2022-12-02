import yaml

def get_admin(update, context):
    chat_id=update.effective_chat.id
    with open(r"./var/admin.yaml") as file:
        data = yaml.full_load(file)
        print(data)
        for admin in data['admin']:
            context.bot.send_message(chat_id, admin)