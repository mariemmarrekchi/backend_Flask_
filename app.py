from flask import Flask,jsonify,request
from pymongo import MongoClient
from pymongo import MongoClient
import json
app=Flask(__name__)
#collection dexcription  
#function add 
@app.route("/add",methods=['Post'])
def Ajout():
    def connect():
       client=MongoClient('mongodb://localhost:27017/')
       db=client.Team
       return db
    col=connect().description
    name1=request.get_json()['Name']
    number=request.get_json()['Num'] 
    desc=request.get_json()['Description']
    level=request.get_json()['level']
    desc={
        "Name":name1,
        "Num":number,
        "Description":desc,
         "level":level
            } 
    
    col.insert_one(desc)
    return jsonify({"message":"insert"})  
        
@app.route("/Get_desc")
def Get_Desc():
    def connect():
           client=MongoClient('mongodb://localhost:27017/')
           db=client.Team
           return db
    col=connect().description
    name=request.args.get('name')
    trouve=col.find({"Name":name})
    return json.dumps(list(trouve))
@app.route("/put",methods=['PUT']) 
def put():
    def connect():
        client=MongoClient('mongodb://localhost:27017/')
        db=client.Team
        return db
    col=connect().description
    name1=request.get_json()['Name']
    number=request.get_json()['Num'] 
    desc=request.get_json()['Description']
    level=request.get_json()['level']
    myquery={"Name":name1,"Num":number,"Description":desc,"level":level}
    change=request.get_json()['new_Name']
    change1=request.get_json()['new_Num'] 
    change2=request.get_json()['new_Description']
    change3=request.get_json()['new_level']
    newvalues={"$set":{"Name":change,"Num":change1,"Description":change2,"level":change3}}
    col.update(myquery,newvalues)
    return jsonify({"mes":"modifié"})

@app.route("/delete_desc",methods=['Delete'])
def delete_desc():
     def connect():
            client=MongoClient('mongodb://localhost:27017/')
            db=client.Team
            return db
     col=connect().description
     
     name1=request.get_json()['Name']
     col.delete({"Name":name1})
     return jsonify({"mes":"delete"})
#collection team 
#function add get update delete finished

@app.route("/Home",methods=['Post'])
#function add
def Add():
    def connect():
        client=MongoClient('mongodb://localhost:27017/')
        db=client.Team
        return db
 
    col=connect().team
    name=request.get_json()['Name']
    Institute=request.get_json()['Institute']
    email=request.get_json()['email']
    tel=request.get_json()['tel']
    team=request.get_json()['team']
    cordination={
      "Name":name,
      "Institute":Institute,
      "email":email,
      "tel":tel,
      "team":team  
    }
    col.insert_one(cordination)
    return jsonify({"message":'insert'})
@app.route("/data")
def GET_inf():
    def connect():
        client=MongoClient('mongodb://localhost:27017/')
        db=client.Team
        return db
    
    col=connect().team
    nom=request.args.get('nom')

    data=col.find({"Name":nom},{"_id":0})
    return json.dumps(list(data))
@app.route("/Gt_All")
def Get_All():
    def connect():
        client=MongoClient('mongodb://localhost:27017/')
        db=client.Team
        return db
    
    col=connect().team
    data=col.find({},{"_id":0})
    return json.dumps(list(data)) 

@app.route("/update",methods=['PUT'])
def update():
    def connect():
        client=MongoClient('mongodb://localhost:27017/')
        db=client.Team
        return db
    col=connect().team
    name=request.get_json()['Name']
    ins=request.get_json()['Institute']
    email=request.get_json()['email']
    tel=request.get_json()['tel']
    team=request.get_json()['team']
    myquery = { "Name":name,"Institute":ins,"email":email,"tel":tel,"team":team }
    change=request.get_json()['new_Name']
    change2=request.get_json()['new_Institute']
    change3=request.get_json()['new_email']
    change4=request.get_json()['new_tel']
    change5=request.get_json()['new_team']
    newvalues = { "$set": { "Name": change, "Institute": change2,"email": change3,"tel": change4,"team": change5} }
  

    col.update(myquery, newvalues)
  
   
    return jsonify({"mes":"update"})
     

@app.route('/delete',methods=["Delete"])
def delete():
    def connect():
        client=MongoClient('mongodb://localhost:27017/')
        db=client.Team
        return db
    col=connect().team
    name=request.get_json()['Name']
    data={"Name":name}
    col.delete_one(data)
    return jsonify({"mes":"delete"})

