import flask
from back_funcs import bot_proba, bot_or_not, get_user_features

app = flask.Flask(__name__)

# return {'id': str(id)}

def bot_likelihood(prob):
    if prob < 20:
        return {'Result': 'Not a bot'}
    elif prob < 35:
        return {'Result': 'Likely not a bot'}
    elif prob < 50:
        return {'Result': 'Probably not a bot'}
    elif prob < 60:
        return {'Result': 'Maybe a bot'}
    elif prob < 80:
        return {'Result': 'Likely a bot'}
    else:
        return {'Result': 'Bot'}


@app.route('/predict', methods=['POST'])
def make_prediction():
    handle_ = flask.request.get_json()
    handle = handle_['username']

    
    user_lookup_message = f'Prediction for @{handle}'

    if get_user_features(handle) == 'User not found':
        prediction = [f'User @{handle} not found', '']

    else:
        prediction = [bot_likelihood(bot_proba(handle)),
                      f'Probability of being a bot: {bot_proba(handle)}%']

    return {"prediction": prediction[0], 
            "probability": prediction[1], 
            "user_lookup_message": user_lookup_message}


# for local dev
if __name__ == '__main__':
    app.run()
