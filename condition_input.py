weight = input("Enter your weight: ")
weight_type = input("Enter your weight_type: KG(K) or LBS(L) ")
if weight_type == "K" or weight_type == "k":
    print("Weight in KG: ", weight)
elif weight_type == "L" or weight_type == "l":
    #converted = weight / 0.45
    print("Weight in LBS: ", weight)
else:
    print("Weight in KG: ", weight)