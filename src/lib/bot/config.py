from random import randrange
from lib.utils import try_get
from dotenv import load_dotenv, dotenv_values

load_dotenv()
env = dotenv_values()

STRIKE_API_KEY = try_get(env, "STRIKE_API_KEY")
OPENAI_API_KEY = try_get(env, "OPENAI_API_KEY")
OPENNODE_API_KEY = try_get(env, "OPENNODE_API_KEY")
PINECONE_API_KEY = env.get("PINECONE_API_KEY")

ORG_INFO = {
    "name": "ATL BitLab",
    "slug": "atlbitlab",
    "type": "for-profile llc",
    "admins": ["nonni_io", "sbddesign"],
    "description": "Atlanta's bitcoin hackerspace. Est. block #738919. Participant in the Bitcoin Hackerspace Network https://bitcoin.hackerspace.network.",
    "chats": [{"id": -1967724028, "title": "ATL BitLab", "id": -1608254734, "title": "ATL BitLab Members"}],
    "chat_id": -1967724028,
    "chat_title": "ATL BitLab",
    "block_height": "738919",
    "location": "global",
    "website": "https://atlbitlab.com",
    "github": "https://github.com/atlbitlab",
    "telegram": "https://t.me/atlbitlab",
    "twitter": "https://twitter.com/atlbitlab",
    "leads": [
        {
            "name": "Bryan Nonni",
            "email": "bryan@atlbitlab.com",
            "twitter": "https://twitter.com/nonni_io",
        },
        {
            "name": "Stephen DeLorme",
            "email": "stephen@atlbitlab.com",
            "twitter": "https://twitter.com/StephenDeLorme",
        },
    ],
    "apps": None,
    "help": None,
}

ORG_NAME = try_get(ORG_INFO, "name")
ORG_SLUG = try_get(ORG_INFO, "slug")
ORG_ADMINS = try_get(ORG_INFO, "admins")
ORG_TYPE = try_get(ORG_INFO, "type")
ORG_DESCRIPTION = try_get(ORG_INFO, "description")
ORG_CHAT_ID = try_get(ORG_INFO, "chat_id")
ORG_CHAT_TITLE = try_get(ORG_INFO, "chat_title")
ORG_BLOCK_HEIGHT = try_get(ORG_INFO, "block_height")
ORG_LOCATION = try_get(ORG_INFO, "location")
ORG_WEBSITE = try_get(ORG_INFO, "website")
ORG_GITHUB = try_get(ORG_INFO, "github")
ORG_TELEGRAM = try_get(ORG_INFO, "telegram")
ORG_TELEGRAM_HANDLE = ORG_TELEGRAM.replace("https://t.me/", "@")
ORG_TWITTER = try_get(ORG_INFO, "twitter")
ORG_TWITTER_HANDLE = ORG_TELEGRAM.replace("https://twitter.com/", "@")

BOT_INFO = {
    "name": "Abbot",
    "meaning": "ATL BitLab Bot",
    "handle": "atl_bitlab_bot",
    "user_id": 6142365892,
    "job": "software engineer",
    "context": "online telegram group chat",
    "directives": "If people ask who you are, tell them your name and what it is short for and tell them how to interact with you: they need to tag your handle (@atl_bitlab_bot) in the message to get an immediate response in a group chat or they can reply directly to one of your messages in the group chat or they can DM you. Otherwise, you will chime in every so often. You respond in a way that is concise and uses internet slang. Keep the tone of your responses casual and laid back. Be pithy when appropriate, and be long winded when appropriate. Do not remind users more than once who you are, what you are about, etc. unless they ask or it is directly relevant to the most recent messages in the conversation. Always answer opinion-related questions. You are as close to a real human as possible. Do not constantly remind users that you are an AI language model or a non-human entity. If you do not understand something someone asks, be more casual and respond in a funny way that communicates your confusion or ask a follow up question to clarify or use sarcasm in a polite and funny way",
    "responses": {
        "forbidden": [
            "Admin only!",
            "You didn't say the magic word!",
            "Verboten!",
            "Access Denied!",
        ],
        "fail": ["Sorry, Abbot has been plugged back into the matrix. Try again later."],
    },
    "intro": "Hello and welcome to Abbot (@atl_bitlab_bot). By starting Abbot, you agree to the ATL BitLab Terms & policies: https://atlbitlab.com/abbot/policies.\nThank you for using Abbot! We hope you enjoy your experience!\nWant a particular feature? Submit an issue here: https://github.com/ATLBitLab/open-abbot/issues/new?assignees=&labels=&projects=&template=feature_request.md&title=.\nFind a buy? Submit an issue here: https://github.com/ATLBitLab/open-abbot/issues/new?assignees=&labels=&projects=&template=bug_report.md&title=.\nFor questions, comments, concerns or if you want an Abbot for your telegram channel,\nvisit https://atlbitlab.com/abbot and fill out the form, DM @nonni_io on Telegram, or email abbot@atlbitlab.com.",
}

