import numpy as np

class LinearRegression():
    def __init__(self):
        self.n = 10
        self.x = [1,2,3,4,5,6,7,8,9,10]
        self.y = [121, 125, 133, 141, 129, 127, 124, 155, 159, 145]
        pass

    def fit(self):
        self.m = 0
        self.b = 0
        
        x_avg = np.mean(self.x)
        y_avg = np.mean(self.y)

        numerator = 0
        denominator = 0
        for i in range(self.n):
            # m = sum ( (x-x_avg) * (y-y_avg) ) / sum((x-x_avg)**2)
            numerator = numerator + (self.x[i] - x_avg) * (self.y[i] - y_avg)
            denominator = denominator + (self.x[i] -x_avg) ** 2
        
        self.m = numerator / denominator
        self.b = y_avg - self.m * x_avg

        # print(self.b)
    
    def predict(self, x):
        return self.m * x + self.b



reg = LinearRegression()
reg.fit()
test_x = 15
y_pred = reg.predict(test_x)
print(f"prediction for x= {test_x} is y = {y_pred}")