####################### Table Dev
@app.route("/TableDev",methods=['Post'])
def AjoutTable ():
    def connect():
        client=MongoClient('mongodb://localhost:27017/')
        db=client.Team
        return db
    col=connect().TableProblem
    Logo=request.get_json()['logo']
    Name=request.get_json()['name']
    Problem1=request.get_json()['problem1']
    Problem2=request.get_json()['problem2']
    Problem3=request.get_json()['problem3']
    Problem4=request.get_json()['problem4']
    Problem5=request.get_json()['problem5']
    Problem6=request.get_json()['problem6']
    Total=request.get_json()['total']
    Score=request.get_json()['score']
    Table={
        "logo":Logo,
        "name":Name,
        "problem1":Problem1,
        "problem2":Problem2,
        "problem3":Problem3,
        "problem4":Problem4,
        "problem5":Problem5,
        "problem6":Problem6,
        "total":Total,
        "score":Score
    }
    col.insert_one(Table)
    return jsonify({'message':"insert"})
@app.route("/GetTable")
def Get_Table():
    def connect():
        client=MongoClient('mongodb://localhost:27017/')
        db=client.Team
        return db
    col=connect().TableProblem
    data=col.find({},{"_id":0})
    return json.dumps(list(data))
@app.route("/UpdateTable",methods=['Put'])	
def UpdateTable():
    def connect():
        client=MongoClient('mongodb://localhost:27017/')
        db=client.Team
        return db
    col=connect().TableProblem
    Logo=request.get_json()['logo']
    Name=request.get_json()['name']
    Problem1=request.get_json()['problem1']
    Problem2=request.get_json()['problem2']
    Problem3=request.get_json()['problem3']
    Problem4=request.get_json()['problem4']
    Problem5=request.get_json()['problem5']
    Problem6=request.get_json()['problem6']
    Total=request.get_json()['total']
    Score=request.get_json()['score']
    # 
    myquery={'logo':Logo,'name':Name,'problem1':Problem1,'problem2':Problem2,'problem3':Problem3,'problem4':Problem4,'problem5':Problem5,'problem6':Problem6,'total':Total,'score':Score}
    change=request.get_json()['new_logo']
    change1=request.get_json()['new_name'] 
    change2=request.get_json()['new_problem1']
    change3=request.get_json()['new_problem2']
    change4=request.get_json()['new_problem3']
    change5=request.get_json()['new_problem4']
    change6=request.get_json()['new_problem5']
    change7=request.get_json()['new_problem6']
    change8=request.get_json()['new_total']
    change9=request.get_json()['new_score']
    # 
    newvalues={"$set":{"logo":change,"name":change1,"problem1":change2,"problem2":change3,"problem3":change4,"problem4":change5,"problem5":change6,"problem6":change7,"total":change8,"score":change9}}
    col.update(myquery,newvalues)
    return jsonify({"mes":"modifié"})
@app.route('/DeleteTable',methods=["Delete"])
def DeleteTable():
    def connect():
        client=MongoClient('mongodb://localhost:27017/')
        db=client.Team
        return db
    col=connect().team
    name=request.get_json()['Name']
    data={"name":name}
    col.delete_one(data)
    return jsonify({"mes":"delete"})
            ############  Table Test ###########
@app.route("/Insert",methods=['Post'])
def Insert():
    def connect():
        client=MongoClient('mongodb://localhost:27017/')
        db=client.Team
        return db
    col=connect().TableTest
    logo=request.get_json()['logo']
    name=request.get_json()['name']
    TcDes=request.get_json()['TcDesigned']
    res=request.get_json()['results']
    bugs=request.get_json()['BugsFound']
    req=request.get_json()['reqcovred']
    
    tab={
        'logo':logo,
        'name':name,
        'TcDesigned':TcDes,
        'results':res,
        'BugsFound':bugs,
        'reqcovred':req
    }
    col.insert_one(tab)
    return jsonify({"mes":"inserted"})
@app.route('/GetTest')
def GetTest():
    def connect():
        client=MongoClient('mongodb://localhost:27017/')
        db=client.Team
        return db
    col=connect().TableTest
    data=col.find({},{"_id":0})
    return json.dumps(list(data))

@app.route('/Envi') 
def GetEnvi():
     def connect():
            client=MongoClient('mongodb://localhost:27017/')
            db=client.Team
            return db
     col=connect().Environnement
     data=col.find({},{"_id":0})
     return json.dumps(list(data))
@app.route("/addsol",methods=['Post'])
def AjoutSol():
    def connect():
        client=MongoClient('mongodb://localhost:27017/')
        db=client.Team
        return db
    
    col=connect().solution
    
    solu=request.get_json()['sol']
   
    desc={
        "sol":solu
        
            } 
    
    col.insert_one(desc)
    return jsonify({"message":"insert"}) 


if __name__=="__main__":
    app.run(debug=True,host='127.0.0.1',port=5000)  
