from sklearn.linear_model import SGDRegressor
from sklearn.svm import SVR
from sklearn.metrics import mean_squared_error

def get_SGDRegressor():
    return SGDRegressor(eta0=0.005, learning_rate='adaptive',max_iter=1000000)

def get_SVMRegressor():
    return SVR(kernel='sigmoid')

def fit(model,x,y):
    model.fit(x,y)
    return model

def get_predictions(model,x):
    return model.predict(x)

def get_error(y_true,y_pred):
    return mean_squared_error(y_true,y_pred)
