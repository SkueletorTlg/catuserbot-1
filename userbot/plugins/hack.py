"""command: .hack & .thack """
# thx to @r4v4n4
import asyncio

from telethon.tl.functions.users import GetFullUserRequest

from . import ALIVE_NAME

DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "cat"


@bot.on(admin_cmd(pattern=r"hack$", outgoing=True))
@bot.on(sudo_cmd(pattern=r"hack$", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    if event.reply_to_msg_id:
        reply_message = await event.get_reply_message()
        await event.client(GetFullUserRequest(reply_message.sender_id))
        idd = reply_message.sender_id
        if idd == 1035034432:
            await edit_or_reply(
                event, "This is My Master\nI can't hack my master's Account"
            )
        else:
            event = await edit_or_reply(event, "Hacking..")
            animation_chars = [
                "`Conectando a un servidor privado para hackear...`",
                "`Objetivo seleccionado.`",
                "`Hackeando... 0%\n▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
                "`Hackeando... 4%\n█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
                "`Hackeando... 8%\n██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
                "`Hackeando... 20%\n█████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
                "`Hackeando... 36%\n█████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
                "`Hackeando... 52%\n█████████████▒▒▒▒▒▒▒▒▒▒▒▒ `",
                "`Hackeando... 84%\n█████████████████████▒▒▒▒ `",
                "`Hackeando... 100%\n█████████HACKEADO███████████ `",
                f"`Cuenta hackeada por Skueletor...\n\nSi quieres remover el ataque, pagame 69$ mediante PayPal.`",
            ]
            animation_interval = 3
            animation_ttl = range(11)
            for i in animation_ttl:
                await asyncio.sleep(animation_interval)
                await event.edit(animation_chars[i % 11])
    else:
        await edit_or_reply(event, "No User is Defined\n Can't hack account")


@bot.on(admin_cmd(pattern=f"thack$", outgoing=True))
@bot.on(sudo_cmd(pattern=r"thack$", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 2
    animation_ttl = range(12)
    event = await edit_or_reply(event, "thack")
    animation_chars = [
        "**Conectando a la base de datos de Telegram**",
        f"Objetivo seleccionado por el hacker: {DEFAULTUSER}",
        "`Hackeando... 0%\n▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `\n\n\n  TERMINAL:\nDownloading Bruteforce-Telegram-0.1.tar.gz (9.3 kB)",
        "`Hackeando... 4%\n█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `\n\n\n  TERMINAL:\nDownloading Bruteforce-Telegram-0.1.tar.gz (9.3 kB)\nCollecting Data Package",
        "`Hackeando... 8%\n██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `\n\n\n  TERMINAL:\nDownloading Bruteforce-Telegram-0.1.tar.gz (9.3 kB)\nCollecting Data Package\n  Downloading Telegram-Data-Sniffer-7.1.1-py2.py3-none-any.whl (82 kB)",
        "`Hackeando... 20%\n█████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `\n\n\n  TERMINAL:\nDownloading Bruteforce-Telegram-0.1.tar.gz (9.3 kB)\nCollecting Data Package\n  Downloading Telegram-Data-Sniffer-7.1.1-py2.py3-none-any.whl (82 kB)\nBuilding wheel for Tg-Bruteforcing (setup.py): terminado con estado de 'listo'",
        "`Hackeando... 36%\n█████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `\n\n\n  TERMINAL:\nDownloading Bruteforce-Telegram-0.1.tar.gz (9.3 kB)\nCollecting Data Package\n  Downloading Telegram-Data-Sniffer-7.1.1-py2.py3-none-any.whl (82 kB)\nBuilding wheel for Tg-Bruteforcing (setup.py): terminado con estado de 'listo'\nCreated wheel for telegram: filename=Telegram-Data-Sniffer-0.0.1-py3-none-any.whl size=1306 sha256=cb224caad7fe01a6649188c62303cd4697c1869fa12d280570bb6ac6a88e6b7e",
        "`Hackeando... 52%\n█████████████▒▒▒▒▒▒▒▒▒▒▒▒ `\n\n\n  TERMINAL:\nDownloading Bruteforce-Telegram-0.1.tar.gz (9.3 kB)\nCollecting Data Package\n  Downloading Telegram-Data-Sniffer-7.1.1-py2.py3-none-any.whl (82 kB)\nBuilding wheel for Tg-Bruteforcing (setup.py): terminado con estado de 'listo'\nCreated wheel for telegram: filename=Telegram-Data-Sniffer-0.0.1-py3-none-any.whl size=1306 sha256=cb224caad7fe01a6649188c62303cd4697c1869fa12d280570bb6ac6a88e6b7e\n  Almacenado en el directorio: /app/.cache/pip/wheels/a2/9f/b5/650dd4d533f0a17ca30cc11120b176643d27e0e1f5c9876b5b",
        "`Hackeando... 84%\n█████████████████████▒▒▒▒ `\n\n\n  TERMINAL:\nDownloading Bruteforce-Telegram-0.1.tar.gz (9.3 kB)\nCollecting Data Package\n  Downloading Telegram-Data-Sniffer-7.1.1-py2.py3-none-any.whl (82 kB)\nBuilding wheel for Tg-Bruteforcing (setup.py): terminado con estado de 'listo'\nCreated wheel for telegram: filename=Telegram-Data-Sniffer-0.0.1-py3-none-any.whl size=1306 sha256=cb224caad7fe01a6649188c62303cd4697c1869fa12d280570bb6ac6a88e6b7e\n  Almacenado en el directorio: /app/.cache/pip/wheels/a2/9f/b5/650dd4d533f0a17ca30cc11120b176643d27e0e1f5c9876b5b\n\n **Base de datos del servidor de Telegram hackeada con éxito**",
        "`Hackeando... 100%\n█████████HACKEADO███████████ `\n\n\n  TERMINAL:\nDownloading Bruteforce-Telegram-0.1.tar.gz (9.3 kB)\nCollecting Data Package\n  Downloading Telegram-Data-Sniffer-7.1.1-py2.py3-none-any.whl (82 kB)\nBuilding wheel for Tg-Bruteforcing (setup.py): terminado con estado 'listo'\nCreated wheel for telegram: filename=Telegram-Data-Sniffer-0.0.1-py3-none-any.whl size=1306 sha256=cb224caad7fe01a6649188c62303cd4697c1869fa12d280570bb6ac6a88e6b7e\n  Almacenado en el directorio: /app/.cache/pip/wheels/a2/9f/b5/650dd4d533f0a17ca30cc11120b176643d27e0e1f5c9876b5b\n\n **Base de datos del servidor de Telegram hackeada con éxito**\n\n\n🔹Producción: Generando.....",
        f"`Cuenta hackeada por Skueletor...\n\nSi quieres remover el ataque, pagame 69$ mediante PayPal.`\n\n\n  TERMINAL:\nDownloading Bruteforce-Telegram-0.1.tar.gz (9.3 kB)\nCollecting Data Package\n  Downloading Telegram-Data-Sniffer-7.1.1-py2.py3-none-any.whl (82 kB)\nBuilding wheel for Tg-Bruteforcing (setup.py): finished with status 'done'\nCreated wheel for telegram: filename=Telegram-Data-Sniffer-0.0.1-py3-none-any.whl size=1306 sha256=cb224caad7fe01a6649188c62303cd4697c1869fa12d280570bb6ac6a88e6b7e\n  Stored in directory: /app/.cache/pip/wheels/a2/9f/b5/650dd4d533f0a17ca30cc11120b176643d27e0e1f5c9876b5b\n\n **Successfully Hacked Telegram Server Database**\n\n\n🔹**Producción:** Exitosa",
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 11])


@bot.on(admin_cmd(pattern=f"wahack$", outgoing=True))
@bot.on(sudo_cmd(pattern=r"wahack$", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 2
    animation_ttl = range(15)
    event = await edit_or_reply(event, "wahack..")
    animation_chars = [
        "Buscando la base de datos de WhatsApp del usuario...",
        " Usuario en línea: True\nAcceso desde Telegram: True\nAcceso a su almacentamiento: True ",
        "Hackeando... 0%\n[░░░░░░░░░░░░░░░░░░░░]\n`Looking for WhatsApp...`\nETA: 0m, 20s",
        "Hackeando... 11.07%\n[██░░░░░░░░░░░░░░░░░░]\n`Looking for WhatsApp...`\nETA: 0m, 18s",
        "Hackeando... 20.63%\n[███░░░░░░░░░░░░░░░░░]\n`Found folder C:/WhatsApp`\nETA: 0m, 16s",
        "Hackeando... 34.42%\n[█████░░░░░░░░░░░░░░░]\n`Found folder C:/WhatsApp`\nETA: 0m, 14s",
        "Hackeando... 42.17%\n[███████░░░░░░░░░░░░░]\n`Searching for databases`\nETA: 0m, 12s",
        "Hackeando... 55.30%\n[█████████░░░░░░░░░░░]\n`Found msgstore.db.crypt12`\nETA: 0m, 10s",
        "Hackeando... 64.86%\n[███████████░░░░░░░░░]\n`Found msgstore.db.crypt12`\nETA: 0m, 08s",
        "Hackeando... 74.02%\n[█████████████░░░░░░░]\n`Trying to Decrypt...`\nETA: 0m, 06s",
        "Hackeando... 86.21%\n[███████████████░░░░░]\n`Trying to Decrypt...`\nETA: 0m, 04s",
        "Hackeando... 93.50%\n[█████████████████░░░]\n`Decryption successful!`\nETA: 0m, 02s",
        "Hackeando... 100%\n[████████████████████]\n`Scanning file...`\nETA: 0m, 00s",
        "¡Hackeo completado con éxito\nSubiendo archivos a mi base de datos...",
        "¡Cuenta Hackeada...!\n\n ✅ El archivo se subió correctamente en mi servidor.\nBase de datos de WhatsApp:\n`./DOWNLOADS/msgstore.db.crypt12`",
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 15])


CMD_HELP.update(
    {
        "hack": "**Plugin : **`hack`\
        \n\n**Syntax : **`.hack reply to a person`\
        \n**Function : **__shows an animation of hacking progess bar__\
        \n\n**Syntax : **`.thack reply to a person`\
        \n**Function : **__shows an animation of Telegram account hacking to a replied person__\
        \n\n**Syntax : **`.wahack reply to a person`\
        \n**Function : **__shows an animation of whatsapp account hacking to a replied person__\
    "
    }
)
