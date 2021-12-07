import json, collections

def summary(filename, summarize_by):
    try:
        with open(filename, 'r') as file:
            j_file = json.load(file)

        counter = collections.Counter()

        for i in j_file:
            try:
                if j_file.get(summarize_by) == None:
                    counter.update({None})
                elif i == summarize_by:
                    counter.update(j_file.get(summarize_by))
            except KeyError:
                counter.update({None})
            except TypeError:
                counter.update({'unhashable'})

        res = dict(sorted(counter.items(), key=lambda x:x[1], reverse = True))
    except ValueError:
        return "Error in decoding JSON."
    return res

# print(summary("file.json", "coutry"))
