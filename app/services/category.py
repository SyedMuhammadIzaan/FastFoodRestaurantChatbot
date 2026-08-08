from app.models.category import Category,db

def createCategory(data):
    try:
        if not data:
            return {"message": "No data provided"}, 400
        else:
            name=data.get('name')
            if not name:
                return {"message": "Name is required"}, 400
            category=Category(name=name)
            db.session.add(category)
            db.session.commit()
            return category.to_dict(), 201
    except Exception as e:
        return {"error": str(e)}, 500


def updateCategory(categoryId,data):
    try:
        if not categoryId or not data:
            return {"message": "Category ID and data are required"}, 400
        if type(categoryId) is not int:
            return {"message": "Category ID must be an integer"}, 400
        else:
            category=Category.query.get(categoryId)
            if not category:
                return {"message": "Category not found"}, 404
            else:
                category.name=data.get('name',category.name)
                db.session.commit()
                return category.to_dict(), 200
    except Exception as e:
        return {"error": str(e)}, 500
    
    
def getAllCategories():
    try:
        categories=Category.query.all()
        if not categories:
            return {"message": "No categories found"}, 404
        else:
            return [category.to_dict() for category in categories], 200
    except Exception as e:
        return {"error": str(e)}, 500

def deleteCategory(categoryId):
    try:
        if not categoryId:
            return {"message":"Category ID is required"}, 400
        else:
            category=Category.query.get(categoryId)
            if not category:
                return {"message":"Category not found"}, 404
            else:
                db.session.delete(category)
                db.session.commit()
                return {"message":"Category deleted successfully"}, 200
    except Exception as e:
        return {"error": str(e)}, 500
    
    
    