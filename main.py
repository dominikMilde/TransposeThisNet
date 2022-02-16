# -*- coding: utf-8 -*-
from exceptionsList import lista
from flask import Flask, render_template, request, g, flash, url_for, redirect, session, make_response, Response, Markup

from flask_mail import Mail, Message

from flask_wtf import FlaskForm, csrf
from wtforms import StringField, TextAreaField, ValidationError
from flask_wtf.csrf import CsrfProtect

#from flask_babel import Babel, gettext, get_locale

import gc
#from passlib.hash import sha256_crypt

from wtforms.validators import DataRequired, Length, Email, EqualTo

app = Flask(__name__)
app.secret_key = "n0t re@al k€y"

app.config.update(
    DEBUG=True,
    #EMAIL SETTINGS
    MAIL_SERVER='smtp.gmail.com',
    MAIL_PORT=465,
    MAIL_USE_SSL=True,
    MAIL_USERNAME='notreal@mail.com',
    MAIL_PASSWORD= 'rAnDoMPasS'
)
mail = Mail(app)
#babel = Babel(app)

#@babel.localeselector
#def get_locale():
 #   if session.get('lang') is None:
  #      session['lang'] = 'en'
   # return session['lang']


class RegistrationForm(FlaskForm):
    def nothing(form, field):
        if len(field.data) < 1:
            raise ValidationError(Markup("""<div class="col-md-4"> <div class="alert alert-danger alert-dismissible fade in">
                                <a href="#" class="close" data-dismiss="alert" aria-label="close">&times;</a>
                                You have to paste some text in here!
                                </div> </div>"""))
    content = TextAreaField('', validators=[nothing])


class BugForm(FlaskForm):
    yourMail = StringField(' ', validators=[Email()])
    buggedContent = TextAreaField(' ', validators=[DataRequired()])
    description = TextAreaField(' ')

@app.route('/', methods=["GET", "POST"])
def home():
    try:
        form = RegistrationForm(request.form)
        content = form.content
        if form.validate_on_submit():
            session['text'] = content.data
            #print(content.data)
            return redirect(url_for('findChords'))
        else:
            return render_template("main.html", form=form)
    except Exception as e:
        return render_template("errorPage.html")


@app.route('/info')
def info():
    return render_template("info.html")


@app.route('/download')
def download():
    return render_template("download.html")


#@app.route('/test')
#def test():
 #   return gettext('THIS WORKSS')

@app.route('/report', methods=["GET", "POST"])
def report():
    try:
        form = BugForm(request.form)
        yourMail = form.yourMail
        buggedContent = form.buggedContent
        description = form.description

        if form.validate_on_submit():
            #print("propai IF")

            msg = Message("BUG REPORT!",
                          sender="probaflask@gmail.com",
                          recipients=["aaaaa@a.a", "bbbbbb@b.b"])
            msg.body = "Hi!\n" \
                       "I found bug in this lyrics: \n" + buggedContent._value() + "\n \n" \
                        "Description of problem: " + description._value() + "\n \n" \
                        "Reply on: " + str(yourMail._value())
            mail.send(msg)
            #print("poslao")
            return redirect(url_for('home'))
        else:
            return render_template("posalji.html", form=form)
    except Exception as e:
        return render_template("errorPage.html")


#@app.route('/lang/hr')
#def hr():
 #   session['lang'] = 'hr'
  #  if session.get("temp") is None:
   #     session['temp'] = 'home'
    #return redirect(url_for(session['temp']))

