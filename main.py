
from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
from connection_handler import ConnectionHandler
from PIL import ImageTk, Image
from utils import generate_random_password
import os


supermarket_app = Tk()
supermarket_app.title("Supermarket Billing System")
supermarket_app.geometry("1920x1080")

class AdminPage:
  #img_url = "./assets/add_img.png"
  const_url = "add_img.png"
  img_url = os.path.realpath(os.path.join(os.curdir, 'assets', const_url))
  add_img = ImageTk.PhotoImage(Image.open(img_url).resize((300, 100)))
  images = []

  try:
    conn = ConnectionHandler()
    resp = conn.get_products()
    images = [
      ImageTk.PhotoImage(Image.open(x[3]).resize((200, 150))) 
      for x in resp["message"]
    ]
  except:
    pass

  def __init__(self, app):
    self.app = app

  def set_image_url(self, url):
    self.img_url = url
    add_img_label.place_forget()
    self.add_img = ImageTk.PhotoImage(Image.open(url).resize((200, 100)))
    add_img_btn["image"] = self.add_img
    add_img_btn.place_configure(anchor="c", relx=0.5, rely=0.25)
    img_display_label.place(anchor="c", relx=0.5, rely=0.33)

  def get_file(self):
    filename = filedialog.askopenfilename()
    self.set_image_url(filename)

  def return_image(self, url):
    return ImageTk.PhotoImage(Image.open(url).resize((300, 100)))

  def add_products(self):
    global add_img_btn, add_img_label, img_display_label
    add_products_page = Frame(
      self.app,     
      width="1920", 
      height="1080",
    )
    back_button = Button(
      add_products_page,
      text="< Back",
      width="15",
      command=lambda: (add_products_page.place_forget(), self.homepage())
    )
    back_button.place(anchor="c", relx=0.3, rely=0.15)

    top_label = Label(
      add_products_page, 
      text="ADD PRODUCT DETAILS", 
      fg="blue",
      font="Times 20 bold"
    )
    top_label.place(anchor="c", relx=0.5, rely=0.15)
    add_img_label = Label (
      add_products_page,
      image=self.add_img
    )
    add_img_label.place(anchor="c", relx=0.5, rely=0.25)
    add_img_btn = Button(
      add_products_page,
      text="Select Image",
      command=self.get_file
    )
    add_img_btn.place(anchor="c", relx=0.5, rely=0.35)
    img_display_label = Label(
      add_products_page,
      text="Click on image to change"
    )

    product_name_label = Label(
      add_products_page,
      text="Product name"
    )
    product_name_label.place(anchor="c", relx=0.5, rely=0.4)
    product_name_var = StringVar()
    product_name_entry = Entry(
      add_products_page,
      textvariable=product_name_var
    )
    product_name_entry.place(anchor="c", relx=0.5, rely=0.45)

    product_quantity_label = Label(
      add_products_page,
      text="Product quantity"
    )
    product_quantity_label.place(anchor="c", relx=0.5, rely=0.5)
    product_quantity_var = IntVar()
    product_quantity_entry = Entry(
      add_products_page,
      textvariable=product_quantity_var
    )
    product_quantity_entry.place(anchor="c", relx=0.5, rely=0.55)

    product_price_label = Label(
      add_products_page,
      text="Product price"
    )
    product_price_label.place(anchor="c", relx=0.5, rely=0.6)
    product_price_var = DoubleVar()
    product_price_entry = Entry(
      add_products_page,
      textvariable=product_price_var
    )
    product_price_entry.place(anchor="c", relx=0.5, rely=0.65)

    def save_product():
      product = (
        product_name_var.get(), 
        product_price_var.get(),
        self.img_url,
        product_quantity_var.get()
      )
      
      connection = ConnectionHandler()
      resp = connection.save_new_product(product)
      if resp["status"] == "Success":
        messagebox.showinfo("Status", "Product added successfully")
        yes_no = messagebox.askyesnocancel(
          "Add product", 
          "Do you want to add another item?"
        )

        if (yes_no):
          product_name_var.set("")
          product_price_var.set(0.0)
          product_quantity_var.set(0)
          self.add_img = ImageTk.PhotoImage(Image.open(self.const_url).resize((200, 100)))
          add_img_btn["image"] = self.add_img

      else:
        messagebox.showerror("Error", "An Error Occurred")

    save_product_btn = Button(
      add_products_page,
      text="Save Product",
      command=save_product
    )
    save_product_btn.place(anchor="c", relx=0.5, rely=0.7)
    add_products_page.place(anchor="c", relx=0.5, rely=0.5)

  def add_users(self):
    add_users_page = Frame(
      self.app,     
      width="1920", 
      height="1080",
    )
    back_button = Button(
      add_users_page,
      text="< Back",
      width="15",
      command=lambda: (add_users_page.place_forget(), self.users())
    )
    back_button.place(anchor="c", relx=0.3, rely=0.15)

    top_label = Label(
      add_users_page, 
      text="ADD NEW USER", 
      fg="blue",
      font="Times 20 bold"
    )
    top_label.place(anchor="c", relx=0.5, rely=0.15)

    username_label = Label(
      add_users_page,
      text="Username",
      font="Times 15 bold"
    )
    username_label.place(anchor="c", relx=0.5, rely=0.25)
    username_var = StringVar()
    username_entry = Entry(
      add_users_page,
      textvariable=username_var
    )
    username_entry.place(anchor="c", relx=0.5, rely=0.3)

    password_label = Label(
      add_users_page,
      text="Password",
      font="Times 15 bold"
    )
    password_label.place(anchor="c", relx=0.5, rely=0.4)
    password_var = StringVar()
    password_entry = Entry(
      add_users_page,
      textvariable=password_var
    )
    password_entry.place(anchor="c", relx=0.5, rely=0.45)

    message_label = Label(
      add_users_page,
      text="Dont have a password in mind? "
    )
    message_label.place(anchor="c", relx=0.43, rely=0.5)

    def insert_password():
      password = generate_random_password()
      password_var.set(password)

    generate_password_btn = Button(
      add_users_page,
      text="Generate Random Password",
      command=insert_password
    )
    generate_password_btn.place(anchor="c", relx=0.55, rely=0.5)

    def save_user():
      user = (
        username_var.get(), 
        password_var.get()
      )

      conn = ConnectionHandler()
      resp = conn.save_new_user(user)
      
      if resp["status"] == "Success":
        messagebox.showinfo("Status", "User added successfully")
        username_var.set("")
        password_var.set("")
      else:
        messagebox.showerror("Status", "An error occurred")  

    save_user_btn = Button(
      add_users_page,
      text="Save User",
      command=save_user
    )
    save_user_btn.place(anchor="c", relx=0.5, rely=0.6)
    add_users_page.place(anchor="c", relx=0.5, rely=0.5)

  def update_user(self, username, user_id):

    update_users_page = Frame(
      self.app,     
      width="1920", 
      height="1080",
    )
    back_button = Button(
      update_users_page,
      text="< Back",
      width="15",
      command=lambda: (update_users_page.place_forget(), self.users())
    )
    back_button.place(anchor="c", relx=0.3, rely=0.15)

    top_label = Label(
      update_users_page, 
      text="UPDATE USER " + username, 
      fg="blue",
      font="Times 20 bold"
    )
    top_label.place(anchor="c", relx=0.5, rely=0.15)

    username_label = Label(
      update_users_page,
      text="Username",
      font="Times 15 bold"
    )
    username_label.place(anchor="c", relx=0.5, rely=0.25)
    username_var = StringVar()
    username_var.set(username)
    username_entry = Entry(
      update_users_page,
      textvariable=username_var
    )
    username_entry.place(anchor="c", relx=0.5, rely=0.3)

    password_label = Label(
      update_users_page,
      text="Password",
      font="Times 15 bold"
    )
    password_label.place(anchor="c", relx=0.5, rely=0.4)
    password_var = StringVar()
    password_entry = Entry(
      update_users_page,
      textvariable=password_var
    )
    password_entry.place(anchor="c", relx=0.5, rely=0.45)

    message_label = Label(
      update_users_page,
      text="Dont have a password in mind? "
    )
    message_label.place(anchor="c", relx=0.43, rely=0.5)

    def insert_password():
      password = generate_random_password()
      password_var.set(password)

    generate_password_btn = Button(
      update_users_page,
      text="Generate Random Password",
      command=insert_password
    )
    generate_password_btn.place(anchor="c", relx=0.55, rely=0.5)

    def update_user():
      user = (
        username_var.get(), 
        password_var.get(),
        user_id
      )

      conn = ConnectionHandler()
      resp = conn.alter_user(user)
      
      if resp["status"] == "Success":
        messagebox.showinfo("Status", "User updated successfully")

      else:
        messagebox.showerror("Status", "An error occurred")  

    save_user_btn = Button(
      update_users_page,
      text="Update User",
      command=update_user
    )
    save_user_btn.place(anchor="c", relx=0.5, rely=0.6)
    update_users_page.place(anchor="c", relx=0.5, rely=0.5)

  def update_product(self, data):
    global update_img_btn,update_img_label, img_display_label
    update_products_page = Frame(
      self.app,     
      width="1920", 
      height="1080",
    )
    back_button = Button(
     update_products_page,
      text="< Back",
      width="15",
      command=lambda: (update_products_page.place_forget(), self.get_products())
    )
    back_button.place(anchor="c", relx=0.3, rely=0.15)

    top_label = Label(
     update_products_page, 
      text="ADD PRODUCT DETAILS", 
      fg="blue",
      font="Times 20 bold"
    )
    top_label.place(anchor="c", relx=0.5, rely=0.15)
    update_img_label = Label (
     update_products_page,
      image=self.images[data.get("img_id") - 1]
    )
    update_img_label.place(anchor="c", relx=0.5, rely=0.25)
    update_img_btn = Button(
     update_products_page,
      text="Select Image",
      command=self.get_file
    )
    update_img_btn.place(anchor="c", relx=0.5, rely=0.35)
    img_display_label = Label(
     update_products_page,
      text="Click on image to change"
    )

    product_name_label = Label(
     update_products_page,
      text="Product name"
    )
    product_name_label.place(anchor="c", relx=0.5, rely=0.4)
    product_name_var = StringVar()
    product_name_var.set(data.get("name"))
    product_name_entry = Entry(
     update_products_page,
      textvariable=product_name_var
    )
    product_name_entry.place(anchor="c", relx=0.5, rely=0.45)

    product_quantity_label = Label(
     update_products_page,
      text="Product quantity"
    )
    product_quantity_label.place(anchor="c", relx=0.5, rely=0.5)
    product_quantity_var = IntVar()
    product_quantity_var.set(data.get("quantity"))
    product_quantity_entry = Entry(
     update_products_page,
      textvariable=product_quantity_var
    )
    product_quantity_entry.place(anchor="c", relx=0.5, rely=0.55)

    product_price_label = Label(
     update_products_page,
      text="Product price"
    )
    product_price_label.place(anchor="c", relx=0.5, rely=0.6)
    product_price_var = DoubleVar()
    product_price_var.set(data.get("price"))
    product_price_entry = Entry(
     update_products_page,
      textvariable=product_price_var
    )
    product_price_entry.place(anchor="c", relx=0.5, rely=0.65)

    def update_product():
      product = (
        product_name_var.get(), 
        product_price_var.get(),
        self.img_url,
        product_quantity_var.get(),
        data.get("id")
      )
      
      connection = ConnectionHandler()
      resp = connection.alter_product(product)
      if resp["status"] == "Success":
        messagebox.showinfo("Status", "Product updated successfully")

      else:
        messagebox.showerror("Error", "An Error Occurred")

    update_product_btn = Button(
     update_products_page,
      text="Update Product",
      command=update_product
    )
    update_product_btn.place(anchor="c", relx=0.5, rely=0.7)
    update_products_page.place(anchor="c", relx=0.5, rely=0.5)

  def get_products(self):
    conn = ConnectionHandler()
    resp = conn.get_products()

    item_list = []
    
    get_products_page = Frame(
      self.app,
      width="1920", 
      height="1080"
    )

    back_button = Button(
      get_products_page,
      text="< Back",
      width="15",
      command=lambda: (get_products_page.place_forget(), self.homepage())
    )
    back_button.place(anchor="c", relx=0.1, rely=0.07)

    scroller = Scrollbar(
      get_products_page, 
      orient=VERTICAL
    )
    scroller.place(anchor="c", relx=0.97, rely=0.52, width=20, height=900)
    entry_canvas = Canvas(
      get_products_page, 
      height=900, 
      width=1700,
      yscrollcommand=scroller.set,
    )
    entry_canvas.place(anchor="c", relx=0.5, rely=0.52)

    entry_frame = Frame(
      entry_canvas, 
      height=900, 
      width=1700,
    )
    entry_canvas.create_window((0,0), window=entry_frame, anchor="c")

    entry_frame.bind(
      "<Configure>", 
      entry_canvas.configure(scrollregion=entry_canvas.bbox("all"))
    )

    scroller.config(command=entry_canvas.yview)

    if resp["status"] == "Success":
      pointer = 0
      mv_x = 0.15
      mv_y = 0.15
      for x in resp["message"]:
        if pointer != 0 and pointer % 5 == 0:
          mv_y += 0.38
          mv_x = 0.15

        image = Label(
          entry_frame,
          image=self.images[pointer],
          width=300,
          height=200,
        )
        image.place(anchor="c", relx=mv_x, rely=mv_y)
        name = Label(
          entry_frame,
          text="Name: " + x[1],
          font="Times 15"
        )
        name.place(anchor="c", relx=mv_x, rely=mv_y+0.13)
        price = Label(
          entry_frame,
          text="Price: GHC " + str(x[2]),
          font="Times 15"
        )
        price.place(anchor="c", relx=mv_x, rely=mv_y+0.16)
        quantity = Label(
          entry_frame,
          text="Quantity: " + str(x[4]),
          font="Times 15"
        )
        quantity.place(anchor="c", relx=mv_x, rely=mv_y+0.19)

        edit_btn = Button(
          entry_frame,
          text="Edit",
          width=10,
          command=lambda id=x[0], name=x[1], price=x[2], quantity=x[4]: 
            self.update_product(
              {
                "id": id,
                "img_id": pointer,
                "name": name,
                "price": price,
                "quantity": quantity,
              }
            )
        )
        edit_btn.place(anchor="c", relx=mv_x-0.03, rely=mv_y+0.24)

        def handle_delete(id):
          conn = ConnectionHandler()
          resp = conn.delete_user(int(id))

          if resp["status"] == "Success":
            messagebox.showinfo("Status", "Product deleted successfully")
            get_products_page.place_forget()
            self.homepage()
          else:
            messagebox.showerror("Status", "An error occurred")

        delete_btn = Button(
          entry_frame,
          text="Delete",
          width=10,
          command=lambda id=x[0]: handle_delete(id)
        )
        delete_btn.place(anchor="c", relx=mv_x+0.03, rely=mv_y+0.24)

        item_list.append(image)
        pointer += 1
        mv_x += 0.18

    get_products_page.place(anchor="c", relx=0.5, rely=0.5)

  def users(self):
    conn = ConnectionHandler()
    resp = conn.get_admins()

    admin_list = []
    users_page = Frame(
      self.app,
      width="1920", 
      height="1080"
    )

    back_button = Button(
      users_page,
      text="< Back",
      width="15",
      command=lambda: (users_page.place_forget(), self.homepage())
    )

    back_button.place(anchor="c", relx=0.1, rely=0.07)

    add_user_btn = Button(
      users_page,
      text="Add User",
      width="15",
      command=lambda: (users_page.place_forget(), self.add_users())
    )

    add_user_btn.place(anchor="c", relx=0.18, rely=0.07)

    scroller = Scrollbar(
      users_page, 
      orient=VERTICAL
    )
    scroller.place(anchor="c", relx=0.97, rely=0.52, width=20, height=900)

    entry_canvas = Canvas(
      users_page, 
      height=900, 
      width=1700,
      yscrollcommand=scroller.set,
    )
    entry_canvas.place(anchor="c", relx=0.5, rely=0.52)

    entry_frame = Frame(
      entry_canvas, 
      height=900, 
      width=1700,
    )
    entry_canvas.create_window((0,0), window=entry_frame, anchor="c")

    entry_frame.bind(
      "<Configure>", 
      entry_canvas.configure(scrollregion=entry_canvas.bbox("all"))
    )

    scroller.config(command=entry_canvas.yview)
    
    if resp["status"] == "Success":
      
      pointer = 0
      mv_x = 0.1
      mv_y = 0.1
      for x in resp["message"]:
        username = Label (
          entry_frame,
          text="Name: " + x[1],
          font="Times 15"
        )
        username.place(anchor="c", relx=mv_x, rely=mv_y)

        edit_btn = Button(
          entry_frame,
          text="Edit",
          width=10,
          command=lambda name=x[1], id=x[0]: 
            (
              users_page.place_forget(), 
              self.update_user(name, id)
            )
        )
        edit_btn.place(anchor="c", relx=mv_x+0.5, rely=mv_y)

        def handle_delete(id):
          conn = ConnectionHandler()
          resp = conn.delete_user(int(id))

          if resp["status"] == "Success":
            messagebox.showinfo("Status", "User deleted successfully")
            users_page.place_forget()
            self.homepage()
          else:
            messagebox.showerror("Status", "An error occurred")

        delete_btn = Button(
          entry_frame,
          text="Delete",
          width=10,
          command=lambda id=x[0]: handle_delete(id)
        )
        delete_btn.place(anchor="c", relx=mv_x+0.57, rely=mv_y)

        admin_list.append(username)
        pointer += 1
        mv_y += 0.1

    users_page.place(anchor="c", relx=0.5, rely=0.5)

  def check_sales(self):
    check_sales_page = Frame(
      self.app,
      width="1920", 
      height="1080"
    )

    back_button = Button(
      check_sales_page,
      text="< Back",
      width="15",
      command=lambda: (check_sales_page.place_forget(), self.homepage())
    )

    back_button.place(anchor="c", relx=0.1, rely=0.07)

    check_sales_page.place(anchor="c", relx=0.5, rely=0.5)
 
  def homepage(self):
    admin_page_handler = Frame(
      self.app, 
      width="1920", 
      height="1080"
    )

    btns_frame = Frame(
      admin_page_handler, 
      width=800, 
      height=600, 
    )

    top_label = Label(
      btns_frame, 
      text="SELECT AN ACTION", 
      fg="blue",
      font="Times 20 bold"
    )
    top_label.place(anchor="c", relx=0.5, rely=0.1)
    add_products_btn = Button(
      btns_frame,
      text="ADD PRODUCTS",
      width=18,
      height=4,
      font="Times 12",
      command=lambda: (admin_page_handler.place_forget(), self.add_products())
    )
    add_products_btn.place(anchor="c", relx=0.38, rely=0.3)
    get_products_btn = Button(
      btns_frame,
      text="GET PRODUCTS",
      width=18,
      height=4,
      font="Times 12",
      command=lambda: (admin_page_handler.place_forget(), self.get_products())
    )
    get_products_btn.place(anchor="c", relx=0.62, rely=0.3)
    users_btn = Button(
      btns_frame,
      text="USERS",
      width=18,
      height=4,
      font="Times 12",
      command=lambda: (admin_page_handler.place_forget(), self.users())
    )
    users_btn.place(anchor="c", relx=0.38, rely=0.5)
    check_sales_btn = Button(
      btns_frame,
      text="CHECK SALES",
      width=18,
      height=4,
      font="Times 12",
      command=lambda: (admin_page_handler.place_forget(), self.check_sales())
    )
    check_sales_btn.place(anchor="c", relx=0.62, rely=0.5)

    btns_frame.place(anchor="c", relx=0.5, rely=0.5)
    admin_page_handler.place(anchor="c", relx=0.5, rely=0.5)



