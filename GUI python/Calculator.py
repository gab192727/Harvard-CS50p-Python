import tkinter as tk
from PIL import ImageTk, Image
from math import factorial, sqrt
from re import findall, sub
from sympy import sympify

class Calculator:
    def __init__(self):
        self.root = tk.Tk()
        self.icon = ImageTk.PhotoImage(Image.open("C:\\Users\\er\\Documents\\gab.py\\download (6).jpg"))
        self.root.iconphoto(False, self.icon)
        self.root.title("Calculator")
        self.root.geometry("575x525")
        self.root.resizable(True, True)

        self.small_fs = ("times_new_roman", 15)
        self.large_fs = ("times_new_roman", 30, "bold")
        self.digit_font = ("times_new_roman", 20)
        self.default_font = ("times_new_roman", 18)
        self.last_answer_font = ("times_new_roman", 15)
        self.subscript_font = ("times_new_roman", 8)

        self.operation_color = '#E4E6E5'
        self.last_ans_label_color = '#708090'
        self.text_label_color = "black"
        self.label_color = "#FAFAFA"
        self.equal_color = "#97EBF4"
        self.bg_color = '#F8FAFF'

        self.current_expression = ''
        self.full_expression = ''
        self.copy_expression = ''
        self.copy_last_expression = ''
        self.evaluated = False
        self.subscript = False
        self.last_answer_used = False
        count_of_r_and_c = 5

        self.superscript_map = {'0': '\u2070', '1': '\u00B9', '2': '\u00B2', '3': '\u00B3', '4': '\u2074',
                                '5': '\u2075', '6': '\u2076', '7': '\u2077', '8': '\u2078', '9': '\u2079'}
        self.digit_buttons = (("7", 1, 1), ("8", 1, 2), ("9", 1, 3), ("4", 2, 1), ("5", 2, 2), ("6", 2, 3),
                              ("1", 3, 1), ("2", 3, 2), ("3", 3, 3), ("0", 4, 1), (".", 4, 2))
        self.operations = (("(", "(", 0, 1), (")", ")", 0, 2), ("/ 100", "%", 0, 0),  ("/", "\u00F7", 1, 4),
                           ("*", "\u00D7", 2, 4), ("-", "-", 3, 4), ("+", "+", 4, 4))
        self.all_clear_button = ('AC', 0, 4)
        self.equal_button = ('=', 4, 3)
        self.entry_clear_button = ("CE", 0, 3)
        self.n_root = ('√', "ⁿ√", 1, 0)
        self.n_raise = ('**', '^', 'xⁿ', 2, 0)
        self.n_factorial = ('!', 'n!', 3, 0)
        self.positive_negative = ('Ans', 4, 0)
        self.pattern = r'(\+|\-|\*|\/|√|\^|!|\(|\)|\d+\.?\d*)'

        self.last_answer_label = self.make_last_answer_label()
        self.full_label, self.current_label = self.make_display_label()
        self.button_frame = self.make_button_frame()
        self.button_configure(count_of_r_and_c)
        self.make_digit_buttons()
        self.make_operation_buttons()
        self.make_all_clear_button()
        self.make_entry_clear_button()
        self.make_equal_button()
        self.make_n_root()
        self.make_n_raise()
        self.make_n_factorial()
        self.make_ans_button()
        self.bind_keys()

    def make_button_frame(self):
        frame = tk.Frame(self.root)
        frame.pack(expand=True, fill='both')
        return frame

    def make_display_label(self):
        frame = tk.Frame(self.root, height=200, bg=self.label_color)
        frame.pack(expand=True, fill='both')

        current_label = tk.Label(frame, text=self.current_expression, bg=self.label_color, fg=self.text_label_color, padx=18,
                                 font=self.last_answer_font, anchor=tk.E, pady=4)
        current_label.pack(expand=True, fill='both')

        full_label = tk.Label(frame, text=self.full_expression, bg=self.label_color, fg=self.text_label_color, padx=18,
                              font=self.large_fs,  anchor=tk.E, pady=4)
        full_label.pack(expand=True, fill='both')
        return current_label, full_label

    def make_last_answer_label(self):
        last_answer_label = tk.Label(self.root, text="", bg=self.label_color, fg=self.last_ans_label_color,
                                     font=self.default_font, anchor=tk.E, padx=10)
        last_answer_label.pack(side=tk.TOP, fill=tk.X)
        return last_answer_label


    def make_digit_buttons(self):
        for digit, row, column in self.digit_buttons:
            button = tk.Button(self.button_frame, text=digit, bg=self.bg_color, fg=self.text_label_color,
                               font=self.digit_font, borderwidth=0, command=lambda x=digit: self.append_digit(x))
            button.grid(row=row, column=column, sticky=tk.NSEW, padx=4, pady=4)
            button.bind("<Enter>", lambda event, btn=button: self.digit_on_enter(btn))
            button.bind("<Leave>", lambda event, btn=button: self.digit_on_leave(btn))

    def make_operation_buttons(self):
        for operator, display, row, column in self.operations:
            button = tk.Button(self.button_frame, text=display, bg=self.operation_color, fg=self.text_label_color,
                               font=self.default_font, borderwidth=0, command=lambda x=operator: self.append_operator(x))
            button.grid(row=row, column=column, sticky=tk.NSEW, padx=4, pady=4)
            button.bind("<Enter>", lambda event, btn=button: self.operation_on_enter(btn))
            button.bind("<Leave>", lambda event, btn=button: self.operation_on_leave(btn))

    def make_all_clear_button(self):
        button = tk.Button(self.button_frame, text=self.all_clear_button[0], bg=self.operation_color,
                           fg=self.text_label_color, font=self.default_font, borderwidth=0, command=self.clear_all)
        button.grid(row=self.all_clear_button[1], column=self.all_clear_button[2], sticky=tk.NSEW, padx=4, pady=4)
        button.bind("<Enter>", lambda event, btn=button: self.operation_on_enter(btn))
        button.bind("<Leave>", lambda event, btn=button: self.operation_on_leave(btn))

    def make_entry_clear_button(self):
        button = tk.Button(self.button_frame, text=self.entry_clear_button[0], bg=self.operation_color,
                           fg=self.text_label_color, font=self.default_font, borderwidth=0, command=self.clear_entry)
        button.grid(row=self.entry_clear_button[1], column=self.entry_clear_button[2], sticky=tk.NSEW, padx=4, pady=4)
        button.bind("<Enter>", lambda event, btn=button: self.operation_on_enter(btn))
        button.bind("<Leave>", lambda event, btn=button: self.operation_on_leave(btn))


    def make_equal_button(self):
        button = tk.Button(self.button_frame, text=self.equal_button[0], bg=self.equal_color, fg=self.text_label_color,
                           font=self.default_font, borderwidth=0,  command=self.evaluate)
        button.grid(row=self.equal_button[1], column=self.equal_button[2], sticky=tk.NSEW, padx=4, pady=4)
        button.bind("<Enter>", lambda event, btn=button: self.equal_on_enter(btn))
        button.bind("<Leave>", lambda event, btn=button: self.equal_on_leave(btn))

    def make_n_root(self):
        button = tk.Button(self.button_frame, text=self.n_root[1], bg=self.operation_color, fg=self.text_label_color,
                           font=self.default_font, borderwidth=0, command=lambda x=self.n_root[0]: self.root_to_n(x))
        button.grid(row=self.n_root[2], column=self.n_root[3], sticky=tk.NSEW, padx=4, pady=4)
        button.bind("<Enter>", lambda event, btn=button: self.operation_on_enter(btn))
        button.bind("<Leave>", lambda event, btn=button: self.operation_on_leave(btn))

    def make_n_raise(self):
        button = tk.Button(self.button_frame, text=self.n_raise[2], bg=self.operation_color,
                           fg=self.text_label_color, font=self.default_font, borderwidth=0, command=self.raise_to_n)
        button.grid(row=self.n_raise[3], column=self.n_raise[4], sticky=tk.NSEW, padx=4, pady=4)
        button.bind("<Enter>", lambda event, btn=button: self.operation_on_enter(btn))
        button.bind("<Leave>", lambda event, btn=button: self.operation_on_leave(btn))

    def make_n_factorial(self):
        button = tk.Button(self.button_frame, text=self.n_factorial[1], bg=self.operation_color,
                           fg=self.text_label_color, font=self.default_font, borderwidth=0,
                           command=lambda x=self.n_factorial[0]: self.factorial_n(x))
        button.grid(row=self.n_factorial[2], column=self.n_factorial[3], sticky=tk.NSEW, padx=4, pady=4)
        button.bind("<Enter>", lambda event, btn=button: self.operation_on_enter(btn))
        button.bind("<Leave>", lambda event, btn=button: self.operation_on_leave(btn))

    def make_ans_button(self):
        button = tk.Button(self.button_frame, text=self.positive_negative[0], bg=self.operation_color,
                           fg=self.text_label_color, font=self.default_font, borderwidth=0, command=self.get_last_answer)
        button.grid(row=self.positive_negative[1], column=self.positive_negative[2], sticky=tk.NSEW, padx=4, pady=4)
        button.bind("<Enter>", lambda event, btn=button: self.operation_on_enter(btn))
        button.bind("<Leave>", lambda event, btn=button: self.operation_on_leave(btn))


    def button_configure(self, n):
        for x in range(n):
            self.button_frame.rowconfigure(x, weight=1)
            self.button_frame.columnconfigure(x, weight=1)

    def update_full_label(self):
        expression = self.full_expression
        for operator, display, row, column in self.operations:
            expression = expression.replace(operator, f' {display} ')

        self.full_label.config(text=expression)

    def update_current_label(self):
        self.current_label.config(text=self.current_expression[:24])

    def append_digit(self, digit):
        if "Error" in self.current_expression:
            self.copy_expression = ''
            self.current_expression = ''
            self.current_expression = str(digit)
            self.update_current_label()
            return
        self.current_expression += str(digit)
        if self.subscript:
            for key, value in self.superscript_map.items():
                self.current_expression = self.current_expression.replace(key, value)

        self.update_current_label()

    def append_operator(self, operation):
        self.subscript = False
        self.evaluated = False
        if "Error" in self.current_expression:
            self.error_check()
            return
        if self.evaluated:
            self.full_expression = ''
        self.current_expression += operation
        self.full_expression += self.current_expression
        self.current_expression = ''
        self.update_full_label()
        self.update_current_label()

    def clear_all(self):
        self.evaluated = False
        self.subscript = False
        self.current_expression = ''
        self.full_expression = ''
        self.update_full_label()
        self.update_current_label()

    def clear_entry(self):
        if "Error" in self.current_expression:
            self.error_check()
            return
        if len(self.current_expression) == 0:
            self.full_expression = self.full_expression[:-1]
            self.update_full_label()
        elif self.evaluated:
            self.full_expression = self.copy_expression[:-1]
            self.current_expression = ''
            self.update_full_label()
            self.update_current_label()
        else:
            self.current_expression = self.current_expression[:-1]
            self.update_current_label()
        self.evaluated = False


    def evaluate(self):
        self.evaluated = True
        self.last_answer_used = False
        self.full_expression += self.current_expression
        self.update_full_label()
        try:
            full_expression = self.full_expression
            for key, value in self.superscript_map.items():
                full_expression = full_expression.replace(value, key)
            full_expression = full_expression.replace(self.n_raise[1], self.n_raise[0])
            full_expression = self.modify_parenthesis_behavior(full_expression)
            components = findall(self.pattern, full_expression)
            components = self.evaluate_factorial(components)
            components = self.evaluate_sqrt(components)
            result = ''.join(components)
            self.current_expression = str(sympify(result))
            self.copy_last_expression = self.current_expression
            self.last_answer_label.config(text=f"Ans: {self.copy_last_expression}")
            self.copy_expression = self.full_expression
            self.full_expression = ''

        except SyntaxError:
            self.current_expression = "Syntax Error"
        except ZeroDivisionError:
            self.current_expression = "Zero Division Error"
        except OverflowError:
            self.current_expression = 'Overflow Error'
        except ValueError:
            self.current_expression = "Value Error"
        finally:
            self.update_current_label()

    @staticmethod
    def modify_parenthesis_behavior(expression):
        return sub(r'(\d)(\()', r'\1*\2', expression)

    @staticmethod
    def evaluate_factorial(expression):
        i = 0
        while i < len(expression):
            if expression[i] == '!':
                expression[i - 1] = str(factorial(int(expression[i - 1])))
                del expression[i]
            else:
                i += 1
        return expression

    @staticmethod
    def evaluate_sqrt(expression):
        expression.reverse()
        i = 0
        while i < len(expression):
            if expression[i] == '√':
                expression[i - 1] = str(sqrt(float(expression[i - 1])))
                del expression[i]
            else:
                i += 1
        expression.reverse()
        return expression


    def root_to_n(self, n):
        if "Error" in self.current_expression:
            self.error_check()
            return
        self.full_expression += f'{n}{self.current_expression}'
        self.current_expression = ''
        self.update_full_label()
        self.update_current_label()

    def raise_to_n(self):
        if "Error" in self.current_expression:
            self.error_check()
            return
        self.subscript = True
        self.full_expression += f'{self.current_expression}{self.n_raise[1]}'
        self.current_expression = ''
        self.update_current_label()
        self.update_full_label()

    def factorial_n(self, x):
        if "Error" in self.current_expression:
            self.error_check()
            return
        self.current_expression = f'{self.current_expression}{x}'
        self.full_expression += self.current_expression
        self.current_expression = ''
        self.update_full_label()
        self.update_current_label()

    def get_last_answer(self):
        if not self.evaluated and not self.last_answer_used:
            self.current_expression += self.copy_last_expression
            self.update_current_label()
            self.last_answer_used = True

    def bind_keys(self):
        self.root.bind("<Return>", lambda event: self.evaluate())

        for operator, display, row, column in self.operations:
            self.root.bind(operator, lambda event, x=operator: self.append_operator(x))

        for digit, row, column in self.digit_buttons:
            self.root.bind(digit, lambda event, x=digit: self.append_digit(x))

    @staticmethod
    def digit_on_enter(button):
        button['background'] = '#cccccc'

    def digit_on_leave(self, button):
        button['background'] = self.bg_color

    @staticmethod
    def operation_on_enter(button):
        button['background'] = '#cccccc'

    def operation_on_leave(self, button):
        button['background'] = self.operation_color

    @staticmethod
    def equal_on_enter(button):
        button['background'] = '#77C3EC'

    def equal_on_leave(self, button):
        button['background'] = self.equal_color

    def run(self):
        self.root.mainloop()

    def error_check(self):
        self.copy_expression = ''
        self.current_expression = ''
        self.update_current_label()




if __name__ == '__main__':
    c = Calculator()
    c.run()
