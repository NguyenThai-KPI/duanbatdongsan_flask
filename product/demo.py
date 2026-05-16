from query.category import Category


cat = Category('database/category.csv',["id_cat","name","des","price","count","id_category"])


print(cat.list(1,10)["data"])

cat.create(["cat3","đồ gia dụng 3", "đây là đồ gia dụng 3"])

cat.update("id_cat","cat3",["name","des"],["Đồ gia dụng đã thay đổi","mô tả đã đổi"])

print(cat.search("id_cat","cat3"))


cat.delete("id_cat","cat3")