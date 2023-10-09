# Functions developed specifically for the ECAS course

import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from sklearn.ensemble import RandomForestRegressor
import time
from sklearn.utils import check_random_state
import rfpimp

def plot_importances(importances, feature_names=None, stderr=None, title=None, order=False):
    if order:
        rank = np.argsort(-importances)
    else:
        rank = range(len(importances))
    if feature_names is None:
        feature_names = np.array(['f'+str(i) for i in range(1,len(importances[0])+1)])
    imp = pd.Series(importances[rank], feature_names[rank])
    if stderr is None:
        imp.plot(kind = "barh", color = ["cornflowerblue" if val>0 else "red" for val in importances[rank]])
    else:
        imp.plot(kind = "barh", color = ["cornflowerblue" if val>0 else "red" for val in importances[rank]], xerr=stderr[rank])
    plt.gca().invert_yaxis()
    if title is not None:
        plt.title(title)
    plt.show()

def plot_importances_comp(importances, title=None, feature_names=None, stderr=None, order=False):
    if order: # we rank according to the first one
        rank = np.argsort(-importances[0])
    else:
        rank = range(len(importances[0]))
    impdf = pd.DataFrame()
    if feature_names is None:
        feature_names = np.array(['f'+str(i) for i in range(1,len(importances[0])+1)])
    if title is None:
        title = np.array(['Imp '+str(i) for i in range(len(importances))])
    for (imp, title) in zip(importances, title):
        impdf[title] = pd.Series(imp[rank], feature_names[rank])
    impdf.plot(kind = "barh")
    plt.gca().invert_yaxis()
    plt.show()

def myplot_waterfall(sv, order=False):
    values = sv.values
    if order:
        rank = np.argsort(-np.abs(values))
    else:
        rank = range(len(sv))
    pred = np.sum(sv.values)+sv.base_values
    plot_importances(sv.values[rank], feature_names=np.array(sv.feature_names)[rank],
                    title="Base value="+str(round(sv.base_values[0],4))+" - Prediction="+str(round(pred[0],4)),
                    )
    plt.show()
    
def mprobes(X,Y, model, nb_perm, join_permute = False, mda=False, verbose = True):
    """
Author: Vân Anh Huynh-Thu
p,rank_mprobes = mprobes(X,Y,model)

 - X : inputs (needs to be a numpy array or a panda DataFrame of size (nsamples,nfeat))
 - Y : outputs (needs to be a numpy array or a panda DataFrame of size (nsamples,))
 - model : a scikit-learn model that fill in model.feature_importances_
 - nb_perm : number of iterations
 - join_permute : whether the constrast variables are permuted jointly or not
 - verbose : if False, no messages are printed

return :
 - R: a pandas DataFrame with original importance scores and computed FWER.
"""

    tic = time.process_time()
    
    if verbose:
        print('Compute the initial ranking...')

    nb_obj = X.shape[0]
    nb_feat = X.shape[1]
    
    if type(X) == pd.core.frame.DataFrame:
        feature_names = X.columns.values
        X = X.values[range(nb_obj)]
        Y = Y.values[range(nb_obj)]
    else:
        feature_names = ["f"+str(i) for i in range(nb_feat)]
    
    model.fit(X,Y)
    vimp0 = model.feature_importances_

    nb_obj = X.shape[0]
    nb_feat = X.shape[1]

    if Y.shape[0] != nb_obj:
        print('X and Y must have the same number of objects.')
        sys.exit()
    
    #data
    X_full = np.zeros((nb_obj,nb_feat*2),dtype=np.float32)
    X_full[:,:nb_feat] = X.copy()

    p = np.zeros(nb_feat)

    if verbose:
        print('Compute the permutation rankings...')
        
    for t in range(nb_perm):
        if verbose:
            print('.',end='')
        #Artificial contrasts
        if join_permute:
            rand_ind = np.random.permutation(nb_obj)
            X_full[:,nb_feat:] = (X.copy())[rand_ind,:]
        else:
            for i in range(nb_feat):
                feat_shuffle = X[:,i].copy()
                np.random.shuffle(feat_shuffle)
                X_full[:,i+nb_feat] = feat_shuffle

        #Learn an ensemble of tree and compute variable relevance scores
        var_imp = model.fit(X_full,Y).feature_importances_

        #Highest relevance score among all contrasts
        contrast_imp_max = max(var_imp[nb_feat:nb_feat*2])

        #Original variables with a score lower than the highest score among all contrasts
        irr_var_idx = np.where(var_imp[:nb_feat] <= contrast_imp_max)
        p[irr_var_idx] += 1

    p = p/nb_perm

    toc = time.process_time()
    if verbose:
        print()
        print('elapsed time: %.2f seconds' % (toc-tic))
        print()
    R = np.zeros((nb_feat,2))
    R[:,0] = vimp0
    R[:,1] = p
    Rd = pd.DataFrame(R,index=feature_names, columns=['Imp','FWER'])

    return Rd 

