# Lab 2 E-Commerce


## a. Objective

The overall objective of the lab is to create an e-commerce website. But, the second lab has the following objectives:
1. To add product,brands and category
2. To perform CRUD operations on products, brands and category
3. To initialize SQL configuration

## b. Introduction

We use different frameworks and environments for this lab. We have used VS Code as the IDE and Python/Django as the framework. An E-commerce website is a website that helps customers and sellers in buying/selling their products on the online platform. It is one of the best modern ways of business. E-commerce websites simplify the buying process of goods and services. We will be creating an e-commerce website for this lab report. 
We will be adding a product module of the following structure as shown below:

![Er diagram, the product module](/lab_manual/images_lab2/ER-product_module.png)

## c. Procedure
We did the following steps in this lab:

**1. Adding Brands in models.py**

```
  class Brand(models.Model):
    name = models.CharField(max_length=200)
    is_active = models.BooleanField()
```

**2. Adding the model Category in the models.py**

```
  class Category(models.Model):
    name = models.CharField(max_length=200)
    is_active = models.BooleanField()
  class Meta:
    verbose_name_plural = "Categories"
```
**3. Adding the model Product in the models.py**

```
  class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.FloatField()
    quantity = models.IntegerField()
    image_url = models.CharField(max_length=500)
    color_code = models.CharField(max_length=20)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    registered_on = models.DateTimeField()
    is_active = models.BooleanField()
```
**4. Making changes to the db by performing migrations**

```
  python manage.py makemigrations
  python manage.py migrate
```
**5. Adding the following code to admin.py for enabling CRUD operations in the admin site**

```
  from .models import Brand, Category, Product
  admin.site.register(Brand)
  admin.site.register(Category)
  admin.site.register(Product)
```

**6. Finally, running the project and performing CRUD operations on Brand, Category and Product**

```
 python manage.py runserver
```
## d. Output

**1. Adding Brand, Category and Product**

![](/lab_manual/images_lab2/three_models.png)

**2. The Brand model**

![](/lab_manual/images_lab2/brand.png)

![](/lab_manual/images_lab2/brand_detailed.png)

**3. The Category model**

![](/lab_manual/images_lab2/category.png)

![](/lab_manual/images_lab2/category_detailed.png)

**4. The Product model**

![](/lab_manual/images_lab2/Product.png)

![](/lab_manual/images_lab2/productdetailed.png)

## e. Conclusion 

The second lab of e-commerce used many concepts from the first lab. We learned to add three new product moduels; brands, categories and products. Additionally, we completed CRUD operations on brand, category and product. Finally, we verified databse using SQLite.
