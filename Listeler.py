if __name__ == '__main__':
    app.run(debug=True)
import os
from flask import Flask

app = Flask(__name__)
DB_FILE = 'kazanc_data.db'
