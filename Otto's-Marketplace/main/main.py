# import DAO
from dao.CustomerDAO import CustomerDAO
from dao.EmployeeDAO import EmployeeDAO
from dao.CommentDAO import CommentDAO
from dao.OrderDAO import OrderDAO
from dao.OrderItemDAO import OrderItemDAO
from dao.PositionDAO import PositionDAO
from dao.ProductDAO import ProductDAO
from dao.ProductCategoryDAO import ProductCategoryDAO
from dao.ShoppingCartDAO import ShoppingCartDAO
from dao.StoreDAO import StoreDAO
from dao.SupplierDAO import SupplierDAO

# import model
from model.Customer import Customer
from model.Employee import Employee
from model.Comment import Comment
from model.Order import Order
from model.OrderItem import OrderItem
from model.Position import Position
from model.Product import Product
from model.ProductCategory import ProductCategory
from model.ShoppingCart import ShoppingCart
from model.Store import Store
from model.Supplier import Supplier

# DAO Objects
comment_dao = CommentDAO()
customer_dao = CustomerDAO()
employee_dao = EmployeeDAO()
order_dao = OrderDAO()
orderItem_dao = OrderItemDAO()
position_dao = PositionDAO()
product_dao = ProductDAO()
product_category_dao = ProductCategoryDAO()
shopping_cart_dao = ShoppingCartDAO()
store_dao = StoreDAO()
supplier_dao = SupplierDAO()

# Model Objects


# SELECT * (
'''
lista = supplier_dao.select_all_suppliers()
for c in lista:
    print(c)
'''


# SELECT WHERE (print
'''
print(supplier_dao.select_supplier_by_key(10))
'''


# insert
'''
supplier = Supplier(None, 'OttoPex', 'Otto too', 'o@tto', '000000000')
supplier_dao.insert_supplier(supplier)
'''


# update

'''
store = Store(None, 'Otto1', ' ', ' ')
store_dao.update_store(store, 11)
'''



# delete
'''
'''
supplier_dao.delete_supplier(11)




