"""
The goal of this coding activity is to design a system that limits the number of active roles that any given person has. A role gives the user access to some thing, whether it be a piece of data or an internal system. The system achieves this requirement by keeping track of the last k roles that a person has used. If a new role is used, the oldest role is removed if there are already k active roles for that person. Each role has a name and a message which contains details about its use by the person. You only need to store the last message for a role invocation.

Implement the constructor, get, and set methods of RolesCache. Each instance of the RolesCache corresponds to a single person.

Finally, fill out the runtime complexity for get and set and the overall space used. Use Big O notation, i.e. O(1), O(N), etc. For a refresher on Big O notation, please review https://danielmiessler.com/study/big-o-notation/.

"""
from collections import OrderedDict

class RolesCache:
    def __init__(self, capacity):
        self.capacity = capacity  # Maximum number of roles allowed (k roles)
        self.cache = OrderedDict()  # OrderedDict to store roles and their messages in order of access

    def get(self, role):
        # Return the message if the role exists, and move the role to the front (most recently used)
        if role in self.cache:
            # Move the accessed role to the end to indicate recent use
            self.cache.move_to_end(role)
            return self.cache[role]
        return None  # Role not in cache

    def set(self, role, message):
        # If the role is already in the cache, update the message and mark it as recently used
        if role in self.cache:
            self.cache.move_to_end(role)  # Move role to the front as it's most recently used
        # If it's a new role and we are at capacity, remove the oldest role
        elif len(self.cache) >= self.capacity:
            self.cache.popitem(last=False)  # Pop the first item (the least recently used role)
        
        # Add or update the role with its message
        self.cache[role] = message

    def _complexity(self):
        return {
            'get': 'O(1)',  # Accessing an element and moving it to the front in an OrderedDict is O(1)
            'set': 'O(1)',  # Adding a new element or updating an existing element is O(1); removing the oldest is also O(1)
            'space': 'O(k)'  # Space is proportional to the number of roles stored, which is at most k
        }
