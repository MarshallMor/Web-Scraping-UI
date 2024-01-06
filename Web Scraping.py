#Libraries
from googlesearch import search
import customtkinter as ctk
import tkinter as tk
from time import sleep
import os, shutil
import webbrowser
from functools import partial
import requests
from bs4 import BeautifulSoup
import operator
from collections import Counter
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
nltk.download('stopwords')
nltk.download('punkt')
stop_words = set(stopwords.words('english'))

#Global values
Basic_Font_ColorL = "#000000"
Basic_Background_ColorL = "#FFFFFF"
Basic_Font_ColorD = "#FFFFFF"
Basic_Background_ColorD = "#000000"
search_path = "Models/file.txt"
default_font = "Roboto"
default_font_size = 12
search_query = ''
number_messages = 1
top = 500
num_wordlist = ['100','200','300','400','500','600','700','800','900','1000']
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
        self.geometry("800x700")# size
        self.title("Review Estimaor Start")#title


        self.leftframe = MyFrame(self, fg_color = (Basic_Background_ColorL, Basic_Background_ColorD))
        self.leftframe.grid(row = 0, column = 0, columnspan = 2, rowspan = 2,sticky = "w", padx = 10, pady =30)

        self.LabelComment = ctk.CTkLabel(self.leftframe, fg_color = (Basic_Background_ColorL, Basic_Background_ColorD ),font = (default_font,default_font_size)  , text = "Enter Search -")
        self.LabelComment.grid(row = 0, column = 0,sticky = "nw", padx = 10, pady =10)

        self.optionmenu = ctk.CTkOptionMenu(self.leftframe, values= options_num_links, command =self.numberoption)
        self.optionmenu.set('3')
        self.optionmenu.grid(row = 0, column = 1,sticky = "e", padx = 10, pady =10)

        self.optionmenu = ctk.CTkOptionMenu(self.leftframe, values= num_wordlist, command =self.wordlistoption)
        self.optionmenu.set('500')
        self.optionmenu.grid(row = 0, column = 2,sticky = "e", padx = 10, pady =10)
        
        self.text_area = tk.Text(self.leftframe, wrap=tk.WORD, 
                                      width=40, height=8, 
                                      font=(default_font, 18)) 
        self.text_area.grid(row = 1, column = 0, columnspan = 8,sticky = "nswe", padx = 10, pady =30)

        
        self.searchbutton = ctk.CTkButton(self.leftframe, text = "Search", fg_color = (Basic_Font_ColorL, Basic_Font_ColorD),text_color= (Basic_Background_ColorL, Basic_Background_ColorD) ,command = self.test)
        self.searchbutton.grid(row = 4, column = 2, columnspan = 1,sticky = "w", padx = 20, pady =20)

        self.clearbutton = ctk.CTkButton(self.leftframe, text = "Clear", fg_color = (Basic_Font_ColorL, Basic_Font_ColorD),text_color= (Basic_Background_ColorL, Basic_Background_ColorD) ,command = self.clear)
        self.clearbutton.grid(row = 4, column = 0, columnspan = 1,sticky = "w", padx = 20, pady =20)

        self.clearlinksbutton = ctk.CTkButton(self.leftframe, text = "Clear Links", fg_color = (Basic_Font_ColorL, Basic_Font_ColorD),text_color= (Basic_Background_ColorL, Basic_Background_ColorD) ,command = self.clear_links)
        self.clearlinksbutton.grid(row = 5, column = 0, columnspan = 1,sticky = "w", padx = 20, pady =20)

        self.clearmessagesbutton = ctk.CTkButton(self.leftframe, text = "Clear Messages", fg_color = (Basic_Font_ColorL, Basic_Font_ColorD),text_color= (Basic_Background_ColorL, Basic_Background_ColorD) ,command = self.clear_messages)
        self.clearmessagesbutton.grid(row = 6, column = 0, columnspan = 1,sticky = "w", padx = 20, pady =20)

        self.clearwordlistbutton = ctk.CTkButton(self.leftframe, text = "Clear Wordlist", fg_color = (Basic_Font_ColorL, Basic_Font_ColorD),text_color= (Basic_Background_ColorL, Basic_Background_ColorD) ,command = self.clear_wordlist)
        self.clearwordlistbutton.grid(row = 4, column = 1, columnspan = 1,sticky = "w", padx = 20, pady =20)

        self.wordlistbutton = ctk.CTkButton(self.leftframe, text = "Create Wordlist", fg_color = (Basic_Font_ColorL, Basic_Font_ColorD),text_color= (Basic_Background_ColorL, Basic_Background_ColorD) ,command = self.start)
        self.wordlistbutton.grid(row = 5, column = 2, columnspan = 1,sticky = "w", padx = 20, pady =20)

        self.rightframe = MyFrame(self, fg_color = (Basic_Background_ColorL, Basic_Background_ColorD))
        self.rightframe.grid(row = 0, column = 6, columnspan = 2, rowspan = 2,sticky = "w", padx = 10, pady =30)

    


    def numberoption(self, choice):
        global num_links
        num_links = int(choice)
        print(num_links)
    def wordlistoption(self, choice):
        global top
        top = int(choice)
        print(num_links)

    def clear(self):
        self.text_area.delete("1.0", "end")

    def search_google(self):
        links = []
        global num_links
        global number_messages
        num_results = num_links
        query = self.text_area.get("1.0", "end - 1 chars")
        ####CHECK TO SEE IF SEARCH HAS ALREDY BEEN MADE
        if os.path.isfile(f'./links/{query}_{num_results}.txt') == True:
                # Perform Google search and retrieve top results
                with open(f'./links/{query}_{num_results}.txt', 'r') as file:
                    # Iterate over each line in the file
                    for line in file:
                        # Process each line as needed
                            self.create_hyperlink(line,number_messages)
                            print(line.strip())  
                            number_messages = number_messages + 1
                            # Print the line after removing leading and trailing whitespaces
                self.Comment = ctk.CTkLabel(self.rightframe, fg_color = (Basic_Background_ColorL, Basic_Background_ColorD ),font = (default_font,default_font_size)  , text = f"The file is already made at {query}_{num_results}.txt")
                self.Comment.grid(sticky = "nw", padx = 10, pady =10)
                
                number_messages = 1
        else:
            results = search(query, num=num_results, stop=num_results)
            for link in results:
                    links.append(link)
                    print(link)

            # Save the links to a file
            with open(f'./links/{query}_{num_results}.txt', 'a') as file:
                for link in links:
                    self.create_hyperlink(link,number_messages)
                    number_messages = number_messages + 1
                    file.write(link + '\n')
            
            self.Comment = ctk.CTkLabel(self.rightframe, fg_color = (Basic_Background_ColorL, Basic_Background_ColorD ),font = (default_font,default_font_size)  , text = f"The new file was created with the name {query}_{num_results}.txt")
            self.Comment.grid(sticky = "nw", padx = 10, pady =10)
            print(f"\nTop {num_results} links saved to {query}{num_results}.txt")
            number_messages = 1

    def create_hyperlink(self, link, num):
        label = tk.Label(self.rightframe, text=f"Hyperlink {num}", fg="blue", cursor="hand2")
        label.grid(sticky="nw", padx=10, pady=10)
        label.bind("<Button-1>", lambda e: self.callback(link))
        
    def grab_urls(self):
        links = []
        global num_links
        global number_messages
        num_results = num_links

        query = self.text_area.get("1.0", "end - 1 chars")
        if os.path.isfile(f'./links/{query}_{num_results}.txt'):
            with open(f'./links/{query}_{num_results}.txt', 'r') as file:
                for line in file:
                    self.create_hyperlink(line,number_messages)
                    links.append(line.strip())
                    number_messages = number_messages  + 1
                    print(line.strip())
                    num_results
                    
            self.Comment = ctk.CTkLabel(self.rightframe, fg_color=(Basic_Background_ColorL, Basic_Background_ColorD),
                                        font=(default_font, default_font_size), text="Link list is made")
            self.Comment.grid(sticky="nw", padx=10, pady=10)
        else:
            self.Comment = ctk.CTkLabel(self.rightframe, fg_color=(Basic_Background_ColorL, Basic_Background_ColorD),
                                        font=(default_font, default_font_size),
                                        text=f"No file name: {query}_{num_results}.txt")
            self.Comment.grid(sticky="nw", padx=10, pady=10)

        return links

    def create_dictionary(self, clean_list):
        global top
        word_count = Counter(clean_list)
        return word_count.most_common(top)

    def remove_stop_words(self, sentence):
        words = word_tokenize(sentence)
        filtered_words = [word for word in words if word.lower() not in stop_words]
        return ' '.join(filtered_words)

    def clean_wordlist(self, wordlist):
        global num_links
        num = num_links
        query = self.text_area.get("1.0", "end - 1 chars")
        clean_list = []
    

        for word in wordlist:
            # Remove symbols
            symbols = "!@#$%^&*()_-+={[}]|\\;:\"<>?/., "
            for symbol in symbols:
                word = word.replace(symbol, '')

            # Remove stop words
            word = self.remove_stop_words(word)

            if len(word) > 0:
                clean_list.append(word)

        top_words = self.create_dictionary(clean_list)
        
        self.save_to_file(top_words, f'{query}{num}WL.txt')

    def start(self):
        urls = self.grab_urls()
        all_wordlists = []

        for url in urls:
            wordlist = []
            source_code = requests.get(url).text
            soup = BeautifulSoup(source_code, 'html.parser')

            for each_text in soup.find_all('div', {'class': 'entry-content'}):
                content = each_text.text
                words = content.lower().split()

                for each_word in words:
                    wordlist.append(each_word)

            all_wordlists.append(wordlist)

        # Flatten the list of lists
        all_words = [word for sublist in all_wordlists for word in sublist]
        self.clean_wordlist(all_words)

    def save_to_file(self, wordlist, filename):
        with open(f'./wordlists/{filename}', 'a') as file:
            for word in wordlist:
                file.write(word + '\n')

