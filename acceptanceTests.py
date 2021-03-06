from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
import time
import unittest


class WebPageTesting(unittest.TestCase):
	def setUp(self):
		chrome_options = Options()
		chrome_options.add_argument("--headless")
		self.browser = webdriver.Chrome(options=chrome_options)
		self.browser.get("http://127.0.0.1:3000")

#Tests that an item is added and displayed on the list correctly
	def test_add_item_name(self):
		remove_overlay = self.browser.find_element_by_id("CreateListButton")
		remove_overlay.click()
		delete = self.browser.find_element_by_id('deleteButton')
		delete.send_keys("\n")
		elem = self.browser.find_element_by_id('ShoppingListItem')
		elem.send_keys("Apple")
		quant = self.browser.find_element_by_id('ShoppingListQuantity')
		quant.send_keys(123)
		button = self.browser.find_element_by_id('SubmitButton')
		button.click()
		time.sleep(0.1)
		assert self.browser.find_element_by_id("shoppingList_0").text == "Apple"

	def test_add_item_category(self):
		remove_overlay = self.browser.find_element_by_id("CreateListButton")
		remove_overlay.click()
		delete = self.browser.find_element_by_id('deleteButton')
		delete.send_keys("\n")

		elem = self.browser.find_element_by_id('ShoppingListItem')
		elem.send_keys("Chicken")
		self.browser.find_element_by_id('dropdownButton').click()
		self.browser.find_element_by_id('categoryDropdown_Base_Item_0').click()
		assert self.browser.find_element_by_id('dropdownButton').get_attribute('innerHTML') == "Baked Goods"

	def test_add_multiple_items_with_distinct_categories(self):
		remove_overlay = self.browser.find_element_by_id("CreateListButton")
		remove_overlay.click()
		delete = self.browser.find_element_by_id('deleteButton')
		delete.send_keys("\n")

		elem = self.browser.find_element_by_id('ShoppingListItem')
		elem.send_keys("Chicken")
		self.browser.find_element_by_id('dropdownButton').click()
		self.browser.find_element_by_id('categoryDropdown_Base_Item_0').click()
		quant = self.browser.find_element_by_id('ShoppingListQuantity')
		quant.send_keys(123)
		button = self.browser.find_element_by_id('SubmitButton')
		button.click()
		time.sleep(0.1)
		assert self.browser.find_element_by_id('dropdownButton_0').get_attribute('innerHTML') == "Baked Goods"
		elem2 = self.browser.find_element_by_id('ShoppingListItem')
		elem2.send_keys("Apple")
		self.browser.find_element_by_id('dropdownButton').click()
		self.browser.find_element_by_id('categoryDropdown_Base_Item_3').click()
		quant1 = self.browser.find_element_by_id('ShoppingListQuantity')
		quant1.send_keys(345)
		button.click()
		time.sleep(0.1)
		assert self.browser.find_element_by_id('dropdownButton_1').get_attribute('innerHTML') == "Fresh Produce"

	def test_item_category_is_editable(self):
		remove_overlay = self.browser.find_element_by_id("CreateListButton")
		remove_overlay.click()
		delete = self.browser.find_element_by_id('deleteButton')
		delete.send_keys("\n")

		elem = self.browser.find_element_by_id('ShoppingListItem')
		elem.send_keys("Chicken")
		self.browser.find_element_by_id('dropdownButton').click()
		self.browser.find_element_by_id('categoryDropdown_Base_Item_0').click()
		assert self.browser.find_element_by_id('dropdownButton').get_attribute('innerHTML') == "Baked Goods"
		quant = self.browser.find_element_by_id('ShoppingListQuantity')
		quant.send_keys(123)
		button = self.browser.find_element_by_id('SubmitButton')
		button.click()
		time.sleep(0.1)

		assert self.browser.find_element_by_id('shoppingList_0').text == "Chicken"
		assert self.browser.find_element_by_id('dropdownButton_0').get_attribute('innerHTML') == "Baked Goods"
		
		self.browser.find_element_by_id('dropdownButton_0').click()
		self.browser.find_element_by_id('categoryDropdown_0_Item_6').click()
		time.sleep(0.1)
		assert self.browser.find_element_by_id('dropdownButton_0').get_attribute('innerHTML') == "Meat"

	def test_blank_item_category_gives_default_value(self):
		remove_overlay = self.browser.find_element_by_id("CreateListButton")
		remove_overlay.click()
		delete = self.browser.find_element_by_id('deleteButton')
		delete.send_keys("\n")
		elem = self.browser.find_element_by_id('ShoppingListItem')
		elem.send_keys("Apple")
		quant = self.browser.find_element_by_id('ShoppingListQuantity')
		quant.send_keys(123)
		button = self.browser.find_element_by_id('SubmitButton')
		button.click()
		time.sleep(0.1)
		assert self.browser.find_element_by_id('dropdownButton').get_attribute('innerHTML') == "Category"

	def test_edit_item_name(self):
		remove_overlay = self.browser.find_element_by_id("CreateListButton")
		remove_overlay.click()
		delete = self.browser.find_element_by_id('deleteButton')
		delete.send_keys("\n")
		elem = self.browser.find_element_by_id('ShoppingListItem')
		elem.send_keys("Apple")
		quant = self.browser.find_element_by_id('ShoppingListQuantity')
		quant.send_keys(123)
		button = self.browser.find_element_by_id('SubmitButton')
		button.click()
		time.sleep(0.1)
		editItem = self.browser.find_element_by_id("shoppingList_0")
		editItem.click()
		editItem.clear()
		editItem.send_keys("Banana")
		editItem.send_keys("\n")
		
		time.sleep(0.1)
		assert self.browser.find_element_by_id("shoppingList_0").text == "Banana"

	def test_add_multiple_items(self):
		remove_overlay = self.browser.find_element_by_id("CreateListButton")
		remove_overlay.click()
		delete = self.browser.find_element_by_id('deleteButton')
		delete.send_keys("\n")
		elem = self.browser.find_element_by_id('ShoppingListItem')
		elem.send_keys("Apple")
		quant = self.browser.find_element_by_id('ShoppingListQuantity')
		quant.send_keys(123)
		button = self.browser.find_element_by_id('SubmitButton')
		button.click()

		elem = self.browser.find_element_by_id('ShoppingListItem')
		elem.send_keys("Banana")
		quant = self.browser.find_element_by_id('ShoppingListQuantity')
		quant.send_keys(238049)
		button = self.browser.find_element_by_id('SubmitButton')
		button.click()
		
		time.sleep(0.1)
		assert self.browser.find_element_by_id("shoppingList_0").text == "Apple"
		assert self.browser.find_element_by_id("shoppingList_1").text == "Banana"
		
	def test_multiple_items_can_be_added_and_stored_in_db(self):
		remove_overlay = self.browser.find_element_by_id("CreateListButton")
		remove_overlay.click()
		delete = self.browser.find_element_by_id('deleteButton')
		delete.send_keys("\n")
		elem = self.browser.find_element_by_id('ShoppingListItem')
		elem.send_keys("Apple")
		quant = self.browser.find_element_by_id('ShoppingListQuantity')
		quant.send_keys(123)
		button = self.browser.find_element_by_id('SubmitButton')
		button.click()

		elem = self.browser.find_element_by_id('ShoppingListItem')
		elem.send_keys("Banana")
		quant = self.browser.find_element_by_id('ShoppingListQuantity')
		quant.send_keys(238049)
		button = self.browser.find_element_by_id('SubmitButton')
		button.click()
		
		time.sleep(0.1)
		assert self.browser.find_element_by_id("shoppingList_0").text == "Apple"
		assert self.browser.find_element_by_id("shoppingList_1").text == "Banana"

		self.browser.find_element_by_id('shareDropdown').click()
		token = self.browser.find_element_by_id('sharingLink').get_attribute('value')
		self.browser.find_element_by_id('loadList').click()
		loadFromToken= self.browser.find_element_by_id('viewListFromLink')
		loadFromToken.send_keys(token)
		self.browser.find_element_by_id('navigateToLink').click()

		time.sleep(0.1)
		assert self.browser.find_element_by_id("shoppingList_0").text == "Apple"
		assert self.browser.find_element_by_id("shoppingList_1").text == "Banana"

	def test_items_can_be_added_and_stored_in_db(self):
		remove_overlay = self.browser.find_element_by_id("CreateListButton")
		remove_overlay.click()
		delete = self.browser.find_element_by_id('deleteButton')
		delete.send_keys("\n")
		elem = self.browser.find_element_by_id('ShoppingListItem')
		elem.send_keys("Apple")
		quant = self.browser.find_element_by_id('ShoppingListQuantity')
		quant.send_keys(123)
		button = self.browser.find_element_by_id('SubmitButton')
		button.click()
		
		time.sleep(0.1)
		assert self.browser.find_element_by_id("shoppingList_0").text == "Apple"

		self.browser.find_element_by_id('shareDropdown').click()
		token = self.browser.find_element_by_id('sharingLink').get_attribute('value')
		self.browser.find_element_by_id('loadList').click()
		loadFromToken= self.browser.find_element_by_id('viewListFromLink')
		loadFromToken.send_keys(token)
		self.browser.find_element_by_id('navigateToLink').click()

		time.sleep(0.1)
		assert self.browser.find_element_by_id("shoppingList_0").text == "Apple"

	def test_mark_as_completed(self):
		remove_overlay = self.browser.find_element_by_id("CreateListButton")
		remove_overlay.click()
		delete = self.browser.find_element_by_id('deleteButton')
		delete.send_keys("\n")
		elem = self.browser.find_element_by_id('ShoppingListItem')
		elem.send_keys("Apple")
		quant = self.browser.find_element_by_id('ShoppingListQuantity')
		quant.send_keys(123)
		button = self.browser.find_element_by_id('SubmitButton')
		button.click()
		time.sleep(0.1)
		elem2 = self.browser.find_element_by_id('purchaseStatus_0')
		assert elem2.is_selected() == False
		elem2.click()
		assert elem2.is_selected() == True

