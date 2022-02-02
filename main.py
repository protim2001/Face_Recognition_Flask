from flask import Flask
from app import views

app = Flask(__name__)

# url
app.add_url_rule('/base','base',views.base,methods=['GET','POST'])
app.add_url_rule('/','index',views.index,methods=['GET','POST'])
app.add_url_rule('/faceapp','faceapp',views.faceapp,methods=['GET','POST'])
app.add_url_rule('/faceapp/gender','gender',views.gender,methods=['GET','POST'])
# 
if __name__ == "__main__":
    app.run(debug=True)