from django.db import models

class Auction(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='auctions/')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateTimeField()
    is_completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title
class AuctionImage(models.Model):
    auction = models.ForeignKey(Auction, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='auctions/')

    def __str__(self):
        return f"{self.auction.title} - Imagen {self.pk}"