# nama file p1.py 
# Isikan email anda dan copy semua cell code yang dengan komentar #Graded

# untuk revisi dan resubmisi sebelum deadline
# silakan di resubmit dengan nilai variable priority yang lebih besar dari
# nilai priority submisi sebelumnya
# JIKA TIDAK ADA VARIABLE priority DIANGGAP priority=0
priority = 1

#netacad email cth: 'abcd@gmail.com'
email='utomopryo@gmail.com'
 
# copy-paste semua #Graded cells YANG SUDAH ANDA KERJAKAN di bawah ini
#PROJECT 1
#Graded
print ('=====================START========================')
def letter_catalog(items,letter='A'):
  itemBaru=[]
  for x in items:
  	if x[0] == letter:
  		itemBaru.append(x)
  return itemBaru

print (letter_catalog(['Apple','Avocado','Banana','Blackberries','Blueberries','Cherries'],'A'))

print ('========= END =========')
print()

#PROJECT 2
#Graded
print ('=====================START========================')

def counter_item(items):
   kamusBaru={}
   for x in items:
   	jml = items.count(x)
   	kamusBaru[x] = int(jml)
   return kamusBaru

print (counter_item(['Cherries', 'Blueberries', 'Banana', 'Avocado', 'Blackberries', 'Banana', 'Blueberries', 'Avocado', 'Banana', 'Blackberries']))

print ('========= END =========')
print()

#PROJECT 3
#Graded
print ('=====================START========================')

# dua variable berikut jangan diubah
fruits = ['Apple','Avocado','Banana','Blackberries','Blueberries','Cherries','Date Fruit','Grapes','Guava','Jackfruit','Kiwifruit']
prices = [6,5,3,10,12,7,14,15,8,7,9]

# list buah
chart = ['Blueberries','Blueberries','Grapes','Apple','Apple','Apple','Blueberries','Guava','Jackfruit','Blueberries','Jackfruit']

# list harga buah
fruit_price ={}
n = len(fruits)
for i in range(n):
	fruit_price[fruits[i]] = prices[i]


def total_price(dcounter,fprice):
  pass
  total = 0
  for x in fruits:
  	if dcounter.get(x) != None :
  		subtotal = int(dcounter.get(x)) * fprice.get(x)
  		total += subtotal
  return total

tes = total_price(counter_item(chart),fruit_price)
print (tes)

print ('========= END =========')
print()

#PROJECT 4
#Graded
print ('=====================START========================')


def discounted_price(total,discount,minprice=100):
  pass
  if total >= minprice:
  	diskon = total * discount/100
  	total -=diskon
  return total

tes = discounted_price(total_price(counter_item(chart),fruit_price),10,minprice=100)
print (tes)

print ('========= END =========')
print()

#PROJECT 5
#Graded
print ('=====================START========================')

def print_summary(item,fprice):
  pass
  items = counter_item(item)
  for x in fruits:
  	if items.get(x) != None:
  		  subtotal = int(items.get(x)) * int(fprice.get(x))
  		  print (items.get(x),x+" :",subtotal,sep=' ',end='')

  print ("total :",total_price(counter_item(item),fprice),sep=' ')
  print ("discounted price :", discounted_price(total_price(counter_item(item),fprice),10,minprice=100),sep=' ')

print_summary(chart,fruit_price)
print ('========= END =========')
