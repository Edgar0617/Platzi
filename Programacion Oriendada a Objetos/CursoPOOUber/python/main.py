from car import Car
from account import Account

if __name__ == "__main__":

    car = Car("MLA301", Account("Edgar Rosales", "ANDA876"))
    print(vars(car))
    print(vars(car.driver))