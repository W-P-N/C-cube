import random
from tkinter import *
import tkinter.ttk as tnt
import Quotes
from Lists_and_dict import *
from ttkthemes import themed_tk as theme
import tkinter.font as font


class UI2:
    def __init__(self):
        self.var = 0
        root = theme.ThemedTk()
        root.get_themes()
        root.set_theme("vista")
        root.title("Carbon Conscious Calci")
        root.geometry("1080x720")
        root.config(padx=20, pady=20)

        # Welcome Script
        welcome_label = Label(root,
                              text="WElCOME TO C\u00b3:\nA simple program to get EE and EC values of the construction materials.\n\n", justify=CENTER, font=("algerian", 20, "bold"), anchor="nw",
                              highlightthickness=0)
        welcome_label.grid(column=1, row=0, columnspan=3)

        # Select Construction Material Label
        select_construction_material_label = Label(root, text="Please select the material: ", justify=CENTER,
                                                   font=("georgia", 12, "bold"), highlightthickness=0, anchor="nw",
                                                   width=20)
        select_construction_material_label.grid(column=0, row=1)

        # Select Type Label
        select_type_material_label = Label(root, text="Please select the type: ", justify=CENTER,
                                           font=("Georgia", 12, "bold"), width=20, anchor="nw", highlightthickness=0)
        select_type_material_label.grid(column=0, row=2)

        # Embodied Carbon label
        self.embodied_carbon_label = Label(root, text="Embodied Carbon:  KgC/Kg", justify=CENTER,
                                           font=("Georgia", 15, "bold"), width=50, anchor="nw", highlightthickness=0)
        self.embodied_carbon_label.grid(row=4, column=1)

        # Embodied Energy label
        self.embodied_energy_label = Label(root, text="Embodied Energy:  MJ/Kg", justify=CENTER,
                                           font=("Georgia", 15, "bold"), width=50, anchor="nw")
        self.embodied_energy_label.grid(row=5, column=1)

        # Functions
        def material_to_type(e):
            if self.select_material.get() == "Brick":
                self.select_type.config(values=brick_list)
                self.select_type.current(0)

            elif self.select_material.get() == "Cement":
                self.select_type.config(values=cement_list)
                self.select_type.current(0)
            elif self.select_material.get() == "Concrete":
                self.select_type.config(values=concrete_list)
                self.select_type.current(0)
            elif self.select_material.get() == "Glass":
                self.select_type.config(values=glass_list)
                self.select_type.current(0)
            elif self.select_material.get() == "Steel":
                self.select_type.config(values=steel_list)
                self.select_type.current(0)
            elif self.select_material.get() == "Timber":
                self.select_type.config(values=timber_list)
                self.select_type.current(0)

        def type_to_energy():
            root.after(2000, quote_timer)
            if self.select_material.get() == "Brick":
                for i in brick_list:
                    if self.select_type.get() == i:
                        self.embodied_carbon_label.config(text=brick_type_dict[i]["embodied carbon"], justify=CENTER,
                                                          font=("Georgia", 15, "bold"), width=50)
                        self.embodied_energy_label.config(text=brick_type_dict[i]["embodied energy"], justify=CENTER,
                                                          font=("Georgia", 15, "bold"), width=50)
            elif self.select_material.get() == "Cement":
                for i in cement_list:
                    if self.select_type.get() == i:
                        self.embodied_carbon_label.config(text=cement_type_dict[i]["embodied carbon"], justify=CENTER,
                                                          font=("Georgia", 15, "bold"), width=50)
                        self.embodied_energy_label.config(text=cement_type_dict[i]["embodied energy"], justify=CENTER,
                                                          font=("Georgia", 15, "bold"), width=50)
            elif self.select_material.get() == "Concrete":
                for i in concrete_list:
                    if self.select_type.get() == i:
                        self.embodied_carbon_label.config(text=concrete_dict[i]["embodied carbon"], justify=CENTER,
                                                          font=("Georgia", 15, "bold"), width=50)
                        self.embodied_energy_label.config(text=concrete_dict[i]["embodied energy"], justify=CENTER,
                                                          font=("Georgia", 15, "bold"), width=50)
            elif self.select_material.get() == "Glass":
                for i in glass_list:
                    if self.select_type.get() == i:
                        self.embodied_carbon_label.config(text=glass_dict[i]["embodied carbon"], justify=CENTER,
                                                          font=("Georgia", 15, "bold"), width=50)
                        self.embodied_energy_label.config(text=glass_dict[i]["embodied energy"], justify=CENTER,
                                                          font=("Georgia", 15, "bold"), width=50)
            elif self.select_material.get() == "Steel":
                for i in steel_list:
                    if self.select_type.get() == i:
                        self.embodied_carbon_label.config(text=steel_dict[i]["embodied carbon"], justify=CENTER,
                                                          font=("Georgia", 15, "bold"), width=50)
                        self.embodied_energy_label.config(text=steel_dict[i]["embodied energy"], justify=CENTER,
                                                          font=("Georgia", 15, "bold"), width=50)
            elif self.select_material.get() == "Timber":
                for i in timber_list:
                    if self.select_type.get() == i:
                        self.embodied_carbon_label.config(text=timber_dict[i]["embodied carbon"], justify=CENTER,
                                                          font=("Georgia", 15, "bold"), width=50)
                        self.embodied_energy_label.config(text=timber_dict[i]["embodied energy"], justify=CENTER,
                                                          font=("Georgia", 15, "bold"), width=50)

        # Button
        # self.button_image = PhotoImage(file="Button.png")
        self.button_font = font.Font(family="Times New Roman", size=16, weight="bold")
        self.get_energy_button = Button(root, text="Get Energy Values", command=type_to_energy, font=self.button_font, compound=LEFT, )
        self.get_energy_button.grid(row=3, column=1)
        # DropDown Material type list
        self.select_material = tnt.Combobox(root, values=material_dict, width=50)
        self.select_material.current(0)
        self.select_material.grid(column=1, row=1)
        self.select_material.bind("<<ComboboxSelected>>", material_to_type)
        # DropDown type list
        self.select_type = tnt.Combobox(root, values=[" "], width=50)
        self.select_type.grid(column=1, row=2)
        # Canvas set up
        self.canvas = Canvas(width=400, height=600, bg="red")
        self.background_img = PhotoImage(file="quote.png")
        self.canvas.create_image(-800, -1700, image=self.background_img, anchor="nw")
        self.quote_text = self.canvas.create_text(100, 50, text=random.choice(Quotes.LIST), width=250,
                                                  font=("The Golden Leaves", 30, "bold"),
                                                  fill="lightgreen", anchor="nw")
        self.canvas.grid(row=2, column=2, rowspan=4)

        # Quote Function
        def quote_timer():
            self.canvas.delete(self.quote_text)
            self.quote_text = self.canvas.create_text(100, 10, text=random.choice(Quotes.LIST), width=250,
                                                  font=("The Golden Leaves", 30, "bold"),
                                                  fill="lightgreen", anchor="nw", )

        root.mainloop()
