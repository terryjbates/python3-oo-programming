"""sole module: contains function sole, save, show"""
import pickle
_sole_mem_cache_d = {}
_sole_disk_file_s = "solecache"
# This initialization code will be executed when this module is first loaded.
file = open(_sole_disk_file_s, 'r')
_sole_mem_cache_d = pickle.load(file)
file.close()
# Public functions

def sole(m, n, t):
    """sole(m,n,t): perform the sole calculation using the cache."""
    global _sole_mem_cache_d
    if _sole_mem_cache_d.has_key((m, n, t)):
        return _sole_mem_cache_d[(m, n, t)]
    else:
        # . . . do some time-consuming calculations . . .
        _sole_mem_cache_d[(m, n, t)] = result
        return result

def save():
    """save(): save the updated cache to disk."""
    global _sole_mem_cache_d, _sole_disk_file_s
    file = open(_sole_disk_file_s, 'w')
    pickle.dump(_sole_mem_cache_d, file)
    file.close()

def show():
    """show(): print the cache"""
    global _sole_mem_cache_d
    print _sole_mem_cache_d
>>> import pickle
>>> file = open("solecache",'w')
>>> pickle.dump({}, file)
>>> file.close()

