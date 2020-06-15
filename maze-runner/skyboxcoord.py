"""
this sky-box is implemented manually
it's not perfect but it works
abdo-taha
"""
class skyboxcoord:
    l = 100 # length of cube

    vertices = [
    [-l,l,l],
    [l,l,l],
    [l,l,-l],
    [-l,l,-l],
    [-l,-l,l],
    [l,-l,l],
    [l,-l,-l],
    [-l,-l,-l]
    ]

    prec = 1.0/3
    # needs to move inside about 1.5 pixel to avoid black line
    #still not the best
    delta3 = 1.5/1536
    delta4 = 1.5/2048
    textcoord = [
        [1-delta3, 0.5-delta4],
        [1-delta3, 0.25+delta4],
        [2 * prec-delta3 , 1-delta4],
        [2 * prec-delta3, 0.75+delta4],
        [2 * prec-delta3, 0.5-delta4],
        [2 * prec-delta3, 0.25+delta4],
        [2 * prec-delta3, 0+delta4],
        [1 * prec+delta3, 1-delta4],
        [1 * prec+delta3, 0.75+delta4],
        [1 * prec+delta3, 0.5-delta4],
        [1 * prec+delta3, 0.25+delta4],
        [1 * prec+delta3, 0+delta4],
        [0+delta3, 0.5-delta4],
        [0+delta3, 0.25+delta4]
    ]

    faces= [
    [1,6],[2,5],[3,1],[4,2],
    [1,6],[2,5],[6,10],[5,11],
    [5,11],[6,10],[7,13],[8,14],
    [2,5],[6,10],[7,9],[3,4],
    [3,4],[7,9],[8,8],[4,3],
    [1,6],[5,11],[8,12],[4,7]
    ]
    co=[]

    def coord(self):
        for pair in self.faces:
            self.co.extend(self.vertices[pair[0]-1])
            self.co.extend(reversed( self.textcoord[pair[1]-1] ))
        return self.co
