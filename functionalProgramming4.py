from copy import deepcopy

bands=[
  {'name':'sunset rubdown','country':'UK','active':False},
  {'name':'women','country':'Germany','active':False},
  {'name':'a silver mt .zion','country':'Spain','active':True},
]

def assoc(_d,key,value):
  d=deepcopy(_d)
  d[key]=value
  return d
  
def setCanadaAsCountry(band):
  print "changing country"
  return assoc( band,'country','Canada' )

def stripPuntuationFromName(band):
  return assoc( band,'name',band["name"].replace('.','') )

def capitalizeNames(band):
  return assoc( band,'name',band["name"].title() )

def pipeline_each(data,fns):
  return reduce( lambda a,x: map(x,a), fns,data )
  
  
pipeline_each( bands,[setCanadaAsCountry,stripPuntuationFromName,capitalizeNames] )
