
def print_predicted_data(x_test,y_test,y_pred):
    for point, true, pred in zip(x_test, y_test, y_pred):
        print(str(point) + ": " + str(true) + " --- "  + str(pred))