def login(role):
  global handler
  handler.place_forget()
  login_handler = Frame(
    supermarket_app, 
    width="1920", 
    height="1080"
  )

  Label(
    login_handler, 
    text="Enter credentials to proceed"
  ).place(anchor="c", relx=0.5, rely=0.2)

  Label(
    login_handler, 
    text="Enter Username"
  ).place(anchor="c", relx=0.5, rely=0.3)

  username_var = StringVar()
  username_entry = Entry(
    login_handler, 
    textvariable=username_var, 
    width=20
  )
  username_entry.place(anchor="c", relx=0.5, rely=0.35)

  password_var = StringVar()
  Label(
    login_handler, 
    text="Enter Password"
  ).place(anchor="c", relx=0.5, rely=0.4)
  password_entry = Entry(
    login_handler, 
    textvariable=password_var, 
    width=20
  )
  password_entry.place(anchor="c", relx=0.5, rely=0.45)

  def authenticate():
    username = username_var.get()
    password = password_var.get()
    creds = {"username": username, "password": password}
    connection = ConnectionHandler()
    resp = connection.login_authenticate(creds, role)
    messagebox.showerror("Login status", resp.get("message"))
    if resp.get("status") == "Success":
      login_handler.place_forget()
      admin_window = AdminPage(supermarket_app)
      admin_window.homepage()

  Button(
    login_handler, 
    text="LOGIN",
    command=authenticate
  ).place(anchor="c", relx=0.5, rely=0.5)

  login_handler.place(anchor="c", relx=0.5, rely=0.5)

