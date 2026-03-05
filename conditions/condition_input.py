weight = int(input("Enter your weight: "))
weight_type = input("Enter your weight_type KG(K) or LBS(L): ")
if weight_type == "K" or weight_type == "k":
    converted = weight * 0.45
    print("Weight in KG: ", str(converted))
elif weight_type == "L" or weight_type == "l":
    converted = weight / 0.45
    print("Weight in LBS: ", str(converted))