class AliPay(object):

    @staticmethod
    def pay():
        print("通过支付宝消费")


class WeChatPay(object):

    @staticmethod
    def pay():
        print("通过微信消费")


class YinLianPay(object):

    @staticmethod
    def pays():
        print("通过银联消费")


class Order(object):

    @staticmethod
    def account(pay_obj):
        pay_obj.pay()


a = AliPay()
w = WeChatPay()
y = YinLianPay()
order = Order()
order.account(a)
order.account(w)
order.account(y)