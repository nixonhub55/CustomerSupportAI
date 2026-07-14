from tools.billing_tools import TOOLS


def execute(tool_name, *args):

    tool = TOOLS.get(tool_name)

    if tool is None:

        return None

    return tool(*args)