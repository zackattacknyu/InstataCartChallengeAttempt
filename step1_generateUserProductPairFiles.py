import csv

#priorDataProductsFile = 'CSV_FILES/order_products__prior.csv'
#priorDataProductsOutputFile = "GENERATED_FILES/userProductPairsPrior.txt"

priorDataProductsFile = 'CSV_FILES/order_products__train.csv'
priorDataProductsOutputFile = "GENERATED_FILES/userProductPairsTrain.txt"

allOrdersCSVfile = 'CSV_FILES/orders.csv'

allOrdersReader = csv.DictReader(open(allOrdersCSVfile))
allOrdersProducts = csv.DictReader(open(priorDataProductsFile))

mapOfUserAndOrder = {}
for row in allOrdersReader:
    currentUser = row['user_id']
    currentOrder = row['order_id']
    mapOfUserAndOrder[currentOrder] = currentUser

mapOfOrderAndProduct = {}
for row in allOrdersProducts:
    currentOrder = row['order_id']
    currentProduct = row['product_id']
    if(currentOrder not in mapOfOrderAndProduct):
        mapOfOrderAndProduct[currentOrder]=[]
    mapOfOrderAndProduct[currentOrder].append(currentProduct)

file1 = open(priorDataProductsOutputFile,"w")
mapOfUserProductAndNumber = {}
for orderId in mapOfOrderAndProduct:
    currentUser = mapOfUserAndOrder[orderId]
    for productId in mapOfOrderAndProduct[orderId]:
        currentUserProductCombo = currentUser+"_"+productId
        file1.write(currentUserProductCombo+"\n")
file1.close()

