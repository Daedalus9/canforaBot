from var.text import NO_ROLE, EMPTY_BACHECA
import yaml

def bacheca(update, context):
    chat_id=update.effective_chat.id
    confirm = 0
    with open(r'var/admin.yaml') as file1:
        data = yaml.full_load(file1)
        for admin in data['admin']:
            if admin.split(" ", 1)[1] == str(chat_id):
                confirm = 1
                break
    if confirm == 1:
        file = open('./var/bacheca', "r")
        lines = file.readlines()
        if len(lines)>0:
            msg=""
            for line in lines:
                msg=msg+line
            context.bot.send_message(chat_id, msg)
        else:
            context.bot.send_message(chat_id, EMPTY_BACHECA)
        file.close()
    else:
        context.bot.send_message(chat_id, NO_ROLE)