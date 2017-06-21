#绘图类
class Echartsmetaclass(type):
	def __new__(cls,name,bases,attrs):
		print(attrs)
		return type.__new__(cls,name,bases,attrs)
class EchartsBase(dict):
	title={}
	legend={}
	tooltip={}
	xAxis={}
	yAxis={}
	series=[]
	def __init__(self,*args):
		temp={}
		for d in args:
			temp[d.name]=d
		super(EchartsBase,self).__init__(**temp)
#选项类
class Optionmetclass(type):
	def __new__(cls,name,bases,attrs):
		attrs['name']=name[0].lower()+name[1:]
		return type.__new__(cls,name,bases,attrs)
class OptionBase(dict,metaclass=Optionmetclass):
	pass
#选项实例
class Title(OptionBase):
	pass
class Legend(OptionBase):
	pass
class Tooltip(OptionBase):
	pass
class XAxis(OptionBase):
	pass
class YAxis(OptionBase):
	pass
class Series(list):
	name='series'
#图形类
class Seriesmetaclass(type):
	def __new__(cls,name,bases,attrs):
		attrs['type']=name.lower()
		return type.__new__(cls,name,bases,attrs)
class SeriesBase(dict,metaclass=Seriesmetaclass):
	def __init__(self,*args,**kwargs):
		kwargs['type']=self.type
		super(SeriesBase,self).__init__(*args,**kwargs)
class Line(SeriesBase):
	pass
#
a=Line(name='a',data=[15, 25, 20, 15, 20, 40])
b=Line(name='b',data=[5, 20, 36, 10, 10, 20])
s=Series((a,b))
t=Title(text='ECharts 入门示例')
x=XAxis(data= ["衬衫","羊毛衫","雪纺衫","裤子","高跟鞋","袜子"],type='category')
y=YAxis()
l=Legend(data=['a','b'])
tt=Tooltip()
d=EchartsBase(s,t,x,y,l,tt)

if __name__=='__main__':
	a=Line(name='a',data=[15, 25, 20, 15, 20, 40])
	b=Line(name='b',data=[5, 20, 36, 10, 10, 20])
	s=Series((a,b))
	t=Title(text='ECharts 入门示例')
	x=XAxis(data= ["衬衫","羊毛衫","雪纺衫","裤子","高跟鞋","袜子"],type='category')
	y=YAxis()
	l=Legend(data=['销量','aa'])
	tt=Tooltip()
	d=EchartsBase(s,t,x,y,l,tt)
	print(d)