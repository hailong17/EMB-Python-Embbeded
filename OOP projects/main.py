from __future__ import annotations

class Contact: #like 1 instance
    all_Contacts: list ["Contact"] = []
    def __init__(self, name: str, email: str) -> None:
        self.name = name
        self.email = email
        Contact.all_Contacts.append(self)
        #print(self)

    def __repr__(self) -> str:
        return (f"{self.__class__.__name__}("f"{self.name!r}, {self.email!r}"f")")

class ContactLists(list["Contact"]): #like list of instances
    def search(self, name: str) -> list["Contact"]:
        matching_contacts : list["Contact"] = []
        for contact in self:
            matching_contacts.append(contact)
        return matching_contacts

class Friend(Contact):
    def __init__(self, name: str, email: str, phone: str) -> None:
        super().__init__(name, email)
        self.phone = phone

    def __repr__(self) -> str:
        return (f"{self.__class__.__name__}("
            f"{self.name!r}, {self.email!r}, {self.phone!r})")


class Supplier(Contact):
    def order(self, order: "Order")-> None:
        print(
            "If this were a real system we would send "
            f"'{order}' order to '{self.name}'"
        )

john = Contact("John", "john@example.com")
jane = Contact("Jane", "jane@example.com")

clist = ContactLists()
clist.append(john)
clist.append(jane)

print(clist.search("Jane"))  # [Contact('Jane', 'jane@example.com')]

f = Friend("long", "hailong97bn@gmail.com", "0389970606")
print(Contact.all_Contacts)
