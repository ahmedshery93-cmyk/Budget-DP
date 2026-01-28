import os
from flask import Flask, request
import telebot
import google.generativeai as genai
import pandas as pd

app = Flask(__name__)

# إعدادات المفاتيح (سنضعها لاحقاً)
TOKEN = 'YOUR_TELEGRAM_TOKEN'
genai.configure(api_key="YOUR_GEMINI_KEY")
bot = telebot.TeleBot(TOKEN)

@app.route('/')
def index():
    return "SiteAiReport is Online!"

# نقطة استقبال رسائل تليجرام
@app.route('/' + TOKEN, methods=['POST'])
def getMessage():
    json_string = request.get_data().decode('utf-8')
    update = telebot.types.Update.de_json(json_string)
    bot.process_new_updates([update])
    return "!", 200

if __name__ == "__main__":
    app.run()
