import time

class FilterModule:
  
    def filters(self):
        return {
            'epoch2isodate': self.epoch2isodate,
            'mtime_size': self.mtime_size
            
        }
            
    def epoch2isodate(self, epochtime):
        return time.strftime(("%Y-%m-%d %H:%M:%S"))

    def mtime_size(self, ansible_stat, hostname, numlines, label):
        result=ansible_stat['stat']
        if bool(result['exists']):
            mtime = self.epoch2isodate(result['mtime'])
            size = result['size']
            owner = result['pw_name']
            group = result['gr_name']
            checksum = result['checksum']
            return f"{ label };{ hostname };{ mtime };{ size };{ numlines };{ owner };{ group };{ checksum }"
        else:
            return f"{ label };{ hostname }; File not found!"
                

