def linearSearchProduct(productList,targetProduct):
  indices=[]
  for index,product in enumerate(productList):
    if product == targetProduct:
      indices.append(index)
  return indices
  if product == targetProduct:
      indices.append(index)
  return index 
product=["shoes","boot","Loafer","shoes","sandal","shoes"]
target="shoes"
result=linearSearchProduct(product, target)
print(result) 