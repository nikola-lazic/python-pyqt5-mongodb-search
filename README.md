# **Python PyQT5 MongoDB Search**
This Python script for searching local mongodb database. As you probably already know, mongodb is non-sql database type, good for horizontal scaling.

![GIF animation](/img/animation.gif)

----
### **Requirements**
Install necessary libraries:
- pymongo
- pyqt5
```
pip install -r requirements.tx
```

---

### **How to Use**
We have to create Test-database and store some data into 2 collections.
You only have to run:
```
data/python-create-mongodb.py
```
This script will create Test-database and import data from JSON files into each collection.
</br>Here is screenshot from MongoDB Compass after running this Python script, to make sure that Test-database is created successfully:
</br>![compass](/img/image-1.png)

</br>Before, we do some searching we have to create indexes for full text search.
In folder data, run Python script:
```
data/python-create-indexes.py
```
Finally, we can run now main.py and this window will appear:
</br>![compass](/img/image-2.png)

---

### **GUI**
</br>GUI is done by using QtDesinger. In folder ui you will find 'Window.ui' which is converted into .py by this command:
```
python -m PyQt5.uic.pyuic -x Window.ui -o Window.py
```

---

### **Useful snippets**
I added 2 useful snippets in folder 'snippets'. I used them as exercise before I started with GUI.
- pymongo_exercise_1.py
- pymongo_exercise_2.py