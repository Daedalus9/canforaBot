from var.text import NO_ROLE, ADDED_MESSAGE, NEW_MESSAGE
import yaml

def addbacheca(update, context):
    chat_id=update.effective_chat.id
    message=update.message.text
    confirm = 0
    nickname=""
    with open(r'var/admin.yaml') as file1:
        data = yaml.full_load(file1)
        for admin in data['admin']:
            if admin.split(" ", 1)[1] == str(chat_id):
                confirm = 1
                nickname = admin.split(" ", 1)[0]
                break
    if confirm == 1:
        file = open('./var/bacheca', "a")
        bacheca_message = "- " + nickname + " [" + message.split(" ",1)[1] + "]\n"
        file.write(bacheca_message)
        context.bot.send_message(chat_id, ADDED_MESSAGE)
        for admin in data['admin']:
            if admin.split(" ", 1)[1] != str(chat_id):
                context.bot.send_message(admin.split(" ", 1)[1], NEW_MESSAGE+bacheca_message)
        file.close()
    else:
        context.bot.send_message(chat_id, NO_ROLE)