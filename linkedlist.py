import flet as ft

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self, header=None):
        self.header = header

    def append(self, data):
        current_node = Node(data)
        if self.header is None:
            self.header = current_node
            return
        last_node = self.header
        while last_node.next:
            last_node = last_node.next
        last_node.next = current_node

    def display(self):
        curent_node = self.header
        while curent_node:
            print(curent_node.data)
            curent_node = curent_node.next


if __name__ == "__main__":
    l = LinkedList()
    l.append("Hello")
    bo= l.append("World")
    l.display()
    # l.remove("World")
    
import flet as ft

def main(page):

    first_name = ft.TextField(label="First name", autofocus=True)
    last_name = ft.TextField(label="Last name")
    greetings = ft.Column()

    def btn_click(e):
        greetings.controls.append(ft.Text(f"Hello, {first_name.value} {last_name.value}!"))
        first_name.value = ""
        last_name.value = ""
        page.update()
        first_name.focus()

    page.add(
        first_name,
        last_name,
        ft.ElevatedButton("Say hello!", on_click=btn_click),
        greetings,
    )

ft.app(target=main)