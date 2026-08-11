from flask import Blueprint, jsonify, render_template, request
from app.services.order import createOrder,updateOrder,getAllOrders,getOrderById,deleteOrder
from app.services.menu import createMenu, getMenuById,updateMenu,deleteMenu,getAllMenu
from app.services.category import createCategory, getAllCategories,updateCategory,deleteCategory

main_bp=Blueprint('main',__name__)

@main_bp.route("/")
def home():
    menus=getAllMenu()
    categories=getAllCategories()
    return render_template("index.html", menus=menus, categories=categories)

@main_bp.route('/order/create',methods=['POST'])
def newOrder():
    data=request.form.to_dict() or request.get_json()
    order=createOrder(data)
    if order:
        return jsonify(order),201
    else:
        return jsonify({'error':'Failed to create order'}),400

@main_bp.route('/order/update/<int:orderId>',methods=['PUT'])
def modifyOrder(orderId):
    data=request.form.to_dict() or request.get_json()
    order=updateOrder(orderId,data)
    if order:
        return jsonify(order),200
    else:
        return jsonify({'error':'Failed to update order'}),400
    

@main_bp.route('/order/<int:orderId>',methods=['GET'])
def getOrder(orderId):
    order=getOrderById(orderId)
    if order:
        return jsonify(order),200
    else:
        return jsonify({'error':'Order not found'}),404

@main_bp.route('/order',methods=['GET'])
def getOrders():
    orders=getAllOrders()
    if orders:
        return jsonify(orders),200
    else:
        return jsonify({'error':'No orders found'}),404
    

@main_bp.route('/order/delete/<int:orderId>',methods=['DELETE'])
def removeOrder(orderId):
    result=deleteOrder(orderId)
    if result:
        return jsonify(result),200
    else:
        return jsonify({'error':'Failed to delete order'}),400
    

@main_bp.route('/menu/create',methods=['POST'])
def newMenu():
    data=request.form.to_dict() or request.get_json()
    menu=createMenu(data)
    if menu:
        return jsonify(menu),201
    else:
        return jsonify({'error':'Failed to create menu'}),400
    
    
@main_bp.route('/menu/update/<int:menuId>',methods=['PUT'])
def modifyMenu(menuId):
    data=request.form.to_dict() or request.get_json()
    menu=updateMenu(menuId,data)
    if menu:
        return jsonify(menu),200
    else:
        return jsonify({'error':'Failed to update menu'}),400

@main_bp.route('/menu/<int:menuId>',methods=['GET'])
def getMenu(menuId):
    menu=getMenuById(menuId)
    if menu:
        return jsonify(menu),200
    else:
        return jsonify({'error':'Menu not found'}),404

@main_bp.route('/menu',methods=['GET'])
def getMenus():
    menus=getAllMenu()
    if menus:
        return jsonify(menus),200
    else:
        return jsonify({'error':'No menus found'}),404
    
@main_bp.route('/menu/delete/<int:menuId>',methods=['DELETE'])
def removeMenu(menuId):
    result=deleteMenu(menuId)
    if result:
        return jsonify(result),200
    else:
        return jsonify({'error':'Failed to delete menu'}),400
    
@main_bp.route('/category/create',methods=['POST'])
def newCategory():
    data=request.form.to_dict() or request.get_json()
    category=createCategory(data)
    if category:
        return jsonify(category),201
    else:
        return jsonify({'error':'Failed to create category'}),400
    
    
@main_bp.route('/category',methods=['GET'])
def getCategories():
    categories=getAllCategories()
    if categories:
        return jsonify(categories),200
    else:
        return jsonify({'error':'No categories found'}),404

@main_bp.route('/category/update/<int:categoryId>',methods=['PUT'])
def modifyCategory(categoryId):
    data=request.form.to_dict() or request.get_json()
    category=updateCategory(categoryId,data)
    if category:
        return jsonify(category),200
    else:
        return jsonify({'error':'Failed to update category'}),400


@main_bp.route('/category/<int:categoryId>',methods=['DELETE'])
def deleteCategory(categoryId):
    result=deleteCategory(categoryId)
    if result:
        return jsonify(result),200
    else:
        return jsonify({'error':'Failed to delete category'}),400
    