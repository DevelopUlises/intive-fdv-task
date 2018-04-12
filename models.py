class Bike:
    def __init__(self,identify):
        self.identify = identify
        self.reservated = False

    def __str__(self):
        return self.identify


class Rent:
    def __init__(self,rent_time,rent_mode,bike=None):
        self.rent_mode = rent_mode
        self.rent_time = rent_time
        self.bike = bike
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
        self.bike_list = list()

    def add_bike(self,identify):
        self.bike_list.append(Bike(identify))

    def add_rent(self,rent_time,rent_mode,bike):
        rent = Rent(rent_time,rent_mode)
        for b in self.bike_list:
            if b.identify == bike :
                b.reservated = True
                rent.bike = b
                break
        self.rent_list.append(rent)

    def add_promotion(self,rent_list):
        if 3 < len(rent_list) < 5:
            for r in rent_list:
                for b in self.bike_list:
                    if b.identify == r.bike:
                        b.reservated = True
                        r.bike = b
                        break

            self.promotion_list.append(Promotion(rent_list))

    def coverage(self):
        bike_reserved = 0
        for b in self.bike_list:
            if b.reservated:
                bike_reserved = bike_reserved + 1

        return bike_reserved *100 / len(self.bike_list)

