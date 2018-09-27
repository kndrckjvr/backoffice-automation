dr_qty = 0
while dr_qty < 1 or dr_qty > 4294967295:
    dr_qty=input("Enter DR Quantity: ")
    if dr_qty < 1:
        print("Minimum is 1!")
        pass
    if dr_qty > 4294967295:
        print("Maximum is 4294967295!")
        pass