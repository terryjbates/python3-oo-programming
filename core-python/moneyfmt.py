class MoneyFmt:
    def __init__(self, value=0.):                # constructor
        if not (isinstance(value, float) or isinstance(value, int)):
            raise ValueError("Value: {} is not float or int".format())
        self.value = float(value)


    def update(self, value=None):                # allow updates
        self.value = value

    def __repr__(self):                                # display as a float number
        return str(self.value)

    def __str__(self):                                # formatted display

        def sign(val):
            if val < 0:
                return '-'
            return ''

        def comma_inserted(input_val):
            dollar_list_result = list()
            dollars, cents = input_val.split(".")

            dollars_list = list(dollars)

            dollars_list.reverse()

            for index, val in enumerate(dollars_list):
                count = index + 1
                if (count - 1) % 3 == 0 and index != 0:
                    dollar_list_result.append(',')
                dollar_list_result.append(val)
            dollar_list_result.reverse()
            dollar_result = ''.join(dollar_list_result)
            return dollar_result + '.' + cents

        trunc_value = "{0:.2f}".format(self.value)
        trunc_value = trunc_value.replace('-', '')
        comma_value = comma_inserted(trunc_value)

        return sign(self.value) + '$' + comma_value

    def __nonzero__(self):                        # boolean test
        ###
        ###        (c) find and fix the bug
        ###
            return self.value != 0