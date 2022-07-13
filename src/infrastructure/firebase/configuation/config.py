import pyrebase

firebaseConfig = {'apiKey': "AIzaSyAZhCA5GiVvPcOCnRn0qJXmEM1nNIV8v_s",
                  'authDomain': "fastapi-ddd.firebaseapp.com",
                  'projectId': "fastapi-ddd",
                  'storageBucket': "fastapi-ddd.appspot.com",
                  'messagingSenderId': "388888077829",
                  'appId': "1:388888077829:web:148e401be9f5d8be339e6c",
                  'measurementId': "G-L96LZ1JD9C",
                  'databaseURL': "https://fastapi-ddd-default-rtdb.firebaseio.com/"
                  }

firebase = pyrebase.initialize_app(firebaseConfig)

db = firebase.database()
auth = firebase.auth()


