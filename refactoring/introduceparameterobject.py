class OrderService(object):
    def __init__(self):
        self.orders = []
        self.transactions = []

    def make_order(self, order_request):
        self._save_order(order_request['product'], order_request['user'])
        self._make_transaction(order_request['amount'], order_request['user'])

    def _save_order(self, product, user):
        self.orders.append({
            'product': product,
            'user': user,
        })

    def _make_transaction(self, amount, user):
        self.transactions.append({
            'amount': amount,
            'user': user,
        })
