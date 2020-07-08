import random

class Board(object):
    def __init__(self, size: int = 1, data: list = None):
        assert isinstance(size, int), f'Size {size} is not an integer'
        if data is None or len(data) == 0:
            assert size > 0, f'Size {size} must be larger than 0'
            self.__size = size
            self.__data = [[random.randint(0, 1) for j in range(size)] for i in range(size)]
            self.__encoding_steps = []
            self.__decoding_steps = []
        else:
            assert isinstance(data, list) or isinstance(data[0], list), f'Given data {data} is not a list of list'
            assert len(data) == len(data[0]), f'Given data {data} does not have the correct size (row must match column)'
            for row in data:
                for val in row:
                    assert val in [0, 1], f'Value {val} does not match either 0 or 1'
            self.__size = len(data)
            self.__data = data
        self.always_winnnable = self.__size & (self.__size - 1) == 0

    def get_loc(self, coin: int):
        assert isinstance(coin, int) and coin < self.__size ** 2, f'Coin {coin} is out of bound of {self.__size} x {self.__size}: has to be less than {self.__size ** 2}'
        return (coin // self.__size, coin % self.__size)

    def to_val(self, x: int, y: int):
        assert isinstance(x, int) and isinstance(y, int) and 0 <= x < self.__size and 0 <= y < self.__size, f'Location ({x}, {y}) is not in range of ({self.__size}, {self.__size})'
        return x*self.__size + y

    def encode(self, key: int = None):
        self.__encoding_steps = []
        if key is None:
            key = random.randint(0, self.__size ** 2 - 1)
        res = key
        print(f'Key value at {key}, location {self.get_loc(key)}')
        self.__encoding_steps.append(f'Take given key as a result with value {key}')
        for x, row in enumerate(self.__data):
            for y, value in enumerate(row):
                if value == 1:
                    self.__encoding_steps.append(f'XOR result with coin at location ({x}, {y}) -> {res} ^ {self.to_val(x, y)} = {res ^ self.to_val(x, y)}')
                    res ^= self.to_val(x, y)
        flip_x, flip_y = self.get_loc(res)
        self.__encoding_steps.append(f'Flip coin-th {res} at location ({flip_x}, {flip_y})')
        self.__data[flip_x][flip_y] = (self.__data[flip_x][flip_y] + 1) % 2
        return key, res

    def decode(self):
        self.__decoding_steps = []
        res = None
        for x, row, in enumerate(self.__data):
            for y, value in enumerate(row):
                if value == 1:
                    coin_value = self.to_val(x, y)
                    if res is None:
                        self.__decoding_steps.append(f'First coin that has value 1 is at coin-th {coin_value} location ({x}, {y})')
                        res = coin_value
                    else:
                        self.__decoding_steps.append(f'XOR result {res} with new coin with value 1 at coin-th {coin_value} and take it as new res -> {res} ^ {coin_value} = {res ^ coin_value}')
                        res ^= coin_value
        return res

    @staticmethod
    def __get_steps(steps_list: list):
        return '\n'.join(f'Step #{i}: {steps}' for i, steps in enumerate(steps_list))
    
    def get_encoding_steps(self):
        return self.__get_steps(self.__encoding_steps)
    
    def get_decoding_steps(self):
        return self.__get_steps(self.__decoding_steps)

    def __str__(self):
        return '\n'.join(str(row) for row in self.__data)

if __name__ == "__main__":
    game = Board(size=8)
    print('Before encoding')
    print(game, end='\n\n')
    print('Guard will randomly place one key on one of the board field')
    print('Prisoner 1 attempts to encode')
    key_val, flip_val = game.encode()
    print(game.get_encoding_steps())
    print(f'Prisoner 1 flips coin {flip_val} at location {game.get_loc(flip_val)}')
    print('Prisoner 2 comes in and see the new board')
    print(game, end='\n\n')
    decoded_val = game.decode()
    print('Prisoner 2 attempts to decode')
    print(game.get_decoding_steps())
    print(f'Prisoner 2 guessed the original key location at coin-th: {decoded_val}, at location {game.get_loc(decoded_val)}')
    print(f'Game is always winnnable: {game.always_winnnable}')
    print(f'Key value {key_val}, Decoded value {decoded_val}')
    