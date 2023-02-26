## Coder are here

import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
admins = {}
SESSION_NAME = getenv("SESSION_NAME", "AQAcfKaNF1tq_lLyA2XqSxUwmdGS9okkJi-B_k1dHiqvS65Ie_izeHOB-u9Q92Zv7YCobKl8QrugWYWSbYsKpzHqMBYwIhflZbLJSSW7D0ZpZx3_IxieMtgsPstmHkaVCWCYyryTzZcZugpVzpjsa8UY7kFVT-iSkp7L6o6AQMQW9J_Sxol93jDpnSpOVemZkHdx1HxdNadldssHx_BjZSfdJ7rJ6dpE2cF4WCyV3MM_H5JHKk2LMCP7_QrZ9o0KMU-83RkdlmHJ0kDbBrXlRlMfGjtN8tf0QiB4OtX2JeQ2bdWRfnudnzCRwhsB2KCF0VXCO4s1mjAwtueiVKMENCgJAAAAAVbQBRYA")
BOT_TOKEN = getenv("BOT_TOKEN","6251600257:AAHwaoPzL23X7Exb2l6-P_WaD8bKDL50pL4")
BOT_NAME = getenv("BOT_NAME","niti")
API_ID = int(getenv("API_ID", "27184365"))
API_HASH = getenv("API_HASH", "e7195f26e0660b154cca646135582a8e")
OWNER_NAME = getenv("OWNER_NAME", "Niti")
ALIVE_NAME = getenv("ALIVE_NAME", "Niti is live to rule")
ASSISTANT_USERNAME = ("doll_quwen")
BOT_USERNAME = getenv("BOT_USERNAME","@NITIDJBOT")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "Paradise niti")
GROUP_SUPPORT = getenv("GROUP_SUPPORT","MeMiC_sQuAd")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL","MeMiC_sQuAd")
SUDO_USERS = list(map(int, getenv("SUDO_USERS","5148516372").spli()))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
ALIVE_IMG = getenv("ALIVE_IMG", "https://telegra.ph/file/02a27e950e46688bf1ae0.jpg")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "9000000000000000000"))
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/AMANTYA1/RaiChu-MusicV2")
IMG_1 = getenv("IMG_1", "https://telegra.ph/file/88f803d13a7899ad49276.jpg")
IMG_2 = getenv("IMG_2", "https://telegra.ph/file/88f803d13a7899ad49276.jpg")
IMG_3 = getenv("IMG_3", "https://telegra.ph/file/88f803d13a7899ad49276.jpg")
IMG_4 = getenv("IMG_4", "https://telegra.ph/file/88f803d13a7899ad49276.jpg")
IMG_5 = getenv("IMG_5", "https://telegra.ph/file/88f803d13a7899ad49276.jpg")
IMG_6 = getenv("IMG_6", "https://telegra.ph/file/88f803d13a7899ad49276.jpg")
YOUTUBE_IMG_URL = getenv("YOUTUBE_IMG_URL", "https://telegra.ph/file/58da23d726b601dc3b18e.jpg")
