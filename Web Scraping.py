#Libraries
from googlesearch import search
import customtkinter as ctk
import tkinter as tk
from time import sleep
import os
#Global values
Basic_Font_ColorL = "#000000"
Basic_Background_ColorL = "#FFFFFF"
Basic_Font_ColorD = "#FFFFFF"
Basic_Background_ColorD = "#000000"
search_path = "Models/file.txt"
default_font = "Roboto"
default_font_size = 15
search_query = ''
####CHANGE NUMBERS TO STRINGS
options_num_links = ['1','2','3','4','5','6','7','8','9','10']
num_links = 3
class MyFrame(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        # add widgets onto the frame, for example:
        self.label = ctk.CTkLabel(self,text='')
        self.label.grid(row=0, column=0, padx=0)

class MainWindow(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("800x600")# size
        self.title("Review Estimaor Start")#title


        self.leftframe = MyFrame(self, fg_color = (Basic_Background_ColorL, Basic_Background_ColorD))
        self.leftframe.grid(row = 0, column = 0, columnspan = 2, rowspan = 2,sticky = "w", padx = 10, pady =30)

        self.LabelComment = ctk.CTkLabel(self.leftframe, fg_color = (Basic_Background_ColorL, Basic_Background_ColorD ),font = (default_font,default_font_size)  , text = "Enter Search -")
        self.LabelComment.grid(row = 0, column = 0,sticky = "nw", padx = 10, pady =10)

        self.optionmenu = ctk.CTkOptionMenu(self.leftframe, values= options_num_links, command =self.numberoption)
        self.optionmenu.set('3')
        self.optionmenu.grid(row = 0, column = 1,sticky = "e", padx = 10, pady =10)


        
        self.text_area = tk.Text(self.leftframe, wrap=tk.WORD, 
                                      width=40, height=8, 
                                      font=(default_font, default_font_size)) 
        self.text_area.grid(row = 1, column = 0, columnspan = 8,sticky = "nswe", padx = 10, pady =30)

        
        self.searchbutton = ctk.CTkButton(self.leftframe, text = "Search", fg_color = (Basic_Font_ColorL, Basic_Font_ColorD),text_color= (Basic_Background_ColorL, Basic_Background_ColorD) ,command = self.test)
        self.searchbutton.grid(row = 4, column = 2, columnspan = 1,sticky = "w", padx = 20, pady =20)

        self.clearbutton = ctk.CTkButton(self.leftframe, text = "Clear", fg_color = (Basic_Font_ColorL, Basic_Font_ColorD),text_color= (Basic_Background_ColorL, Basic_Background_ColorD) ,command = self.clear)
        self.clearbutton.grid(row = 4, column = 0, columnspan = 1,sticky = "w", padx = 20, pady =20)

        self.rightframe = MyFrame(self, fg_color = (Basic_Background_ColorL, Basic_Background_ColorD))
        self.rightframe.grid(row = 0, column = 6, columnspan = 2, rowspan = 2,sticky = "w", padx = 10, pady =30)



    def numberoption(self, choice):
        global num_links
        num_links = int(choice)
        print(num_links)

    def clear(self):
        self.text_area.delete("1.0", "end")

    def search_google(self):
        links = []
        global num_links
        num_results = num_links
        query = self.text_area.get("1.0", "end - 1 chars")
        ####CHECK TO SEE IF SEARCH HAS ALREDY BEEN MADE
        if os.path.isfile(f'./links/{query}{num_results}.txt') == True and os.path.isfile('./model_tfidf') == True:
                self.Message.configure(text = "The model number 1 is saved")
                # Perform Google search and retrieve top results
                with open('./links/{query}{num_results}.txt', 'r') as file:
                    # Iterate over each line in the file
                    for line in file:
                        # Process each line as needed
                        print(line.strip())  # Print the line after removing leading and trailing whitespaces
        else:
                results = search(query, num=num_results, stop=num_results)

                # Iterate through the results and store the links
                with open(f'./links/{query}{num_results}.txt', 'w') as file:
                    file.write(f'The searched string is {query}' + '\n')
                    file.write(f'The number of links are {num_results}' + '\n')
                for link in results:
                    links.append(link)
                    print(link)

                # Save the links to a file
                with open(f'./links/{query}{num_results}.txt', 'w') as file:
                    for link in links:
                        file.write(link + '\n')

                print(f"\nTop {num_results} links saved to '{query}{num_results}.txt'")

    def test(self):
        self.search_google()

ctk.set_appearance_mode("system")
# Perform the Google search and save the top three links
root = MainWindow()
root.mainloop()   