# Test that one item can be marked as completed without changing the completion status of 
# the other items
	def test_one_item_can_be_marked_as_completed_in_isolation(self):
		remove_overlay = self.browser.find_element_by_id("CreateListButton")
		remove_overlay.click()
		delete = self.browser.find_element_by_id('deleteButton')
		delete.send_keys("\n")
		newItem = self.browser.find_element_by_id('ShoppingListItem')
		newItem.send_keys("Chocolate")
		quant = self.browser.find_element_by_id('ShoppingListQuantity')
		quant.send_keys(123)
		button = self.browser.find_element_by_id('SubmitButton')
		button.click()
		time.sleep(0.1)

		newItem2 = self.browser.find_element_by_id('ShoppingListItem')
		newItem2.send_keys("More Chocolate")
		quant = self.browser.find_element_by_id('ShoppingListQuantity')
		quant.send_keys(123)
		button.click()
		time.sleep(0.1)

		checkBox = self.browser.find_element_by_id('purchaseStatus_0')
		checkBox2 = self.browser.find_element_by_id('purchaseStatus_1')

		assert checkBox.is_selected() == False
		assert checkBox2.is_selected() == False

		checkBox.click()
		time.sleep(0.1)
		assert checkBox.is_selected() == True
		assert checkBox2.is_selected() == False

	# Test that the completion status of an item is stored and kept when the page is reloaded
	def test_completion_status_is_persistent(self):
		remove_overlay = self.browser.find_element_by_id("CreateListButton")
		remove_overlay.click()
		delete = self.browser.find_element_by_id('deleteButton')
		delete.send_keys("\n")
		newItem = self.browser.find_element_by_id('ShoppingListItem')
		newItem.send_keys("Chocolate")
		quant = self.browser.find_element_by_id('ShoppingListQuantity')
		quant.send_keys(123)
		button = self.browser.find_element_by_id('SubmitButton')
		button.click()
		time.sleep(0.1)
		checkBox = self.browser.find_element_by_id('purchaseStatus_0')
		time.sleep(0.2)
		assert checkBox.is_selected() == False
		checkBox.click()
		time.sleep(0.1)
		assert checkBox.is_selected() == True

		self.browser.find_element_by_id('shareDropdown').click()
		token = self.browser.find_element_by_id('sharingLink').get_attribute('value')
		self.browser.find_element_by_id('loadList').click()
		loadFromToken= self.browser.find_element_by_id('viewListFromLink')
		loadFromToken.send_keys(token)
		self.browser.find_element_by_id('navigateToLink').click()

		time.sleep(0.1)
		checkBoxReloaded = self.browser.find_element_by_id('purchaseStatus_0')
		assert checkBoxReloaded.is_selected() == True
		checkBoxReloaded.click()
		time.sleep(0.1)
		assert checkBoxReloaded.is_selected() == False

	# Test that the completion status of multiple items are stored and kept when the page is reloaded
	def test_completion_status_of_multiple_items_are_persistent(self):
		remove_overlay = self.browser.find_element_by_id("CreateListButton")
		remove_overlay.click()
		delete = self.browser.find_element_by_id('deleteButton')
		delete.send_keys("\n")
		newItem = self.browser.find_element_by_id('ShoppingListItem')
		newItem.send_keys("Chocolate")
		quant = self.browser.find_element_by_id('ShoppingListQuantity')
		quant.send_keys(123)
		button = self.browser.find_element_by_id('SubmitButton')
		button.click()
		time.sleep(0.1)
		newItem2 = self.browser.find_element_by_id('ShoppingListItem')
		newItem2.send_keys("More Chocolate")
		quant = self.browser.find_element_by_id('ShoppingListQuantity')
		quant.send_keys(123)
		button.click()
		time.sleep(0.1)
		checkBox = self.browser.find_element_by_id('purchaseStatus_0')
		assert checkBox.is_selected() == False
		checkBox2 = self.browser.find_element_by_id('purchaseStatus_1')
		assert checkBox2.is_selected() == False
		checkBox.click()
		time.sleep(0.1)
		checkBox2.click()
		time.sleep(0.1)
		assert checkBox.is_selected() == True
		assert checkBox2.is_selected() == True

		self.browser.find_element_by_id('shareDropdown').click()
		token = self.browser.find_element_by_id('sharingLink').get_attribute('value')
		self.browser.find_element_by_id('loadList').click()
		loadFromToken= self.browser.find_element_by_id('viewListFromLink')
		loadFromToken.send_keys(token)
		self.browser.find_element_by_id('navigateToLink').click()

		checkBoxReloaded = self.browser.find_element_by_id('purchaseStatus_0')
		assert checkBoxReloaded.is_selected() == True
		checkBoxReloaded2 = self.browser.find_element_by_id('purchaseStatus_1')
		assert checkBoxReloaded2.is_selected() == True

