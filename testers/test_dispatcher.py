from framework.framework import Framework
from core.action import Action

framework = Framework()

framework.start()

action = Action(

    tool="customer.profile",

    args={

        "account_no":"100001"

    }

)

result = framework.dispatcher.dispatch(action)

print(result)