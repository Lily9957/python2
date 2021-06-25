
from flask import Flask, render_template, request
import pandas as pd
import json
import plotly
import plotly.express as px

import csv, re, operator
# from textblob import TextBlob

app = Flask(__name__)

person = {
    'first_name': 'Lily',
    'address' : 'Hubei Normal University',
    # 'job': 'Student',
    'tel': '131565487',
    'email': 'lily4434@outlook.com',
    'capsname':'李某的简历',
    'description' : 'I spend most of my time on study,i have passed CET4/6 . and ihave acquired basic knowledge of my major during my schooltime. ',
    'qq': '123',
    'wechat': 'bdf',
    'github': 'https://github.com/lily9957',

	'languages' : ['HTNL','CSS (Stylus)', 'JavaScript & jQuery', 'Killer Taste'],
	'education' : ['湖北师范大学','XXXhigh school',  'XXXmiddle school'],

    'experiences' : [
        {
            'NO' : 'Job #1',
            'light': 'First Experience description',
            'justified' : 'Plaid gentrify put a bird on it, pickled XOXO farm-to-table irony raw denim messenger bag leggings. Hoodie PBR&B photo booth, vegan chillwave meh paleo freegan ramps. Letterpress shabby chic fixie semiotics. Meditation sriracha banjo pour-over. Gochujang pickled hashtag mixtape cred chambray. Freegan microdosing VHS, 90s bicycle rights aesthetic hella PBR&B.',
           
        },
        {
        	'NO' : ' Job #2',
        	'light': 'First Experience description',
        	'justified' : 'Beard before they sold out photo booth distillery health goth. Hammock franzen green juice meggings, ethical sriracha tattooed schlitz mixtape man bun stumptown swag whatever distillery blog. Affogato iPhone normcore, meggings actually direct trade lomo plaid franzen shoreditch. Photo booth pug paleo austin, pour-over banh mi scenester vice food truck slow-carb. Street art kogi normcore, vice everyday carry crucifix thundercats man bun raw denim echo park pork belly helvetica vinyl. ',
           
        }
    ]

}

@app.route('/')
def cv(person=person):
    return render_template('index.html', person=person)




@app.route('/callback', methods=['POST', 'GET'])
def cb():
	return gm(request.args.get('data'))
   
@app.route('/chart')
def index():
	return render_template('chartsajax.html',  graphJSON=gm(),graphJSON1=gm1(),graphJSON2=gm2(),graphJSON3=gm3(),graphJSON4=gm4(),graphJSON5=gm5(),graphJSON6=gm6(),graphJSON7=gm7(),graphJSON8=gm8(),graphJSON9=gm9(),graphJSON10=gm10(),graphJSON11=gm11())

#鸢尾属植物数据集sepal_width：花萼宽度，sepal_length花萼长度，petal length（花瓣长度），petal width（花瓣宽度）
def gm(): 
	df = pd.DataFrame(px.data.iris())
	fig = px.scatter(df, x="sepal_width", y="sepal_length")
	graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
	return graphJSON

def gm1(): 
	df = pd.DataFrame(px.data.iris())
	fig = px.scatter(df, x="sepal_width", y="sepal_length", color="species")
	# print()
	graphJSON1 = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
	return graphJSON1

def gm2(): 
	df = pd.DataFrame(px.data.iris())
	fig = px.scatter(df, x="sepal_width", y="sepal_length", color="species", marginal_y="rug", marginal_x="histogram")
	graphJSON2 = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
	return graphJSON2
def gm3(): 
	df = pd.DataFrame(px.data.iris())
	fig = px.density_contour(df, x="sepal_width", y="sepal_length")
	graphJSON3 = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
	return graphJSON3

def gm4(): 
	df = pd.DataFrame(px.data.iris())
	fig = px.density_heatmap(df, x="sepal_width", y="sepal_length")
	graphJSON4 = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
	return graphJSON4

def gm5(): 
	df = pd.DataFrame(px.data.iris())
	fig = px.parallel_coordinates(df, color="species_id", labels={"species_id": "Species",
                "sepal_width": "Sepal Width", "sepal_length": "Sepal Length",
                "petal_width": "Petal Width", "petal_length": "Petal Length", },
                color_continuous_scale=px.colors.diverging.Tealrose, color_continuous_midpoint=2)
	graphJSON5 = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
	return graphJSON5
#violin
def gm6(): 
	df = pd.DataFrame(px.data.iris())
	fig = px.scatter_matrix(df, dimensions=["sepal_width", "sepal_length", "petal_width", "petal_length"], color="species")
	graphJSON6 = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
	return graphJSON6

def gm7(): 
	df = pd.DataFrame(px.data.iris())
	fig = px.violin(df, x="sepal_width", y="sepal_length")
	graphJSON7 = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
	return graphJSON7
def gm8(): 
	df = pd.DataFrame(px.data.iris())
	fig = px.box(df, x="sepal_width", y="sepal_length", color="species")
	graphJSON8 = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
	return graphJSON8
def gm9(): 
	df = pd.DataFrame(px.data.iris())
	fig = px.bar(df, x="sepal_width", y="sepal_length")
	graphJSON9 = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
	return graphJSON9
def gm10(): 
	df = pd.DataFrame(px.data.iris())
	fig = px.histogram(df, x="sepal_width", y="sepal_length")
	graphJSON10 = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
	return graphJSON10
def gm11(): 
	df = pd.DataFrame(px.data.iris())
	fig = px.area(df, x="sepal_width", y="sepal_length")
	graphJSON11 = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
	return graphJSON11
@app.route('/senti')
def main():
	text = ""
	values = {"positive": 0, "negative": 0, "neutral": 0}

	with open('ask_politics.csv', 'rt') as csvfile:
		reader = csv.DictReader(csvfile, delimiter=',', quotechar='"')
		for idx, row in enumerate(reader):
			if idx > 0 and idx % 2000 == 0:
				break
			if  'text' in row:
				nolinkstext = re.sub(r'''(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'".,<>?«»“”‘’]))''', '', row['text'], flags=re.MULTILINE)
				text = nolinkstext

			blob = TextBlob(text)
			for sentence in blob.sentences:
				sentiment_value = sentence.sentiment.polarity
				if sentiment_value >= -0.1 and sentiment_value <= 0.1:
					values['neutral'] += 1
				elif sentiment_value < 0:
					values['negative'] += 1
				elif sentiment_value > 0:
					values['positive'] += 1

	values = sorted(values.items(), key=operator.itemgetter(1))
	top_ten = list(reversed(values))
	if len(top_ten) >= 11:
		top_ten = top_ten[1:11]
	else :
		top_ten = top_ten[0:len(top_ten)]

	top_ten_list_vals = []
	top_ten_list_labels = []
	for language in top_ten:
		top_ten_list_vals.append(language[1])
		top_ten_list_labels.append(language[0])

	graph_values = [{
					'labels': top_ten_list_labels,
					'values': top_ten_list_vals,
					'type': 'pie',
					'insidetextfont': {'color': '#FFFFFF',
										'size': '14',
										},
					'textfont': {'color': '#FFFFFF',
										'size': '14',
								},
					}]

	layout = {'title': '<b>意见挖掘</b>'}

	return render_template('sentiment.html', graph_values=graph_values, layout=layout)


if __name__ == '__main__':
  app.run(debug= True,port=5000,threaded=True)
