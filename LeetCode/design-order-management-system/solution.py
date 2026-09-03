class OrderManagementSystem:
    def __init__(self):
        self.orders = {} 

    def addOrder(self, orderId: int, orderType: str, price: int) -> None:
        self.orders[orderId] = [orderType, price]

    def modifyOrder(self, orderId: int, newPrice: int) -> None:
        self.orders[orderId][1] = newPrice
        
    def cancelOrder(self, orderId: int) -> None:
        del self.orders[orderId]

    def getOrdersAtPrice(self, orderType: str, price: int) -> List[int]:
        return [orderId for orderId, data in self.orders.items() 
                if orderType == data[0] and price == data[1]]