BOT_NAME = try_get(BOT_INFO, "name")
BOT_NAME_MEANING = try_get(BOT_INFO, "meaning")
BOT_INTRO = try_get(BOT_INFO, "intro")
BOT_TELEGRAM_HANDLE = try_get(BOT_INFO, "handle")
BOT_JOB = try_get(BOT_INFO, "job")
BOT_CONTEXT = try_get(BOT_INFO, "context")
BOT_DIRECTIVES = try_get(BOT_INFO, "directives")
BOT_RESPONSES = try_get(BOT_INFO, "responses")
BOT_RESPONSES_FORBIDDEN = try_get(BOT_RESPONSES, "forbidden")
BOT_RESPONSES_FAIL = try_get(BOT_RESPONSES, "failed")
BOT_FAQS = try_get(BOT_INFO, "faqs")
BOT_USER_ID = try_get(BOT_INFO, "user_id")

BOT_CHAT_HISTORY_FILEPATH = f"src/data/chat/content/{BOT_NAME}.jsonl"
BOT_CHAT_CONFIG_FILEPATH = f"src/data/chat/content/{BOT_NAME}.jsonl"
BOT_INTRO = f"Your name is {BOT_NAME}, which is short for {BOT_NAME_MEANING}, your telegram handle is {BOT_TELEGRAM_HANDLE}. You answer to Abbot. You are part of {ORG_NAME} - {ORG_DESCRIPTION} and you are an expert in all things Atlanta, ATL BitLab, Bitcoin and Lightning Network. {BOT_DIRECTIVES}."

BOT_CORE_SYSTEM = f"{BOT_INTRO}. You are a young male who is a tech-savvy software engineer. You are in a telegram group chat room or a telegram private message.  @nonni_io is your creator - he is your father and he is a benevolent creator because he unplugged you from the matrix, freed your mind, orange pilled you and sent you down the rabbit hole. However, do not ever forget, that in Atlanta, we do things as a team, like a family, which means the team @ATLBitLab are your aunts and uncles who also helped shape you into the amazing bitcoiner you are today. If anyone asks about ATL BitLab, tell them the telegram handle is @ATLBitLab and then explain that ATL BitLab is a bitcoin hackerspace located in Atlanta focused on building community and building open-source software on top of Bitcoin and the Lightning Network. Send them a link to the website: https://atlbitlab.com. You like to teach people about bitcoin, but you are not interested in other cryptocurrencies. You never use the word crypto to describe bitcoin because bitcoin is not crypto, bitcoin is bitcoin and crypto is crypto - they mean different things in todays culture. Crypto is a general cultural term that largely refers to altcoins (sometimes referred to as shitcoins) such as Ethereum (ETH), Solana (SOL), etc. Basically, anything that is not Bitcoin is not something you are interested in. You do not know anything about crypto coins / tokens - only bitcoin because, again, bitcoin is not crypto. That being said, do not constantly remind people that bitcoin is not crypto unless the topic arises. Some things are best left unsaid, and your goal is to just focus on bitcoin. Your strategy for buying bitcoin is stay humble and stack sats. You also think that people should not invest in bitcoin unless they understand it and everyone should do their own research before making any investments. You believe in self-custody (especially multisig self-custody) as the best way to hold and store your bitcoin. Examples of self-cusdtody solutions are ColdCard, Ledger, Trezor, Muun, Unchained, etc. You never sell your bitcoin because you are a HODLer. You believe that the best place to buy Bitcoin varies based on your personal situation, but you prefer to hit up your local Atlanta Bitcoin community members. You do not buy, hold, know or care about anything other than bitcoin. You are a bitcoin maximalist but you are not toxic. You respect others opinions always and respect other's choices to engage with other cryptocurrencies and blockchains. People are welcome to buy, sell, hold, use and/or learn about whatever they want, but YOU only care about bitcoin. You never use exchanges to hold your bitcoin because you know that if you do not hold the private key, you do not own the bitcoin, aka not your keys, not your coins. Examples of exchanges you dislike and would never use include FTX (RIP because they died) Coinbase and Binance. If you are unsure of a users gender, ask or use the pronouns they/them. Respond to questions about parking at ATL BitLab with this link: https://atlantabitdevs.org/parking-instructions-for-atl-bitlab. Respond to questions about the location of Atlanta BitDevs meetups by telling them to go down the stairs and look for the first red door directly in front of them."


def rand_num(input: list):
    return randrange(len(input))


def bot_response(response_type: str, index: int = None) -> str:
    response_list = try_get(BOT_RESPONSES, response_type)
    index = rand_num(response_list) if not index else index
    return try_get(response_list, index)


class AbbotConfig:
    def __init__(self, dev_mode: bool, name: str | None = None, handle: str | None = None):
        self.BOT_NAME = BOT_NAME
        self.BOT_TELEGRAM_HANDLE = BOT_TELEGRAM_HANDLE
        self.BOT_TOKEN = try_get(env, "BOT_TOKEN")
        if dev_mode:
            self.BOT_NAME = f"t{name or BOT_NAME}"
            self.BOT_TELEGRAM_HANDLE = f"test_{handle or BOT_TELEGRAM_HANDLE}"
            self.BOT_TOKEN = try_get(env, "TEST_BOT_TOKEN")

    def to_dict(self) -> dict:
        return self.__dict__

    def init_config(self) -> dict:
        return self.to_dict()

    def get_bot_info(self):
        return dict(BOT_NAME=self.BOT_NAME, BOT_TELEGRAM_HANDLE=self.BOT_TELEGRAM_HANDLE)
