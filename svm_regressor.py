from pre_steps import *
from models import *
from utils import *

x,y=get_processed_data()
x_train,x_test,y_train,y_test=split_data(x,y)
regressor=get_SVMRegressor()
fit(regressor,x_train,y_train)
# y_pred=get_predictions(regressor,x_test)
# error=get_error(y_test,y_pred)
# gl_error=error
# print("error: "+str(error))
# print_predicted_data(x_test,y_test,y_pred)


x_1980_2030=make_1980_2030_data(x)
y_1980_2030=get_predictions(regressor,x_1980_2030)

# save_predictions(x_1980_2030,y_1980_2030,'1980-2030 predictions.csv')
