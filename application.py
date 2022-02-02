from tkinter import *
from tkinter import ttk
from tkinter import filedialog, messagebox
from scrapy import spiderloader
from scrapy.crawler import CrawlerRunner
from scrapy.utils.log import configure_logging
from scrapy.utils.project import get_project_settings
from twisted.internet import reactor
import threading
import time
import os


def main():
    absolute_path = os.path.abspath(".")
    print("Full path from Application: " + absolute_path)
    settings = get_project_settings()
    FEED_TYPES = ["CSV", "JSON", "XML"]

    FEED_TYPE_DICT = {
        "CSV": "csv",
        "JSON": "json",
        "XML": "xml"
    }

    ######################### Window #########################

    APP_TITLE = f"{settings['BOT_NAME'].replace('_', ' ').title()} Scraper"
    GEOMETRY_WIDTH = 480
    GEOMETRY_HEIGHT = int(GEOMETRY_WIDTH*0.55)
    PADDING = GEOMETRY_WIDTH*0.02

    window = Tk()


    ######################### Helper Functions #########################

    def get_spiders():
        """Loads Scraper Spiders From Project Settings

        Returns:
            list: List of all Spiders found in project.
        """
        spider_loader = spiderloader.SpiderLoader.from_settings(settings)
        spiders_list = [spider for spider in spider_loader.list()]
        return spiders_list

    # def get_chosen_spider(value):
    #     """Gets chosen spider from user input.

    #     Args:
    #         value (str): Chosen spider name.

    #     Returns:
    #         str: Chosen spider name.
    #     """
    #     global chosen_spider
    #     chosen_spider = value
    #     return chosen_spider

    # def get_chosen_feed(value):
    #     """Gets chosen feed type from user input.

    #     Args:
    #         value (str): Chosen feed type.

    #     Returns:
    #         str: Chosen feed type.
    #     """
    #     global chosen_feed
    #     chosen_feed = value
    #     return chosen_feed

    def browse_btn():
        """Gets file path from user input.

        Args:
            value (str): File path.

        Returns:
            str: File path.
        """
        global folder_path
        folder_path = filedialog.askdirectory()
        ent_local_file_path.delete(0, END)
        ent_local_file_path.insert(0, folder_path)
        return folder_path

    def on_focus_in(entry):
        if entry.cget('state') == 'disabled':
            entry.configure(state='normal')
            entry.delete(0, 'end')

    def on_focus_out(entry, placeholder):
        if entry.get() == "":
            entry.insert(0, placeholder)
            entry.configure(state='disabled')

    def execute_spider():
        """Executes Scrapy Spider and saves results at user file path.
        """
        FEEDS = {}
        chosen_spider = choose_spider_text.get()
        chosen_feed = choose_feed_text.get()
        file_path = ent_local_file_path.get()
        file_name = ent_file_name.get()
        include_datetime = include_datetime_checked.get()

        if file_path == "" or file_name == "" or chosen_feed not in FEED_TYPES:
            messagebox.showerror("Error", "Please be sure to complete all fields.")
            return

        t = time.localtime()
        timestamp = time.strftime('%b-%d-%Y_%H_%M', t)

        try:
            if include_datetime == 1:
                feed_uri = f"file:///{folder_path}/{file_name}_{timestamp}.{FEED_TYPE_DICT[chosen_feed]}"
            elif include_datetime == 0:
                feed_uri = f"file:///{folder_path}/{file_name}.{FEED_TYPE_DICT[chosen_feed]}"

            if FEED_TYPE_DICT[chosen_feed] == "json":
                FEEDS[feed_uri] = {
                    "format": FEED_TYPE_DICT[chosen_feed],
                    "encoding": "utf8",
                    "store_empty": False,
                    "fields": None,
                    "indent": 4,
                    "item_export_kwargs": {
                    "export_empty_fields": True,
                    }
                }
            elif FEED_TYPE_DICT[chosen_feed] == "xml":
                FEEDS[feed_uri] = {
                    "format": FEED_TYPE_DICT[chosen_feed],
                    'encoding': 'latin1',
                    'indent': 8,
                }
            elif FEED_TYPE_DICT[chosen_feed] == "csv":
                FEEDS[feed_uri] = {
                    "format": FEED_TYPE_DICT[chosen_feed],
                    'encoding': 'utf8'
                }
            else:
                raise
        except:
            messagebox.showerror("Error", "Please be sure to complete all fields.")
            


        settings.set("FEEDS", FEEDS)
        configure_logging()

        runner = CrawlerRunner(settings)
        d = runner.crawl(chosen_spider)
        d.addBoth(lambda _: reactor.stop())
        d.addBoth(lambda _: stop_progress())
        reactor.run(installSignalHandlers=False)
        


    def start_execute_thread(event):
        """Helper function to create separate thread for application to run spider program in the background.
        """
        start_progress()
        global execute_thread
        execute_thread = threading.Thread(target=execute_spider, daemon=True)
        execute_thread.start()
        window.after(10, check_execute_thread)


    def check_execute_thread():
        """Helper function to check thread health for application to run spider program in the background.
        """
        if execute_thread.is_alive():
            window.after(100, check_execute_thread)
        else:
            stop_progress()


    def start_progress():
        lbl_progress.config(text="Running!")
        progress_bar.start(10)
        btn_execute.config(state=DISABLED)
        btn_browse.config(state=DISABLED)
        ent_local_file_path.config(state=DISABLED)
        ent_file_name.config(state=DISABLED)

    def stop_progress():
        window.destroy()
        # progress_bar.stop()
        # progress_bar["value"] = 100
        # lbl_progress.config(text="Complete!")
        # btn_execute.config(state=NORMAL)
        # btn_browse.config(state=NORMAL)
        # ent_local_file_path.config(state=NORMAL)
        # ent_file_name.config(state=NORMAL)


    ######################### Choose Spider #########################

    lbl_choose_spider = Label(master=window, text="Choose a Spider", padx=PADDING, pady=PADDING)
    lbl_choose_spider.place(x=GEOMETRY_WIDTH*0.02, y=GEOMETRY_WIDTH*0.02)

    choose_spider_text = StringVar(master=window)
    choose_spider_text.set("Select Spider".center(10))
    spiders = get_spiders()
    # spiders = ["houses"]
    opt_select_spider = OptionMenu(window, choose_spider_text, *spiders)
    opt_select_spider.place(x=GEOMETRY_WIDTH*0.41, y=GEOMETRY_WIDTH*0.04, width=130)


    ######################### Feed Type #########################

    lbl_choose_feed = Label(master=window, text="Choose Export Type", padx=PADDING, pady=PADDING)
    lbl_choose_feed.place(x=GEOMETRY_WIDTH*0.02, y=GEOMETRY_WIDTH*0.10)

    choose_feed_text = StringVar(master=window)
    choose_feed_text.set("Select Option".center(10))
    feed_types = FEED_TYPES

    # opt_select_feed = OptionMenu(window, choose_feed_text, *feed_types, command=lambda value: get_chosen_feed(value))
    opt_select_feed = OptionMenu(window, choose_feed_text, *feed_types)
    opt_select_feed.place(x=GEOMETRY_WIDTH*0.41, y=GEOMETRY_WIDTH*0.12, width=130)


    ######################### Local Path Entry #########################

    lbl_local_file_path = Label(master=window, text="Local File Path", padx=PADDING, pady=PADDING)
    lbl_local_file_path.place(x=GEOMETRY_WIDTH*0.02, y=GEOMETRY_WIDTH*0.18)

    local_file_path_text = StringVar(window)
    ent_local_file_path = Entry(window, textvariable=local_file_path_text)
    ent_local_file_path.place(x=GEOMETRY_WIDTH*0.3, y=GEOMETRY_WIDTH*0.20)
    # ent_local_file_path.insert(0, "File_Path".center(40))
    # ent_local_file_path.configure(state='disabled')

    # ent_file_name_focus_in = ent_local_file_path.bind('<Button-1>', lambda x: on_focus_in(ent_local_file_path))
    # ent_file_name_focus_out = ent_local_file_path.bind('<FocusOut>', lambda x: on_focus_out(ent_local_file_path, "File_Path".center(40)))

    btn_browse = Button(window, text="Browse", command=browse_btn)
    btn_browse.place(x=GEOMETRY_WIDTH*0.77, y=GEOMETRY_WIDTH*0.20)


    ######################### Local File Name #########################

    lbl_local_file_name = Label(master=window, text="Local File Name", padx=PADDING, pady=PADDING)
    lbl_local_file_name.place(x=GEOMETRY_WIDTH*0.02, y=GEOMETRY_WIDTH*0.26)

    local_file_name_text = StringVar(window)
    ent_file_name = Entry(window, textvariable=local_file_name_text)
    ent_file_name.place(x=GEOMETRY_WIDTH*0.3, y=GEOMETRY_WIDTH*0.28)
    ent_file_name.insert(0, "Output_File".center(40))
    ent_file_name.configure(state='disabled')

    ent_file_name_focus_in = ent_file_name.bind('<Button-1>', lambda x: on_focus_in(ent_file_name))
    ent_file_name_focus_out = ent_file_name.bind('<FocusOut>', lambda x: on_focus_out(ent_file_name, "Output_File".center(40)))

    include_datetime_checked = IntVar()
    include_datetime = Checkbutton(window, text='Add Timestamp?',variable=include_datetime_checked, onvalue=1, offvalue=0)
    include_datetime.place(x=GEOMETRY_WIDTH*0.71, y=GEOMETRY_WIDTH*0.285)
    include_datetime.select()


    ######################### Execute Button #########################

    btn_execute = Button(window, text="RUN", padx=PADDING*2, pady=PADDING*0.4, command=lambda: start_execute_thread(None))
    btn_execute.place(x=GEOMETRY_WIDTH*0.4, y=GEOMETRY_WIDTH*0.37)


    ######################### Progress Bar #########################

    progress_bar=ttk.Progressbar(window,orient=HORIZONTAL,length=250,mode='determinate')
    progress_bar.place(x=GEOMETRY_WIDTH*0.23, y=GEOMETRY_WIDTH*0.45)

    lbl_progress = Label(master=window, text="*Window will close upon crawl completion*", font=("Ariel 10"))
    lbl_progress.place(x=GEOMETRY_WIDTH*0.28, y=GEOMETRY_WIDTH*0.48)



    ######################### App Geometry #########################

    window.title(APP_TITLE)
    window.geometry(f"{GEOMETRY_WIDTH}x{GEOMETRY_HEIGHT}")
    window.resizable(False, False)
    window.mainloop()


if __name__=='__main__':
    main()