from telegram import InlineKeyboardButton
from telegram.utils.helpers import escape_markdown as es


def welcome_msg():
    welcome_msg = '''Hello my*@👋🏻😇\n\n oru Instagram username thannal aynte DP angot theerum'''

    return welcome_msg


def acc_type(val):
    if(val):
        return "🔒Pootti vechekkuva🔒"
    else:
        return "🔓Thuranna manassaa🔓"


def create_caption(user):
    caption_msg = f'''📛*Aynte Peru*📛: {es(user.full_name,version=2)} \n😁*Followers*😁: {es(str(user.followers),version=2)} \n🤩*Following*🤩: {es(str(user.followees),version=2)}\
\n🧐*Account Type*🧐: {acc_type(user.is_private)} \n\nNandhi veendum Varika (Thanthakk vilikkaruth)\n\nEee bot njangalude swakarya Ahankaramaanu by @darkprince163 & @the_hsk'''

    return caption_msg


def get_username(url):
    try:
        data = url.split("/")[3]
        if "?" in data:
            try:
                data = data.split("?")
                return data[0]
            except Exception:
                return "incorrect format"
        return data
    except Exception:
        return "incorrect format"


ratingkey = [[InlineKeyboardButton(
    "⚠️ivide click cheyyaruth⚠️", url="https://t.me/SJ_HSK_bots/2")]]