# The code below comes from 

def _generate_sample_indices(random_state, n_samples):
    """Private function used to _parallel_build_trees function."""
    random_instance = check_random_state(random_state)
    sample_indices = random_instance.randint(0, n_samples, n_samples)

    return sample_indices



def inbag_times_(self, X):
    """ Return n_samples by n_estimators array which keeps track of which samples are
        "in-bag" in which trees for how many times.

    Parameters  
    ----------
    self : RandomForest object. 
    X : array-like of shape = [n_samples, n_features]
    The training input samples. It should be the same data as you use to fit RandomForest. 

    Returns
    -------
    inbag_times_ : array, shape = [n_samples, n_estimators]
    """
    n_samples = X.shape[0]
    inbag = np.zeros((n_samples, self.n_estimators))
    for t_idx in range(self.n_estimators):
        sample_idx = _generate_sample_indices(self.estimators_[t_idx].random_state, n_samples)
        inbag[:, t_idx] = np.bincount(sample_idx, minlength = n_samples)

    return inbag

def debiased_mdi_clas(self, X, y):
    """Return unbiased measurement of feature importance or RandomForestClassifier using out-of-bag samples.

    Parameters  
    ----------
    self : RandomForestClassifier object. 
    X : array-like of shape = [n_samples, n_features]
        The training input samples. It should be the same data as you use to fit RandomForestClassifier.
    y : array-like of shape = [n_samples]
        The target values (class labels in classification). Only binary classsfication is supported currently.

    Returns
    -------
    feature importance: array, shape = [n_features]
    """   
    VI = np.array([0.] * self.n_features_in_)

    n_estimators = self.n_estimators

    inbag = inbag_times_(self, X)

    for index, tree in enumerate(self.estimators_):

        print(".", end="")

        temp = np.array([0.] * self.n_features_)

        n_nodes = tree.tree_.node_count

        tree_X_inb = X.repeat((inbag[:, index]).astype("int"), axis = 0)
        tree_y_inb = y.repeat((inbag[:, index]).astype("int"), axis = 0)
        decision_path_inb = tree.decision_path(tree_X_inb).todense()

        tree_X_oob = X[inbag[:, index] == 0]
        tree_y_oob = y[inbag[:, index] == 0]
        decision_path_oob = tree.decision_path(tree_X_oob).todense()

        impurity = [0] * n_nodes

        flag = [True] * n_nodes

        weighted_n_node_samples = np.array(np.sum(decision_path_inb, axis = 0))[0] / tree_X_inb.shape[0]

        for i in range(n_nodes):

            arr1 = tree_y_oob[np.array(decision_path_oob[:, i]).ravel().nonzero()[0].tolist()]
            arr2 = tree_y_inb[np.array(decision_path_inb[:, i]).ravel().nonzero()[0].tolist()]

            if len(arr1) == 0:
                if sum(tree.tree_.children_left == i) > 0:
                    parent_node = np.arange(n_nodes)[tree.tree_.children_left == i][0]
                    flag[parent_node] = False
                else:
                    parent_node = np.arange(n_nodes)[tree.tree_.children_right == i][0]
                    flag[parent_node] = False
            else:
                p1 = float(sum(arr1)) / len(arr1)
                pp1 = float(sum(arr2)) / len(arr2)
                p2 = 1 - p1
                pp2 = 1- pp1

                impurity[i] = 1 - p1 * pp1 - p2 * pp2

        for node in range(n_nodes):

            if tree.tree_.children_left[node] == -1 or tree.tree_.children_right[node] == -1:
                continue

            v = tree.tree_.feature[node]

            node_left = tree.tree_.children_left[node]
            node_right = tree.tree_.children_right[node]

            if flag[node] == True:

                incre = (weighted_n_node_samples[node] * impurity[node] -
                         weighted_n_node_samples[node_left] * impurity[node_left] -
                         weighted_n_node_samples[node_right] * impurity[node_right])

                temp[v] += incre

        VI += temp

    return VI / n_estimators


