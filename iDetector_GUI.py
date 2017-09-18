from tkinter import Tk, Text, ttk, filedialog, messagebox, Menu, StringVar, Scrollbar, LEFT, RIGHT, Frame
from clarifai.rest import ClarifaiApp, Image as ClImage, Video as ClVid
from timeit import default_timer
from terminaltables import DoubleTable

#common settings...
file_img_name = " ";
file_vid_name = " ";
dir_init = "/home";
bgcolor = "blue";
model = ' ';
'''__________________________________________All_Functions_______________________________________...'''

#Settings Menu function....
def stg():
    print("In Settings Menu...");

#Help Function menu..
def hlp():
    print("In help Menu..");

def abt():
    print("In About menu");

def mak_con():
    global model;
    #creating instance of ClarifaiApp() here because it is taking time to load thereby making the GUI to load very late..
    srt_tim = default_timer();
    try:
        app = ClarifaiApp()
        model = app.models.get('general-v1.3');
        clf_con_txt.set('Connected');
        messagebox.showinfo('Connection Status', 'Connection Established.\nTime Taken : %2f sec.'%(default_timer() - srt_tim));

    except Exception as e:
        messagebox.showerror('Connection Status', str(e));
    

def vid_anl():
    global file_vid_name;
    try:
        global model;
        vid_fil = ClVid(file_obj=open(file_vid_name, 'rb'))

        #clarifai returns dictionary by default....
        pre = model.predict([vid_fil]);

        #inserting data into the textbox from dictionary returned from clarifai...
        pre_vid_inf.config(state = 'normal');
        pre_vid_inf.delete("1.0", "end-1c");
        tab = [['Frame_no.','Sr.No.', 'Category', 'Prediction Value']];
        for i in range(len(pre['outputs'][0]['data']['frames'])):
            tab.append([i + 1]);
            for j in range(len(pre['outputs'][0]['data']['frames'][i]['data']['concepts'])):
                tab.append([' ', j+1, pre['outputs'][0]['data']['frames'][i]['data']['concepts'][j]['name'], pre['outputs'][0]['data']['frames'][i]['data']['concepts'][j]['value']]);

        pre_vid_inf.insert("insert", DoubleTable(tab).table);
        print(DoubleTable(tab).table);
        
        pre_vid_inf.config(state = 'disabled');
        print("Video Analysis Complete");

    except Exception as e:
        print(str(e));
        messagebox.showerror('I/O Error', str(e));

def img_anl():
    global file_img_name;
    try:
        global model;
        img_fil = ClImage(file_obj=open(file_img_name, 'rb'))

        #clarifai returns dictionary by default....
        pre = model.predict([img_fil]);
        
        #inserting data into the textbox...
        pre_img_inf.config(state = 'normal');
        pre_img_inf.delete("1.0", "end-1c");
        tab = [['Sr.No.', 'Category', 'Prediction Value']];

        for i in range(len(pre['outputs'][0]['data']['concepts'])):
            tab.append([i+1, pre['outputs'][0]['data']['concepts'][i]['name'] ,pre['outputs'][0]['data']['concepts'][i]['value']]);
        
        tbl = DoubleTable(tab);
        print(tbl.table);
        
        pre_img_inf.insert("insert", tbl.table);
        pre_img_inf.config(state = 'disabled');

        print("Image Analysis Complete");
    except Exception as e:
        print(str(e));
        if str(e) == "'str' object has no attribute 'predict'":
            messagebox.showerror('I/O Error', 'Please Connect to Clarifai');
        else:
            messagebox.showerror('I/O Error', str(e));
        
    
#function to open an image through file_dialog Box..
def img_bwr(file_type):
    global file_img_name;
    global file_vid_name;
    global dir_init;

    #Distinguishing FileDailog for image and Videofiles...
    if file_type is 'img':
        file = filedialog.askopenfile(initialdir = dir_init, title = 'Select Files...',filetypes = (("jpeg files","*.jpg"), ("all files","*.*")));
        print("File Opened is : {}".format(file));
        file_img_name = str(file);
        
        #extracting filename from askopenfile object...
        file_img_name = file_img_name[file_img_name.find('name') + 6 : file_img_name.find('mode') - 2];
        print('File_img_name = ',file_img_name);
        
        #preserving browsed directory...
        for i in range(len(file_img_name)-1, 0, -1):
            if file_img_name[i] == '/':
                print(i);
                dir_init = file_img_name[:i];
                break;
        
    else:
        file = filedialog.askopenfile(initialdir = dir_init, title = 'Select Files...',filetypes = (("Mp4 files","*.mp4"), ("all files","*.*")));
        print("File Opened is : {}".format(file));
        file_vid_name = str(file);
        file_vid_name = file_vid_name[file_vid_name.find('name') + 6 : file_vid_name.find('mode') - 2];

        print('File_vid_name = ',file_vid_name);
        for i in range(len(file_vid_name)-1, 0, -1):
            if file_vid_name[i] == '/':
                dir_init = file_vid_name[:i];
                break;
        
'''__________________________Root_window...________________________________________'''    

#root..and its initial settings....
root = Tk();
root.title('iDetector');
root.config(background = bgcolor);

