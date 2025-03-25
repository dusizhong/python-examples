import time  
import threading  
  
class SnowFlake:  
    def __init__(self, datacenter_id, worker_id):  
        self.datacenter_id = datacenter_id  
        self.worker_id = worker_id  
        self.sequence = 0  
        self.last_timestamp = -1  
        self.lock = threading.Lock()  
  
    def _time_gen(self):  
        return int(time.time() * 1000)  
  
    def get_id(self):  
        with self.lock:  
            timestamp = self._time_gen()  
  
            if timestamp < self.last_timestamp:  
                raise Exception(f"Clock moved backwards. Refusing to generate id for {self.last_timestamp - timestamp} milliseconds")  
  
            if timestamp == self.last_timestamp:  
                self.sequence = (self.sequence + 1) & 0xfff  # Handle sequence rollover  
                if self.sequence == 0:  
                    timestamp = self._til_next_millis(self.last_timestamp)  
            else:  
                self.sequence = 0  
  
            self.last_timestamp = timestamp  
  
            return ((timestamp - 1672537200000) << 22) | (self.datacenter_id << 17) | (self.worker_id << 12) | self.sequence  
  
    def _til_next_millis(self, last_timestamp):  
        timestamp = self._time_gen()  
        while timestamp <= last_timestamp:  
            timestamp = self._time_gen()  
        return timestamp