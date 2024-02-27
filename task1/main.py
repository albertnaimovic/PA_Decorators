# Create a shop item  manage system. The program main aim is to take inputs (create) from user (item name, amount, price, best_before if aplicable, date entered, item_type (electronic etc)):
#  - The name should be converted all capitals
#  - amount can't be negative
#  - price should be float.
#  - best before should be a date (YYYY-MM-DD)
#  - date entered should be (YYYY-MM-DD hh:mm:ss)
#  - total price value of entered items

# All methods in a class should have a error handling and logging handling through decorators.
# All data must be saved and retrieved from sql database.
# After submiting data I should be able to retreive all data from database based on item_type.


import datetime, os, time
from sqlalchemy import Column, Integer, String, Float, DateTime, create_engine, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine("sqlite:///item_database.db")
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()


class Items(Base):
    __tablename__ = "items"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    amount = Column(Integer)
    price = Column(Float)
    total_price = Column(Float)
    best_before = Column(String, nullable=True)
    category = Column(String)
    createdAt = Column(DateTime, default=text("(datetime('now', 'localtime'))"))

    def __init__(
        self,
        name: str,
        amount: int,
        price: float,
        total_price: float,
        best_before: str,
        category: str,
    ):
        self.name = name
        self.amount = amount
        self.price = price
        self.total_price = total_price
        self.best_before = best_before
        self.category = category


# Base.metadata.create_all(engine)


# class Item:
#     name: str
#     amount: int
#     price: int
#     total_price = price * amount
#     best_before: str
#     category: str


# cia turetu buti dataklase
def add_item() -> None:
    os.system("cls")
    print("\nAdding new item")
    name = str(input("\nEnter name: "))
    amount = int(input("Enter amount: "))
    price = float(input("Enter price: "))
    total_price = price * amount
    best_before = str(input("Enter best before if necessary: "))
    if best_before == "":
        best_before = None
    category = str(input("Enter category: "))
    return name, amount, price, best_before, category
    # atskira clase CRUD
    # new_item = Items(name.upper(), amount, price, total_price, best_before, category)
    # session.add(new_item)
    # session.commit()
    # print(f"Item {name} to category {category} has been added")
    # time.sleep(1.5)


def main_menu() -> None:
    os.system("cls")
    while True:
        os.system("cls")
        print("\n-----------\n|--Items--|\n-----------")
        category: str = input(
            "--Menu--\n1. Add item\n2. \n6. Exit\n\nEnter number of selection: "
        )
        if category.isnumeric() == True:
            if category == "1":
                add_item()
            elif category == "2":
                pass
            elif category == "3":
                pass
            elif category == "4":
                pass
            elif category == "5":
                pass
            elif category == "6":
                print("\nBye.")
                break
            else:
                print("\nThere is no such selection")
                time.sleep(1.5)
        else:
            print(
                "\nPlease enter number from list provided without any symbols and spaces."
            )
            time.sleep(2)


# main_menu()

print(add_item())