def debiased_mdi_regr(self, X, y):
    """Return unbiased measurement of feature importance for RandomForestRegressor using out-of-bag samples.

    Parameters  
    ----------
    self : RandomForestRegressor object. 
    X : array-like of shape = [n_samples, n_features]
        The training input samples. It should be the same data as you use to fit RandomForestRegressor.
    y : array-like of shape = [n_samples]
        The target values (real numbers in regression). 

    Returns
    -------
    feature importance: array, shape = [n_features]
    """   
    VI = np.array([0.] * self.n_features_in_)

    n_estimators = self.n_estimators

    inbag = inbag_times_(self, X)

    for index, tree in enumerate(self.estimators_):

        print(".", end="")
        
        temp = np.array([0.] * self.n_features_in_)

        n_nodes = tree.tree_.node_count
        
        tree_X_inb = X.repeat((inbag[:, index]).astype("int"), axis = 0)
        tree_y_inb = y.repeat((inbag[:, index]).astype("int"), axis = 0)
        decision_path_inb = tree.decision_path(tree_X_inb).todense()

        tree_X_oob = X[inbag[:, index] == 0]
        tree_y_oob = y[inbag[:, index] == 0]
        decision_path_oob = tree.decision_path(tree_X_oob).todense()

        impurity_train = tree.tree_.impurity
        impurity = [0] * n_nodes

        flag = [True] * n_nodes

        weighted_n_node_samples = np.array(np.sum(decision_path_inb, axis = 0))[0] / tree_X_inb.shape[0]

        for i in range(n_nodes):

            arr1 = tree_y_oob[np.array(decision_path_oob[:, i]).ravel().nonzero()[0].tolist()]
            arr2 = tree_y_inb[np.array(decision_path_inb[:, i]).ravel().nonzero()[0].tolist()]

            if len(arr1) == 0:
                if sum(tree.tree_.children_left == i) > 0:
                    parent_node = np.arange(n_nodes)[tree.tree_.children_left == i][0]
                    flag[parent_node] = False
                else:
                    parent_node = np.arange(n_nodes)[tree.tree_.children_right == i][0]
                    flag[parent_node] = False
            else:
                impurity[i] = np.sum((arr1 - np.mean(arr2)) ** 2) / len(arr1)

        for node in range(n_nodes):

            if tree.tree_.children_left[node] == -1 or tree.tree_.children_right[node] == -1:
                continue

            v = tree.tree_.feature[node]

            node_left = tree.tree_.children_left[node]
            node_right = tree.tree_.children_right[node]

            if flag[node] == True:

                incre = (weighted_n_node_samples[node] * (impurity[node] + impurity_train[node]) -
                         weighted_n_node_samples[node_left] * (impurity[node_left] + impurity_train[node_left]) - 
                         weighted_n_node_samples[node_right] * (impurity_train[node_right] + impurity[node_right]))

                temp[v] += incre

        VI += temp 

    return VI / n_estimators


