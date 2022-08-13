import pickle

def predict_class(a):
    with open('model_rf_clf_hyp.pkl','rb') as f:
        model=pickle.load(f)
        predicted_value=model.predict(a)
        return predicted_value[0]

