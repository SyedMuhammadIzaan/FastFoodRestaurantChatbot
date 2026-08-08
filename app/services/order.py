from app.models.order import OrderMenu,db

def createOrder(data):
    try:
        if not data:
            return None
        else:
            customerName=data.get('customerName')
            phoneNo=data.get('phoneNo')
            email=data.get('email')
            address=data.get('address')
            city=data.get('city')
            country=data.get('country')
            itemName=data.get('itemName')
            quantity=data.get('quantity')
            totalPrice=data.get('totalPrice')
            order=OrderMenu(customerName=customerName,phoneNo=phoneNo,email=email,address=address,city=city,country=country,itemName=itemName,quantity=quantity,totalPrice=totalPrice)
            db.session.add(order)
            db.session.commit()
            return order.to_dict()
    except Exception as e:
        return {"error": str(e)}
    

def updateOrder(orderId,data):
    try:
        if not orderId or not data:
            return None
        if type(orderId) is not int:
            return None
        else:
            order=OrderMenu.query.get(orderId)
            if not order:
                return None
            else:
                order.customerName=data.get('customerName',order.customerName)
                order.phoneNo=data.get('phoneNo',order.phoneNo)
                order.email=data.get('email',order.email)
                order.address=data.get('address',order.address)
                order.city=data.get('city',order.city)
                order.country=data.get('country',order.country)
                order.itemName=data.get('itemName',order.itemName)
                order.quantity=data.get('quantity',order.quantity)
                order.totalPrice=data.get('totalPrice',order.totalPrice)

                db.session.commit()
                return order.to_dict()
    except Exception as e:
        return {"error": str(e)}
    

def getOrderById(orderId):
    try:
        if not orderId:
            return None
        else:
            order=OrderMenu.query.get(orderId)
            if not order:
                return None
            else:
                return order.to_dict()
    except Exception as e:
        return {"error": str(e)}
    
    
    
def getAllOrders():
    try:
        orders=OrderMenu.query.all()
        if not orders:
            return None
        else:
            return [order.to_dict() for order in orders]
    except Exception as e:
        return {"error": str(e)}
    
    
def deleteOrder(orderId):
    try:
        if not orderId:
            return None
        else:
            order=OrderMenu.query.get(orderId)
            if not order:
                return None
            else:
                db.session.delete(order)
                db.session.commit()
                return 'Order deleted successfully'
    except Exception as e:
        return {"error": str(e)}