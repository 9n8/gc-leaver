import discord, os, colorama
from colorama import Fore

os.system(f'title [gc leaver]')
os.system(f'mode 80,20')

client = discord.Client()
p = ">"
c = "gl"

token = input(f'{Fore.CYAN}Enter {Fore.LIGHTCYAN_EX}Token:{Fore.GREEN} ')

os.system('cls')

print(f'                        type >gl 2 leave all group chats \n\n')

print(f'                                   {Fore.YELLOW}@pw1337 {Fore.LIGHTMAGENTA_EX} \n')

@client.event
async def on_message(message):
    if message.author == client.user:
        cmd = str(message.content).split(' ')
        if cmd[0] == p + c:
            await message.delete()
            count = 0
            for channel in client.private_channels:
                if isinstance(channel, discord.GroupChannel):
                    if channel.id != message.channel.id:
                        count = count + 1
                        await channel.leave()
            await message.channel.send("``left [" + str(count) + "] gc(s)!``")
            await client.logout()
            exit(1)
if __name__ == '__main__':
    try:
        client.run(token, bot=False)
    except:
        os._exit(0)