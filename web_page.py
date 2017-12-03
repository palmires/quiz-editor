# -*- coding: utf-8 -*-
#!/usr/bin/env python
from flask import Flask
from flask import jsonify
from flask import render_template
from flask import request
from flask import url_for
from flask import redirect
import os
import json



quiz_editor = Flask(__name__)
path_toquizzes = '/home/deliany/Project/quiz/quizzes/'
path_tothemes = '/home/deliany/Project/question_outsource/themes/'

themes = json.loads(open(os.path.join(path_tothemes, 'themes_keys')).read())

@quiz_editor.route('/quizzes/show')
def hello():
    #import simplejson as json
    quiz_list = [themes.keys()[themes.values().index(x)] for x in os.listdir(path_toquizzes)]
    
    return render_template('index.html',quizzes=quiz_list, themes=themes)

@quiz_editor.route('/quizzes/<theme>')
def show_question(theme):
    quizzes = json.loads(open(os.path.join(path_toquizzes, theme)).read())
    return render_template('question.html',quizzes=quizzes, theme=theme)

@quiz_editor.route('/quizzes/save', methods=["POST"])
def save_quiz():
    #quiz = request.args.get('1')
    quiz_name = request.args.get('theme')
    questions = request.get_json()
    current_quiz = json.loads(open(os.path.join(path_toquizzes, quiz_name)).read())
    current_quiz["questions"] = questions
    with open(os.path.join(path_toquizzes,quiz_name),'w') as f:
        f.write(json.dumps(current_quiz,f,ensure_ascii=False).encode('utf8'))
    return redirect(url_for('hello'))

@quiz_editor.route('/quizzes/new')
def new_quiz():
    name = request.args.get('q_name')
    description = request.args.get('q_descr')
    if name and description:
        quiz_name = name.replace(' ','')
        save_new_quiz(quiz_name, description)
    return redirect(url_for('hello'))
        #print name.replace(' ',''), description
    

@quiz_editor.route('/quizzes/edit/<theme>')
def delete_all():
    passed = {"lucky":[]}
    full_passed = {"fully_granted":[]}
    with open(full_path_tofile,'w') as f:
        f.write(json.dumps(passed,f,ensure_ascii=False).encode('utf8'))

    with open(full_path_to100,'w') as f:
        f.write(json.dumps(full_passed,f,ensure_ascii=False).encode('utf8'))
    return redirect(url_for('hello'))
# @editor.route('/<name>')
# def hello_name(name):

#   return "Hello {}!".format(name)

def save_new_quiz(quiz_name, description):
    new_quiz = {"name": quiz_name,"description": description,"questions": []}
    filename_quiz = "%s"%len(themes)
    themes[quiz_name] = filename_quiz
    try:
        with open(os.path.join(path_tothemes,'themes_keys'),'w') as f:
            f.write(json.dumps(themes,f,ensure_ascii=False).encode('utf8'))
            with open(os.path.join(path_toquizzes,filename_quiz),'w') as f_quiz:
             f_quiz.write(json.dumps(new_quiz,f_quiz, ensure_ascii=False).encode('utf8'))
             return True
    except:
        return False  

if __name__ == '__main__':
    quiz_editor.run(debug=True,host='0.0.0.0')
