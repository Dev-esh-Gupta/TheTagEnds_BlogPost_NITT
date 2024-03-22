from datetime import datetime
from flask import Flask, render_template, request, jsonify
import csv

fields = ['id', 'author', 'title', 'content', 'date']  

rows = []

app = Flask(__name__)


@app.route('/')
def home():
  return render_template('blog.html')

@app.route('/blogs', methods=['GET','POST'])
def blogs():
  if request.method == 'POST':
    with open('blogs.csv', mode ='r')as file:  
      csvFile = csv.reader(file)  
      for lines in csvFile:  
          rows.append(lines)
  
    id = len(rows) + 1
    author = request.form.get('author')
    title = request.form.get('title')
    content = request.form.get('content')
    curr_time = datetime.now()
    print(author)
    rows.append([id,author,title,content,curr_time])
      
    with open('blogs.csv', 'w') as csvfile:  
      csvwriter = csv.writer(csvfile)  
      csvwriter.writerow(fields)
      csvwriter.writerows(rows) 
    rows.clear()
  
  return "<h1>Post Submitted Successfully</h1>"


if __name__ == "__main__":
  app.run(host="0.0.0.0", debug=True)