#@app.route('/lang/en')
#def en():
 #   session['lang'] = 'en'
  #  if session.get("temp") is None:
   #     session['temp'] = 'home'
    #return redirect(url_for(session['temp']))

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.route('/find')
def findChords():
    try:
        def isChord(chord): #Not for routing purposes, logic function.
            first = ['a', 'b', 'h', 'c', 'd', 'e', 'f', 'g']
            second = ['m', '4', '5', '9', '2', '7', 'b', '#', '+', '/', 'd', 'a', '.', 's', 'i', 'e']

            if chord != "": #eliminating index exception
                if len(chord) > 8 or chord[0].lower() not in first or chord.lower() in lista:
                    return 0
                elif len(chord) == 1 and chord.lower() in first:
                    return 1
                elif len(chord) <= 8 and len(chord) > 1 and chord.lower()[1] in second:
                    flag = 1
                    try:
                        if chord[1] == "i":
                            if chord[2] != "s":
                                flag = 0
                    except Exception:
                        flag = 0
                    return flag
                else:
                    return 0
            else:
                pass

        listLines = []
        listFlag = []
        listChords = []                         # here go chords only
        for line in session['text'].splitlines():
            line = line.replace("-", " ")#.replace("(", " ").replace(")", " ")
            listLines.append(line)


        listLines = [i.split(' ') for i in listLines]
        listLinesNoBlank = []
        for line in listLines:
            listLinesNoBlank.append([item for item in line if item != ''])

        print(listLines)
        for i in range(len(listLines)):
            for j in range(len(listLines[i])):
                if len(listLines[i][j]) > 1:
                    if listLines[i][j].startswith("("):
                        print("PRVIII")
                        listLines[i][j] = listLines[i][j][1:]
                    if listLines[i][j].endswith(")"):
                        print("DRUGII")
                        listLines[i][j] = listLines[i][j][:-1]

        for line in listLinesNoBlank:
            _sum = 0
            for word in line:
                if isChord(word) in [0, 1]:
                    _sum += isChord(word)

            try:
                if _sum/len(line) >= 0.5:
                    listFlag.append(1)
                else:
                    listFlag.append(0)
            except Exception:
                listFlag.append(0)

        for i in range(len(listFlag)):
            if listFlag[i]:
                for j in range(len(listLines[i])):
                    if isChord(listLines[i][j]):
                        lenghthFirst = len(listLines[i][j])
                        try:
                            if listLines[i][j][2] == 'u': #cheching for SUS chord
                                #so we woudn't change "Esus4" for example
                                listLines[i][j] = listLines[i][j].replace("H", "B").replace("Cis", "C#")\
                                    .replace("Des", "Db").replace("Dis", "D#").replace("Eis", "F").replace("Fis", "F#")\
                                    .replace("Ges", "Gb").replace("Gis", "G#").replace("Ais", "A#").replace("Hes", "Bb")\
                                    .replace("FIS", "F#").replace("CIS", "C#").replace("GIS", "G#")
                            else:
                                listLines[i][j] = listLines[i][j].replace("H", "B").replace("Cis", "C#") \
                                    .replace("Des", "Db").replace("Dis", "D#").replace("Es", "Eb").replace("Eis", "F")\
                                    .replace("Fis", "F#").replace("Ges", "Gb").replace("Gis", "G#").replace("As", "Ab")\
                                    .replace("Ais", "A#").replace("Hes", "Bb").replace("Es", "Eb").replace("FIS", "F#")\
                                    .replace("CIS", "C#").replace("GIS", "G#")

                        except Exception:
                            listLines[i][j] = listLines[i][j].replace("H", "B").replace("Cis", "C#") \
                                .replace("Des", "Db").replace("Dis", "D#").replace("Es", "Eb").replace("Eis", "F")\
                                .replace("Fis", "F#").replace("Ges", "Gb").replace("Gis", "G#").replace("As", "Ab")\
                                .replace("Ais", "A#").replace("Hes", "Bb").replace("Es", "Eb").replace("FIS", "F#")\
                                .replace("CIS", "C#").replace("GIS", "G#")
                        listLines[i][j] += " " * (lenghthFirst-len(listLines[i][j]))  #to compensate any changes in length
                    #print("FOUND", listLines[i][j])
                        listChords.append(listLines[i][j])
                        temp = '<span class="chord">' + listLines[i][j] + '</span>'
                        listLines[i][j] = temp

        #session['chords'] = listChords
        #print(session['chords'])
        finalString = ""
        for i in range(len(listLines)):
            for j in range(len(listLines[i])):
                if listLines[i][j] == ' ':
                    finalString += '&nbsp;'
                else:
                    finalString += listLines[i][j] + '&nbsp;'
            finalString += "<br>"

        finalString = Markup(finalString)
        print(finalString)
        return Response(render_template("template.html", finalString=finalString, listChords=listChords))
    except Exception as e:
        return render_template("errorPage.html")

if __name__ == "__main__":
    app.run(debug=True, port=80, host="0.0.0.0")