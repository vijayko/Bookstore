from django.db import models
from django.conf import settings
from django.shortcuts import reverse
from django.db.models.signals import post_save


CATEGORY_CHOICES = (
	('CS', 'Computer Science'), 
	('B', 'Biology' ), 
	('M', 'Mathematics'), 
	('F', 'Fiction'),
	('NF', 'Non Fiction'), 
	('UC', 'Unclassified')
	)

LABEL_CHOICES = {
	('N', 'new'), 
	('G', 'good'), 
	('A', 'acceptable')

}
class UserProfile(models.Model):
	user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	stripe_customer_id = models.CharField(max_length=50, blank=True, null=True)

	def __str__(self):
		return self.user.username

class Publisher(models.Model):
	name = models.CharField(max_length=200, blank=True, null=True)

	def __str__(self):
		return self.name

class Author(models.Model):
	firstname = models.CharField(max_length=200, blank=True, null=True)
	lastname = models.CharField(max_length=200, blank=True, null=True)

	def __str__(self):
		return (self.firstname + " " + self.lastname)

class Book(models.Model):
	title = models.CharField(max_length=200)
	price = models.FloatField()
	category = models.CharField(choices=CATEGORY_CHOICES, max_length=2)
	label = models.CharField(choices=LABEL_CHOICES, max_length=1)
	publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
	author = models.ManyToManyField(Author)
	ISBN = models.CharField(max_length=20)
	slug = models.SlugField()
	description = models.TextField( )

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse("bookstore:product", kwargs={
			'slug': self.slug
			})

	def get_add_to_cart_url(self):
		return reverse("bookstore:add-to-cart", kwargs={
			'slug': self.slug
			})

	def get_remove_from_cart_url(self):
		return reverse("bookstore:remove-from-cart", kwargs={
			'slug': self.slug
			})


class OrderItem(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	item = models.ForeignKey(Book, on_delete=models.CASCADE)
	quantity = models.IntegerField(default=1)
	ordered = models.BooleanField(default=False)

	def __str__(self):
		return f"{self.quantity} of {self.item.title}"

	def get_total_book_item_price(self):
		return self.quantity * self.item.price

class Order(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	ref_code = models.CharField(max_length=20, blank=True, null=True)
	items = models.ManyToManyField(OrderItem)
	ordered = models.BooleanField(default=False)
	ordered_date = models.DateTimeField()

	def __str__(self):
		return self.user.username

	def get_total(self):
		total = 0
		for order_item in self.items.all():
			total += order_item.get_final_price()
		return total

class Warehouse(models.Model):
	book = models.ForeignKey(Book, on_delete=models.CASCADE)
	quantity = models.IntegerField()

	def __str__(self):
		return f"{self.quantity} of {self.book.title}"

	def alter(self):
		if quantity <= 5: 
			print("LOW IN STOCK!!")


# def userprofile_receiver(sender, instance, created, *args, **kwargs):
# 	if created: 
# 		userprofile = UserProfile.objects.create(user=instance)

# post_save.connect(userprofile_receiver, sender=settings.AUTH_USER_MODEL)


