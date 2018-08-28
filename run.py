import os
from remote_access import Remote
from countin import CountIn
import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--track', '-t', default=None, help='Track URI')
    parser.add_argument('--bpm', '-b', default=None, type=int, help= 'bpm of count in')
    args = parser.parse_args()

    username = os.environ['USERNAME']
    client_id = os.environ['CLIENT_ID']
    client_secret = os.environ['CLIENT_SECRET']

    phone = '743eb5597fe6dfb1855c40453baced0234e81074'
    laptop = 'b26204cd57cda44dc2890dce9444f7fe07c69ea8'
    device = laptop

    count = CountIn()
    remote = Remote(username, client_id, client_secret)


    if not args.track and not args.bpm:
        print('Defaulting to 100bpm')
        args.bpm = 100
        count.count(4, args.bpm)
        remote.playback(device)

    elif args.track and args.bpm:
        print('Use either track or bpm, not both')

    elif args.bpm:
        print('Playing at custom BPM- {}'.format(args.bpm))
        count.count(4, args.bpm)
        remote.playback(device)

    else:
        bpm = remote.get_song_bpm(args.track)
        print('Playing at {}'.format(bpm))
        count.count(4, bpm)
        remote.playback(device)
