import uvicorn
import pandas as pd
from fastapi import FastAPI
from lifetimes import BetaGeoFitter, GammaGammaFitter
from api.inputs_data import inputs, profit, cltv

bgf = BetaGeoFitter()
bgf.load_model('bgf.pkl')

ggf = GammaGammaFitter()
ggf.load_model('ggf.pkl')

app = FastAPI()

@app.post("/predict")
def predict(data:inputs):
    data = data.dict()
    t = 4 * data['t']
    frequency = data['frequency']
    recency = data['recency']
    T = data['T']
    out_model = bgf.predict(t, frequency, recency, T)
    return {"prediction": out_model}


@app.post("/profit")
def profit(data:profit):
    data = data.dict()
    frequency = data['frequency']
    monetary = data['monetary']
    out_model = ggf.conditional_expected_average_profit(frequency, monetary)
    return {"prediction profit": out_model}

@app.post("/cltv")
def cltv(data:cltv):
    data = data.dict()
    frequency = data['frequency']
    recency = data['recency']
    T = data['T']
    monetary = data['monetary']

    df_input = pd.DataFrame({'frequency': [frequency],
                            'recency': [recency],
                            'T': [T],
                            'monetary_value': [monetary]})

    out_model = ggf.customer_lifetime_value(transaction_prediction_model=bgf, 
                                            frequency=df_input['frequency'],
                                            recency=df_input['recency'],
                                            T=df_input['T'],
                                            monetary_value=df_input['monetary_value'],
                                            time=6,     
                                            discount_rate=0.01,
                                            )[0]

    return {"prediction cltv": out_model}

# 5. Run the API with uvicorn
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)