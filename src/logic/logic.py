class CalculatorLogic:
    def evaluate(self, expression):
        """
        Evaluates a mathematical expression provided as a string.
        :param expression: str, the mathematical expression to evaluate
        :return: result of the evaluation
        """
        try:
            # Use Python's eval function to evaluate the expression
            result = eval(expression)
            return result
        except Exception as e:
            # Raise an exception if the evaluation fails
            raise ValueError("Invalid mathematical expression") from e