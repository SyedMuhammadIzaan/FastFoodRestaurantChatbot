from app.models.menu import Menu,db

def createMenu(data):
    try:
        if not data:
            return None
        else: 
            name=data.get('name')
            description=data.get('description')
            deliveryTime=data.get('deliveryTime') 
            price=int(data.get('price'))
            categoryId=data.get('categoryId')
            menu=Menu(name=name,description=description,deliveryTime=deliveryTime,price=price,categoryId=categoryId)

            db.session.add(menu)
            db.session.commit()
            return menu.to_dict()
    except Exception as e:
        return {"error": str(e)}

def getMenuById(menuId):
    try:
        if not menuId:
            return None
        else:
            menu=Menu.query.get(menuId)
            if not menu:
                return None
            else:
                return menu.to_dict()
    except Exception as e:
        return {"error": str(e)}

def updateMenu(menuId,data):
    try:
        if not menuId or not data:
            return None
        if type(menuId) is not int:
            return None
        else:
            menu=Menu.query.get(menuId)
            if not menu:
                return None
            else:
                menu.name=data.get('name',menu.name)
                menu.description=data.get('description',menu.description)
                menu.deliveryTime=data.get('deliveryTime',menu.deliveryTime)
                menu.price=data.get('price',menu.price)
                menu.categoryId=data.get('categoryId',menu.categoryId)

                db.session.commit()
                return menu.to_dict()
    except Exception as e:
        return {"error": str(e)}


def deleteMenu(menuId):
    try:
        if not menuId:
            return None
        else:
            menu=Menu.query.get(menuId)
            if not menu:
                return None
            else:
                db.session.delete(menu)
                db.session.commit()
                return 'Menu deleted successfully'
    except Exception as e:
        return {"error": str(e)}
    
    
def getAllMenu():
    try:
        menus=Menu.query.all()
        print("Menus in getAllMenu:", menus)
        if not menus:
            return None
        else:
            return [menu.to_dict() for menu in menus]
    except Exception as e:
        return {"error": str(e)}