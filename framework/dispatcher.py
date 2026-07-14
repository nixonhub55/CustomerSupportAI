class ToolDispatcher:

    def __init__(self, framework):

        self.framework = framework

    def dispatch(self, action):

        tool = action.tool

        args = action.args

        return self.framework.tools.execute(
            tool,
            **args
        )