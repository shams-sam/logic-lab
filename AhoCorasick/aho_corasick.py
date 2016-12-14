from collections import deque

class AhoCorasick(object):
    def __init__(self, keywords):
        self.adj_list = []
        self.adj_list.append({
            "value"       : "",
            "next_states" : [],
            "fail_state"  : 0,
            "output"      : []
        })
        self.add_keywords(keywords)
        self.set_fail_transitions()

    def add_keywords(self, keywords):
        for keyword in keywords:
            self.add_keyword(keyword)

    def find_next_state(self, current_state, value):
        for node in self.adj_list[current_state]["next_states"]:
            if self.adj_list[node]["value"] == value:
                return node
        return None

    def add_keyword(self, keyword):
        current_state = 0
        j = 0
        keyword = keyword.lower()
        child = self.find_next_state(current_state, keyword[j])
        while child != None:
            current_state = child
            j += 1
            if j < len(keyword):
                child = self.find_next_state(current_state, keyword[j])
            else:
                break
        for i in xrange(j, len(keyword)):
            node = {
                "value"       : keyword[i],
                "next_states" : [],
                "fail_state"  : 0,
                "output"      : []
            }
            self.adj_list.append(node)
            self.adj_list[current_state]["next_states"].append(len(self.adj_list) - 1)
            current_state = len(self.adj_list) - 1
        self.adj_list[current_state]["output"].append(keyword)

    def set_fail_transitions(self):
        q = deque()
        child = 0
        for node in self.adj_list[0]["next_states"]:
            q.append(node)
            self.adj_list[node]["fail_state"] = 0
        while q:
            r = q.popleft()
            for child in self.adj_list[r]["next_states"]:
                q.append(child)
                state = self.adj_list[r]["fail_state"]
                while self.find_next_state(state, self.adj_list[child]["value"]) == None and state != 0:
                    state = self.adj_list[state]["fail_state"]
                self.adj_list[child]["fail_state"] = self.find_next_state(state, self.adj_list[child]["value"])
                if self.adj_list[child]["fail_state"] is None:
                    self.adj_list[child]["fail_state"] = 0
                self.adj_list[child]["output"] = self.adj_list[child]["output"] + self.adj_list[self.adj_list[child]["fail_state"]]["output"]

    def get_matches(self, line):
        line = line.lower()
        current_state = 0
        found = []

        for i in xrange(len(line)):
            while self.find_next_state(current_state, line[i]) is None and current_state != 0:
                current_state = self.adj_list[current_state]["fail_state"]
            current_state = self.find_next_state(current_state, line[i])
            if current_state is None:
                current_state = 0
            else:
                for j in self.adj_list[current_state]["output"]:
                    found.append({"index": i - len(j) + 1, "word": j})
        return found
