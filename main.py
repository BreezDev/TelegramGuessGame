import random
import telebot
from telebot import types

bot = telebot.TeleBot("YOUR_BOT_TOKEN")

def start_game(message):
    # generate a random number between 1 and 100
    secret_number = random.randint(1, 100)
    bot.send_message(message.chat.id, "I am thinking of a number between 1 and 100. Can you guess what it is? You have 5 attempts.")
    bot.register_next_step_handler(message, guess_number, secret_number)

def guess_number(message, secret_number):
    try:
        # checking if the input is a number
        guess = int(message.text)
    except ValueError:
        bot.send_message(message.chat.id, "Please enter a valid number.")
        return

    if guess == secret_number:
        bot.send_message(message.chat.id, "Congratulations! You guessed the number correctly.")
    elif guess < secret_number:
        bot.send_message(message.chat.id, "The number is higher.")
    else:
        bot.send_message(message.chat.id, "The number is lower.")

@bot.message_handler(commands=['start'])
def start(message):
    start_game(message)

bot.polling()
