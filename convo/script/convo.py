from tkinter import *
from tkinter import ttk
import tkinter.filedialog
tk = Tk()
boi=StringVar()




canvas = Canvas(width=600, height=100)


bot = PhotoImage(file="C:\\Users\\lucas.bachand\\Desktop\\convo\\images\\bot.gif")
bot2 = PhotoImage(file="C:\\Users\\lucas.bachand\\Desktop\\convo\\images\\bot2.gif")
canvas.create_image(230, 0, anchor=NW, image=bot)

tk.title("bot")

canvas.create_image(230, 0, anchor=NW, image=bot)

text0 = ttk.Label(tk, text="hello", font=("Courier", 25))

nxt = 0
typing_box = ttk.Entry(tk, textvariable=boi)
typing_box.pack()
def Kill():
    quit()

kill_switch = ttk.Button(tk, text ="Bye", command=Kill)

def Send():
    mtext = boi.get()

    global nxt


    if mtext in ['what']:

        if nxt == 5:
            global text6
            global text3
            global text1
            global bot
            global name
            global text5
            global were
            global pets_name


            text7 = ttk.Label(tk, text="your pets name is " + pets_name + " you live at " + were + " your name is " + name + " intresting info for the dark web which I will now upload", font=("Courier", 25), wraplength=200)
            text6.destroy()
            text7.pack()
            typing_box.destroy
            button.destroy()
            kill_switch.pack()
            
            typing_box.delete(0, 'end')





    if not mtext in ['']:
        if nxt == 4:
            pets_name=mtext
            text6 = ttk.Label(tk, text="nice " + name + " cool name guss what I've got (;", font=("Courier", 25))
            text5.destroy()
            text6.pack()
            nxt += 1
            typing_box.delete(0, 'end')

    if mtext in ['no', 'nope', 'I do not']:

        if nxt == 3:


            text4 = ttk.Label(tk, text="loser I don't like with people with no pets " + name + " bye", font=("Courier", 25))
            text3.destroy()
            text4.pack()
            typing_box.destroy()
            button.destroy()
            kill_switch.pack()
            
            
            

    if mtext in ['yes', 'I do']:
        if nxt == 3:
            text5 = ttk.Label(tk, text="nice " + name + " name your most liked pets name", font=("Courier", 25))
            text3.destroy()
            text5.pack()
            nxt += 1
            typing_box.delete(0, 'end')


    if not mtext in ['']:
        if nxt == 2:
            global text2
            were=mtext
            nxt += 1
            text3 = ttk.Label(tk, text="cool " + name + " do you have any pets?", font=("Courier", 25))        
            text3.pack()
            text2.destroy()
            typing_box.delete(0, 'end')
        else:
            pass
            
    if not mtext in ['']:    
        if nxt == 1:
        
            nxt += 1
            text2 = ttk.Label(tk, text="nice name " + mtext + " were do you live?", font=("Courier", 25))        
            text2.pack()
            text1.destroy()
            name=mtext
            typing_box.delete(0, 'end')
        else:
            pass
            
   
    
    if mtext in ['hello', 'hey', 'hi', 'howdy']:
        if nxt == 0:
            nxt += 1
            text1 = ttk.Label(tk, text="my name is the aim bot 6000 and yours?", font=("Courier", 25))
            text0.destroy()
            text1.pack()
            typing_box.delete(0, 'end')
            
            
        else:
            pass







            
        
        
    else:
        return
    


    

    





button = ttk.Button(tk, text ="Ok", command=Send)









    
    

button.pack()
canvas.pack()
text0.pack()