#search about frames.........
frm_int = Frame(root, background = bgcolor);
frm_int.grid(row = 0, columnspan = 6, sticky = 'ew');

frm_img_txt_box = Frame(root, background = bgcolor);
frm_img_txt_box.grid(row = 2, column = 0, sticky = 'nsew');

frm_vid_txt_box = Frame(root, background = bgcolor);
frm_vid_txt_box.grid(row = 2, column = 1, sticky = 'nsew');

frm_con = Frame(root, background = bgcolor);
frm_con.grid(row = 4, columnspan = 4, sticky = 'ew');


'''_________________________________________________MenuBar_______________________'''
#Menubar instance...
mnu_bar = Menu(root);

#Settings_Menu:
set_mnu = Menu(mnu_bar, tearoff = 1);
set_mnu.add_command(label = "Command_1.1", command = stg);
mnu_bar.add_cascade(label = "Settings", menu = set_mnu);

#Help_Menu:
hlp_mnu = Menu(mnu_bar, tearoff = 1);
hlp_mnu.add_command(label = 'command_2.1', command = hlp);
mnu_bar.add_cascade(label = 'Help', menu = hlp_mnu);

#About_Menu:
abt_mnu = Menu(mnu_bar, tearoff = 1);
abt_mnu.add_command(label = 'command_3.1', command = abt);
mnu_bar.add_cascade(label = 'About', menu = abt_mnu);

#Packing menubar on root..
root.config(menu = mnu_bar);

'''_________________________________________________Other_Widgets_used..._________________'''

'''______________________________for_image_analysis______________'''
#Universal Label...
uni_lbl = ttk.Label(frm_int, text = "                       iDetector", background = bgcolor, font = 'Lucinda').grid(row = 1, column = 2, sticky = 'ew');
uni_lbl = ttk.Label(frm_int, text = "Detect Information from Images and Videos", background = bgcolor, font = 'Lucinda').grid(row = 2, column = 2, sticky = 'ew');

frm_int.grid_rowconfigure(0, weight = 1);
frm_int.grid_columnconfigure(0, weight = 1);
frm_int.grid_rowconfigure(4, weight = 2);
frm_int.grid_columnconfigure(4, weight = 1);

uni_lbl = ttk.Label(frm_int, background = bgcolor, font = 'Lucinda').grid(row = 3, column = 3, sticky = 'ew');

#Button to fetch image....
img_btn = ttk.Button(frm_img_txt_box, text = "Browse", command = lambda: img_bwr('img')).grid(row = 0, column = 0, sticky = 'ew');

#Button to fetch video....
vid_btn = ttk.Button(frm_vid_txt_box, text = "Browse", command = lambda: img_bwr('vid')).grid(row = 0, column = 0, sticky = 'ew');

#Text box to show image prediction info..
pre_img_inf = Text(frm_img_txt_box,)
pre_img_inf.grid(row = 1, column = 0, sticky = 'nsew');


#Scrollbar for image details text box....
img_srl_bar = Scrollbar(frm_img_txt_box, command = pre_img_inf.yview);
img_srl_bar.grid(row = 1, column = 2, sticky = 'nsew');
pre_img_inf.config(yscrollcommand = img_srl_bar.set);
pre_img_inf.config(state = 'disabled');

#Empty Lable to seprate two Text boxes..
uni_lbl = ttk.Label(frm_img_txt_box, width = 10, background = bgcolor, font = 'Lucinda').grid(row = 0, column = 3, sticky = 'ns');

#Text box to show video prediction info..
pre_vid_inf = Text(frm_vid_txt_box,)
pre_vid_inf.config(state = 'disabled');
pre_vid_inf.grid(row = 1, column = 0, sticky = 'ew');

#Scrollbar for video details text box....
vid_srl_bar = Scrollbar(frm_vid_txt_box, command = pre_vid_inf.yview);
vid_srl_bar.grid(row = 1, column = 2, sticky = 'nsew');
pre_vid_inf.config(yscrollcommand = vid_srl_bar.set);
pre_vid_inf.config(state = 'disabled');

#Button for send request and analyze an image...
alz_img_btn = ttk.Button(frm_img_txt_box, text = 'Ananlyze', command = img_anl).grid(row = 2, column = 0, sticky = 'ew');

#Button for send request and analyze an image...
alz_vid_btn = ttk.Button(frm_vid_txt_box, text = 'Ananlyze', command = vid_anl).grid(row = 2, sticky = 'ew');

#Empty Lable to seprate rows..
uni_lbl = ttk.Label(frm_con, background = bgcolor, font = 'Lucinda').grid(row = 0, column = 0, sticky = 'ew');

#Button to make connection through Clarifai API client....;
clf_con_txt = StringVar()
clf_con_txt.set('Connect To Clarifai');
clf_con_btn = ttk.Button(frm_con, textvariable = clf_con_txt, command = mak_con).grid(row = 1, column = 1, sticky = 'nsew');
frm_con.grid_rowconfigure(0, weight = 1);
frm_con.grid_columnconfigure(0, weight = 1);
frm_con.grid_rowconfigure(2, weight = 1);
frm_con.grid_columnconfigure(2, weight = 1);

root.mainloop();
