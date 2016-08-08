from names import POKEMON_NAMES
from notifier import Notifier
from pushbullet import Pushbullet
import config

MAPS_URL = "https://maps.google.it/?q="

class PushbulletNotifier(Notifier):
    pb = None

    def __init__(self):
        self.pb = Pushbullet(config.PB_API_KEY)

    def do_notify(self, pokemon):
        name = POKEMON_NAMES[pokemon['pokemon_id']]
        coords = str(pokemon['lat']) + "," + str(pokemon['lon'])
        expire_time = pokemon['expire_timestamp']
        if self.pb != None:
            push = self.pb.push_link(name + " - disappears at " + self.unixtimetostr(expire_time), MAPS_URL + coords)
