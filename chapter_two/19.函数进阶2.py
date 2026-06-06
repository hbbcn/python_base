# ------案列：函数进阶2------
#案例1：计算n的阶乘
#递归调用：函数调用自身 ps: 递归调用必须满足结束条件 否则会死循环
def jc(n):
    if n==1:
        return 1
    else:
        return n * jc(n-1)

print(jc(10))

def calc_order_const(*args,coupon = 0,score = 0,express = 0):
  """
   案例2: 定义一个用于根据传入的一批商品信息（商品名、价格、数量）、优惠（优惠券、积分抵扣)、运费信息计算订单总金额
    :param args: 商品信息（商品名、价格、数量） --->如("手机", 5000, 2), ("电脑", 8000, 1)
    :param coupon: 优惠券金额
    :param score: 积分抵扣金额
    :param express: 运费金额
    :return: 订单总金额
  """
  # 1.商品总价格
  # itemSum = [arg[1] * arg[2] for arg in args]
  # totle = sum(itemSum)
  totle = 0
  for arg in args:
      totle += arg[1] * arg[2]

  # 2.优惠金额
  if totle > 5000 and coupon <= totle:
      totle -= coupon
  # 3.积分抵扣金额
  if totle > 5000 and score // 100 <= totle:
      totle -= score // 100
  # 4.运费金额
  totle += express
  return totle

print(calc_order_const(("手机", 5000, 2), ("电脑", 8000, 1), coupon=500, score=1000, express=100))




