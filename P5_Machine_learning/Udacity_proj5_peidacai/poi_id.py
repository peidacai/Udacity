#!/usr/bin/python

import sys
import pickle
sys.path.append("../tools/")

from feature_format import featureFormat, targetFeatureSplit
from tester import dump_classifier_and_data

import pandas as pd
import numpy as np
import math

from sklearn.naive_bayes import GaussianNB
from sklearn.cross_validation import train_test_split, StratifiedShuffleSplit

from sklearn.pipeline import Pipeline, make_pipeline, FeatureUnion
from sklearn.preprocessing import MinMaxScaler
from sklearn.decomposition import PCA
from sklearn.feature_selection import SelectKBest

from sklearn.metrics import f1_score
from sklearn.grid_search import GridSearchCV


### Task 1: Select what features you'll use.
### features_list is a list of strings, each of which is a feature name.
### The first feature must be "poi".

data_list = ['poi',
 'total_stock_value',
 'total_payments',
 'restricted_stock',
 'exercised_stock_options',
 'expenses',
 'salary',
 'other',
 'to_messages',
 'from_messages',
 'from_poi_to_this_person',
 'from_this_person_to_poi',
 'shared_receipt_with_poi',
 'bonus',
 'exp_sal_ratio',
 'to_poi_ratio', 
 'from_poi_ratio', 
 'shared_poi_ratio']

features_list = ['poi',
 'total_stock_value',
 'total_payments',
 'restricted_stock',
 'exercised_stock_options',
 'expenses',
 'salary',
 'other',
 'to_messages',
 'from_messages',
 'from_poi_to_this_person',
 'from_this_person_to_poi',
 'shared_receipt_with_poi',
 'bonus']

### Load the dictionary containing the dataset
with open("final_project_dataset.pkl", "r") as data_file:
    data_dict = pickle.load(data_file)

### Task 2: Remove outliers

# total of all 145 entries need to be removed
del data_dict['TOTAL']

# Travel agency was not an employee
del data_dict['THE TRAVEL AGENCY IN THE PARK']

# The following 2 individual didn't had tally in the sum of all finance and email features with their respective total
del data_dict['BELFER ROBERT']
del data_dict['BHATNAGAR SANJAY']

# Converting to pandas dataframe
df = pd.DataFrame(data_dict)
df = df.T.reset_index()

# Remove "email address" column
del df['email_address']

# Replacing NaN values with np.nan and convert all number features to float type
df.replace('NaN',np.nan, inplace = True)
df.iloc[:,1:] = df.iloc[:,1:].astype(float)

# Replacing nans with zeros
df.replace(np.nan, 0, inplace = True)

### Task 3: Create new feature(s)

# Expenses salary ratio
df['exp_sal_ratio'] = df['expenses'] / df['salary']
df.loc[:, 'exp_sal_ratio'] = df['exp_sal_ratio'].apply(lambda x: 0 if ((x == np.inf) or (math.isnan(x))) else x)

# ratio of emails to poi to total emails sent
df['to_poi_ratio'] = df['from_this_person_to_poi'] / df['from_messages']
df.loc[:, 'to_poi_ratio'] = df['to_poi_ratio'].apply(lambda x: 0 if ((x == np.inf) or (math.isnan(x))) else x)

# ratio of emails from poi to total emails received
df['from_poi_ratio'] = df['from_poi_to_this_person'] / df['to_messages']
df.loc[:, 'from_poi_ratio'] = df['from_poi_ratio'].apply(lambda x: 0 if ((x == np.inf) or (math.isnan(x))) else x)

# ratio of shared receipt emails with poi to total emails received
df['shared_poi_ratio'] = df['shared_receipt_with_poi'] / df['to_messages']
df.loc[:, 'shared_poi_ratio'] = df['shared_poi_ratio'].apply(lambda x: 0 if ((x == np.inf) or (math.isnan(x))) else x)

### Store to my_dataset for easy export below.
my_dataset = df.T[df.columns.isin(data_list)].to_dict()

### Extract features and labels from dataset for local testing
data = featureFormat(my_dataset, features_list, sort_keys = True)
labels, features = targetFeatureSplit(data)

### Task 4: Try a varity of classifiers
### Please name your classifier clf for easy export below.
### Note that if you want to do PCA or other multi-stage operations,
### you'll need to use Pipelines. For more info:
### http://scikit-learn.org/stable/modules/pipeline.html

# Provided to give you a starting point. Try a variety of classifiers.

# Setting up X and y for modeling

rand_state = 42
y = df['poi']
X = df.T[df.columns.isin(features_list)].T.drop(['poi'], axis = 1)

# Gridsearch for GaussianNB

combined_features = FeatureUnion([("kbest", SelectKBest()), ("pca", PCA())])

k = [5,6,7,8, 9, 10, 11,12,13]
n_components = [2,3,4,5,6]

pipeline = Pipeline([("standard_scale", MinMaxScaler()),("features", combined_features), ("gnb", GaussianNB())])
param_grid_neigh = dict(features__pca__n_components=n_components, \
                  features__kbest__k=k)

sss = StratifiedShuffleSplit(y, n_iter=100, test_size=0.3, random_state = rand_state)

gsgnb = GridSearchCV(pipeline, \
                    param_grid_neigh, \
                    scoring= 'f1', cv=sss, n_jobs = -1
                   )

gsgnb.fit(X,y)

clf = gsgnb.best_estimator_

### Task 5: Tune your classifier to achieve better than .3 precision and recall 
### using our testing script. Check the tester.py script in the final project
### folder for details on the evaluation method, especially the test_classifier
### function. Because of the small size of the dataset, the script uses
### stratified shuffle split cross validation. For more info: 
### http://scikit-learn.org/stable/modules/generated/sklearn.cross_validation.StratifiedShuffleSplit.html

# Example starting point. Try investigating other evaluation techniques!


### Task 6: Dump your classifier, dataset, and features_list so anyone can
### check your results. You do not need to change anything below, but make sure
### that the version of poi_id.py that you submit can be run on its own and
### generates the necessary .pkl files for validating your results.

dump_classifier_and_data(clf, my_dataset, features_list)