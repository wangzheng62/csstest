import json

line = {
            'title': {
                'text': 'ECharts 入门示例'
            },
            'tooltip': {},
            'legend': {
                'data':['销量','aa']
            },
            'xAxis': {'type':'category',
                'data': ["衬衫","羊毛衫","雪纺衫","裤子","高跟鞋","袜子"]
            },
            'yAxis': {},
			'series': [{
                'name': '销量',
                'type': 'line',
                'data': [5, 20, 36, 10, 10, 20]
            },{
                'name': 'aa',
                'type': 'line',
                'data': [15, 25, 20, 15, 20, 40]
            }]
        };
if __name__=='__main__':
	print(line)
	s=json.dumps(line)
	print(s)