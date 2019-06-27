from enum import Enum


class Rank(Enum):
    RESPONDENT = 0
    MANAGER = 1
    DIRECTOR = 2


class Employee(object):
    def __init__(self, name: str):
        self.name = name
        self.rank = None
        self.currentCall = None

    def receive_call(self, call):
        return

    def call_completed(self):
        return

    def escalate_and_reassign(self):
        return

    def assign_new_call(self) -> bool:
        return False

    def is_free(self) -> bool:
        return self.currentCall is None

    def get_rank(self) -> Rank:
        return self.rank


class Respondent(Employee):
    def __init__(self, name):
        super().__init__(name)
        self.rank = Rank.RESPONDENT


class Manager(Employee):
    def __init__(self, name):
        super().__init__(name)
        self.rank = Rank.MANAGER


class Director(Employee):
    def __init__(self, name):
        super().__init__(name)
        self.rank = Rank.DIRECTOR


class Call(object):
    def __init__(self, caller):
        self.caller = caller
        self.rank = Rank.RESPONDENT
        self.handler = None

    def set_handler(self, handler: Employee):
        self.handler = handler

    def reply(self, message: str):
        return

    def get_rank(self):
        return self.rank

    def set_rank(self, r: Rank):
        self.rank = r

    def increment_rank(self):
        if self.rank == Rank.RESPONDENT:
            self.rank = Rank.MANAGER
        elif self.rank == Rank.MANAGER:
            self.rank = Rank.DIRECTOR

    def disconnect(self):
        return


class CallCenter(object):
    LEVELS = 3
    NUM_RESPONDENTS = 10
    NUM_MANAGERS = 4
    NUM_DIRECTORS = 2

    def __init__(self):
        self.employees = []
        self.callQueues = []

        for i in range(self.LEVELS):
            self.employees.append([])
            self.callQueues.append([])

    def assign_handler_for_call(self, call: Call) -> Employee:
        return None

    def dispatch_caller(self, caller):
        call = Call(caller)
        dispatch_call(call)

    def dispatch_call(self, call):
        emp = self.assign_handler_for_call(call)
        if emp:
            emp.receive_call(call)
            call.set_handler(emp)
        else:
            call.reply("Wait ...")
            self.callQueues[call.get_rank().value].append(call)

            

Vahid = Director("Vahid")
Elahe = Manager("Elahe")
Joe = Respondent("Joe")

print(Vahid.get_rank(), Elahe.get_rank(), Joe.get_rank())

call1 = Call("Hassan")
print(call1.get_rank())
call1.increment_rank()
print(call1.get_rank())

call1.set_handler(Joe)
print(call1.handler.name)


center1 = CallCenter()
print(center1.employees)
print(center1.callQueues)

rank1 = Rank.RESPONDENT
print(rank1)
