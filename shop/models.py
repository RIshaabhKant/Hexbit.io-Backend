from django.db import models


class ShopManager(models.Manager):
    '''Manager for Shop Model'''

    def create_shop(self, profileId: int, name: str, city='', state='', accountNumber='', ifscCode='', incorporatioName='', incorporationType='',
                    gstin='', pan='', phone='', email=''):
        
        print(profileId, name)
        
        shop = self.model(profileId=profileId, name=name, city=city, state=state, accountNumber=accountNumber, ifscCode=ifscCode,incorporatioName=incorporatioName,
                          incorporationType=incorporationType, gstin=gstin, pan=pan, phone=phone, email=email)
        
        self.save(shop=shop)

        return shop
    
    def save(self, shop):
        shop.save(using=self._db)


class Shop(models.Model):
    '''Database model for shops in the system'''

    profileId = models.IntegerField(null=False, unique=True) #TODE: change to forkey to profile ID

    name = models.CharField(max_length=255, null=False, default='')
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    accountNumber = models.CharField(max_length=255)
    ifscCode = models.CharField(max_length=255)
    incorporatioName = models.CharField(max_length=255)
    incorporationType = models.CharField(max_length=255)
    gstin = models.CharField(max_length=255)
    pan = models.CharField(max_length=255)
    phone = models.CharField(max_length=20)
    email = models.CharField(max_length=255)
    is_anonymous = models.BooleanField(default=False)
    is_authenticated = models.BooleanField(default=True)

    REQUIRED_FIELDS = ['name']
    object = ShopManager()


    def __str__(self) -> str:
        ShopVis = f"""Name: {self.name} \n shopId: {self.id} \n profileId: {self.profileId} \n 
                        city: {self.city} \n state: {self.state} \n"""
        

