import random

class Apple:
    counter = 0
    weight_count = 0

    def __init__(self, name):
        self.name = name
        self.weight = round(random.uniform(0.2,0.5),2)
        Apple.counter += 1
        Apple.weight_count += self.weight
            
    def evaluate(self):
        if Apple.counter < 1000:
            if Apple.weight_count >= 300:
                    print('Apple units processed:', Apple.counter, ' - Weight:', Apple.weight_count)
                    Apple.weight_count = 0
        if Apple.counter == 1000:
            print('Apple units processed:', Apple.counter, ' - Weight:', Apple.weight_count)

count = 0
for i in [('apple_'+str(z)) for z in range(1000) ]:
    i = Apple(str(count))
    i.evaluate()
    
    count +=1