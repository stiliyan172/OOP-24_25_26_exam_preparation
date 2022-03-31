from unittest import TestCase, main

from project.pet_shop import PetShop


class PetShopTest(TestCase):
    def setUp(self) -> None:
        self.pet_shop = PetShop('PetShop')

    def test_pet_shop_init(self):
        name = 'PetShop'
        pet_shop = PetShop(name)

        self.assertEqual(name, pet_shop.name)
        self.assertEqual({}, pet_shop.food)
        self.assertEqual([], pet_shop.pets)

    def test_add_food_raises_when_quantity_is_negative(self):
        with self.assertRaises(ValueError) as context:
            self.pet_shop.add_food("Pesho", -25)
        self.assertEqual('Quantity cannot be equal to or less than 0', str(context.exception))

    def test_add_food_adds_food_to_food_dict(self):
        food_name = "food1"
        food_quantity = 50

        result = self.pet_shop.add_food(food_name, food_quantity)

        self.assertEqual(f"Successfully added 50.00 grams of food1.", result)
        self.assertTrue(food_name in self.pet_shop.food)
        self.assertEqual(food_quantity, self.pet_shop.food[food_name])

    def test_add_food_adds_food_quantity_to_existing_food(self):
        food_name = 'food1'
        initial_qty = 100
        self.pet_shop.food[food_name] = initial_qty
        add_qty = 50

        result = self.pet_shop.add_food(food_name, add_qty)
        self.assertEqual('Successfully added 50.00 grams of food1.', result)
        self.assertTrue(food_name in self.pet_shop.food)
        self.assertEqual(initial_qty + add_qty, self.pet_shop.food[food_name])

    def test_add_test_raises_when_pet_name_exists(self):
        pet_name = "pet_name1"
        self.pet_shop.pets.append(pet_name)

        with self.assertRaises(Exception) as context:
            self.pet_shop.add_pet(pet_name)

        self.assertEqual("Cannot add a pet with the same name", str(context.exception))

    def test_add_pet_adds_pet_to_pet_shop(self):
        pet_name = 'pet_name1'
        result = self.pet_shop.add_pet(pet_name)

        self.assertEqual('Successfully added pet_name1.', result)
        self.assertTrue(pet_name in self.pet_shop.pets)

    def test_feed_pet_raises_when_pet_name_does_not_exist(self):
        with self.assertRaises(Exception) as context:
            self.pet_shop.feed_pet('food_name', 'pet_name')

        self.assertEqual("Please insert a valid pet name", str(context.exception))

    def test_feed_returns_error_message_when_food_name_does_not_exist(self):
        pet_name = 'pet_name'
        self.pet_shop.pets.append(pet_name)

        result = self.pet_shop.feed_pet('invalid food', pet_name)
        self.assertEqual("You do not have invalid food", result)

    def test_feed_is_adding_food_when_food_quantity_is_less_than_100(self):
        pet_name = 'pet_name'
        food_name = 'food_name'
        initial_qty = 65

        self.pet_shop.pets.append(pet_name)
        self.pet_shop.food[food_name] = initial_qty
        result = self.pet_shop.feed_pet(food_name, pet_name)

        self.assertEqual('Adding food...', result)
        self.assertEqual(initial_qty + 1000, self.pet_shop.food[food_name])

    def test_feed_decreases_food_qty_when_pet_is_fed(self):
        pet_name = 'pet_name'
        food_name = 'food_name'
        initial_qty = 165

        self.pet_shop.pets.append(pet_name)
        self.pet_shop.food[food_name] = initial_qty

        result = self.pet_shop.feed_pet(food_name, pet_name)
        self.assertEqual('pet_name was successfully fed', result)
        self.assertEqual(initial_qty - 100, self.pet_shop.food[food_name])

    def test_repr_return_proper_string(self):
        self.pet_shop.pets.append("pet1")
        self.pet_shop.pets.append("pet2")
        result = repr(self.pet_shop)

        self.assertEqual('Shop PetShop:\nPets: pet1, pet2', result)


if __name__ == '__main':
    main()
