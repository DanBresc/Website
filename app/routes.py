from flask import render_template
from app import app
from app.forms import *
from flask import render_template, flash, redirect
import time
import random
import string

#Created Packages 
from app import wordJumblerBackEnd as WJ
from app import caesarCipherBackEnd as CC
from app import soundReverserBackEnd as SR
#from app import typingTestBackEnd as TT

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='Home')

@app.route('/wordJumbler', methods =['GET','POST']) 
def wordJumbler():
    form = WordJumblerForm()
    if form.validate_on_submit():
        
        jWord = form.jWord.data.lower()
        newWordList = WJ.jumbleWords(jWord);
        
        for word in newWordList:
            flash("Unjumbled Word(s): %s" %word)
        if not newWordList:
            flash("No words found")
            
    return render_template('wordJumbler.html', title = 'Word Jumbler', form = form)
    
@app.route('/caesarCipher',methods =['GET','POST'])
def caesarCipher():    
    form = CaesarCipherForm()
    if form.validate_on_submit():
        cipherKey = form.cipherKey.data
        originalMessage = form.originalMessage.data.lower()
        encodedMessage = form.encodedMessage.data.lower()
        
        encodedString = CC.encodeMessage(originalMessage,cipherKey)
        decodedString = CC.decodeMessage(encodedMessage,cipherKey)
        
        flash("Encoded Message: " + encodedString)
        flash("Decoded String: " + decodedString)
    return render_template('caesarCipher.html', title = "Caesar Cipher",form = form)
    
@app.route('/soundReverser', methods = ['GET','POST'])
def soundReverser():
    form = SoundReverserForm()
    if form.validate_on_submit():
        recordTime = form.recordTime.data
        
        SR.reverseSound(recordTime)
        time.sleep(3)
        SR.playSound()
        
        flash("Finished Playing Sound")
    return render_template('soundReverser.html', title = "Sound Reverser", form = form)
    
@app.route('/workExperience')
def workExperience():
    return render_template('workExperience.html', title = "My Work Experiance")

@app.route('/lgl')
def logicGateLibary():
    return render_template('lgl.html', title = "Logic Gate Library")

@app.route('/about')
def about():
    return render_template('about.html',title = 'About The Project')
    

    