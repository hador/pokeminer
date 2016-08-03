from abc import ABC, abstractmethod
import config
import datetime

class Notifier(ABC):
    NOTIFIED = {}

    @abstractmethod
    def do_notify(self, pokemon):
        pass

    def notify(self, pokemon):
        self.__clear_notified()
        hash_key = hash(pokemon['pokemon_id']) + hash(pokemon['lat']) + hash(pokemon['lon'])
        if hash_key not in self.NOTIFIED.keys():
            self.NOTIFIED[hash_key] = pokemon['expire_timestamp']
            self.do_notify(pokemon)

    def unixtimetostr(self, utime):
        return datetime.datetime.fromtimestamp(utime).strftime('%H:%M:%S')

    def __clear_notified(self):
        cur_time = datetime.datetime.now().timestamp()
        for key, val in self.NOTIFIED.items():
            if val < cur_time:
                del self.NOTIFIED[key]
