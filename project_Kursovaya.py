import tkinter as tk
from tkinter import ttk, messagebox

class EventCostCalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Калькулятор стоимости мероприятия")
        self.root.geometry("600x700")
        self.root.resizable(False, False)
        self.create_widgets()

    def create_widgets(self):
        tk.Label(self.root, text="Калькулятор стоимости мероприятия", font=("Arial", 16, "bold")).pack(pady=10)

        self.fields = {}
        self.add_input_field("Аренда помещения (₽):", "venue_rent")
        self.add_input_field("Стоимость оборудования (₽):", "equipment_cost")
        self.add_input_field("Число участников:", "attendees")
        self.add_input_field("Цена билета на одного участника (₽):", "ticket_price")
        self.add_input_field("Прочие расходы (₽):", "misc_expenses")

        tk.Button(self.root, text="Рассчитать", command=self.calculate).pack(pady=20)

        self.result_label = tk.Label(self.root, text="", font=("Arial", 12, "bold"), justify="left")
        self.result_label.pack(pady=10)

    def add_input_field(self, label_text, field_name):
        tk.Label(self.root, text=label_text, font=("Arial", 12)).pack(pady=5)
        entry = tk.Entry(self.root)
        entry.pack(pady=5)
        self.fields[field_name] = entry

    def calculate(self):
        try:
            venue_rent = self.get_positive_float(self.fields["venue_rent"].get(), "Аренда помещения")
            equipment_cost = self.get_positive_float(self.fields["equipment_cost"].get(), "Стоимость оборудования")
            attendees = self.get_positive_int(self.fields["attendees"].get(), "Число участников")
            ticket_price = self.get_positive_float(self.fields["ticket_price"].get(), "Цена билета на одного участника")
            misc_expenses = self.get_positive_float(self.fields["misc_expenses"].get(), "Прочие расходы")

            total_cost = venue_rent + equipment_cost + misc_expenses
            total_revenue = attendees * ticket_price
            profit = total_revenue - total_cost

            self.result_label.config(
                text=(
                    f"Общая стоимость мероприятия: {total_cost:,.2f} ₽\n"
                    f"Общий доход от билетов: {total_revenue:,.2f} ₽\n"
                    f"Прибыль: {profit:,.2f} ₽"
                )
            )
        except ValueError as e:
            messagebox.showerror("Ошибка ввода", str(e))

    def get_positive_float(self, value, field_name):
        if not value.strip():
            raise ValueError(f"Поле '{field_name}' не должно быть пустым.")
        try:
            val = float(value)
            if val < 0:
                raise ValueError(f"Поле '{field_name}' должно быть положительным числом.")
            return val
        except ValueError:
            raise ValueError(f"Поле '{field_name}' должно содержать число.")

    def get_positive_int(self, value, field_name):
        if not value.strip():
            raise ValueError(f"Поле '{field_name}' не должно быть пустым.")
        try:
            val = int(value)
            if val <= 0:
                raise ValueError(f"Поле '{field_name}' должно быть положительным целым числом.")
            return val
        except ValueError:
            raise ValueError(f"Поле '{field_name}' должно содержать целое число.")


if __name__ == "__main__":
    root = tk.Tk()
    app = EventCostCalculatorApp(root)
    root.mainloop()
