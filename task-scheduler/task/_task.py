class Task:
    def __init__(self, name: str,content: str, minutes: int) -> None:
        super().__init__()
        if len(content) == 0 or content.isspace() or len(name) == 0 or name.isspace() or minutes <=0:
            raise ValueError('Invalid values for a task.')
        self.content = content
        self.time_in_minites = minutes