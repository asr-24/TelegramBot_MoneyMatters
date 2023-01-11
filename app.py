import asyncio
import telegram


async def main():
    print("\n\n\n\n")
    bot = telegram.Bot("5708512739:AAFcD64r-lKy3ZlPQCV8y8xPP0LYAYiD8ug")
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
    

#Update(message=Message(channel_chat_created=False, chat=Chat(first_name='Arushi', id=1313488817, last_name='Rai', type=<ChatType.PRIVATE>, username='arushirai'), date=datetime.datetime(2023, 1, 11, 6, 55, 56, tzinfo=datetime.timezone.utc), delete_chat_photo=False, from_user=User(first_name='Arushi', id=1313488817, is_bot=False, language_code='en', last_name='Rai', username='arushirai'), group_chat_created=False, message_id=5, supergroup_chat_created=False, text='nhk bhai'), update_id=348960600)