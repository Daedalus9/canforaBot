from var.text import NO_ROLE, CLEAN_BACHECA
import yaml

def cleanbacheca(update, context):
    chat_id=update.effective_chat.id
    confirm = 0
    with open(r'var/admin.yaml') as file1:
        data = yaml.full_load(file1)
        for admin in data['admin']:
            if admin.split(" ", 1)[1] == str(chat_id):
                confirm = 1
                break
    if confirm == 1:
        file = open('./var/bacheca', "w")
        file.write("")
        file.close()
        context.bot.send_message(chat_id, CLEAN_BACHECA)
        file.close()
    else:
        context.bot.send_message(chat_id, NO_ROLE)