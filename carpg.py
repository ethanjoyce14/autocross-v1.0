class Car:

    def __init__(self, make, model, year, hrspr, weight, pr):
        self.make = make
        self.model = model
        self.year = year
        self.hrspr = hrspr
        self.weight = weight
        self.pr = pr

    def carstats(self):
        car_stats = (f"Your {current.year} {current.make} {current.model} weighs {current.weight} lbs" +
        f" and has {current.hrspr} Hrspr. It has a PR of {current.pr}.")
        return car_stats

    def cardesc(self):
        car_desc = f"{current.year} {current.make} {current.model}"
        return car_desc

honda_civic_si_2002 = Car('Honda', 'Civic SI', '2002', 160, 2744, 20)
mazda_miata_r_1994 = Car('Mazda', 'Miata R', '1994', 128, 2323, 23)
honda_crx_si_1991 = Car('Honda', 'CRX SI', '1991', 105, 2174, 22)
volkswagen_golf_gti_2019 = Car('Volkswagen', 'Golf GTI', '2019', 228, 3062, 24)

current = honda_civic_si_2002