def cashier_login():
  pass


handler = Frame(
  supermarket_app, 
  width="1920", 
  height="1080"
)

# homepage_title = Label(
#   handler, 
#   text="SUPERMARKET BILLING SYSTEM", 
#   fg="blue",
#   font="Times 20 bold"
# )

# cashier_login_btn = Button(
#   handler, 
#   text="Cashier Login", 
#   width=30, 
#   height=5, 
#   command=lambda: login("cashier"),
#   font="Times 15 bold"
# )

# admin_login_btn = Button(
#   handler, 
#   text="Admin Login", 
#   width=30, 
#   height=5,
#   command=lambda: login("admin"),
#   font="Times 15 bold"
# )

# homepage_title.place(anchor="c", relx=0.5, rely=0.2)
# cashier_login_btn.place(anchor="c", relx=0.5, rely=0.35)
# admin_login_btn.place(anchor="c", relx=0.5, rely=0.5)
handler.place(anchor="c", relx=0.5, rely=0.5)

new_page = AdminPage(supermarket_app)
new_page.homepage()

supermarket_app.mainloop()

  # home_btn = Button(
    #   admin_page_handler, 
    #   text="Home", 
    #   width="20"
    # )
    # home_btn.place(anchor="c", relx="0.045", rely="0.043")
    # pages_btn = Button(
    #   admin_page_handler, 
    #   text="Pages", 
    #   width="20",
    #   command=lambda: (
    #     admin_page_handler.place_forget(), 
    #     self.pages()
    #   )
    # )
    # pages_btn.place(anchor="c", relx="0.13", rely="0.043")
    # quit_btn = Button(
    #   admin_page_handler, 
    #   text="Help", 
    #   width="20"
    # )
    # quit_btn.place(anchor="c", relx="0.215", rely="0.043")