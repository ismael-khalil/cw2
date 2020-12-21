class Menu:
    def show(items, pre_choosed = [], can_back = False):
        ask = True
        isvalid = False
        while ask:
            pre_text = '';
            if len(pre_choosed):
                for x in range(0, len(pre_choosed)):
                    pre_text += "> " + pre_choosed[x]

            if pre_text:
                print("\n")
                print(pre_text)

            for i in range(0, len(items)):
                print(i + 1, ")", items[i]['name'])

            if can_back == True:
                print("Q)", "Go back")

            ans = input("Selection: ")

            if can_back and (ans == "Q" or ans == "q"):
                return {"name": "back", 'value': "back"}


            try:
                ans = int(ans)
                isvalid = False
            except Exception as e:
                isvalid = True
                print('\nInvalid option, Please enter number between', 1, '-' ,len(items))
            else:
                if ans < 1 or ans > len(items):
                    isvalid = True
                    print('\nInvalid option, Please enter number between', 1, '-' ,len(items))

            if isvalid is False:
                ask = False

        return items[ans - 1]

    def show_object(items, pre_choosed = [], can_back = False):
        ask = True
        isvalid = False
        while ask:
            pre_text = '';
            if len(pre_choosed):
                for x in range(0, len(pre_choosed)):
                    pre_text += "> " + pre_choosed[x]

            if pre_text:
                print("\n")
                print(pre_text)

            for i in range(0, len(items)):
                print(i + 1, ")", items[i].get_name())

            if can_back == True:
                print("Q)", "Go back")

            ans = input("Selection: ")

            if can_back and (ans == "Q" or ans == "q"):
                return {"name": "back", 'value': "back"}


            try:
                ans = int(ans)
                isvalid = False
            except Exception as e:
                isvalid = True
                print('\nInvalid option, Please enter number between', 1, '-' ,len(items))
            else:
                if ans < 1 or ans > len(items):
                    isvalid = True
                    print('\nInvalid option, Please enter number between', 1, '-' ,len(items))

            if isvalid is False:
                ask = False

        return items[ans - 1]

    def print_student_score(data):
        formatter = ''
        widths = [15, 15, 10]
        for width in widths:
            formatter += '%-'+ str(width) +'s'

        for item in data:
            print(formatter % (item[0], item[1], item[2]))

    def print_student_performance(data):
        formatter = ''
        widths = [12, 12, 10, 30, 20]
        for width in widths:
            formatter += '%-'+ str(width) +'s'

        for item in data:
            print(formatter % (item[0], item[1], item[2], item[3], item[4]))
