
from sklearn.ensemble import RandomForestClassifier
import pandas as pd


data = pd.DataFrame.from_csv("/tmp/creditcard.csv")

y = data['Class']
X = data[[c for c in data.columns if "V" in c ]]

clf = RandomForestClassifier(max_depth=2, random_state=0)
clf.fit(X, y)

pgs = {
    "foo" : [1, 2, 3],
    "bar" : ["a", "b", "c"],
    "zoo" : ["ping", "pang"]
}





import itertools

list(itertools.product([['a','b'], [1, 2]]))
list(itertools.product(*[[{k: v} for v in pgs[k]] for k in pgs.keys()]))

param_grid = [{param_grid_spec.keys()[0] : v} for v in param_grid_spec[param_grid_spec.keys()[0]]]

dlist = [[d1, {k : d2}] for d1 in param_grid for k in param_grid_spec.keys()[1:] for d2 in param_grid_spec[k] ]

[{k:v} for l in dlist for k, v in l.items()]
