g_var = 0
nl_var = 0
print("top level->", "g_var:", g_var, "nl_var:", nl_var)
def test():
    nl_var = 2
    print("in test->", "g_var:", g_var, "nl_var:", nl_var)
    def inner_test():
        global g_var
        nonlocal nl_var
        g_var = 1
        nl_var = 4
        print("in inner_test->", "g_var:", g_var, "nl_var:", nl_var)
        
    inner_test()
    print("in test->", "g_var:", g_var, "nl_var:", nl_var)

test()
print("top level->", "g_var:", g_var, "nl_var:", nl_var)
