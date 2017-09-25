from tkinter import Tk, Text, Button, Label, filedialog, messagebox, Menu, StringVar, Scrollbar, LEFT, RIGHT, Frame
from clarifai.rest import ClarifaiApp, Image as ClImage, Video as ClVid
from timeit import default_timer
from terminaltables import DoubleTable

#common settings...
fil_img_nam = " ";
fil_vid_nam = " ";
dir_int = "/home";
bgcolor = "blue";
model = ' ';
'''__________________________________________All_Functions_______________________________________...'''


#Image Information Function...
def img_inf(img):
##    try:
##        global fil_mg_nam
    pass;


#Settings Menu function....
def stg():
    print("In Settings Menu...");
    
#Help Menu Function.....
def hlp():
    print("In help Menu..");
    
#About Menu Function.....
def abt():
    print("In About menu");

#Making conection to Clarifai...
def mak_con():
    global model;
    #creating instance of ClarifaiApp() here because it is taking time to load thereby making the GUI to load very late..
    srt_tim = default_timer();
    try:
        app = ClarifaiApp()
        model = app.models.get('general-v1.3');
        clf_con_btn.config(bg = 'green');
        clf_con_txt.set('Connected');
        
        messagebox.showinfo('Connection Status', 'Connection Established.\nTime Taken : %2f sec.'%(default_timer() - srt_tim));

    except Exception as e:
        messagebox.showerror('Connection Status', str(e));
    

#Video Analysis.
def vid_anl():
    global fil_vid_nam;
    try:
        global model;
        vid_fil = ClVid(file_obj=open(fil_vid_nam, 'rb'))

        #clarifai returns dictionary by default....
        pre = model.predict([vid_fil]);

        #inserting data into the textbox from dictionary returned from clarifai...
        pre_vid_inf.config(state = 'normal');
        pre_vid_inf.delete("1.0", "end-1c");

        for i in range(len(pre['outputs'][0]['data']['frames'])):
            for j in range(len(pre['outputs'][0]['data']['frames'][i]['data']['concepts'])):
                text = "{}: Name: {} \n   Value: {} \n".format(j+1, pre['outputs'][0]['data']['frames'][i]['data']['concepts'][j]['name'],\
                                                             pre['outputs'][0]['data']['frames'][i]['data']['concepts'][j]['value']);
                pre_vid_inf.insert("insert", text);
        print(i, j);
        ##pre_vid_inf.insert('insert', pre['outputs'][0]['data']['frames'][0]['data']['concepts'][0]);
        pre_vid_inf.config(state = 'disabled');
        print("Video Analysis Complete");

    except Exception as e:
        print(str(e));
        if str(e) == "'str' object has no attribute 'predict'":
            messagebox.showerror('I/O Error', 'Please Connect to Clarifai');
        else:
            messagebox.showerror('I/O Error', str(e));


#Image Analysis....
def img_anl():
    global fil_img_nam;
    try:
        global model;
        img_fil = ClImage(file_obj=open(fil_img_nam, 'rb'))

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
    global fil_img_nam;
    global fil_vid_nam;
    global dir_int;

    #Distinguishing FileDailog for image and Videofiles...
    if file_type is 'img':
        file = filedialog.askopenfile(initialdir = dir_int, title = 'Select Files...',filetypes = (("jpeg files","*.jpg"), ("all files","*.*")));
        print("File Opened is : {}".format(file));
        fil_img_nam = str(file);
        
        #extracting filename from askopenfile object...
        fil_img_nam = fil_img_nam[fil_img_nam.find('name') + 6 : fil_img_nam.find('mode') - 2];
        print('fil_img_nam = ',fil_img_nam);
        #preserving browsed directory...
        for i in range(len(fil_img_nam)-1, 0, -1):
            if fil_img_nam[i] == '/':
                print(i);
                dir_int = fil_img_nam[:i];
                break;
        
    else:
        file = filedialog.askopenfile(initialdir = dir_int, title = 'Select Files...',filetypes = (("Mp4 files","*.mp4"), ("all files","*.*")));
        print("File Opened is : {}".format(file));
        fil_vid_nam = str(file);
        fil_vid_nam = fil_vid_nam[fil_vid_nam.find('name') + 6 : fil_vid_nam.find('mode') - 2];

        print('fil_vid_nam = ',fil_vid_nam);
        for i in range(len(fil_vid_nam)-1, 0, -1):
            if fil_vid_nam[i] == '/':
                dir_int = fil_vid_nam[:i];
                break;
        
'''__________________________Root_window...________________________________________'''    

#root..and its initial settings....
root = Tk();
root.title('iDetector');
root.config(background = bgcolor);
#root.geometry("897x650");
##root.resizable(0,0);



#frames.........
frm_int = Frame(root, background = bgcolor);
frm_int.grid(row = 0, columnspan = 6, sticky = 'ew');


