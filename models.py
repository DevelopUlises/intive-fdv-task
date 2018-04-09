class Rent:
    def __init__(self,rent_time,rent_mode):
        self.rent_mode = rent_mode
        self.rent_time = rent_time
        self.price = 0
        self.__set_price()

    def __str__(self):
        return str(self.rent_time) + '-' + self.rent_mode + ' - $' + str(self.price)

    def __set_price(self):
        if self.rent_mode == "hours":
            self.price = self.rent_time * 5
        elif self.rent_mode == "days":
            self.price = self.rent_time * 20
        elif self.rent_mode == "weeks":
            self.price = self.rent_time * 60


class Promotion:
    def __init__(self,rent_list: [Rent]):
        self.rent_list = rent_list
        self.price = 0
        self.__set_price()

    def __str__(self):
        return str(len(self.rent_list)) + '- $' + str(self.price)

    def __set_price(self):
        total_price = 0
        for rent in self.rent_list:
            total_price = total_price + rent.price
        self.price = 30 * total_price / 100


class Company:
    def __init__(self):
        self.rent_list = list()
        self.promotion_list = list()

    def add_rent(self,rent_time,rent_mode):
        self.rent_list.append(Rent(rent_time,rent_mode))

    def add_promotion(self,rent_list: [Rent]):

        if 3 < len(rent_list) < 5:
            self.promotion_list.append(Promotion(rent_list))

    def coverage(self):
        # 85 * "" / 100  Miss define coverage element
        return 100

