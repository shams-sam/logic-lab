from collections import deque
import _pickle as pkl
from tqdm import tqdm
import sys


class AhoCorasick(object):

    def __init__(self, keywords=[]):
        self.adj_list = []
        self.adj_list.append({
            "value": "",
            "next_states": [],
            "fail_state": 0,
            "output": [],
            "payload": []
        })
        if len(keywords):
            self.add_keywords(keywords)
            self.set_fail_transitions()

    def add_keywords(self, keywords):
        if not isinstance(keywords, dict):
            for keyword in tqdm(keywords):
                self.add_keyword(keyword)
        else:
            for keyword, payload in tqdm(keywords.items(), total=len(keywords)):
                self.add_keyword(keyword, payload)

    def find_next_state(self, current_state, value):
        for node in self.adj_list[current_state]["next_states"]:
            if self.adj_list[node]["value"] == value:
                return node
        return None

    def add_keyword(self, keyword, payload=None):
        current_state = 0
        j = 0
        keyword = " " + keyword.lower().strip() + " "
        child = self.find_next_state(current_state, keyword[j])
        while child != None:
            current_state = child
            j += 1
            if j < len(keyword):
                child = self.find_next_state(current_state, keyword[j])
            else:
                break
        for i in range(j, len(keyword)):
            node = {
                "value": keyword[i],
                "next_states": [],
                "fail_state": 0,
                "output": [],
                "payload": []
            }
            self.adj_list.append(node)
            self.adj_list[current_state][
                "next_states"].append(len(self.adj_list) - 1)
            current_state = len(self.adj_list) - 1
        self.adj_list[current_state]["output"].append(keyword)
        if payload:
            self.adj_list[current_state]["payload"].append(payload)

    def set_fail_transitions(self):
        q = deque()
        child = 0
        for node in self.adj_list[0]["next_states"]:
            q.append(node)
            self.adj_list[node]["fail_state"] = 0
        counter = 0
        while q:
            if counter % 100000 == 0:
                counter = 1
                print(len(q))
            counter += 1
            r = q.popleft()
            for child in self.adj_list[r]["next_states"]:
                q.append(child)
                state = self.adj_list[r]["fail_state"]
                while self.find_next_state(state, self.adj_list[child]["value"]) == None and state != 0:
                    state = self.adj_list[state]["fail_state"]
                self.adj_list[child]["fail_state"] = self.find_next_state(
                    state, self.adj_list[child]["value"])
                if self.adj_list[child]["fail_state"] is None:
                    self.adj_list[child]["fail_state"] = 0
                self.adj_list[child]["output"] = self.adj_list[child][
                    "output"] + self.adj_list[self.adj_list[child]["fail_state"]]["output"]

    def get_matches(self, line, superset=False):
        line = " " + line.lower().strip() + " "
        current_state = 0
        found = []

        for i in range(len(line)):
            while self.find_next_state(current_state, line[i]) is None and current_state != 0:
                current_state = self.adj_list[current_state]["fail_state"]
            current_state = self.find_next_state(current_state, line[i])
            if current_state is None:
                current_state = 0
            else:
                for j in self.adj_list[current_state]["output"]:
                    j = j.strip()
                    block = {
                        "index": i - len(j),
                        "length": len(j),
                        "word": j,
                        "payload": self.adj_list[current_state]["payload"]
                    }
                    found.append(block)
        if superset:
            iter_found = found
            found = []
            for i in range(len(iter_found)):
                found_flag = 0
                for j in range(len(iter_found)):
                    if i != j and iter_found[i]['word'] in iter_found[j]['word']:
                        found_flag = 1
                        break
                if not found_flag:
                    found.append(iter_found[i])

        return found

    def save_automaton(self, file):
        print('Saving FSM automaton...')
        pkl.dump(self.adj_list, open(file, 'wb'))
        print('Model saved in: %s' % file)

    def load_automaton(self, file):
        print('Loading from file: %s ...' % file)
        self.adj_list = pkl.load(open(file, 'rb'))
        print('FSM with %d nodes loaded' % len(self.adj_list))
