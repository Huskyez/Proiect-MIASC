from pre_steps import *
from models import *
from utils import *

x,y=get_processed_data()
x_train,x_test,y_train,y_test=split_data(x,y)
regressor=get_SGDRegressor()
fit(regressor,x_train,y_train)
y_pred=get_predictions(regressor,x_test)
error=get_error(y_test,y_pred)
print("error: "+str(error))
print_predicted_data(x_test,y_test,y_pred)