# Example usage:
# Replace 'your_url_1', 'your_url_2', etc. with the URLs you want to analyze

    def test(self):
        self.search_google()
    def callback(self, url):
        webbrowser.open_new(url)
    def clear_wordlist(self):
        folder = './wordlists'
        for filename in os.listdir(folder):
            file_path = os.path.join(folder, filename)
            try:
                if os.path.isfile(file_path) or os.path.islink(file_path):
                    os.unlink(file_path)
                elif os.path.isdir(file_path):
                    shutil.rmtree(file_path)
            except Exception as e:
                print('Failed to delete %s. Reason: %s' % (file_path, e))
    def clear_links(self):
        folder = './links'
        for filename in os.listdir(folder):
            file_path = os.path.join(folder, filename)
            try:
                if os.path.isfile(file_path) or os.path.islink(file_path):
                    os.unlink(file_path)
                elif os.path.isdir(file_path):
                    shutil.rmtree(file_path)
            except Exception as e:
                print('Failed to delete %s. Reason: %s' % (file_path, e))
    def clear_messages(self):
        for widget in self.rightframe.winfo_children():
            widget.destroy()
         
        self.rightframe.pack_forget()

        self.rightframe = MyFrame(self, fg_color = (Basic_Background_ColorL, Basic_Background_ColorD))
        self.rightframe.grid(row = 0, column = 6, columnspan = 2, rowspan = 2,sticky = "w", padx = 10, pady =30)


    
ctk.set_appearance_mode("system")
# Perform the Google search and save the top three links
root = MainWindow()
root.mainloop()  
 