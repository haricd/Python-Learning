class Program:
    def sum(self):
        return 'sum', self

print(Program.sum(1))

program = Program()

print(program.sum())