import tkinter
from tkinter import ttk, filedialog
from tkinter import *
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import os
import csv
import os.path
import time
from functools import partial
import urllib.request

url = 'https://example.com/login'
url2 = 'https://example.com'
url3 = 'https://example.com'
url4 = 'https://example.com'
url5 = 'https://example.com'

root = Tk()
frm = ttk.Frame(root, padding=10)
root.title('ceny i zdjecia')
frm.grid()
start_count = ''
zmienna = ''


def link_zdjecia():
    global zmienna, start_count
    root.zdjecia = filedialog.askopenfilename(initialdir="/", title="Select file",
                                              filetypes=(("csv files", "*.csv"), ("all files", "*.*")))
    zmienna = root.zdjecia
    labelPlik['text'] = zmienna
    labelPlik['background'] = '#5FD068'
    start_count += 'A'
    print(start_count)
    AAA = start_count.find('A')
    BBB = start_count.find('B')
    CCC = start_count.find('C')
    if AAA >= 0 and BBB >= 0 and CCC >= 0:
        start_normal()
    return


zmienna1 = ''


def zdjecia():
    global zmienna1, start_count
    root.savezdj = filedialog.askdirectory(initialdir="/", title="Select folder")

    zmienna1 = root.savezdj
    labelFolder['text'] = zmienna1
    labelFolder['background'] = '#5FD068'
    start_count += 'B'
    print(start_count)
    AAA = start_count.find('A')
    BBB = start_count.find('B')
    CCC = start_count.find('C')
    if AAA >= 0 and BBB >= 0 and CCC >= 0:
        start_normal()
    return


login1 = ''
haslo1 = ''


def login():
    global login1, haslo1, start_count
    # print("username entered :", username.get())
    # print("password entered :", password.get())
    login1 = username.get()
    haslo1 = password.get()
    label['text'] = "zapisano login i haslo"
    label['background'] = '#5FD068'
    start_count += 'C'
    print(start_count)
    AAA = start_count.find('A')
    BBB = start_count.find('B')
    CCC = start_count.find('C')
    if AAA >= 0 and BBB >= 0 and CCC >= 0:
        start_normal()
    return


# ttk.Button(frm, text="login", command=login).grid(column=1, row=1)
username = StringVar()
ttk.Entry(frm, textvariable=username).grid(column=1, row=0)

password = StringVar()
ttk.Entry(frm, textvariable=password).grid(column=1, row=1)
ttk.Button(frm, text="dodaj login i haslo", command=login, padding=1).grid(column=1, row=2)
validateLogin = partial(login, username, password)
label = ttk.Label(frm, text="dodaj login i hasło", background='#FC4F4F')
label.grid(column=1, row=3)

ttk.Label(frm, text="ceny i zdjęcia ").grid(column=0, row=0)
ttk.Button(frm, text="Wybierz plik", command=link_zdjecia).grid(column=0, row=1)
ttk.Button(frm, text="Wybierz folder", command=zdjecia).grid(column=0, row=2)
labelPlik = ttk.Label(frm, text="Ścieżka do pliku csv po wybraniu pojawi sie tutaj", background='#FC4F4F')
labelPlik.grid(column=0, row=5, columnspan=2)
labelFolder = ttk.Label(frm, text="Ścieżka do folderu zapisu po wybraniu pojawi sie tutaj", background='#FC4F4F')
labelFolder.grid(column=0, row=6, columnspan=2)

xd = ''
feom = ''


def is_good():

    if not login1:
        print("nie podales loginu")
        tkinter.messagebox.showinfo(title=None, message='nie podałes loginu')
    elif not haslo1:
        print("nie podales loginu")
        tkinter.messagebox.showinfo(title=None, message='nie podałes hasla')
    elif not zmienna:
        print("nie podales loginu")
        tkinter.messagebox.showinfo(title=None, message='nie wybrałeś pliku csv')
    elif not zmienna1:
        print("nie podales loginu")
        tkinter.messagebox.showinfo(title=None, message='nie wybrałeś ścieżki folderu do zapisu')
    else:
        start_zdjecia()



