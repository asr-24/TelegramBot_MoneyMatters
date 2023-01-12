import asyncio
import telegram


async def main():
    print("\n\n\n\n")
    bot = telegram.Bot("TOKEN")
    async with bot:
        print(await bot.get_me())
        get_updates_var = (await bot.get_updates())
        print(len(get_updates_var))
        for msg in get_updates_var:
            print("\n\n")
            first_name = msg.message.from_user.first_name
            id = msg.message.from_user.id
            username = msg.message.from_user.username
            text = msg.message.text
            print(first_name, id, username, text)
        
        
if __name__ == '__main__':
    asyncio.run(main())
    
