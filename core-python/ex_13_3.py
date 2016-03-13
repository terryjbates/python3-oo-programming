#!/usr/bin/env python3


def dollarize(value):
    def comma_inserted(input_val):
        dollar_list_result = list()
        dollars, cents = input_val.split(".")
        print("{}: {}".format(dollars, cents))

        dollars_list = list(dollars)
        print("dol list: {}".format(dollars_list))

        dollars_list.reverse()
        print("rev doll list {}".format(dollars_list))

        for index, val in enumerate(dollars_list):
            if (index + 1) % 4 == 0:
                dollar_list_result.append(',')
            dollar_list_result.append(val)
        dollar_list_result.reverse()
        dollar_result = ''.join(dollar_list_result)
        return dollar_result + '.' + cents

    sign = ''
    if not (isinstance(value, float) or isinstance(value, int)):
        raise ValueError("Value: {} is not float or int".format())

    if value < 0:
        sign = '-'
    trunc_value = "{0:.2f}".format(value)
    trunc_value = trunc_value.replace('-', '')
    comma_value = comma_inserted(trunc_value)

    return sign + '$' + comma_value


class MoneyFmt:

    def __init__(self, value=0.):                # constructor
        if not (isinstance(value, float) or isinstance(value, int)):
            raise ValueError("Value: {} is not float or int".format())
        self.value = float(value)
        if self.value < 0:
            self.sign = '-'
        self.sign = '+'

    def update(self, value=None):                # allow updates
        self.value = value

    def __repr__(self):                                # display as a float number
        return str(self.value)

    def __str__(self):                                # formatted display
        def comma_inserted(input_val):
            dollar_list_result = list()
            dollars, cents = input_val.split(".")
            print("{}: {}".format(dollars, cents))

            dollars_list = list(dollars)
            print("dol list: {}".format(dollars_list))

            dollars_list.reverse()
            print("rev doll list {}".format(dollars_list))

            for index, val in enumerate(dollars_list):
                if (index + 1) % 4 == 0:
                    dollar_list_result.append(',')
                dollar_list_result.append(val)
            dollar_list_result.reverse()
            dollar_result = ''.join(dollar_list_result)
            return dollar_result + '.' + cents

        trunc_value = "{0:.2f}".format(self.value)
        trunc_value = trunc_value.replace('-', '')
        comma_value = comma_inserted(trunc_value)

        return self.sign + '$' + comma_value


    def __nonzero__(self):                        # boolean test
        ###
        ###        (c) find and fix the bug
        ###
            return self.value != 0