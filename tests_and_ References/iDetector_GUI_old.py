from tkinter import Tk, Text, ttk, filedialog, messagebox, Menu, StringVar, Scrollbar, LEFT, RIGHT, Frame
from clarifai.rest import ClarifaiApp, Image as ClImage, Video as ClVid
from timeit import default_timer

#common settings...
file_img_name = " ";
file_vid_name = " ";
dir_init = "/home";
bgcolor = "blue";
x_cor = 10;
y_cor = 5;
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
        lbl_txt.set('   Connected');
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

        for i in range(len(pre['outputs'][0]['data']['concepts'])):
            text = "{}: Name: {} \n   Value: {} \n".format(i+1, pre['outputs'][0]['data']['concepts'][i]['name'],\
                                                         pre['outputs'][0]['data']['concepts'][i]['value']);
            pre_img_inf.insert("insert", text);
        pre_img_inf.config(state = 'disabled');
        print("Image Analysis Complete");
    except Exception as e:
        print(str(e));
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
root.geometry("697x550");
root.resizable(0,0);


#search about frames.........
'''frm_int = Frame(root);
frm_int.pack();
frm_fil_upl = Frame(root);
frm_fil_upl.pack();

frm_txt_box = Frame(root);
frm_txt_box.pack();

frm_anl = Frame(root);
frm_anl.pack();

frm_con = Frame(root);
frm_con.pack();'''


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
uni_lbl = ttk.Label(root, text = "iDetector", background = bgcolor, font = 'Lucinda').place(x = x_cor + 300, y = y_cor);
uni_lbl = ttk.Label(root, text = "Detect Information from Images and Videos", background = bgcolor, font = 'Lucinda').place(x = x_cor + 180, y = y_cor + 25);

uni_lbl = ttk.Label(root, text = 'Upload Image', background = bgcolor).place(x = x_cor + 50, y = y_cor + 65);

#Button to fetch image....
img_btn = ttk.Button(root, text = "Browse", command = lambda: img_bwr('img')).place(x = x_cor + 140, y = y_cor + 55);

#Text box to show image prediction info..
pre_img_inf = Text(root,width = 40,)
pre_img_inf.place(x = x_cor, y = y_cor + 85);

#Scrollbar for image details text box....
img_srl_bar = Scrollbar(root, command = pre_img_inf.yview);
img_srl_bar.pack(side = RIGHT, fill = 'y');
pre_img_inf.config(yscrollcommand = img_srl_bar.set);
pre_img_inf.config(state = 'disabled');

#Button for send request and analyze an image...
alz_img_btn = ttk.Button(root, text = 'Ananlyze', command = img_anl).place(x = x_cor + 90, y = y_cor + 445);


'''___________________Same_but_different_things_for_Video_Analysis..._______________________________________'''

#Universal Label...
uni_lbl = ttk.Label(root, text = 'Upload Video', background = bgcolor).place(x = x_cor + 440, y = y_cor + 65);

#Button to fetch image....
vid_btn = ttk.Button(root, text = "Browse", command = lambda: img_bwr('vid')).place(x = x_cor + 530, y = y_cor + 55);

#Text box to show image prediction info..
pre_vid_inf = Text(root,width = 40,)
pre_vid_inf.config(state = 'disabled');
pre_vid_inf.place(x = x_cor + 390, y = y_cor + 85);

#Button for send request and analyze an image...
alz_vid_btn = ttk.Button(root, text = 'Ananlyze', command = vid_anl).place(x = x_cor + 480, y = y_cor + 445);

##print(root.children);
##print(root._windowingsystem);

#Button to make connection through Clarifai API client....
clf_con_btn = ttk.Button(root, text = 'Connect to Clarifai', command = mak_con).place(x = x_cor + 280, y = y_cor + 485);

#Label to notify the connection status at startup using StringVar..(not possible otherwise..)....
lbl_txt = StringVar();
lbl_txt.set(' Not Connected');
uni_lbl = ttk.Label(root, textvariable = lbl_txt , background = bgcolor).place(x = x_cor + 290, y = y_cor + 520);

root.mainloop();
