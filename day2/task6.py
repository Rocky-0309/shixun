class Car:
    def __init__(self, brand, speed=0):
        self.brand = brand
        self.speed = speed

    def accelerate(self, m):
        # 加速m次，每次速度增加10
        self.speed += 10 * m
        return self.speed

    def brake(self, n):
        # 刹车n次，每次速度减少10（不低于0）
        self.speed = max(0, self.speed - 10 * n)
        return self.speed


# 创建Car实例并测试
my_car = Car("Toyota", 30)
print(f"初始速度: {my_car.speed} km/h")  # 初始速度: 30 km/h

my_car.accelerate(3)  # 加速3次
print(f"加速后: {my_car.speed} km/h")  # 加速后: 60 km/h

my_car.brake(2)  # 刹车2次
print(f"刹车后: {my_car.speed} km/h")  # 刹车后: 40 km/h


class ElectricCar(Car):
    def __init__(self, brand, speed=0, battery=50):
        super().__init__(brand, speed)
        self.battery = battery

    def charge(self):
        # 充电：电量增加20，不超过100
        self.battery = min(100, self.battery + 20)
        return self.battery


# 创建ElectricCar实例并测试
my_ev = ElectricCar("Tesla", 40, 60)
print(f"\n电动车初始速度: {my_ev.speed} km/h, 电量: {my_ev.battery}%")

my_ev.accelerate(2)  # 从Car继承的加速方法
print(f"加速后速度: {my_ev.speed} km/h")

my_ev.charge()  # 充电一次
print(f"充电后电量: {my_ev.battery}%")

my_ev.charge()  # 再次充电（测试不超过100）
print(f"二次充电后: {my_ev.battery}%")