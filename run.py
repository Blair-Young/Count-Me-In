import os
from remote_access import Remote
from countin import CountIn
import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--track', '-t', help='Track URI')
    parser.add_argument('--bpm', '-b', default=None, type=int, help= 'bpm of count in')
    args = parser.parse_args()

    username = os.environ['USERNAME']
    client_id = os.environ['CLIENT_ID']
    client_secret = os.environ['CLIENT_SECRET']

    phone = '743eb5597fe6dfb1855c40453baced0234e81074'
    laptop = 'b26204cd57cda44dc2890dce9444f7fe07c69ea8'
    song_uris = [args.track]
    device = laptop

    count = CountIn()
    remote = Remote(username, client_id, client_secret)

    if not args.track and not args.bpm:
        print('Playing at default 100 BPM at last paused position ')
        args.bpm = 100
        count.count(4, args.bpm)
        remote.playback(device)

    elif args.track and args.bpm:
        bpm = remote.get_song_bpm(args.track)
        print('Warning: Track played at {} but user has set count in BPM to {}'.format(bpm, args.bpm))
        count.count(4, args.bpm)
        remote.playback(device, song_uris)

    elif args.bpm:
        print('Playing at custom BPM- {} from last paused position'.format(args.bpm))
        count.count(4, args.bpm)
        remote.playback(device)

    else:
        bpm = remote.get_song_bpm(args.track)
        print('Playing at {}'.format(bpm))
        count.count(4, bpm)
        remote.playback(device, song_uris)
