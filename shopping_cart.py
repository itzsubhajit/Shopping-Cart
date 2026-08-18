# Empty shopping cart
cart = []

# Repeat until user exits
while True:

    # Display menu
    print("\n===== SHOPPING CART =====")
    print("1. Add Product")
    print("2. View Products")
    print("3. Update Product")
    print("4. Delete Product")
    print("5. Exit")

    # Take user's choice
    choice = input("Enter your choice: ")

    # Match the user's choice
    match choice:

        # CREATE - Add Product
        case "1":
            product = input("Enter product name: ")
            cart.append(product)
            print("Product added successfully!")

        # READ - View Products
        case "2":
            if len(cart) == 0:
                print("Cart is empty!")
            else:
                print("\nProducts in Cart:")

                for i in range(len(cart)):
                    print(i + 1, ".", cart[i])

        # UPDATE - Change Product
        case "3":
            if len(cart) == 0:
                print("Cart is empty!")
            else:
                # Display products
                for i in range(len(cart)):
                    print(i + 1, ".", cart[i])

                # Take product number
                n = int(input("Enter product number to update: "))

                # Update product
                cart[n - 1] = input("Enter new product name: ")

                print("Product updated successfully!")

        # DELETE - Remove Product
        case "4":
            if len(cart) == 0:
                print("Cart is empty!")
            else:
                # Display products
                for i in range(len(cart)):
                    print(i + 1, ".", cart[i])

                # Take product number
                n = int(input("Enter product number to delete: "))

                # Delete product
                cart.pop(n - 1)

                print("Product deleted successfully!")

        # EXIT
        case "5":
            print("Thank You!")
            break

        # Invalid choice
        case _:
            print("Invalid Choice!")