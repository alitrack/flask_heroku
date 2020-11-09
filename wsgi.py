from app import app,db  

if __name__ == "__main__": 
        # automatically create table if not exists
        db.create_all()
        app.run() 
