class Buffer:
    """
    A buffer that handles insertion & consumption of items.
    Has 2 possible policies: FIFO (First In First Out) and LIFO (Last In
    First Out).
    """
​
    def __init__(self, policy):
        policy = policy.upper()
        if policy not in ['FIFO', 'LIFO']:
            raise ValueError()
        self._policy = policy
​
    def insert(self, item):
        pass

    def extract(self):
        pass
