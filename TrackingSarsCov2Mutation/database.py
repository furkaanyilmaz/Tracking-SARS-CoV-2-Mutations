
import  mysql.connector as mysql



class database:
    def __init__(self,localhost,root,fy21_98):
        try:
            self.db = mysql.connect(host = localhost, user = root, passwd = fy21_98, database ="test2")
            self.cursor = self.db.cursor()
        except:
            self.db = mysql.connect(host = localhost, user = root, passwd = fy21_98)
            self.cursor = self.db.cursor()
            self.cursor.execute( "CREATE DATABASE test2")
            self.db.close()
            self.db = mysql.connect(host = localhost, user = root, passwd = fy21_98, database ="test2")
            self.cursor = self.db.cursor()
        
    def create(self):
        create_table = """
                CREATE TABLE IF NOT EXISTS user_(
                    email  VARCHAR(50) PRIMARY KEY,
                    passwd VARCHAR(50),
                    name  VARCHAR(50) ,
                    surname  VARCHAR(50) ,
                    confirmation_code VARCHAR(6),
                    confirmation CHAR(1)
                )
        """
        self.cursor.execute(create_table)
        create_table = """
                CREATE TABLE IF NOT EXISTS mutations(
                    mutation_name  VARCHAR(50),
                    voc_vol  VARCHAR(50),
                    effect_on_vaccine VARCHAR(50),
                    infectiousness  VARCHAR(50) ,
                    death_rate  VARCHAR(50) ,
                    anti_body_rate VARCHAR(50),
                    doi_number VARCHAR(50)
                )
        """
        self.cursor.execute(create_table)
        self.db.commit()

    def add_user(self,email,passwd,name,surname,confirmation_code,confirmation = "f"):
        command = "INSERT INTO user_ (email, passwd,name,surname,confirmation_code,confirmation)VALUES ('{}'," \
                  "'{}','{}','{}','{}','{}');".\
            format(email,passwd,name,surname,confirmation_code,confirmation)
        self.cursor.execute(command)
        self.db.commit()

    def add_mutation(self,mutation_name,voc_vol,effect_on_vaccine,infectiousness,death_rate,anti_body_rate,doi_number):
        command = "INSERT INTO mutations (mutation_name,voc_vol,effect_on_vaccine,infectiousness,death_rate,anti_body_rate,doi_number)VALUES " \
                  "('{}','{}'," \
                  "'{}','{}','{}','{}','{}');".format(mutation_name,voc_vol,effect_on_vaccine,infectiousness,death_rate,
                                                      anti_body_rate,doi_number)
        self.cursor.execute(command)
        self.db.commit()

    def search_mutation(self,search_word):
        columns = ["mutation_name","voc_vol","effect_on_vaccine","infectiousness","death_rate","anti_body_rate","doi_number"]
        liste = []
        for column in columns:
            self.cursor.execute("""SELECT * FROM mutations WHERE {} LIKE '{}%';""".format( str(column),str(search_word)))
            data = self.cursor.fetchall()
            for i in data:
                if not i in liste:
                    liste.append(i)
        self.db.commit()
        return liste

    def update_confirmation(self,email):
        self.cursor.execute("UPDATE user_ SET confirmation='{}'  WHERE email='{}';".format("y",email))
        self.db.commit()

    def get_user(self,email,passwd):
        self.cursor.execute("""SELECT * FROM user_ WHERE email LIKE '{}%';""".format(str(email)))
        result = self.cursor.fetchall()
        self.db.commit()
        if len(result) == 0:
            return False
        else:
            if result[0][0] == email and result[0][1] == passwd and result[0][5] == "y":
                return True
            else:
                return False


