import yaml


def analyze_with_file(file_name, case_name, *args):
    with open("./data/" + file_name + ".yml", "r", encoding='utf-8') as f:
        res = yaml.load(f)[case_name]

        temp_list = list()
        for values in res.values():
            a = list()
            for i in args:
                temp = values[i]
                a.append(temp)
            temp_list.append(a)

        return temp_list

        # temp_list = list()
        # for values in res.values():
        #     a = list()
        #     for i in values.values():
        #         a.append(i)
        #     temp_list.append(a)
        #
        # return temp_list
