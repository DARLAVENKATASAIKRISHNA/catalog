from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import Materials, Base, MenuItem, User

engine = create_engine('sqlite:///materials.db')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()

# Create a dummy user
User1 = User(name="saikrishna darla", email="saikrishnadarla30@gmail.com",
             picture='https://o.aolcdn.com/images/dims3/GLOB/legacy_thumbnail'
             '/1200x630/format/jpg/quality/85/http%3A%2F%2Fi.huffpost.com%2'
             'Fgen%2F5334782%2Fimages%2Fn-TWIN-BABY-628x314.jpg')
session.add(User1)
session.commit()

# Menu for Clothes
materials1 = Materials(user_id=1, name="Clothes")

session.add(materials1)
session.commit()

menuItem1 = MenuItem(user_id=1, name="T-shirt",
                     descrption="it's kind of T-shirt", price="7050",
                     materials_id=1, materials=materials1)

session.add(menuItem1)
session.commit()


menuItem2 = MenuItem(user_id=1, name="FullHand T-shirt",
                     descrption="its's kind of FullHand shirt", price="2099",
                     materials_id=1, materials=materials1)

session.add(menuItem2)
session.commit()

menuItem3 = MenuItem(user_id=1, name="Formal shirt", descrption="it's kind of"
                     " Formal shirt which used during interview",
                     price="5050", materials_id=1, materials=materials1)

session.add(menuItem3)
session.commit()

menuItem4 = MenuItem(user_id=1, name="Pants", descrption="Pants which made"
                     " of jeans ", price="3099", materials_id=1,
                     materials=materials1)

session.add(menuItem4)
session.commit()

menuItem5 = MenuItem(user_id=1, name="FormalPants", descrption="Which wear in"
                     " the time of interview", price="7099", materials_id=1,
                     materials=materials1)

session.add(menuItem5)
session.commit()

menuItem6 = MenuItem(user_id=1, name="Tie", descrption="Wear in the term of"
                     " the interview", price="1099", materials_id=1,
                     materials=materials1)

session.add(menuItem6)
session.commit()

menuItem7 = MenuItem(user_id=1, name="Belt", descrption="Belt which is used"
                     " in terms for wear", price="$1099", materials_id=1,
                     materials=materials1)

session.add(menuItem7)
session.commit()

menuItem8 = MenuItem(user_id=1, name="Shoe", descrption="Shoe is used for the"
                     " wear to legs", price="3049", materials_id=1,
                     materials=materials1)

session.add(menuItem8)
session.commit()

# Menu for Home Made
materials2 = Materials(user_id=1, name="Home Made")

session.add(materials2)
session.commit()


menuItem1 = MenuItem(user_id=1, name="Chair", descrption="To sit",
                     price="7099", materials_id=2, materials=materials2)

session.add(menuItem1)
session.commit()

menuItem2 = MenuItem(user_id=1, name="Table", descrption="Table", price="6250",
                     materials_id=2, materials=materials2)

session.add(menuItem2)
session.commit()

menuItem3 = MenuItem(user_id=1, name="Sofa", descrption="Which is used to sit",
                     price="1500", materials_id=2, materials=materials2)

session.add(menuItem3)
session.commit()

menuItem4 = MenuItem(user_id=1, name="Dewan Guard ", descrption="which is"
                     " used for sleeping and sitting purpose", price="1200",
                     materials_id=2, materials=materials2)

session.add(menuItem4)
session.commit()

menuItem5 = MenuItem(user_id=1, name="window Courtens", descrption="which is"
                     " used for window wear ", price="1400", materials_id=2,
                     materials=materials2)

session.add(menuItem5)
session.commit()

menuItem6 = MenuItem(user_id=1, name="DoorCourtens", descrption="Using of"
                     " wear the doors", price="1200", materials_id=2,
                     materials=materials2)

session.add(menuItem6)
session.commit()

# Menu for Shoes
materials3 = Materials(user_id=1, name="Shoes")

session.add(materials3)
session.commit()


menuItem1 = MenuItem(user_id=1, name="fullshoe", descrption="wearing for"
                     " shoee", price="8099", materials_id=3,
                     materials=materials3)

session.add(menuItem1)
session.commit()

menuItem2 = MenuItem(user_id=1, name=" formalshoe", descrption=" wearing for"
                     " interview time", price="6099", materials_id=3,
                     materials=materials3)

session.add(menuItem2)
session.commit()

menuItem3 = MenuItem(user_id=1, name="Sportsshoe", descrption="Wearing for the"
                     " given time", price="9095", materials_id=3,
                     materials=materials3)

session.add(menuItem3)
session.commit()

menuItem4 = MenuItem(user_id=1, name="Schoolshoes", descrption="wearing for"
                     " school days", price="6099", materials_id=3,
                     materials=materials3)

session.add(menuItem4)
session.commit()

menuItem5 = MenuItem(user_id=1, name="casualshoes", descrption="wearing for"
                     " different ways", price="9050", materials_id=3,
                     materials=materials3)

session.add(menuItem5)
session.commit()

print ("added menu items!")