frm_img_txt_box = Frame(root, background = bgcolor);
frm_img_txt_box.grid(row = 2, column = 0, sticky = 'nsew');
frm_img_txt_box.isgridded = True;

frm_vid_txt_box = Frame(root, background = bgcolor);
frm_vid_txt_box.grid(row = 2, column = 1, sticky = 'nsew');
frm_vid_txt_box.isgridded = True;


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
uni_lbl = Label(frm_int, text = "iDetector", background = bgcolor, font = 'Lucinda').grid(row = 1, column = 2, sticky = 'ew');
uni_lbl = Label(frm_int, text = "Detect Information from Images and Videos", background = bgcolor, font = 'Lucinda').grid(row = 2, column = 2, sticky = 'ew');

frm_int.grid_rowconfigure(0, weight = 1);
frm_int.grid_columnconfigure(0, weight = 1);
frm_int.grid_rowconfigure(4, weight = 2);
frm_int.grid_columnconfigure(4, weight = 1);

#uni_lbl = Label(root, text = 'Upload Image', background = bgcolor).place(x = x_cor + 50, y = y_cor + 65);
uni_lbl = Label(frm_int, background = bgcolor, font = 'Lucinda').grid(row = 3, column = 3, sticky = 'ew');

#Button to fetch image....
img_btn = Button(frm_img_txt_box, text = "Browse Image",  command = lambda: img_bwr('img'), bg = 'violet', ).grid(row = 0, column = 0, sticky = 'ew');

#Button to fetch video....
vid_btn = Button(frm_vid_txt_box, text = "Browse Video", command = lambda: img_bwr('vid'), bg = 'violet').grid(row = 0, column = 0, sticky = 'ew');

#Text box to show image prediction info..
pre_img_inf = Text(frm_img_txt_box,)
pre_img_inf.grid(row = 1, column = 0, sticky = 'nsew');


#Scrollbar for image details text box....
img_srl_bar = Scrollbar(frm_img_txt_box, command = pre_img_inf.yview);
img_srl_bar.grid(row = 1, column = 2, sticky = 'nsew');
pre_img_inf.config(yscrollcommand = img_srl_bar.set);
pre_img_inf.config(state = 'disabled');

#Empty Lable to seprate two Text boxes..
uni_lbl = Label(frm_img_txt_box, width = 10, background = bgcolor, font = 'Lucinda').grid(row = 0, column = 3, sticky = 'ns');

#Text box to show image prediction info..
pre_vid_inf = Text(frm_vid_txt_box,)
pre_vid_inf.config(state = 'disabled');
pre_vid_inf.grid(row = 1, column = 0, sticky = 'ew');


#Scrollbar for video details text box....
vid_srl_bar = Scrollbar(frm_vid_txt_box, command = pre_vid_inf.yview);
vid_srl_bar.grid(row = 1, column = 2, sticky = 'nsew');
pre_vid_inf.config(yscrollcommand = vid_srl_bar.set);
pre_vid_inf.config(state = 'disabled');

'''______________________________Buttons_for_Image_and_Video_Analysis___________________________________________________'''
#Button for send request and analyze an image...
alz_img_btn = Button(frm_img_txt_box, text = 'Ananlyze Image', command = img_anl, bg = 'light green').grid(row = 2, column = 0, sticky = 'ew');

#Button for send request and analyze an image...
alz_vid_btn = Button(frm_vid_txt_box, text = 'Ananlyze Video', command = vid_anl, bg = 'light green').grid(row = 2, sticky = 'ew');

'''_____________________________Info._Buttons_image_and_video____________________________________'''
#Button for showing image information.......
shw_img_inf = Button(frm_img_txt_box, text = 'Show Image with Analysis', bg = 'yellow').grid(row = 3, column = 0, sticky = 'ew');

#Button for showing video information.......
shw_vid_inf = Button(frm_vid_txt_box, text = 'Show Frames with Aanalysis', bg = 'yellow').grid(row = 3, column = 0, sticky = 'ew');

##print(root.children);
##print(root._windowingsystem);

#Empty Labels to create gaps between connection button and text_box...
for i in range(2):
    uni_lbl = Label(frm_con, background = bgcolor, ).grid(row = i, column = 0, sticky = 'ew');

#Button to make connection through Clarifai API client....;
clf_con_txt = StringVar()
clf_con_txt.set('Connect To Clarifai');
clf_con_btn = Button(frm_con, textvariable = clf_con_txt, command = mak_con, bg = 'red')
clf_con_btn.grid(row = 4, column = 1, sticky = 'nsew');
frm_con.grid_rowconfigure(0, weight = 1);
frm_con.grid_columnconfigure(0, weight = 1);
frm_con.grid_rowconfigure(10, weight = 1);
frm_con.grid_columnconfigure(10, weight = 1);

root.mainloop();
