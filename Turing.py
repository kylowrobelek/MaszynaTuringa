#-*- coding: utf-8 -*-

import sys; sys.path.append('/usr/local/lib/python2.7/site-packages')
from Tape import Tape

class DefineTuring(object):


    def __init__(self, tape="", blank_symbol=" ", initial_state="", finalState=None,transitionFunction=None):
        self.tape = Tape(tape)
        self.blank_symbol = blank_symbol
        self.head_position = 0
        self.current_state = initial_state
        if transitionFunction == None:
            self.transitionFunction = {}
        else:
            self.transitionFunction = transitionFunction
        self.final_states = finalState

    def get_tape(self):
        return str(self.tape)

    def transition(self):
        char_under_head = self.tape[self.head_position]
        x = (self.current_state, char_under_head)
        if x in self.transitionFunction:
            y = self.transitionFunction[x]
            self.tape[self.head_position] = y[1]
            if y[2] == "R":
                self.head_position += 1
            elif y[2] == "L":
                self.head_position -= 1
            self.current_state = y[0]

    def final(self):
        if self.current_state in self.final_states:
            return True

    def performAction(self):
        while not self.final():
            try:
                self.transition()
            except:
                raise Exception
