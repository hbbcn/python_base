"""
封装: 将数据（属性）和操作数据的方法绑定在一起，形成一个独立的单元（类），保护数据不被外部访问，通过访问修饰符实现封装
    1.私有属性: 在属性名前加双下划线__
    2.私有方法：在方法名前加双下划线__
"""

class Car:
    def __init__(self,brand,model,color,owner):
        self.brand = brand
        self.model = model
        self.color = color
        self.__owner = owner


    def start(self):
        print(f"{self.brand} {self.model} 正在启动...")

    def run(self):
        print(f"{self.__owner} {self.brand} {self.model} 启动成功, 正在加速...")

    def stop(self):
        print(f"{self.brand} {self.model} 停止运行...")

    def __get_owner(self):
        return self.__owner

    def __set_owner(self,owner):
        self.__owner = owner


    # 属性描述符：：将 owner 属性变成一个“智能属性”，在获取或修改它时，自动触发你定义好的逻辑（比如数据验证、日志记录等）。
    owner = property(__get_owner,__set_owner)


if __name__ == '__main__':
    c1 = Car("Audi","A6","黑色","张三")
    print(c1.brand)
    print(c1.model)
    print(c1.color)

    c1.start()
    c1.run()
    c1.stop()
    print(c1._Car__get_owner())
    c1._Car__set_owner("王五")
    c1.run()
