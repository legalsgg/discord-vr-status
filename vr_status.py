"""Give a discord.py bot the VR status (the VR headset icon on its profile).

Usage:
    from vr_status import show_vr_status

    show_vr_status()   # before bot.run()
    bot.run(TOKEN)

This is unofficial: Discord doesn't document it and could stop it at any time.
"""

from discord.gateway import DiscordWebSocket

# What the bot tells Discord it is when it connects. These values make Discord show the VR headset.
VR_PROPERTIES = {'os': 'android', 'browser': 'Discord VR', 'device': 'Discord VR'}


def show_vr_status():
    """Report the bot as Discord's VR app when it connects, so its profile shows the VR headset.

    Call it before bot.run(). It also connects as online, because Discord only shows the
    headset for online accounts (idle shows the moon, do-not-disturb the red dot).
    """
    send_as_json = DiscordWebSocket.send_as_json

    async def send_as_vr(self, data):
        if data.get('op') == self.IDENTIFY:
            data['d']['properties'].update(VR_PROPERTIES)
            if 'presence' in data['d']:
                data['d']['presence']['status'] = 'online'
        await send_as_json(self, data)

    DiscordWebSocket.send_as_json = send_as_vr
