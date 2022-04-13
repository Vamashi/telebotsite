 from browser import document, ajax
        import telebot

        url = 'https://api.chucknorris.io/jokes/random'

        datafile = open("data.txt","r")

        def authbot(e):
            token = document['token'].value
            id = document['uid'].value
            try:
                bot = telebot.TeleBot(token)
                bot.send_message(id, "Bot authorized")
                browser.alert("Succesfully conected!")
            except:
                browser.alert("Error was to connect! Check your token and id, and be sure you writed something to your bot before!")

        document['telesendbtn'].bind('click', authbot)