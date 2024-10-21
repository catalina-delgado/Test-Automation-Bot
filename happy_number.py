class FooBarProblem:
    codeFoo = 3
    codeBar = 5
    FOO = "Foo"
    BAR = "Bar"

    def TurnFooBar(self, number):
        try:

            inputs = ''
            outputs = ''

            if not isinstance(number, int):
                raise print(f"El numero {number} no es un entero")

            # If the number is divisible by 3, concatenate Foo.
            if number % self.codeFoo == 0:
                outputs += self.FOO

            # If the number is divisible by 5, concatenate Bar.
            if number % self.codeBar == 0:
                outputs += self.BAR

            # If the number is not divisible by either 3 or 5, return the number.
            if outputs == '':
                outputs = number

            return print(f"Entrada: {inputs} \nSalida:  {outputs}")

        except Exception as e:
            print(f"There was an error: {e}")

instance = FooBarProblem()
instance.TurnFooBar(9)
instance.TurnFooBar(10)
instance.TurnFooBar(15)
instance.TurnFooBar(16)
