from telebot import TeleBot
from telebot import types

channelId = -1001492219555
bot = TeleBot('1706939990:AAEQ2KZ4VRbincT7Sa9TvaL-FRJ7SiD6Z08')

TIMEZONE = 'Russia/Moscow'
TIMEZONE_COMMON_NAME = 'Moscow'

inline_btn = types.InlineKeyboardButton("1-я поддгруппа", callback_data="button1")
inline_btn2 = types.InlineKeyboardButton("2-я подгруппа", callback_data="button2")
inline_kb = types.InlineKeyboardMarkup()
inline_kb.add(inline_btn)
inline_kb.add(inline_btn2)


@bot.message_handler(commands=['start'])
def start_command(message):
    bot.send_message(message.chat.id, "please choose, your group of english language(hint: /first or /second)")
    # with open("users_id_first.txt", "r") as file:
    #     global users
    #     users = file.read().splitlines()
    #     file.close()
    # if str(message.chat.id) in users:
    #     bot.send_message(message.chat.id, "Sorry, you're already in list")
    # else:
    #     with open("users_id_first.txt", "a") as file:
    #         file.write('\n' + str(message.chat.id))
    #         bot.send_message(message.chat.id, "You have been successfully subscribed on updates!")
    #         file.close()

@bot.message_handler(commands=['first'])
def add_in_first_group(mesage):
    add_user("users_id_first.txt", mesage)


@bot.message_handler(commands=['second'])
def add_in_second_group(message):
    add_user("users_id_second.txt", message)

def add_user(group, message):
    global second_group
    if group == "users_id_first.txt":
        second_group = "users_id_second.txt"
    else:
        second_group = "users_id_first.txt"
    with open(group, 'r') as file:
        global us
        us = file.read().splitlines()
        file.close()
    with open(second_group, 'r') as file:
        global us2
        us2 = file.read().splitlines()
        file.close()
    if str(message.chat.id) in us:
        bot.send_message(message.chat.id, "sorry, you're already in list")
    elif str(message.chat.id) in us2:
        bot.send_message(message.chat.id, "sorry, you're already in list")
    else:
        with open(group, 'a') as file:
            file.write(str(message.chat.id) + "\n")
            bot.send_message(message.chat.id, "You have benn successfully subscribed on updates")
            file.close()


# @bot.message_handler(content_types=['text'])
# def text_processor(message):
#     if message.text == 'Привет':
#         bot.send_message(message.chat.id, 'Соси хуй быдло', reply_markup=inline_kb)


@bot.channel_post_handler(content_types=['text'])
def send_posts(channel_post):
    if channel_post.chat.id == -1001492219555:
        if "#Англ 1 подгруппа" in channel_post.text:
            send_to_first(channel_post)
        elif "#Англ 2 подгруппа" in channel_post.text:
            send_to_second(channel_post)
        else:
            send_to_first(channel_post)
            send_to_second(channel_post)



def send_to_first(channel_post):
    with open("users_id_first.txt", 'r') as file:
        for user in file.read().splitlines():
            bot.forward_message(chat_id=user, from_chat_id=channel_post.chat.id,
                message_id=channel_post.message_id)


def send_to_second(channel_post):
    with open("users_id_second.txt", 'r') as file:
        for user in file.read().splitlines():
            bot.forward_message(chat_id=user, from_chat_id=channel_post.chat.id,
                message_id=channel_post.message_id)




# @bot.callback_query_handler(func=lambda callback: callback.data.startswith("button"))
# def callback_inline_catcher(call):
#     if call.message:
#         if call.data == "button1":
#             bot.send_message(chat_id=call.message.chat.id, text="you was added in first group")
#             bot.answer_callback_query(call.id, show_alert=False, text="It works")
#         if call.data == "button2":
#             bot.send_message(chat_id=call.message.chat.id, text="you was added in second group")


bot.polling()
