from telethon import TelegramClient, events, sync
from telethon.tl.types import InputPhoneContact
from telethon import functions, types
from time import sleep

def check(phone_number, name, famil):
    try:
        print(phone_number)
        contact = InputPhoneContact(client_id = 0, phone = phone_number, first_name=name, last_name=famil)
        contacts = client(functions.contacts.ImportContactsRequest([contact]))
        username = contacts.to_dict()['users'][0]['username']
        return username
        dell = client(functions.contacts.DeleteContactsRequest(id=[username]))
    except:
        res = "__err__"
        return res

def list_checker():
    list_file = 'List.txt' #input("List of numbers: ")
    list = open(list_file, 'r',encoding='utf-8').read().splitlines()

    for num in list:
        try:
            (name, famil, number) = num.split(',')
            name = name.strip()
            famil = famil.strip()
            number = number.strip()
            number = '+' + number
            ress = check(number,name, famil)
            sleep(1)
            final = ''
            print(ress, number, name, famil)
            if ress == None:
                ress == '__err__'
            if ress == '__err__':
                final = "null\n"
            else:
                final = '@' + ress + '\n'
            f = open("usernames.txt", "a", encoding='utf-8')
            f.write(final)
            f.close()
        except RuntimeError as err:
            print (err)

if __name__ == '__main__':
    phone = 'phone number'
    # get api_id and app api-hash from https://my.telegram.org/auth
    client = TelegramClient(phone, App api_id, 'App api_hash')
    client.connect()
    if not client.is_user_authorized():
        client.send_code_request(phone)
        client.sign_in(phone, input('Enter the code: '))
    list_checker()
