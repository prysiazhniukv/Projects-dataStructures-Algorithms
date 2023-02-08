class Dijkstra:
    def __init__(self):
        self.start = None
        self.end = None
        pass
    def askForStartEnd(self, start, end):
        self.start = start
        self.end = end
        return print(f"The start of the graph is \"{self.start}\", and the end is \"{self.end}\".")
        
solveme = Dijkstra()
solveme.askForStartEnd(start="Book", end="Piano")

        