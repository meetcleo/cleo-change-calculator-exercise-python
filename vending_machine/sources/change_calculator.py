class ChangeCalculator:
    def coins_needed(self, amount):
        if amount == 0:
            return []

        required_coins = []
        for available_coin in self._available_coins():
            if amount >= available_coin:
                required_coins.append(available_coin)
                amount -= available_coin

        return required_coins

    def _available_coins(self):
        return DENOMINATIONS


DENOMINATIONS = [
    50,
    5,
    200,
    20,
    2,
    100,
    10,
    1,
]
