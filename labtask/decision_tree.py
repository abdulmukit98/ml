import pandas as pd
import numpy as np
import pprint
from sklearn.model_selection import train_test_split

class ID3DecisionTree:
    """
    Decision tree using ID3
    """
    def __init__(self):
        pass

    def get_entropy(self, df):
        # TODO: Calculate the entropy(s)
        class_values, class_counts = np.unique(df['play'],return_counts=True)
        # print(class_values)
        # print(class_counts)
        probability_of_play = class_counts / len(df)
        # print(probability_of_play)
        entropy = - np.sum(probability_of_play * np.log2(probability_of_play))
        # print(entropy)
        return entropy

    def split_table(self, df, attr, value):
        return df[df[attr] == value].reset_index(drop=True)

    def fit(self, df):
        # create tree dictionary
        tree = {}

        # compute entropy(s)
        entropy_s = self.get_entropy(df)

        # List of all attrs except the class
        attrs = df.keys()[:-1]

        max_gain = 0
        max_gain_attr = None
        # for all attr, find the attr with max gain
        for attr in attrs:
            values = df[attr].unique()
            
            # TODO: Calculate the entropies of unique values of attr
            # Example: attr=Outlook has entropies = [0.971, 0.971, 0]
            entropies = []
            for value in values:
                subset = df[df[attr] == value]
                subset_entropy=self.get_entropy(subset)
                entropies.append(subset_entropy)
              

            # TODO: Calculate the probabilities of unique values of attr
            # Example: attr=Outlook has entropies = [5/14, 5/14, 0]
            probabilities = []

            for value in values:
                subset = df[df[attr] == value]
                subset_entropy=self.get_entropy(subset)
                probabilities.append(len(subset)/len(df))
            

            # Calculate the average information entropy
            average_info_entropy = 0 
            for probability, entropy in zip(probabilities, entropies):
                average_info_entropy += probability * entropy
            
            # print(average_info_entropy)

            # TODO: Calculate attr gain
            attr_gain = entropy_s - average_info_entropy

            # TODO: Update the max_gain_attr
            if attr_gain > max_gain:
                max_gain = attr_gain
                max_gain_attr = attr

        tree[max_gain_attr] = {}
        # print(tree)
        # Split the df based on the values of max_gain_attr
        values = df[max_gain_attr].unique()
        for value in values:
            new_df = self.split_table(df, max_gain_attr, value)
            class_values, class_counts = np.unique(new_df['play'],return_counts=True)

            # If it is a pure class, then this is the leaf node
            # else divide the new_df further
            if len(class_counts)==1:
                tree[max_gain_attr][value] = class_values[0]
            else:
                tree[max_gain_attr][value] = self.fit(new_df)

        return tree

    def predict(self, example, tree, default=None):
        attribute = next(iter(tree))
        if example[attribute] in tree[attribute].keys():
            subtree = tree[attribute][example[attribute]]
            if isinstance(subtree, dict):
                return self.predict(example, subtree)
            else:
                return subtree
        else:
            return default

    def evaluate(self, tree, df):
        # TODO: Complete the evaluate method
        correct_prediction = 0
        # iterate through test_df
        for index, row in df.iterrows():
            example = row.drop('play').to_dict()
            # print(example)
            prediction_result = self.predict(example, tree)
            # print(prediction_result)
            if prediction_result == row['play']:
                correct_prediction += 1
        
        accuracy = correct_prediction / len(df) * 100
        return accuracy


# TODO: Complete the class for decision tree using CART
class CARTDecisionTree:
    def __init__(self):
        pass

    def fit(self, df):
        pass 

    def predict(self, example, tree, default=None):
        pass

    def evaluate(self, tree, df):
        pass


# Read the dataset
data_path = 'E:/Downloads/play_tennis.csv'
df = pd.read_csv(data_path)
# print(df)


# TODO: Shuffle the df randomly
df = df.sample(frac=1,random_state=42).reset_index(drop=True)
# print(df)


# TODO: Split the df into train_df and test_df using 80:20 ratio
train_df , test_df = train_test_split(df, test_size=0.2, random_state=42)
train_df = train_df.reset_index(drop=True)
test_df = test_df.reset_index(drop=True)
# print(train_df)
# print(test_df)

# Train the model
model = ID3DecisionTree()
tree = model.fit(train_df)
# print(model.get_entropy(df))
# print(model.fit(train_df))

# Visualize the decision tree
print('the decision tree for ID3 algorithm:\n')
pprint.pprint(tree)

# # Predict an example
x ={'Outlook':'Rain','Temperature':'Hot','Humidity':'High','Wind':'Weak'}
y_pred = model.predict(x, tree)
print("#ID3: Output class:", y_pred)

# # Evaluate the model
print(model.evaluate(tree, test_df))
acc = model.evaluate(tree, test_df)
print("#ID3: Accuracy: {:.3f}".format(acc))

# Train the model
# model = CARTDecisionTree()
# tree = model.fit(train_df)

# # Visualize the decision tree
# pprint.pprint(tree)

# # Predict an example
# x ={'Outlook':'Sunny','Temperature':'Hot','Humidity':'High','Wind':'Weak'}
# y_pred = model.predict(x, tree)
# print("#CART: Output class:", y_pred)

# # Evaluate the model
# acc = model.evaluate(tree, test_df)
# print("#CART: Accuracy: {.3f}".format(acc))
