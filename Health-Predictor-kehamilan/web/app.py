import flask
import pandas as pd
from joblib import dump, load


with open(f'model/fatalhealthprediction.joblib', 'rb') as f:
    model = load(f)


app = flask.Flask(__name__, template_folder='templates')


@app.route('/', methods=['GET', 'POST'])
def main():
    if flask.request.method == 'GET':
        return (flask.render_template('main.html')) 

    if flask.request.method == 'POST':
        baselinevalue = flask.request.form['baselinevalue']
        accelerations = flask.request.form['accelerations']
        fetalmovement = flask.request.form['fetalmovement']
        uterinecontractions = flask.request.form['uterinecontractions']
        lightdecelerations = flask.request.form['lightdecelerations']
        severedecelertions = flask.request.form['severedecelertions']
        prolongueddecelerations = flask.request.form['prolongueddecelerations']
        abnormalshorttermvariability = flask.request.form['abnormalshorttermvariability']
        meanvalueofshorttermvariability = flask.request.form['meanvalueofshorttermvariability']
        percentageoftime = flask.request.form['percentageoftime']

        meanvalueoflongtermvariability = flask.request.form['meanvalueoflongtermvariability']
        histogramwidth = flask.request.form['histogramwidth']
        histogrammin = flask.request.form['histogrammin']
        histogrammax = flask.request.form['histogrammax']
        histogramnumberofpeaks = flask.request.form['histogramnumberofpeaks']
        histogramnumberofzeroes = flask.request.form['histogramnumberofzeroes']
        histogrammode = flask.request.form['histogrammode']
        histogrammean = flask.request.form['histogrammean']
        histogrammedian = flask.request.form['histogrammedian']
        histogramvariance = flask.request.form['histogramvariance']
        histogramtendency = flask.request.form['histogramtendency']

        input_variables = pd.DataFrame([[baselinevalue, accelerations, fetalmovement, uterinecontractions, lightdecelerations, severedecelertions, prolongueddecelerations, abnormalshorttermvariability, meanvalueofshorttermvariability, percentageoftime, meanvalueoflongtermvariability, histogramwidth,histogrammin,histogrammax,histogramnumberofpeaks,histogramnumberofzeroes,histogrammode,histogrammean,histogrammedian,histogramvariance,histogramtendency]],
                                       columns=['baselinevalue', 'accelerations', 'fetalmovement', 'uterinecontractions', 'lightdecelerations',
                                                'severedecelertions', 'prolongueddecelerations', 'abnormalshorttermvariability', 'meanvalueofshorttermvariability', 'percentageoftime','meanvalueoflongtermvariability','histogramwidth','histogrammin','histogrammax','histogramnumberofpeaks','histogramnumberofzeroes','histogrammode','histogrammean','histogrammedian','histogramvariance','histogramtendency'],
                                       dtype='float',
                                       index=['input'])

        predictions = model.predict(input_variables)[0]
        predictions = "{:.0f}".format(predictions)

        if predictions == '1' :
            pred= "Janin dalam keadaan Normal."
        elif predictions == '2' :
            pred= "Janin dalam keadaan Suspect."
        elif predictions == '3' :
            pred="Janin dalam keadaan Pathological."
        else:
           pred= "Data tidak valid"

        return flask.render_template('main.html',result=pred)


if __name__ == '__main__':
    app.run(debug=True)