# Test that the completion status of multiple items are stored and kept when the page is reloaded
	def test_completion_status_of_multiple_items_with_different_completion_statuses_are_persistent(self):
		remove_overlay = self.browser.find_element_by_id("CreateListButton")
		remove_overlay.click()
		time.sleep(2)
		delete = self.browser.find_element_by_id('deleteButton')
		delete.send_keys("\n")
		newItem = self.browser.find_element_by_id('ShoppingListItem')
		newItem.send_keys("Kit Kat")
		quant = self.browser.find_element_by_id('ShoppingListQuantity')
		quant.send_keys(123)
		button = self.browser.find_element_by_id('SubmitButton')
		button.click()
		time.sleep(0.1)
		newItem2 = self.browser.find_element_by_id('ShoppingListItem')
		newItem2.send_keys("Bar One")
		quant = self.browser.find_element_by_id('ShoppingListQuantity')
		quant.send_keys(123)
		button.click()
		time.sleep(0.1)
		checkBox = self.browser.find_element_by_id('purchaseStatus_0')
		checkBox2 = self.browser.find_element_by_id('purchaseStatus_1')
		assert checkBox.is_selected() == False
		assert checkBox2.is_selected() == False
		checkBox.click()
		time.sleep(0.1)
		checkBox = self.browser.find_element_by_id('purchaseStatus_0')
		checkBox2 = self.browser.find_element_by_id('purchaseStatus_1')
		time.sleep(0.1)
		assert checkBox.is_selected() == True
		assert checkBox2.is_selected() == False

		self.browser.find_element_by_id('shareDropdown').click()
		token = self.browser.find_element_by_id('sharingLink').get_attribute('value')
		self.browser.find_element_by_id('loadList').click()
		loadFromToken= self.browser.find_element_by_id('viewListFromLink')
		loadFromToken.send_keys(token)
		self.browser.find_element_by_id('navigateToLink').click()

		checkBoxReloaded = self.browser.find_element_by_id('purchaseStatus_0')
		checkBoxReloaded2 = self.browser.find_element_by_id('purchaseStatus_1')
		time.sleep(2)
		assert checkBoxReloaded.is_selected() == True
		assert checkBoxReloaded2.is_selected() == False

	def test_add_item_quantity(self):
		remove_overlay = self.browser.find_element_by_id("CreateListButton")
		remove_overlay.click()
		delete = self.browser.find_element_by_id('deleteButton')
		delete.send_keys("\n")
		elem = self.browser.find_element_by_id('ShoppingListItem')
		elem.send_keys("Apple")
		quant = self.browser.find_element_by_id('ShoppingListQuantity')
		quant.send_keys(123)
		button = self.browser.find_element_by_id('SubmitButton')
		button.click()
		time.sleep(0.1)
		assert self.browser.find_element_by_id("shoppingListQuantity_0").text == "123"

	def test_add_item_quantity_and_verify_that_quantity_is_stored_in_database_and_rendered_on_page_after_reload(self):
		remove_overlay = self.browser.find_element_by_id("CreateListButton")
		remove_overlay.click()
		delete = self.browser.find_element_by_id('deleteButton')
		delete.send_keys("\n")
		elem = self.browser.find_element_by_id('ShoppingListItem')
		elem.send_keys("Apple")
		quant = self.browser.find_element_by_id('ShoppingListQuantity')
		quant.send_keys(123)
		button = self.browser.find_element_by_id('SubmitButton')
		button.click()

		self.browser.find_element_by_id('shareDropdown').click()
		token = self.browser.find_element_by_id('sharingLink').get_attribute('value')
		self.browser.find_element_by_id('loadList').click()
		loadFromToken= self.browser.find_element_by_id('viewListFromLink')
		loadFromToken.send_keys(token)
		self.browser.find_element_by_id('navigateToLink').click()
		time.sleep(0.1)
		assert self.browser.find_element_by_id("shoppingListQuantity_0").text == "123"

	def test_add_item_quantity_for_multiple_items(self):
		remove_overlay = self.browser.find_element_by_id("CreateListButton")
		remove_overlay.click()
		delete = self.browser.find_element_by_id('deleteButton')
		delete.send_keys("\n")
		elem = self.browser.find_element_by_id('ShoppingListItem')
		elem.send_keys("Apple")
		quant = self.browser.find_element_by_id('ShoppingListQuantity')
		quant.send_keys(123)
		button = self.browser.find_element_by_id('SubmitButton')
		button.click()
		elem = self.browser.find_element_by_id('ShoppingListItem')
		elem.send_keys("Perterdeeeeeeers")
		quant = self.browser.find_element_by_id('ShoppingListQuantity')
		quant.send_keys(1234)
		button = self.browser.find_element_by_id('SubmitButton')
		button.click()

		self.browser.find_element_by_id('shareDropdown').click()
		token = self.browser.find_element_by_id('sharingLink').get_attribute('value')

		self.browser.find_element_by_id('loadList').click()
		loadFromToken= self.browser.find_element_by_id('viewListFromLink')
		loadFromToken.send_keys(token)
		self.browser.find_element_by_id('navigateToLink').click()
		time.sleep(0.1)
		assert self.browser.find_element_by_id("shoppingListQuantity_0").text == "123"
		assert self.browser.find_element_by_id("shoppingListQuantity_1").text == "1234"

	def test_add_item_quantity_for_multiple_items_and_verify_that_quantity_is_stored_in_database_and_rendered_on_page_after_reload(self):
		remove_overlay = self.browser.find_element_by_id("CreateListButton")
		remove_overlay.click()
		delete = self.browser.find_element_by_id('deleteButton')
		delete.send_keys("\n")
		elem = self.browser.find_element_by_id('ShoppingListItem')
		elem.send_keys("Apple")
		quant = self.browser.find_element_by_id('ShoppingListQuantity')
		quant.send_keys(123)
		button = self.browser.find_element_by_id('SubmitButton')
		button.click()
		elem = self.browser.find_element_by_id('ShoppingListItem')
		elem.send_keys("Perterdeeeeeeers")
		quant = self.browser.find_element_by_id('ShoppingListQuantity')
		quant.send_keys(1234)
		button = self.browser.find_element_by_id('SubmitButton')
		button.click()
		time.sleep(0.1)
		assert self.browser.find_element_by_id("shoppingListQuantity_0").text == "123"
		assert self.browser.find_element_by_id("shoppingListQuantity_1").text == "1234"

		self.browser.find_element_by_id('shareDropdown').click()
		token = self.browser.find_element_by_id('sharingLink').get_attribute('value')

		self.browser.find_element_by_id('loadList').click()
		loadFromToken= self.browser.find_element_by_id('viewListFromLink')
		loadFromToken.send_keys(token)
		self.browser.find_element_by_id('navigateToLink').click()

		time.sleep(0.1)
		assert self.browser.find_element_by_id("shoppingListQuantity_0").text == "123"
		assert self.browser.find_element_by_id("shoppingListQuantity_1").text == "1234"

	def test_add_two_shopping_lists_and_load_the_first_one(self):
		remove_overlay = self.browser.find_element_by_id("CreateListButton")
		remove_overlay.click()
		delete = self.browser.find_element_by_id('deleteButton')
		delete.send_keys("\n")
		elem = self.browser.find_element_by_id('ShoppingListItem')
		elem.send_keys("Apple")
		quant = self.browser.find_element_by_id('ShoppingListQuantity')
		quant.send_keys(123)
		button = self.browser.find_element_by_id('SubmitButton')
		button.click()
		elem = self.browser.find_element_by_id('ShoppingListItem')
		elem.send_keys("Perterdeeeeeeers")
		quant = self.browser.find_element_by_id('ShoppingListQuantity')
		quant.send_keys(1234)
		button = self.browser.find_element_by_id('SubmitButton')
		button.click()
		self.browser.find_element_by_id('shareDropdown').click()
		token = self.browser.find_element_by_id('sharingLink').get_attribute('value')

		remove_overlay = self.browser.find_element_by_id("createList")
		remove_overlay.click()
		elem = self.browser.find_element_by_id('ShoppingListItem')
		elem.send_keys("Apple2")
		quant = self.browser.find_element_by_id('ShoppingListQuantity')
		quant.send_keys(238049)
		button = self.browser.find_element_by_id('SubmitButton')
		button.click()
		elem = self.browser.find_element_by_id('ShoppingListItem')
		elem.send_keys("Perterdeeeeeeers2")
		quant = self.browser.find_element_by_id('ShoppingListQuantity')
		quant.send_keys(7896)
		button = self.browser.find_element_by_id('SubmitButton')
		button.click()

		self.browser.find_element_by_id('loadList').click()
		loadFromToken= self.browser.find_element_by_id('viewListFromLink')
		loadFromToken.send_keys(token)
		self.browser.find_element_by_id('navigateToLink').click()
		
		time.sleep(0.1)
		assert self.browser.find_element_by_id("shoppingList_0").text == "Apple"

	def test_add_item_to_loaded_shopping_list(self):
		remove_overlay = self.browser.find_element_by_id("CreateListButton")
		remove_overlay.click()
		delete = self.browser.find_element_by_id('deleteButton')
		delete.send_keys("\n")
		elem = self.browser.find_element_by_id('ShoppingListItem')
		elem.send_keys("Apple")
		quant = self.browser.find_element_by_id('ShoppingListQuantity')
		quant.send_keys(123)
		button = self.browser.find_element_by_id('SubmitButton')
		button.click()
		self.browser.find_element_by_id('shareDropdown').click()
		token = self.browser.find_element_by_id('sharingLink').get_attribute('value')

		remove_overlay = self.browser.find_element_by_id("createList")
		remove_overlay.click()
		elem = self.browser.find_element_by_id('ShoppingListItem')
		elem.send_keys("Apple2")
		quant = self.browser.find_element_by_id('ShoppingListQuantity')
		quant.send_keys(238049)
		button = self.browser.find_element_by_id('SubmitButton')
		button.click()
		elem = self.browser.find_element_by_id('ShoppingListItem')
		elem.send_keys("Perterdeeeeeeers2")
		quant = self.browser.find_element_by_id('ShoppingListQuantity')
		quant.send_keys(7896)
		button = self.browser.find_element_by_id('SubmitButton')
		button.click()

		self.browser.find_element_by_id('loadList').click()
		loadFromToken= self.browser.find_element_by_id('viewListFromLink')
		loadFromToken.send_keys(token)
		self.browser.find_element_by_id('navigateToLink').click()
		elem = self.browser.find_element_by_id('ShoppingListItem')
		elem.send_keys("Perterdeeeeeeers")
		quant = self.browser.find_element_by_id('ShoppingListQuantity')
		quant.send_keys(1234)
		button = self.browser.find_element_by_id('SubmitButton')
		button.click()
		
		time.sleep(0.1)
		assert self.browser.find_element_by_id("shoppingList_0").text == "Apple"
		assert self.browser.find_element_by_id("shoppingList_1").text == "Perterdeeeeeeers"

	def test_add_item_to_loaded_shopping_list_and_save_in_db(self):
		remove_overlay = self.browser.find_element_by_id("CreateListButton")
		remove_overlay.click()
		delete = self.browser.find_element_by_id('deleteButton')
		delete.send_keys("\n")
		elem = self.browser.find_element_by_id('ShoppingListItem')
		elem.send_keys("Apple")
		quant = self.browser.find_element_by_id('ShoppingListQuantity')
		quant.send_keys(123)
		button = self.browser.find_element_by_id('SubmitButton')
		button.click()
		self.browser.find_element_by_id('shareDropdown').click()
		token = self.browser.find_element_by_id('sharingLink').get_attribute('value')

		remove_overlay = self.browser.find_element_by_id("createList")
		remove_overlay.click()
		elem = self.browser.find_element_by_id('ShoppingListItem')
		elem.send_keys("Apple2")
		quant = self.browser.find_element_by_id('ShoppingListQuantity')
		quant.send_keys(238049)
		button = self.browser.find_element_by_id('SubmitButton')
		button.click()
		elem = self.browser.find_element_by_id('ShoppingListItem')
		elem.send_keys("Perterdeeeeeeers2")
		quant = self.browser.find_element_by_id('ShoppingListQuantity')
		quant.send_keys(7896)
		button = self.browser.find_element_by_id('SubmitButton')
		button.click()

		self.browser.find_element_by_id('loadList').click()
		loadFromToken= self.browser.find_element_by_id('viewListFromLink')
		loadFromToken.send_keys(token)
		self.browser.find_element_by_id('navigateToLink').click()
		elem = self.browser.find_element_by_id('ShoppingListItem')
		elem.send_keys("Chocolate")
		quant = self.browser.find_element_by_id('ShoppingListQuantity')
		quant.send_keys(1234)
		button = self.browser.find_element_by_id('SubmitButton')
		button.click()
		
		time.sleep(0.1)
		assert self.browser.find_element_by_id("shoppingList_0").text == "Apple"
		assert self.browser.find_element_by_id("shoppingList_1").text == "Chocolate"

		self.browser.find_element_by_id('loadList').click()
		loadFromToken.send_keys(token)
		self.browser.find_element_by_id('navigateToLink').click()
		assert self.browser.find_element_by_id("shoppingList_0").text == "Apple"
		assert self.browser.find_element_by_id("shoppingList_1").text == "Chocolate"

	def test_edit_item_in_shopping_list_and_save_in_db(self):
		remove_overlay = self.browser.find_element_by_id("CreateListButton")
		remove_overlay.click()
		delete = self.browser.find_element_by_id('deleteButton')
		delete.send_keys("\n")
		elem = self.browser.find_element_by_id('ShoppingListItem')
		elem.send_keys("Apple")
		quant = self.browser.find_element_by_id('ShoppingListQuantity')
		quant.send_keys(123)
		button = self.browser.find_element_by_id('SubmitButton')
		button.click()
		self.browser.find_element_by_id('shareDropdown').click()
		token = self.browser.find_element_by_id('sharingLink').get_attribute('value')

		remove_overlay = self.browser.find_element_by_id("createList")
		remove_overlay.click()
		elem = self.browser.find_element_by_id('ShoppingListItem')
		elem.send_keys("Apple2")
		quant = self.browser.find_element_by_id('ShoppingListQuantity')
		quant.send_keys(238049)
		button = self.browser.find_element_by_id('SubmitButton')
		button.click()

		self.browser.find_element_by_id('loadList').click()
		loadFromToken= self.browser.find_element_by_id('viewListFromLink')
		loadFromToken.send_keys(token)
		self.browser.find_element_by_id('navigateToLink').click()
		time.sleep(0.1)
		editBox = self.browser.find_element_by_id("shoppingList_0")
		editBox.click()
		editBox.clear()
		editBox.send_keys("Chocolate")
		editBox.send_keys("\n")
		
		time.sleep(0.1)
		assert self.browser.find_element_by_id("shoppingList_0").text == "Chocolate"

		self.browser.find_element_by_id('loadList').click()
		loadFromToken.send_keys(token)
		self.browser.find_element_by_id('navigateToLink').click()
		assert self.browser.find_element_by_id("shoppingList_0").text == "Chocolate"

	# Test that an item can be deleted
	def test_item_deletion(self):
		remove_overlay = self.browser.find_element_by_id("CreateListButton")
		remove_overlay.click()
		delete = self.browser.find_element_by_id('deleteButton')
		delete.send_keys("\n")
		newItem = self.browser.find_element_by_id('ShoppingListItem')
		newItem.send_keys("Astros")
		quant = self.browser.find_element_by_id('ShoppingListQuantity')
		quant.send_keys(1000)
		button = self.browser.find_element_by_id('SubmitButton')
		button.click()
		time.sleep(0.1)
		assert len(self.browser.find_elements_by_id("shoppingList_0")) == 1

		button = self.browser.find_element_by_id('deleteButton_0')
		button.click()
		time.sleep(0.1)
		assert len(self.browser.find_elements_by_id("shoppingList_0")) == 0

	# Test that multiple items can be deleted
	def test_multiple_item_deletion(self):
		remove_overlay = self.browser.find_element_by_id("CreateListButton")
		remove_overlay.click()
		delete = self.browser.find_element_by_id('deleteButton')
		delete.send_keys("\n")
		newItem = self.browser.find_element_by_id('ShoppingListItem')
		newItem.send_keys("Astros")
		quant = self.browser.find_element_by_id('ShoppingListQuantity')
		quant.send_keys(1000)
		button = self.browser.find_element_by_id('SubmitButton')
		button.click()
		time.sleep(0.1)
		assert len(self.browser.find_elements_by_id("shoppingList_0")) == 1
		
		newItem.send_keys("Smarties")
		quant.send_keys(2000)
		button.click()
		time.sleep(0.1)
		assert len(self.browser.find_elements_by_id("shoppingList_1")) == 1

		button = self.browser.find_element_by_id('deleteButton_0')
		button.click()
		time.sleep(0.1)
		assert len(self.browser.find_elements_by_id("shoppingList_0")) == 0
		
		assert len(self.browser.find_elements_by_id("shoppingList_1")) == 1
		button = self.browser.find_element_by_id('deleteButton_1')
		button.click()
		time.sleep(0.1)
		assert len(self.browser.find_elements_by_id("shoppingList_1")) == 0

	# Test that an item can be deleted and remains deleted after reloading the list
	def test_item_deletion_persistence(self):
		remove_overlay = self.browser.find_element_by_id("CreateListButton")
		remove_overlay.click()
		delete = self.browser.find_element_by_id('deleteButton')
		delete.send_keys("\n")
		newItem = self.browser.find_element_by_id('ShoppingListItem')
		newItem.send_keys("Astros")
		quant = self.browser.find_element_by_id('ShoppingListQuantity')
		quant.send_keys(1000)
		button = self.browser.find_element_by_id('SubmitButton')
		button.click()
		time.sleep(0.1)
		assert len(self.browser.find_elements_by_id("shoppingList_0")) == 1
		
		newItem.send_keys("Smarties")
		quant.send_keys(2000)
		button.click()
		time.sleep(0.1)
		assert len(self.browser.find_elements_by_id("shoppingList_1")) == 1

		button = self.browser.find_element_by_id('deleteButton_0')
		button.click()
		time.sleep(0.1)
		assert len(self.browser.find_elements_by_id("shoppingList_0")) == 0

		self.browser.find_element_by_id('shareDropdown').click()
		token = self.browser.find_element_by_id('sharingLink').get_attribute('value')
		self.browser.find_element_by_id('loadList').click()
		loadFromToken= self.browser.find_element_by_id('viewListFromLink')
		loadFromToken.send_keys(token)
		self.browser.find_element_by_id('navigateToLink').click()
		time.sleep(0.1)
		
		assert len(self.browser.find_elements_by_id("shoppingList_0")) == 1
		assert self.browser.find_element_by_id('shoppingList_0').text == "Smarties"
		assert len(self.browser.find_elements_by_id("shoppingList_1")) == 0

	# Test that multiple items can be deleted and remain deleted after reloading the list
	def test_multiple_item_deletion_persistence(self):
		remove_overlay = self.browser.find_element_by_id("CreateListButton")
		remove_overlay.click()
		delete = self.browser.find_element_by_id('deleteButton')
		delete.send_keys("\n")
		newItem = self.browser.find_element_by_id('ShoppingListItem')
		newItem.send_keys("Astros")
		quant = self.browser.find_element_by_id('ShoppingListQuantity')
		quant.send_keys(1000)
		button = self.browser.find_element_by_id('SubmitButton')
		button.click()
		time.sleep(0.1)
		assert len(self.browser.find_elements_by_id("shoppingList_0")) == 1
		
		newItem.send_keys("Smarties")
		quant.send_keys(2000)
		button.click()
		time.sleep(0.1)
		assert len(self.browser.find_elements_by_id("shoppingList_1")) == 1
		
		newItem.send_keys("Speckled Eggs")
		quant.send_keys(3001)
		button.click()
		time.sleep(0.1)
		assert len(self.browser.find_elements_by_id("shoppingList_2")) == 1

		button = self.browser.find_element_by_id('deleteButton_0')
		button.click()
		time.sleep(0.1)
		assert len(self.browser.find_elements_by_id("shoppingList_0")) == 0
		
		button = self.browser.find_element_by_id('deleteButton_2')
		button.click()
		time.sleep(0.1)
		assert len(self.browser.find_elements_by_id("shoppingList_2")) == 0

		self.browser.find_element_by_id('shareDropdown').click()
		token = self.browser.find_element_by_id('sharingLink').get_attribute('value')
		self.browser.find_element_by_id('loadList').click()
		loadFromToken= self.browser.find_element_by_id('viewListFromLink')
		loadFromToken.send_keys(token)
		self.browser.find_element_by_id('navigateToLink').click()
		time.sleep(0.1)
		
		assert len(self.browser.find_elements_by_id("shoppingList_0")) == 1
		assert self.browser.find_element_by_id('shoppingList_0').text == "Smarties"
		assert len(self.browser.find_elements_by_id("shoppingList_1")) == 0
		assert len(self.browser.find_elements_by_id("shoppingList_2")) == 0

	def test_share_list_with_email_and_render_email_on_share_list(self):
		remove_overlay = self.browser.find_element_by_id("CreateListButton")
		remove_overlay.click()
		delete = self.browser.find_element_by_id('deleteButton')
		delete.send_keys("\n")
		elem = self.browser.find_element_by_id('ShoppingListItem')
		elem.send_keys("Apple")
		quant = self.browser.find_element_by_id('ShoppingListQuantity')
		quant.send_keys(123)
		button = self.browser.find_element_by_id('SubmitButton')
		button.click()
		share_email = self.browser.find_element_by_id("email-share")
		share_email.send_keys("test1@mail.com")
		share_button = self.browser.find_element_by_id("share-email-button")
		share_button.send_keys("\n")
		time.sleep(0.1)
		assert self.browser.find_element_by_id("emailShare_0").text == "test1@mail.com"

	def test_share_list_with_email_and_verify_that_email_is_stored_in_databse_and_render_email_on_share_list(self):
		remove_overlay = self.browser.find_element_by_id("CreateListButton")
		remove_overlay.click()
		delete = self.browser.find_element_by_id('deleteButton')
		delete.send_keys("\n")
		elem = self.browser.find_element_by_id('ShoppingListItem')
		elem.send_keys("Apple")
		quant = self.browser.find_element_by_id('ShoppingListQuantity')
		quant.send_keys(123)
		button = self.browser.find_element_by_id('SubmitButton')
		button.click()
		share_email = self.browser.find_element_by_id("email-share")
		share_email.send_keys("test1@mail.com")
		share_button = self.browser.find_element_by_id("share-email-button")
		share_button.send_keys("\n")

		self.browser.find_element_by_id('shareDropdown').click()
		token = self.browser.find_element_by_id('sharingLink').get_attribute('value')
		self.browser.find_element_by_id('loadList').click()
		loadFromToken= self.browser.find_element_by_id('viewListFromLink')
		loadFromToken.send_keys(token)
		self.browser.find_element_by_id('navigateToLink').click()
		time.sleep(0.1)
		assert self.browser.find_element_by_id("emailShare_0").text == "test1@mail.com"

	def test_share_list_with_multiple_email_and_render_emails_on_share_list(self):
		remove_overlay = self.browser.find_element_by_id("CreateListButton")
		remove_overlay.click()
		delete = self.browser.find_element_by_id('deleteButton')
		delete.send_keys("\n")
		elem = self.browser.find_element_by_id('ShoppingListItem')
		elem.send_keys("Apple")
		quant = self.browser.find_element_by_id('ShoppingListQuantity')
		quant.send_keys(123)
		button = self.browser.find_element_by_id('SubmitButton')
		button.click()
		share_email = self.browser.find_element_by_id("email-share")
		share_email.send_keys("test1@mail.com")
		share_button = self.browser.find_element_by_id("share-email-button")
		share_button.send_keys("\n")
		share_email = self.browser.find_element_by_id("email-share")
		share_email.send_keys("test2@mail.com")
		share_button = self.browser.find_element_by_id("share-email-button")
		share_button.send_keys("\n")
		time.sleep(0.1)
		assert self.browser.find_element_by_id("emailShare_0").text == "test1@mail.com"
		assert self.browser.find_element_by_id("emailShare_1").text == "test2@mail.com"

	def test_share_list_with_multiple_email_and_verify_that_email_is_stored_in_databse_and_render_email_on_share_list(self):
		remove_overlay = self.browser.find_element_by_id("CreateListButton")
		remove_overlay.click()
		delete = self.browser.find_element_by_id('deleteButton')
		delete.send_keys("\n")
		elem = self.browser.find_element_by_id('ShoppingListItem')
		elem.send_keys("Apple")
		quant = self.browser.find_element_by_id('ShoppingListQuantity')
		quant.send_keys(123)
		button = self.browser.find_element_by_id('SubmitButton')
		button.click()
		share_email = self.browser.find_element_by_id("email-share")
		share_email.send_keys("test1@mail.com")
		share_button = self.browser.find_element_by_id("share-email-button")
		share_button.send_keys("\n")
		share_email = self.browser.find_element_by_id("email-share")
		share_email.send_keys("test2@mail.com")
		share_button = self.browser.find_element_by_id("share-email-button")
		share_button.send_keys("\n")

		self.browser.find_element_by_id('shareDropdown').click()
		token = self.browser.find_element_by_id('sharingLink').get_attribute('value')
		self.browser.find_element_by_id('loadList').click()
		loadFromToken= self.browser.find_element_by_id('viewListFromLink')
		loadFromToken.send_keys(token)
		self.browser.find_element_by_id('navigateToLink').click()
		time.sleep(0.1)
		assert self.browser.find_element_by_id("emailShare_0").text == "test1@mail.com"
		assert self.browser.find_element_by_id("emailShare_1").text == "test2@mail.com"

	def test_multiple_item_sort_by_purchased(self):
		remove_overlay = self.browser.find_element_by_id("CreateListButton")
		remove_overlay.click()
		delete = self.browser.find_element_by_id('deleteButton')
		delete.send_keys("\n")
		newItem = self.browser.find_element_by_id('ShoppingListItem')
		newItem.send_keys("Astros")
		quant = self.browser.find_element_by_id('ShoppingListQuantity')
		quant.send_keys(1000)
		button = self.browser.find_element_by_id('SubmitButton')
		button.click()
		time.sleep(0.1)
		
		newItem.send_keys("Smarties")
		quant.send_keys(2000)
		button.click()
		time.sleep(0.1)
		
		newItem.send_keys("Speckled Eggs")
		quant.send_keys(3001)
		button.click()
		time.sleep(0.1)
		
		assert self.browser.find_element_by_id('purchaseStatus_0').is_selected() == False
		assert self.browser.find_element_by_id('shoppingList_0').text == "Astros"
		assert self.browser.find_element_by_id('purchaseStatus_1').is_selected() == False
		assert self.browser.find_element_by_id('shoppingList_1').text == "Smarties"
		assert self.browser.find_element_by_id('purchaseStatus_2').is_selected() == False
		assert self.browser.find_element_by_id('shoppingList_2').text == "Speckled Eggs"
		time.sleep(0.1)
		self.browser.find_element_by_id('purchaseStatus_1').click()
		time.sleep(0.1)
		assert self.browser.find_element_by_id('purchaseStatus_1').is_selected() == True

		self.browser.find_element_by_id('actionsDropdown').click()
		time.sleep(0.1)
		self.browser.find_element_by_id('sortButton').click()
		time.sleep(0.1)
		
		assert self.browser.find_element_by_id('purchaseStatus_0').is_selected() == False
		assert self.browser.find_element_by_id('shoppingList_0').text == "Astros"
		assert self.browser.find_element_by_id('purchaseStatus_1').is_selected() == False
		assert self.browser.find_element_by_id('shoppingList_1').text == "Speckled Eggs"
		assert self.browser.find_element_by_id('purchaseStatus_2').is_selected() == True
		assert self.browser.find_element_by_id('shoppingList_2').text == "Smarties"		

	def test_remove_email_from_shared_list_and_verify_removed_email_is_no_longer_in_db_when_reloaded(self):
		remove_overlay = self.browser.find_element_by_id("CreateListButton")
		remove_overlay.click()
		delete = self.browser.find_element_by_id('deleteButton')
		delete.send_keys("\n")
		elem = self.browser.find_element_by_id('ShoppingListItem')
		elem.send_keys("Apple")
		quant = self.browser.find_element_by_id('ShoppingListQuantity')
		quant.send_keys(123)
		button = self.browser.find_element_by_id('SubmitButton')
		button.click()
		share_email = self.browser.find_element_by_id("email-share")
		share_email.send_keys("test1@mail.com")
		share_button = self.browser.find_element_by_id("share-email-button")
		share_button.send_keys("\n")
		share_email = self.browser.find_element_by_id("email-share")
		share_email.send_keys("test2@mail.com")
		share_button = self.browser.find_element_by_id("share-email-button")
		share_button.send_keys("\n")
		time.sleep(0.1)
		assert self.browser.find_element_by_id("emailShareClass_0").text == "test1@mail.com"
		assert self.browser.find_element_by_id("emailShareClass_1").text == "test2@mail.com"

		remove_email = self.browser.find_element_by_id("emailDelete_0")
		remove_email.click()
		self.browser.find_element_by_id('shareDropdown').click()
		token = self.browser.find_element_by_id('sharingLink').get_attribute('value')
		self.browser.find_element_by_id('loadList').click()
		loadFromToken= self.browser.find_element_by_id('viewListFromLink')
		loadFromToken.send_keys(token)
		self.browser.find_element_by_id('navigateToLink').click()
		time.sleep(0.1)
		assert self.browser.find_element_by_id("emailShareClass_0").text == "test2@mail.com"

	def test_add_shopping_list_name(self):
		remove_overlay = self.browser.find_element_by_id("CreateListButton")
		remove_overlay.click()
		delete = self.browser.find_element_by_id('deleteButton')
		delete.send_keys("\n")

		self.browser.find_element_by_id('actionsDropdown').click()
		time.sleep(0.1)
		self.browser.find_element_by_id('addName').click()
		time.sleep(0.1)
		self.browser.find_element_by_id('listName').send_keys("My List")
		self.browser.find_element_by_id('saveListName').click()

		assert self.browser.find_element_by_id("printName").text == "My List"

	def test_shopping_list_name_can_be_saved(self):
		remove_overlay = self.browser.find_element_by_id("CreateListButton")
		remove_overlay.click()
		delete = self.browser.find_element_by_id('deleteButton')
		delete.send_keys("\n")

		self.browser.find_element_by_id('actionsDropdown').click()
		time.sleep(0.1)
		self.browser.find_element_by_id('addName').click()
		time.sleep(0.1)
		self.browser.find_element_by_id('listName').send_keys("My List")
		self.browser.find_element_by_id('saveListName').click()
		time.sleep(0.1)
		assert self.browser.find_element_by_id("printName").text == "My List"

		self.browser.find_element_by_id('shareDropdown').click()
		token = self.browser.find_element_by_id('sharingLink').get_attribute('value')
		self.browser.find_element_by_id('loadList').click()
		loadFromToken= self.browser.find_element_by_id('viewListFromLink')
		loadFromToken.send_keys(token)
		self.browser.find_element_by_id('navigateToLink').click()
		time.sleep(0.1)
		assert self.browser.find_element_by_id("printName").text == "My List"

		self.browser.find_element_by_id('shareDropdown').click()
		token = self.browser.find_element_by_id('sharingLink').get_attribute('value')
		self.browser.find_element_by_id('loadList').click()
		loadFromToken= self.browser.find_element_by_id('viewListFromLink')
		loadFromToken.send_keys(token)
		self.browser.find_element_by_id('navigateToLink').click()
		time.sleep(0.1)
		assert self.browser.find_element_by_id("printName").text == "My List"

	def test_shopping_list_name_can_be_edited(self):
		remove_overlay = self.browser.find_element_by_id("CreateListButton")
		remove_overlay.click()
		delete = self.browser.find_element_by_id('deleteButton')
		delete.send_keys("\n")

		self.browser.find_element_by_id('actionsDropdown').click()
		time.sleep(0.1)
		self.browser.find_element_by_id('addName').click()
		time.sleep(0.1)
		self.browser.find_element_by_id('listName').send_keys("My List")
		self.browser.find_element_by_id('saveListName').click()

		assert self.browser.find_element_by_id("printName").text == "My List"

		self.browser.find_element_by_id('actionsDropdown').click()
		time.sleep(0.1)
		self.browser.find_element_by_id('addName').click()
		time.sleep(0.1)
		self.browser.find_element_by_id('listName').send_keys("My New List")
		self.browser.find_element_by_id('saveListName').click()

		assert self.browser.find_element_by_id("printName").text == "My New List"

	def test_edited_list_name_can_be_saved(self):
		remove_overlay = self.browser.find_element_by_id("CreateListButton")
		remove_overlay.click()
		delete = self.browser.find_element_by_id('deleteButton')
		delete.send_keys("\n")

		self.browser.find_element_by_id('actionsDropdown').click()
		time.sleep(0.1)
		self.browser.find_element_by_id('addName').click()
		time.sleep(0.1)
		self.browser.find_element_by_id('listName').send_keys("My List")
		self.browser.find_element_by_id('saveListName').click()

		assert self.browser.find_element_by_id("printName").text == "My List"

		self.browser.find_element_by_id('actionsDropdown').click()
		time.sleep(0.1)
		self.browser.find_element_by_id('addName').click()
		time.sleep(0.1)
		self.browser.find_element_by_id('listName').send_keys("My New List")
		self.browser.find_element_by_id('saveListName').click()

		assert self.browser.find_element_by_id("printName").text == "My New List"

		self.browser.find_element_by_id('shareDropdown').click()
		token = self.browser.find_element_by_id('sharingLink').get_attribute('value')
		self.browser.find_element_by_id('loadList').click()
		loadFromToken= self.browser.find_element_by_id('viewListFromLink')
		loadFromToken.send_keys(token)
		self.browser.find_element_by_id('navigateToLink').click()

		assert self.browser.find_element_by_id("printName").text == "My New List"

	def test_shopping_list_name_is_saved_when_items_are_added_to_list(self):
		remove_overlay = self.browser.find_element_by_id("CreateListButton")
		remove_overlay.click()
		delete = self.browser.find_element_by_id('deleteButton')
		delete.send_keys("\n")

		self.browser.find_element_by_id('actionsDropdown').click()
		time.sleep(0.1)
		self.browser.find_element_by_id('addName').click()
		time.sleep(0.1)
		self.browser.find_element_by_id('listName').send_keys("My List")
		self.browser.find_element_by_id('saveListName').click()

		newItem = self.browser.find_element_by_id('ShoppingListItem')
		newItem.send_keys("Astros")
		quant = self.browser.find_element_by_id('ShoppingListQuantity')
		quant.send_keys(1000)
		button = self.browser.find_element_by_id('SubmitButton')
		button.click()
		time.sleep(0.1)

		self.browser.find_element_by_id('shareDropdown').click()
		token = self.browser.find_element_by_id('sharingLink').get_attribute('value')
		self.browser.find_element_by_id('loadList').click()
		loadFromToken= self.browser.find_element_by_id('viewListFromLink')
		loadFromToken.send_keys(token)
		self.browser.find_element_by_id('navigateToLink').click()

		assert self.browser.find_element_by_id("printName").text == "My List"
		assert self.browser.find_element_by_id("shoppingList_0").text == "Astros"

	def test_category_is_selected_from_dropdown_upon_addition_and_is_persistent(self):
		remove_overlay = self.browser.find_element_by_id("CreateListButton")
		remove_overlay.click()
		delete = self.browser.find_element_by_id('deleteButton')
		delete.send_keys("\n")

		elem = self.browser.find_element_by_id('ShoppingListItem')
		elem.send_keys("Chocolate")
		self.browser.find_element_by_id('dropdownButton').click()
		self.browser.find_element_by_id('categoryDropdown_Base_Item_0').click()
		assert self.browser.find_element_by_id('dropdownButton').get_attribute('innerHTML') == "Baked Goods"
		quant = self.browser.find_element_by_id('ShoppingListQuantity')
		quant.send_keys(123)
		button = self.browser.find_element_by_id('SubmitButton')
		button.click()
		time.sleep(0.1)

		assert self.browser.find_element_by_id('shoppingList_0').text == "Chocolate"
		assert self.browser.find_element_by_id('dropdownButton_0').get_attribute('innerHTML') == "Baked Goods"

		self.browser.find_element_by_id('shareDropdown').click()
		token = self.browser.find_element_by_id('sharingLink').get_attribute('value')
		self.browser.find_element_by_id('loadList').click()
		loadFromToken= self.browser.find_element_by_id('viewListFromLink')
		loadFromToken.send_keys(token)
		self.browser.find_element_by_id('navigateToLink').click()
		time.sleep(0.1)

		assert self.browser.find_element_by_id('shoppingList_0').text == "Chocolate"
		assert self.browser.find_element_by_id('dropdownButton_0').get_attribute('innerHTML') == "Baked Goods"

	def test_notes_can_be_added(self):
		remove_overlay = self.browser.find_element_by_id("CreateListButton")
		remove_overlay.click()
		delete = self.browser.find_element_by_id('deleteButton')
		delete.send_keys("\n")

		self.browser.find_element_by_id('notesBox').send_keys("These are the notes for my list")
		self.browser.find_element_by_id('saveNotesButton').click()
		time.sleep(0.1)

		assert self.browser.find_element_by_id("notesBox").get_attribute('value') == "These are the notes for my list"

	def test_notes_can_be_saved(self):
		remove_overlay = self.browser.find_element_by_id("CreateListButton")
		remove_overlay.click()
		delete = self.browser.find_element_by_id('deleteButton')
		delete.send_keys("\n")

		self.browser.find_element_by_id('notesBox').send_keys("These are the notes for my list")
		self.browser.find_element_by_id('saveNotesButton').click()
		time.sleep(0.1)

		assert self.browser.find_element_by_id("notesBox").get_attribute('value') == "These are the notes for my list"

		newItem = self.browser.find_element_by_id('ShoppingListItem')
		newItem.send_keys("Astros")
		quant = self.browser.find_element_by_id('ShoppingListQuantity')
		quant.send_keys(1000)
		button = self.browser.find_element_by_id('SubmitButton')
		button.click()
		time.sleep(0.1)
		self.browser.find_element_by_id('shareDropdown').click()
		token = self.browser.find_element_by_id('sharingLink').get_attribute('value')
		self.browser.find_element_by_id('loadList').click()
		loadFromToken= self.browser.find_element_by_id('viewListFromLink')
		loadFromToken.send_keys(token)
		self.browser.find_element_by_id('navigateToLink').click()

		assert self.browser.find_element_by_id("notesBox").get_attribute('value') == "These are the notes for my list"

	def test_category_is_editable_from_card_dropdown_and_is_persistent(self):
		remove_overlay = self.browser.find_element_by_id("CreateListButton")
		remove_overlay.click()
		delete = self.browser.find_element_by_id('deleteButton')
		delete.send_keys("\n")

		elem = self.browser.find_element_by_id('ShoppingListItem')
		elem.send_keys("Chicken")
		self.browser.find_element_by_id('dropdownButton').click()
		self.browser.find_element_by_id('categoryDropdown_Base_Item_0').click()
		assert self.browser.find_element_by_id('dropdownButton').get_attribute('innerHTML') == "Baked Goods"
		quant = self.browser.find_element_by_id('ShoppingListQuantity')
		quant.send_keys(123)
		button = self.browser.find_element_by_id('SubmitButton')
		button.click()
		time.sleep(0.1)

		assert self.browser.find_element_by_id('shoppingList_0').text == "Chicken"
		assert self.browser.find_element_by_id('dropdownButton_0').get_attribute('innerHTML') == "Baked Goods"
		
		self.browser.find_element_by_id('dropdownButton_0').click()
		self.browser.find_element_by_id('categoryDropdown_0_Item_6').click()
		time.sleep(0.1)
		assert self.browser.find_element_by_id('dropdownButton_0').get_attribute('innerHTML') == "Meat"

		self.browser.find_element_by_id('shareDropdown').click()
		token = self.browser.find_element_by_id('sharingLink').get_attribute('value')
		self.browser.find_element_by_id('loadList').click()
		loadFromToken= self.browser.find_element_by_id('viewListFromLink')
		loadFromToken.send_keys(token)
		self.browser.find_element_by_id('navigateToLink').click()
		time.sleep(0.1)

		assert self.browser.find_element_by_id('shoppingList_0').text == "Chicken"
		assert self.browser.find_element_by_id('dropdownButton_0').get_attribute('innerHTML') == "Meat"

	def test_notes_can_be_edited_and_saved(self):
		remove_overlay = self.browser.find_element_by_id("CreateListButton")
		remove_overlay.click()
		delete = self.browser.find_element_by_id('deleteButton')
		delete.send_keys("\n")

		self.browser.find_element_by_id('notesBox').send_keys("These are the notes for my list")
		self.browser.find_element_by_id('saveNotesButton').click()
		time.sleep(0.1)

		assert self.browser.find_element_by_id("notesBox").get_attribute('value') == "These are the notes for my list"

		newItem = self.browser.find_element_by_id('ShoppingListItem')
		newItem.send_keys("Astros")
		quant = self.browser.find_element_by_id('ShoppingListQuantity')
		quant.send_keys(1000)
		button = self.browser.find_element_by_id('SubmitButton')
		button.click()
		time.sleep(0.1)
		self.browser.find_element_by_id('notesBox').send_keys(". Here are the things I want to say.")
		self.browser.find_element_by_id('saveNotesButton').click()
		self.browser.find_element_by_id('shareDropdown').click()
		token = self.browser.find_element_by_id('sharingLink').get_attribute('value')
		self.browser.find_element_by_id('loadList').click()
		loadFromToken= self.browser.find_element_by_id('viewListFromLink')
		loadFromToken.send_keys(token)
		self.browser.find_element_by_id('navigateToLink').click()
		time.sleep(0.1)
		assert self.browser.find_element_by_id("notesBox").get_attribute('value') == "These are the notes for my list. Here are the things I want to say."

	def test_multiple_item_sort_by_category(self):
		remove_overlay = self.browser.find_element_by_id("CreateListButton")
		remove_overlay.click()
		delete = self.browser.find_element_by_id('deleteButton')
		delete.send_keys("\n")

		newItem = self.browser.find_element_by_id('ShoppingListItem')
		newItem.send_keys("Chicken")
		categoryBase = self.browser.find_element_by_id('dropdownButton')
		categoryBase.click()
		self.browser.find_element_by_id('categoryDropdown_Base_Item_6').click()
		quant = self.browser.find_element_by_id('ShoppingListQuantity')
		quant.send_keys(1000)
		button = self.browser.find_element_by_id('SubmitButton')
		button.click()
		time.sleep(0.1)
		
		newItem.send_keys("Shampoo")
		categoryBase.click()
		self.browser.find_element_by_id('categoryDropdown_Base_Item_5').click()
		quant.send_keys(2000)
		button.click()
		time.sleep(0.1)
		
		newItem.send_keys("Pizza")
		categoryBase.click()
		self.browser.find_element_by_id('categoryDropdown_Base_Item_4').click()
		quant.send_keys(3001)
		button.click()
		time.sleep(0.1)
		
		assert self.browser.find_element_by_id('dropdownButton_0').get_attribute('innerHTML') == "Meat"
		assert self.browser.find_element_by_id('shoppingList_0').text == "Chicken"
		assert self.browser.find_element_by_id('dropdownButton_1').get_attribute('innerHTML') == "Hygiene"
		assert self.browser.find_element_by_id('shoppingList_1').text == "Shampoo"
		assert self.browser.find_element_by_id('dropdownButton_2').get_attribute('innerHTML') == "Frozen Foods"
		assert self.browser.find_element_by_id('shoppingList_2').text == "Pizza"
		time.sleep(0.1)

		self.browser.find_element_by_id('actionsDropdown').click()
		time.sleep(0.1)
		self.browser.find_element_by_id('sortButtonCategory').click()
		time.sleep(0.1)
		
		assert self.browser.find_element_by_id('dropdownButton_0').get_attribute('innerHTML') == "Frozen Foods"
		assert self.browser.find_element_by_id('shoppingList_0').text == "Pizza"
		assert self.browser.find_element_by_id('dropdownButton_1').get_attribute('innerHTML') == "Hygiene"
		assert self.browser.find_element_by_id('shoppingList_1').text == "Shampoo"
		assert self.browser.find_element_by_id('dropdownButton_2').get_attribute('innerHTML') == "Meat"
		assert self.browser.find_element_by_id('shoppingList_2').text == "Chicken"

	def test_item_colour_change(self):
		remove_overlay = self.browser.find_element_by_id("CreateListButton")
		remove_overlay.click()
		delete = self.browser.find_element_by_id('deleteButton')
		delete.send_keys("\n")
		newItem = self.browser.find_element_by_id('ShoppingListItem')
		newItem.send_keys("Astros")
		quant = self.browser.find_element_by_id('ShoppingListQuantity')
		quant.send_keys(1000)
		self.browser.execute_script("document.getElementById('itemColor').value = 'rgba(0, 0, 0, 1)';")
		button = self.browser.find_element_by_id('SubmitButton')
		button.click()
		time.sleep(0.1)
		assert self.browser.find_element_by_id("list-entry_0").value_of_css_property('background-color') == 'rgba(0, 0, 0, 1)'

	def test_list_colour_change(self):
		remove_overlay = self.browser.find_element_by_id("CreateListButton")
		remove_overlay.click()
		delete = self.browser.find_element_by_id('deleteButton')
		delete.send_keys("\n")
		self.browser.execute_script("document.getElementById('listColor').value = 'rgba(250, 250, 250, 1)';")
		time.sleep(5)
		assert self.browser.find_element_by_id("list-container").value_of_css_property('background-color') == 'rgba(250, 250, 250, 1)'

	def test_item_colour_can_be_saved_in_db(self):
		remove_overlay = self.browser.find_element_by_id("CreateListButton")
		remove_overlay.click()
		delete = self.browser.find_element_by_id('deleteButton')
		delete.send_keys("\n")
		elem = self.browser.find_element_by_id('ShoppingListItem')
		elem.send_keys("Apple")
		quant = self.browser.find_element_by_id('ShoppingListQuantity')
		quant.send_keys(123)
		self.browser.execute_script("document.getElementById('itemColor').value = 'rgba(0, 0, 0, 1)';")
		button = self.browser.find_element_by_id('SubmitButton')
		button.click()
		self.browser.find_element_by_id('shareDropdown').click()
		token = self.browser.find_element_by_id('sharingLink').get_attribute('value')

		remove_overlay = self.browser.find_element_by_id("createList")
		remove_overlay.click()
		elem = self.browser.find_element_by_id('ShoppingListItem')
		elem.send_keys("Apple2")
		quant = self.browser.find_element_by_id('ShoppingListQuantity')
		quant.send_keys(238049)
		self.browser.execute_script("document.getElementById('itemColor').value = 'rgba(0, 0, 0, 1)';")
		button = self.browser.find_element_by_id('SubmitButton')
		button.click()

		self.browser.find_element_by_id('loadList').click()
		loadFromToken= self.browser.find_element_by_id('viewListFromLink')
		loadFromToken.send_keys(token)
		self.browser.find_element_by_id('navigateToLink').click()

	def test_edit_item_quantity(self):
		remove_overlay = self.browser.find_element_by_id("CreateListButton")
		remove_overlay.click()
		delete = self.browser.find_element_by_id('deleteButton')
		delete.send_keys("\n")
		elem = self.browser.find_element_by_id('ShoppingListItem')
		elem.send_keys("Apple")
		quant = self.browser.find_element_by_id('ShoppingListQuantity')
		quant.send_keys(123)
		button = self.browser.find_element_by_id('SubmitButton')
		button.click()
		time.sleep(0.1)
		assert self.browser.find_element_by_id("shoppingListQuantity_0").text == "123"

		editItem = self.browser.find_element_by_id("shoppingListQuantity_0")
		editItem.click()
		editItem.clear()
		editItem.send_keys(456)
		editItem.send_keys("\n")

		time.sleep(0.1)
		assert self.browser.find_element_by_id("shoppingListQuantity_0").text == "456"

	def test_edit_item_quantity_and_verify_that_quantity_is_stored_in_database_and_rendered_on_page_after_reload(self):
		remove_overlay = self.browser.find_element_by_id("CreateListButton")
		remove_overlay.click()
		delete = self.browser.find_element_by_id('deleteButton')
		delete.send_keys("\n")
		elem = self.browser.find_element_by_id('ShoppingListItem')
		elem.send_keys("Apple")
		quant = self.browser.find_element_by_id('ShoppingListQuantity')
		quant.send_keys(123)
		button = self.browser.find_element_by_id('SubmitButton')
		button.click()
		time.sleep(0.1)
		assert self.browser.find_element_by_id("shoppingListQuantity_0").text == "123"

		editItem = self.browser.find_element_by_id("shoppingListQuantity_0")
		editItem.click()
		editItem.clear()
		editItem.send_keys(456)
		editItem.send_keys("\n")

		time.sleep(0.1)
		assert self.browser.find_element_by_id("shoppingListQuantity_0").text == "456"

		self.browser.find_element_by_id('shareDropdown').click()
		token = self.browser.find_element_by_id('sharingLink').get_attribute('value')

		self.browser.find_element_by_id('loadList').click()
		loadFromToken= self.browser.find_element_by_id('viewListFromLink')
		loadFromToken.send_keys(token)
		self.browser.find_element_by_id('navigateToLink').click()

		time.sleep(0.1)
		assert self.browser.find_element_by_id("shoppingListQuantity_0").text == "456"

	def test_edits_of_multiple_item_quantities_are_persistent(self):
		remove_overlay = self.browser.find_element_by_id("CreateListButton")
		remove_overlay.click()
		delete = self.browser.find_element_by_id('deleteButton')
		delete.send_keys("\n")
		elem = self.browser.find_element_by_id('ShoppingListItem')
		elem.send_keys("Apple")
		quant = self.browser.find_element_by_id('ShoppingListQuantity')
		quant.send_keys(123)
		button = self.browser.find_element_by_id('SubmitButton')
		button.click()
		elem2 = self.browser.find_element_by_id('ShoppingListItem')
		elem2.send_keys("Banana")
		quant2 = self.browser.find_element_by_id('ShoppingListQuantity')
		quant2.send_keys(111)
		button.click()
		time.sleep(0.1)
		assert self.browser.find_element_by_id("shoppingListQuantity_0").text == "123"
		assert self.browser.find_element_by_id("shoppingListQuantity_1").text == "111"

		editItem = self.browser.find_element_by_id("shoppingListQuantity_0")
		editItem.click()
		editItem.clear()
		editItem.send_keys(456)
		editItem.send_keys("\n")
		editItem2 = self.browser.find_element_by_id("shoppingListQuantity_1")
		editItem2.click()
		editItem2.clear()
		editItem2.send_keys(222)
		editItem2.send_keys("\n")

		time.sleep(0.1)
		assert self.browser.find_element_by_id("shoppingListQuantity_0").text == "456"
		assert self.browser.find_element_by_id("shoppingListQuantity_1").text == "222"
		
	def tearDown(self):
		self.browser.close()

if __name__ == "__main__":
	unittest.main()
