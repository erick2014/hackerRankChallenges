def zero(s):
  
  if s[0] == "0":
    return s[1:]

def one(s):
  if s[0] == "1":
    return s[1:]

def applyRule(conf):
 
  cbList=conf["cbsList"]
  counter=conf["counter"]
  myStr=conf["myStr"]

  myStr=cbList[counter](myStr);

  conf["myStr"]=myStr
  conf["counter"]+=1;

  return conf

def rule_sequence(conf): 
    if len( conf["cbsList"] ) == conf["counter"]:
      conf["myStr"]
      print conf["myStr"]
    else: 
      rule_sequence( applyRule(conf) )

rule_sequence({"myStr":"0101","cbsList":[zero,zero],"counter":0})
