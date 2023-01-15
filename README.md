# TelegramGuessGame
A Telegram guessing game bot.

This code creates a simple guessing game Telegram bot using the python-telegram-bot library (telebot). The bot starts by generating a random number between 1 and 100 and sending a message to the user asking them to guess the number. The user can then input their guesses and the bot will check if the guess is correct and if not it will give hint if the number is higher or lower. The bot also has a 5 attempts limit to let the user know how many attempts they have left, and it also checks if the input is a number or not.

This bot has a start_game function that generates a random number between 1 and 100 and sends a message to the user asking them to guess the number. It then registers the guess_number function as a handler for the next message, which will check if the user's guess is correct, and if not, sends a hint about whether the number is higher or lower.

Please make sure to replace YOUR_BOT_TOKEN with your actual token for this script to work.
