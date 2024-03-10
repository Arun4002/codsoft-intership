import tkinter as tk
from tkinter import messagebox, simpledialog

class ContactManagerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Contact Manager")
        self.contacts = []

        # GUI Elements
        self.label_name = tk.Label(root, text="Name:")
        self.entry_name = tk.Entry(root)

        self.label_phone = tk.Label(root, text="Phone:")
        self.entry_phone = tk.Entry(root)

        self.label_email = tk.Label(root, text="Email:")
        self.entry_email = tk.Entry(root)

        self.label_address = tk.Label(root, text="Address:")
        self.entry_address = tk.Entry(root)

        self.button_add = tk.Button(root, text="Add Contact", command=self.add_contact)
        self.button_view = tk.Button(root, text="View Contacts", command=self.view_contacts)
        self.button_search = tk.Button(root, text="Search Contacts", command=self.search_contacts)
        self.button_update = tk.Button(root, text="Update Contact", command=self.update_contact)
        self.button_delete = tk.Button(root, text="Delete Contact", command=self.delete_contact)

        # Layout
        self.label_name.grid(row=0, column=0, padx=10, pady=5)
        self.entry_name.grid(row=0, column=1, padx=10, pady=5)

        self.label_phone.grid(row=1, column=0, padx=10, pady=5)
        self.entry_phone.grid(row=1, column=1, padx=10, pady=5)

        self.label_email.grid(row=2, column=0, padx=10, pady=5)
        self.entry_email.grid(row=2, column=1, padx=10, pady=5)

        self.label_address.grid(row=3, column=0, padx=10, pady=5)
        self.entry_address.grid(row=3, column=1, padx=10, pady=5)

        self.button_add.grid(row=4, column=0, columnspan=2, pady=10)
        self.button_view.grid(row=5, column=0, columnspan=2, pady=5)
        self.button_search.grid(row=6, column=0, columnspan=2, pady=5)
        self.button_update.grid(row=7, column=0, columnspan=2, pady=5)
        self.button_delete.grid(row=8, column=0, columnspan=2, pady=5)

    def add_contact(self):
        name = self.entry_name.get()
        phone = self.entry_phone.get()
        email = self.entry_email.get()
        address = self.entry_address.get()

        if name and phone:
            contact = {"Name": name, "Phone": phone, "Email": email, "Address": address}
            self.contacts.append(contact)
            messagebox.showinfo("Success", "Contact added successfully!")
            self.clear_entries()
        else:
            messagebox.showwarning("Warning", "Name and phone number are required.")

    def view_contacts(self):
        if not self.contacts:
            messagebox.showinfo("Info", "No contacts found.")
            return

        contact_list = "Contacts:\n"
        for i, contact in enumerate(self.contacts, start=1):
            contact_list += f"{i}. {contact['Name']} - {contact['Phone']}\n"

        messagebox.showinfo("Contact List", contact_list)

    def search_contacts(self):
        search_term = simpledialog.askstring("Search Contacts", "Enter name or phone number:")
        if search_term:
            found_contacts = [contact for contact in self.contacts
                              if search_term.lower() in contact["Name"].lower() or
                              search_term in contact["Phone"]]
            if found_contacts:
                contact_list = "Search Results:\n"
                for i, contact in enumerate(found_contacts, start=1):
                    contact_list += f"{i}. {contact['Name']} - {contact['Phone']}\n"
                messagebox.showinfo("Search Results", contact_list)
            else:
                messagebox.showinfo("Info", "No matching contacts found.")
        else:
            messagebox.showwarning("Warning", "Please enter a search term.")

    def update_contact(self):
        search_term = simpledialog.askstring("Update Contact", "Enter name or phone number:")
        if search_term:
            found_contacts = [contact for contact in self.contacts
                              if search_term.lower() in contact["Name"].lower() or
                              search_term in contact["Phone"]]
            if found_contacts:
                selected_contact = found_contacts[0]
                updated_name = simpledialog.askstring("Update Contact", "Enter updated name:", initialvalue=selected_contact["Name"])
                updated_phone = simpledialog.askstring("Update Contact", "Enter updated phone:", initialvalue=selected_contact["Phone"])
                updated_email = simpledialog.askstring("Update Contact", "Enter updated email:", initialvalue=selected_contact["Email"])
                updated_address = simpledialog.askstring("Update Contact", "Enter updated address:", initialvalue=selected_contact["Address"])

                if updated_name:
                    selected_contact["Name"] = updated_name
                if updated_phone:
                    selected_contact["Phone"] = updated_phone
                if updated_email:
                    selected_contact["Email"] = updated_email
                if updated_address:
                    selected_contact["Address"] = updated_address

                messagebox.showinfo("Success", "Contact updated successfully!")
            else:
                messagebox.showinfo("Info", "No matching contacts found.")
        else:
            messagebox.showwarning("Warning", "Please enter a search term.")

    def delete_contact(self):
        search_term = simpledialog.askstring("Delete Contact", "Enter name or phone number:")
        if search_term:
            found_contacts = [contact for contact in self.contacts
                              if search_term.lower() in contact["Name"].lower() or
                              search_term in contact["Phone"]]
            if found_contacts:
                confirm_delete = messagebox.askyesno("Delete Contact", f"Are you sure you want to delete {found_contacts[0]['Name']} - {found_contacts[0]['Phone']}?")
                if confirm_delete:
                    self.contacts.remove(found_contacts[0])
                    messagebox.showinfo("Success", "Contact deleted successfully!")
            else:
                messagebox.showinfo("Info", "No matching contacts found.")
        else:
            messagebox.showwarning("Warning", "Please enter a search term.")

    def clear_entries(self):
        self.entry_name.delete(0, tk.END)
        self.entry_phone.delete(0, tk.END)
        self.entry_email.delete(0, tk.END)
        self.entry_address.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = ContactManagerApp(root)
    root.mainloop()
