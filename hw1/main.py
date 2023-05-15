from lru_cache import LRUCache

if __name__ == '__main__':
    cache = LRUCache(10)
    cache.set('Jesse', 'Pinkman')
    cache.set('Walter', 'White')
    print(cache.get('Jesse')) # вернёт 'Pinkman'
    cache.set('Jesse', 'James')
    print(cache.get('Jesse')) # вернёт 'James'
    print(cache.get('Walter')) # вернёт 'Walter'
    cache.rem('Walter')
    print(cache.get('Walter')) # вернёт ''
    for i in range(10):
        cache.set(f'{i}', f'{i}')
        print(len(cache))
        print(cache.h.keys())
