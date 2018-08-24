import os
from remote_access import Remote
from countin import CountIn

if __name__ == '__main__':
    username = os.environ['USERNAME']
    client_id = os.environ['CLIENT_ID']
    client_secret = os.environ['CLIENT_SECRET']

    phone = '743eb5597fe6dfb1855c40453baced0234e81074'
    laptop = 'b26204cd57cda44dc2890dce9444f7fe07c69ea8'
    bpm = 140

    device = phone
    remote = Remote(username, client_id, client_secret)

    count = CountIn()
    count.count(4, bpm)
    remote.playback(device)