def start_zdjecia():
    try:
        ###tworzenie folderów
        par_dir = zmienna1
        path = os.path.join(par_dir, 'zdjecia')
        try:
            os.mkdir(path)
        except:
            pass
        path1 = os.path.join(path, '1')
        path2 = os.path.join(path, '2')
        path3 = os.path.join(path, '3')
        path4 = os.path.join(path, '4')
        path5 = os.path.join(path, '5')
        path6 = os.path.join(path, '6')
        path7 = os.path.join(path, '7')
        path8 = os.path.join(path, '8')
        try:
            os.mkdir(path1)
            os.mkdir(path2)
            os.mkdir(path3)
            os.mkdir(path4)
            os.mkdir(path5)
            os.mkdir(path6)
            os.mkdir(path7)
            os.mkdir(path8)
        except:
            pass


        ###
        # print(zmienna, zmienna1)
        # zmienna = link_zdjecia()
        # zmienna1 = zdjecia()
        # print("username entered :", login1)
        # print("password entered :", haslo1)
        print(zmienna, zmienna1)  # zmienna1 jest do folderu

        s = Service('C:\webdriver\chromedriver.exe')
        browser = webdriver.Chrome(service=s)
        browser.get(url)
        browser.implicitly_wait(2)
        m = browser.find_element("id", 'userID')
        m.send_keys(login1)
        time.sleep(0.1)
        m1 = browser.find_element("id", 'password')
        m1.send_keys(haslo1)
        time.sleep(0.1)
        m1.send_keys(Keys.TAB)
        m1.send_keys(Keys.ENTER)
        browser.implicitly_wait(2)
        browser.find_element(By.ID, "CybotCookiebotDialogBodyButtonAccept").click()
        browser.implicitly_wait(2)
        time.sleep(2)
        browser.get(url2)
        browser.implicitly_wait(2)
        browser.find_element(By.ID, "idBtn_Back").click()  # id microsoftu
        browser.implicitly_wait(7)
        print(zmienna)
        with open(fr'{zmienna}', 'r',
                  encoding='Windows-1252') as fil:  ###tutaj dodac zmienna o csv z którego sie pobiera
            reader = csv.reader(fil, delimiter=',')
            lista = list()
            for row in reader:
                lista.append(row[0])  # .lstrip()
        ##tutaj foldery

        ##
        for item in lista:
            time.sleep(1)
            browser.refresh()
            time.sleep(1)
            l = browser.find_element("id", 'searchText')
            l.send_keys(item)
            l.send_keys(Keys.ENTER)
            browser.implicitly_wait(1)
            try:

                browser.find_element(By.ID, "product-code-1").click()
            except:
                pass

            browser.implicitly_wait(1)

            # images
            global y, xd, feom
            html_doc = browser.page_source
            soup = BeautifulSoup(html_doc, 'html.parser')
            try:
                feom = soup.find(class_='Magic360')

            except:
                pass
            if not feom:
                xd = '0'
            else:
                xd = '1'
            print("FEOM:", feom)
            print("a to xd: ", xd)
            try:
                y = soup.find(id="product-code").text
                print(y)
                if item == soup.find(id="product-code").text:
                    x = soup.find_all(class_='modal-image')
                    print(x)
                    """
                    sak = list()
                    for fak in x:
                        sake1 = fak['src']
                        sak.append(str(sake1))
                    """

                    try:
                        kat = soup.find(id="price-list").text
                        kat = kat.replace("\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\n\t\t\t\t\t\t\t\t", '')
                        # kat = kat.replace(",", '')
                        net = soup.find(id="net-price").text
                        net = net.replace("\n\t\t\t\t\t\t\t\t", '')
                        # net = net.replace(",", '')

                        ceny = list()
                        zdjeciaa = list()
                        czystaszesc = list()
                        ceny.append(item)
                        # ceny.append(xd)
                        ceny.append(net)
                        ceny.append(kat)
                        # ceny.append(x)
                        czystaszesc.append(item)
                        czystaszesc.append(feom)
                        zdjeciaa.append(item)
                        zdjeciaa.append(x)
                        # ceny.append(xd)

                        with open(fr"{zmienna1}/ceny.csv",
                                  'a') as fi:  ## tutaj podac scieżke gdzie ma sie zapisać plik csv
                            writer = csv.writer(fi)  # , quoting=csv.QUOTE_NONE, quotechar='')
                            writer.writerow(ceny)
                            print("dodało wiersz")
                        with open(fr"{zmienna1}/zdjecia.csv",
                                  'a') as fi:  ## tutaj podac scieżke gdzie ma sie zapisać plik csv
                            writer = csv.writer(fi)  # , quoting=csv.QUOTE_NONE, quotechar='')
                            writer.writerow(zdjeciaa)

                            print("dodało wiersz")
                        ####
                        # dodac pobieranie zdjec, najpierw musi byc stworzony folder
                        # folder ze zdjeciami id folderami od 1 do 9 i do nich odowiednio doawac zdjecia o takim id
                        # ale zanim zdjęcia bedą pobierane to trzeba przyszykować zmienna pociachac ja na
                        # pojedyncze zdjęcia do pobierania
                        monitor = x
                        print('x = ', x)
                        print('x = ', type(x))
                        monitor1 = list(monitor)
                        print('monit = ', type(monitor1))
                        print('monit = :', monitor1)
                        monitor2 = list()
                        for itemA in x:
                            monitor2.append(itemA['src'])
                        print("gotowa lista:", monitor2)
                        ###
                        iterate = 1
                        print(" pierwszy element listy:", monitor2[1])
                        try:
                            imgURL = monitor2[0]
                            urllib.request.urlretrieve(imgURL, path + '/1/' + f'{item}' + ".jpg")
                        except:
                            pass
                        try:
                            imgURL = monitor2[1]
                            urllib.request.urlretrieve(imgURL, path + '/2/' + f'{item}' + ".jpg")
                        except:
                            pass
                        try:
                            imgURL = monitor2[2]
                            urllib.request.urlretrieve(imgURL, path + '/3/' + f'{item}' + ".jpg")
                        except:
                            pass
                        try:
                            imgURL = monitor2[3]
                            urllib.request.urlretrieve(imgURL, path + '/4/' + f'{item}' + ".jpg")
                        except:
                            pass
                        try:
                            imgURL = monitor2[4]
                            urllib.request.urlretrieve(imgURL, path + '/5/' + f'{item}' + ".jpg")
                        except:
                            pass
                        try:
                            imgURL = monitor2[5]
                            urllib.request.urlretrieve(imgURL, path + '/6/' + f'{item}' + ".jpg")
                        except:
                            pass
                        try:
                            imgURL = monitor2[6]
                            urllib.request.urlretrieve(imgURL, path + '/7/' + f'{item}' + ".jpg")
                        except:
                            pass
                        try:
                            imgURL = monitor2[7]
                            urllib.request.urlretrieve(imgURL, path + '/8/' + f'{item}' + ".jpg")
                        except:
                            pass



                                                #for pobieranie in monitor2:
                         #   imgURL = pobieranie
                          #  urllib.request.urlretrieve(imgURL, path + f'{iterate}' + pobieranie + ".jpg")
                           # iterate += 1



                        ####
                        with open(fr"{zmienna1}/360.csv",
                                  'a') as fi:  ## tutaj podac scieżke gdzie ma sie zapisać plik csv
                            writer = csv.writer(fi)  # , quoting=csv.QUOTE_NONE, quotechar='')
                            writer.writerow(czystaszesc)
                            print("dodało wiersz")
                    except:
                        pass
                else:
                    pass
            except:
                pass
            # https://support.microsoft.com/pl-pl/office/importowanie-lub-eksportowanie-plik%C3%B3w-tekstowych-txt-lub-csv-5250ac4c-663c-47ce-937b-339e391393ba
            browser.get(url3)
            browser.implicitly_wait(1)
    except:
        browser.refresh()


start_button = ttk.Button(frm, text="Start", command=is_good, state='disabled')
start_button.grid(column=0, row=7, columnspan=2)


def start_normal():
    start_button['state'] = "enable"




root.configure(bg='red')
root.mainloop()
